"""
Unified LLM Client for KAIRA 2025.
Handles interactions with OpenAI, Anthropic, and Google models.
"""

import os
import json
from typing import Dict, Any, Optional, List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LLMClient:
    """
    Unified client for generating lyrics and translations using multiple providers.
    """
    
    PROVIDERS = ["openai", "anthropic", "google"]
    
    def __init__(self, provider: str = "openai", model: Optional[str] = None, api_key: Optional[str] = None):
        """
        Initialize the LLM client.
        
        Args:
            provider: 'openai', 'anthropic', or 'google'
            model: Model name (defaults based on provider)
            api_key: API key (defaults to env vars)
        """
        self.provider = provider.lower()
        if self.provider not in self.PROVIDERS:
            raise ValueError(f"Unsupported provider: {self.provider}. Supported: {self.PROVIDERS}")
            
        self.api_key = api_key
        self.model = model
        
        self._setup_client()
        
    def _setup_client(self):
        """Set up the specific provider client."""
        if self.provider == "openai":
            from openai import OpenAI
            self.api_key = self.api_key or os.getenv("OPENAI_API_KEY")
            if not self.api_key:
                raise ValueError("OpenAI API key not found.")
            self.client = OpenAI(api_key=self.api_key)
            self.model = self.model or "gpt-4o"
            
        elif self.provider == "anthropic":
            try:
                import anthropic
            except ImportError:
                raise ImportError("anthropic package not installed. Run `pip install anthropic`")
            
            self.api_key = self.api_key or os.getenv("ANTHROPIC_API_KEY")
            if not self.api_key:
                raise ValueError("Anthropic API key not found.")
            self.client = anthropic.Anthropic(api_key=self.api_key)
            self.model = self.model or "claude-3-5-sonnet-20240620"
            
        elif self.provider == "google":
            try:
                import google.generativeai as genai
            except ImportError:
                raise ImportError("google-generativeai package not installed. Run `pip install google-generativeai`")
                
            self.api_key = self.api_key or os.getenv("GOOGLE_API_KEY")
            if not self.api_key:
                raise ValueError("Google API key not found.")
            genai.configure(api_key=self.api_key)
            self.client = genai
            self.model = self.model or "gemini-1.5-pro"

    def generate_lyrics(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.8,
        max_tokens: int = 2500
    ) -> Dict[str, Any]:
        """
        Generate lyrics using the configured provider.
        """
        try:
            if self.provider == "openai":
                return self._generate_openai(system_prompt, user_prompt, temperature, max_tokens)
            elif self.provider == "anthropic":
                return self._generate_anthropic(system_prompt, user_prompt, temperature, max_tokens)
            elif self.provider == "google":
                return self._generate_google(system_prompt, user_prompt, temperature, max_tokens)
        except Exception as e:
            logger.error(f"Generation failed: {str(e)}")
            raise Exception(f"{self.provider.capitalize()} generation failed: {str(e)}")

    def _generate_openai(self, system, user, temp, tokens) -> Dict[str, Any]:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user}
            ],
            temperature=temp,
            max_tokens=tokens,
            response_format={"type": "json_object"}
        )
        content = response.choices[0].message.content
        return self._parse_json(content)

    def _generate_anthropic(self, system, user, temp, tokens) -> Dict[str, Any]:
        # Anthropic doesn't have a separate system role in messages list in the same way for some versions,
        # but the latest API supports a top-level system parameter.
        response = self.client.messages.create(
            model=self.model,
            max_tokens=tokens,
            temperature=temp,
            system=system,
            messages=[
                {"role": "user", "content": user + "\n\nRespond with valid JSON only."}
            ]
        )
        content = response.content[0].text
        return self._parse_json(content)

    def _generate_google(self, system, user, temp, tokens) -> Dict[str, Any]:
        generation_config = {
            "temperature": temp,
            "max_output_tokens": tokens,
            "response_mime_type": "application/json"
        }
        model = self.client.GenerativeModel(
            model_name=self.model,
            generation_config=generation_config,
            system_instruction=system
        )
        response = model.generate_content(user)
        return self._parse_json(response.text)

    def translate_text(self, text: str, target_language: str = "English") -> str:
        """
        Translate text to the target language.
        """
        prompt = f"Translate the following song lyrics to {target_language}. Maintain the poetic feel and meaning, but prioritize accuracy. Return ONLY the translated text.\n\n{text}"
        
        try:
            if self.provider == "openai":
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.3
                )
                return response.choices[0].message.content.strip()
                
            elif self.provider == "anthropic":
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=2000,
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.content[0].text.strip()
                
            elif self.provider == "google":
                model = self.client.GenerativeModel(self.model)
                response = model.generate_content(prompt)
                return response.text.strip()
                
        except Exception as e:
            return f"Translation failed: {str(e)}"

    def _parse_json(self, content: str) -> Dict[str, Any]:
        """Helper to parse JSON from response string."""
        try:
            # Clean up markdown code blocks if present
            content = content.strip()
            if content.startswith("```json"):
                content = content[7:]
            if content.startswith("```"):
                content = content[3:]
            if content.endswith("```"):
                content = content[:-3]
            
            return json.loads(content)
        except json.JSONDecodeError:
            # Fallback for malformed JSON
            return {
                "lyrics": content,
                "phonetics": {},
                "qa_log": "JSON parsing failed",
                "metadata": {"error": "Invalid JSON format"}
            }
