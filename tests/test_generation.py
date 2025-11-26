import sys
import os
from pathlib import Path
import unittest
from unittest.mock import MagicMock, patch

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

# Mock dependencies BEFORE importing core
sys.modules['openai'] = MagicMock()
sys.modules['anthropic'] = MagicMock()
sys.modules['google'] = MagicMock()
sys.modules['google.generativeai'] = MagicMock()

from core import LLMClient, PromptBuilder

class TestKAIRAGeneration(unittest.TestCase):
    
    def setUp(self):
        self.payload = {
            "genre": "Reggaeton",
            "type": "Romantic",
            "vibe": "Sensual",
            "energy": "High",
            "language": "Spanish",
            "slang_density": "Medium",
            "structure_override": None
        }

    def test_prompt_builder_strict_dna(self):
        """Test that system prompt contains strict DNA requirements."""
        system_prompt = PromptBuilder.get_system_prompt()
        
        # Debug print
        print("\nSystem Prompt Snippet:")
        print(system_prompt[-500:])
        
        # Check for strict structure enforcement
        self.assertIn("STRICT ADHERENCE REQUIRED", system_prompt)
        self.assertIn("NEVER start with Pre-Chorus", system_prompt)
        # Relaxed check for structure to avoid whitespace issues
        self.assertIn("[verse 1] -> [chorus]", system_prompt)
        
        # Check for phonetics and slang
        self.assertIn("PHONETICS: You MUST provide phonetic guides", system_prompt)
        self.assertIn("SLANG: Respect the density setting", system_prompt)
        
        # Check for Gen Z Spanish requirements
        self.assertIn("GEN-Z SPANISH", system_prompt)
        self.assertIn("Conversational: Spoken-but-singable", system_prompt)
        self.assertIn("Visuals: Real-world visuals", system_prompt)

    def test_translation_prompt(self):
        """Test translation prompt builder."""
        lyrics = "Hola mundo"
        prompt = PromptBuilder.build_translation_prompt(lyrics)
        
        self.assertIn("Translate the following song lyrics", prompt)
        self.assertIn("Hola mundo", prompt)

    def test_llm_client_openai(self):
        """Test OpenAI client initialization and generation."""
        # Setup mock
        mock_openai = sys.modules['openai'].OpenAI.return_value
        mock_response = MagicMock()
        mock_response.choices[0].message.content = '{"lyrics": "test"}'
        mock_openai.chat.completions.create.return_value = mock_response
        
        client = LLMClient(provider="openai", api_key="test_key")
        result = client.generate_lyrics("sys", "user")
        
        self.assertEqual(result["lyrics"], "test")
        mock_openai.chat.completions.create.assert_called_once()

    def test_llm_client_anthropic(self):
        """Test Anthropic client initialization."""
        client = LLMClient(provider="anthropic", api_key="test_key")
        self.assertEqual(client.provider, "anthropic")
        self.assertEqual(client.model, "claude-3-5-sonnet-20240620")

    def test_llm_client_google(self):
        """Test Google client initialization."""
        mock_genai = sys.modules['google.generativeai']
        client = LLMClient(provider="google", api_key="test_key")
        self.assertEqual(client.provider, "google")
        self.assertEqual(client.model, "gemini-1.5-pro")
        mock_genai.configure.assert_called_with(api_key="test_key")

if __name__ == '__main__':
    unittest.main()
