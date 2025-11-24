"""
GPT Client for KAIRA 2025.
Handles OpenAI API interactions with support for GPT-4+, GPT-4o, and future models.
"""

import os
from typing import Dict, Any, Optional
from openai import OpenAI
import json


class GPTClient:
    """
    Client for generating lyrics using OpenAI GPT models.
    Supports GPT-4 Turbo, GPT-4o, GPT-4o-mini, and future GPT-5+ models.
    """
    
    SUPPORTED_MODELS = [
        "gpt-4o",
        "gpt-4o-mini",
        "gpt-4-turbo",
        "gpt-4-turbo-preview",
        "gpt-4",
        "gpt-5",  # Future support
        "gpt-5-turbo"  # Future support
    ]
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        """
        Initialize the GPT client.
        
        Args:
            api_key: OpenAI API key (defaults to OPENAI_API_KEY env var)
            model: Model name (defaults to gpt-4o or DEFAULT_MODEL env var)
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key not found. Set OPENAI_API_KEY environment variable.")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = model or os.getenv("DEFAULT_MODEL", "gpt-4o")
        
        # Model-specific configurations
        self.temperature = float(os.getenv("DEFAULT_TEMPERATURE", "0.8"))
        self.max_tokens = int(os.getenv("DEFAULT_MAX_TOKENS", "2500"))
        
    def generate_lyrics(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        use_json_mode: bool = True
    ) -> Dict[str, Any]:
        """
        Generate lyrics using GPT model.
        
        Args:
            system_prompt: System instruction (KAIRA MAINSTREAM persona)
            user_prompt: User request with payload details
            temperature: Sampling temperature (0.0-2.0), defaults to 0.8
            max_tokens: Maximum tokens in response, defaults to 2500
            use_json_mode: Use JSON response format
            
        Returns:
            Dict containing lyrics, phonetics, qa_log, and metadata
        """
        temp = temperature if temperature is not None else self.temperature
        tokens = max_tokens if max_tokens is not None else self.max_tokens
        
        try:
            # Prepare messages
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
            
            # Call OpenAI API
            kwargs = {
                "model": self.model,
                "messages": messages,
                "temperature": temp,
                "max_tokens": tokens
            }
            
            # Use JSON mode if requested and supported
            if use_json_mode and self.model in ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "gpt-4-turbo-preview"]:
                kwargs["response_format"] = {"type": "json_object"}
            
            response = self.client.chat.completions.create(**kwargs)
            
            # Extract response
            response_text = response.choices[0].message.content
            
            # Parse JSON response
            try:
                result = json.loads(response_text)
            except json.JSONDecodeError:
                # If JSON parsing fails, wrap in structure
                result = {
                    "lyrics": response_text,
                    "phonetics": "",
                    "qa_log": "Response was not in valid JSON format",
                    "metadata": {}
                }
            
            # Add metadata
            result["metadata"] = result.get("metadata", {})
            result["metadata"]["model_used"] = self.model
            result["metadata"]["temperature"] = temp
            result["metadata"]["tokens_used"] = response.usage.total_tokens
            
            return result
            
        except Exception as e:
            raise Exception(f"GPT API call failed: {str(e)}")
    
    def generate_with_retry(
        self,
        system_prompt: str,
        user_prompt: str,
        max_retries: int = 3,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Generate lyrics with automatic retry on failure.
        
        Args:
            system_prompt: System instruction
            user_prompt: User request
            max_retries: Maximum number of retry attempts
            **kwargs: Additional arguments for generate_lyrics
            
        Returns:
            Dict containing response or error information
        """
        last_error = None
        
        for attempt in range(max_retries):
            try:
                result = self.generate_lyrics(system_prompt, user_prompt, **kwargs)
                
                # Validate that we have lyrics
                if "lyrics" in result and result["lyrics"]:
                    return result
                else:
                    # Retry with correction prompt
                    user_prompt += "\n\nPlease ensure the response includes the 'lyrics' field with the generated lyrics."
                    
            except Exception as e:
                last_error = e
                if attempt < max_retries - 1:
                    # Add error correction to prompt
                    user_prompt += f"\n\nPrevious attempt failed with error: {str(e)}. Please try again with valid JSON output."
        
        # All retries failed
        return {
            "lyrics": "",
            "phonetics": "",
            "qa_log": f"Failed after {max_retries} attempts. Last error: {str(last_error)}",
            "metadata": {
                "error": True,
                "error_message": str(last_error)
            }
        }
    
    def set_model(self, model: str):
        """
        Change the GPT model.
        
        Args:
            model: Model name (e.g., 'gpt-4o', 'gpt-4-turbo')
        """
        if model in self.SUPPORTED_MODELS:
            self.model = model
        else:
            raise ValueError(f"Unsupported model: {model}. Supported: {self.SUPPORTED_MODELS}")
    
    def get_available_models(self) -> list:
        """Get list of supported models."""
        return self.SUPPORTED_MODELS
