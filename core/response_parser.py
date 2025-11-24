"""
Response Parser for KAIRA 2025.
Parses and validates GPT responses.
"""

import json
from typing import Dict, Any, Optional


class ResponseParser:
    """
    Parses and validates GPT responses for KAIRA lyrics generation.
    """
    
    @staticmethod
    def parse(response_text: str) -> Dict[str, Any]:
        """
        Parse GPT response text into structured format.
        
        Args:
            response_text: Raw response from GPT
            
        Returns:
            Parsed dictionary with lyrics, phonetics, qa_log, metadata
        """
        try:
            # Try to parse as JSON
            data = json.loads(response_text)
            
            # Validate structure
            validated = ResponseParser._validate_structure(data)
            return validated
            
        except json.JSONDecodeError:
            # Not valid JSON, try to extract sections manually
            return ResponseParser._extract_from_text(response_text)
    
    @staticmethod
    def _validate_structure(data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate and normalize response structure.
        
        Args:
            data: Parsed JSON data
            
        Returns:
            Validated and normalized structure
        """
        result = {
            "lyrics": {},
            "phonetics": {},
            "qa_log": {},
            "metadata": {}
        }
        
        # Extract lyrics
        if "lyrics" in data:
            if isinstance(data["lyrics"], dict):
                result["lyrics"] = data["lyrics"]
            elif isinstance(data["lyrics"], str):
                # Legacy format: single string
                result["lyrics"] = {"full_text": data["lyrics"]}
        
        # Extract phonetics
        if "phonetics" in data:
            result["phonetics"] = data["phonetics"]
        
        # Extract QA log
        if "qa_log" in data:
            if isinstance(data["qa_log"], dict):
                result["qa_log"] = data["qa_log"]
            elif isinstance(data["qa_log"], str):
                result["qa_log"] = {"notes": data["qa_log"]}
        
        # Extract metadata
        if "metadata" in data:
            result["metadata"] = data["metadata"]
        
        return result
    
    @staticmethod
    def _extract_from_text(text: str) -> Dict[str, Any]:
        """
        Extract structured data from plain text response.
        
        Args:
            text: Plain text response
            
        Returns:
            Best-effort structured extraction
        """
        # Try to find JSON within text
        import re
        json_pattern = r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}'
        matches = re.findall(json_pattern, text, re.DOTALL)
        
        for match in matches:
            try:
                data = json.loads(match)
                return ResponseParser._validate_structure(data)
            except json.JSONDecodeError:
                continue
        
        # Fallback: return text as lyrics
        return {
            "lyrics": {"full_text": text},
            "phonetics": {},
            "qa_log": {"notes": "Response was not in JSON format"},
            "metadata": {"format": "plain_text"}
        }
    
    @staticmethod
    def format_lyrics_display(lyrics: Dict[str, Any]) -> str:
        """
        Format lyrics dictionary into readable display text.
        
        Args:
            lyrics: Lyrics dictionary
            
        Returns:
            Formatted string for display
        """
        if not lyrics:
            return "No lyrics generated."
        
        # If full_text exists, return it
        if "full_text" in lyrics:
            return lyrics["full_text"]
        
        # Build from sections
        output = []
        section_order = [
            ("intro", "INTRO"),
            ("verse_1", "VERSE 1"),
            ("pre_chorus", "PRE-CHORUS"),
            ("chorus", "CHORUS"),
            ("verse_2", "VERSE 2"),
            ("chanteo", "CHANTEO"),
            ("chorus_repeat", "CHORUS"),
            ("bridge", "BRIDGE"),
            ("outro", "OUTRO")
        ]
        
        for key, label in section_order:
            if key in lyrics and lyrics[key]:
                output.append(f"[{label}]")
                output.append(lyrics[key])
                output.append("")  # Blank line
        
        return "\n".join(output)
    
    @staticmethod
    def format_phonetics_display(phonetics: Dict[str, Any]) -> str:
        """
        Format phonetics dictionary into readable display text.
        
        Args:
            phonetics: Phonetics dictionary
            
        Returns:
            Formatted string for display
        """
        if not phonetics:
            return "No phonetics provided."
        
        output = []
        
        # Display difficult phrases
        if "difficult_phrases" in phonetics and phonetics["difficult_phrases"]:
            output.append("DIFFICULT PHRASES:\n")
            for phrase_data in phonetics["difficult_phrases"]:
                if isinstance(phrase_data, dict):
                    phrase = phrase_data.get("phrase", "")
                    phonetic = phrase_data.get("phonetic", "")
                    note = phrase_data.get("note", "")
                    
                    output.append(f"Phrase: {phrase}")
                    output.append(f"PHON: {phonetic}")
                    if note:
                        output.append(f"Note: {note}")
                    output.append("")
        
        # Display rhythm notes
        if "rhythm_notes" in phonetics:
            output.append("\nRHYTHM NOTES:")
            output.append(phonetics["rhythm_notes"])
        
        return "\n".join(output) if output else "No phonetic details provided."
    
    @staticmethod
    def format_qa_log_display(qa_log: Dict[str, Any]) -> str:
        """
        Format QA log dictionary into readable display text.
        
        Args:
            qa_log: QA log dictionary
            
        Returns:
            Formatted string for display
        """
        if not qa_log:
            return "No QA log provided."
        
        # If it's a simple string
        if isinstance(qa_log, str):
            return qa_log
        
        # If it's just notes
        if "notes" in qa_log and len(qa_log) == 1:
            return qa_log["notes"]
        
        # Build from sections
        output = []
        
        if "creative_choices" in qa_log:
            output.append("CREATIVE CHOICES:")
            output.append(qa_log["creative_choices"])
            output.append("")
        
        if "cultural_references" in qa_log:
            output.append("CULTURAL REFERENCES:")
            output.append(qa_log["cultural_references"])
            output.append("")
        
        if "slang_used" in qa_log and qa_log["slang_used"]:
            output.append("SLANG USED:")
            output.append(", ".join(qa_log["slang_used"]))
            output.append("")
        
        if "structure_notes" in qa_log:
            output.append("STRUCTURE NOTES:")
            output.append(qa_log["structure_notes"])
            output.append("")
        
        if "revision_notes" in qa_log:
            output.append("REVISION NOTES:")
            output.append(qa_log["revision_notes"])
            output.append("")
        
        return "\n".join(output) if output else "No detailed QA information."
