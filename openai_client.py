"""
OpenAI API client for lyrics generation.
"""
import os
from typing import Dict, Any
from openai import OpenAI
from utils import get_system_prompt, parse_response


class LyricsGenerator:
    """
    Client for generating lyrics using OpenAI API.
    """
    
    def __init__(self, api_key: str = None):
        """
        Initialize the lyrics generator.
        
        Args:
            api_key: OpenAI API key (if not provided, will use OPENAI_API_KEY env var)
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY environment variable.")
        self.client = OpenAI(api_key=self.api_key)
    
    def generate_lyrics(self, payload: Dict[str, Any], model: str = "gpt-4o") -> Dict[str, str]:
        """
        Generate lyrics based on the provided payload.
        
        Args:
            payload: Dictionary containing all generation parameters
            model: OpenAI model to use (default: gpt-4o)
            
        Returns:
            Dictionary with lyrics, phonetics, and qa_log
        """
        # Create user message from payload
        user_message = self._create_user_message(payload)
        
        # Call OpenAI API
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": get_system_prompt()},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.8,
                max_tokens=2000
            )
            
            # Extract and parse response
            response_text = response.choices[0].message.content
            return parse_response(response_text)
            
        except Exception as e:
            return {
                "lyrics": "",
                "phonetics": "",
                "qa_log": f"Error generating lyrics: {str(e)}"
            }
    
    def _create_user_message(self, payload: Dict[str, Any]) -> str:
        """
        Create a formatted user message from the payload.
        
        Args:
            payload: Dictionary containing all generation parameters
            
        Returns:
            Formatted user message string
        """
        message = f"""Generate lyrics with the following specifications:

Genre: {payload['genre']}
Type: {payload['type']}
Vibe: {payload['vibe']}
Energy: {payload['energy']}
Language: {payload['language']}
Slang Density: {payload['slang_density']}/10
Structure: {payload['structure']}
Include Chanteo: {'Yes' if payload['chanteo'] else 'No'}
Include Bridge: {'Yes' if payload['bridge'] else 'No'}
Include Phonetics: {'Yes' if payload['phonetics'] else 'No'}
Lyrics Part: {payload['lyrics_part']}
"""
        
        if payload.get('notes'):
            message += f"\nAdditional Notes: {payload['notes']}"
        
        message += "\n\nPlease generate the lyrics following the JSON format specified in the system prompt."
        
        return message
