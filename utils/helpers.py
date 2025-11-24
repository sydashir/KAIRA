"""
Helper functions for KAIRA 2025.
"""

from typing import Dict, Any, List
import re


def build_json_payload(
    genre: str,
    song_type: str,
    vibe: str,
    energy: str,
    language: str,
    slang_density: str,
    singer_gender: str = "",
    singer_nationality: str = "",
    singer_vocal_style: str = "",
    include_chanteo: bool = False,
    include_bridge: bool = False,
    include_phonetics: bool = True,
    structure_override: str = "",
    lyrics_part: str = "Full Song",
    notes: str = "",
    length: str = "Medium",
    keywords: str = "",
    forbidden_words: str = ""
) -> Dict[str, Any]:
    """
    Build JSON payload from UI selections.
    
    Args:
        All parameters from UI dropdowns and inputs
        
    Returns:
        Structured payload dictionary
    """
    payload = {
        "genre": genre,
        "type": song_type,
        "vibe": vibe,
        "energy": energy,
        "language": language,
        "slang_density": slang_density,
        "include_chanteo": include_chanteo,
        "include_bridge": include_bridge,
        "include_phonetics": include_phonetics,
        "structure_override": structure_override if structure_override else None,
        "lyrics_part": lyrics_part,
        "notes": notes,
        "length": length
    }
    
    # Add singer profile if provided
    if singer_gender or singer_nationality or singer_vocal_style:
        payload["singer"] = {
            "gender": singer_gender,
            "nationality": singer_nationality,
            "vocal_style": singer_vocal_style
        }
    
    # Parse keywords
    if keywords:
        payload["keywords"] = extract_keywords(keywords)
    
    # Parse forbidden words
    if forbidden_words:
        payload["forbidden_words"] = extract_keywords(forbidden_words)
    
    return payload


def extract_keywords(text: str) -> List[str]:
    """
    Extract keywords from comma-separated text.
    
    Args:
        text: Comma-separated keywords
        
    Returns:
        List of cleaned keywords
    """
    if not text:
        return []
    
    # Split by comma and clean
    keywords = [kw.strip() for kw in text.split(',')]
    keywords = [kw for kw in keywords if kw]  # Remove empty strings
    
    return keywords


def parse_structure(structure_text: str) -> List[str]:
    """
    Parse structure text into list of sections.
    
    Args:
        structure_text: Structure string (e.g., "[verse 1] → [chorus] → [verse 2]")
        
    Returns:
        List of section names
    """
    # Extract sections between brackets
    sections = re.findall(r'\[([^\]]+)\]', structure_text)
    return [s.strip() for s in sections]


def estimate_duration(num_lines: int, energy: str) -> str:
    """
    Estimate song duration based on line count and energy.
    
    Args:
        num_lines: Total number of lines
        energy: Energy level
        
    Returns:
        Estimated duration string (e.g., "3:15")
    """
    # Rough estimate: higher energy = faster delivery
    seconds_per_line = {
        "Low": 6,
        "Medium-Low": 5,
        "Medium": 4,
        "Medium-High": 3.5,
        "High": 3
    }
    
    spl = seconds_per_line.get(energy, 4)
    total_seconds = int(num_lines * spl)
    
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    
    return f"{minutes}:{seconds:02d}"


def clean_slang_density(value: Any) -> str:
    """
    Normalize slang density value.
    
    Args:
        value: Input value (string or int)
        
    Returns:
        Normalized string value
    """
    if isinstance(value, int):
        if value <= 3:
            return "Low"
        elif value <= 6:
            return "Medium"
        else:
            return "High"
    
    if isinstance(value, str):
        if value in ["Low", "Medium", "High"]:
            return value
        
        # Try to extract number
        nums = re.findall(r'\d+', value)
        if nums:
            return clean_slang_density(int(nums[0]))
    
    return "Medium"  # Default
