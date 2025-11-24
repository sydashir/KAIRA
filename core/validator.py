"""
Validator for KAIRA 2025.
Validates payloads and responses.
"""

from typing import Dict, Any, List, Optional


def validate_payload(payload: Dict[str, Any]) -> tuple[bool, Optional[List[str]]]:
    """
    Validate user payload before GPT generation.
    
    Args:
        payload: User selections dictionary
        
    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []
    
    # Required fields
    required = ["genre", "type", "vibe", "energy", "language"]
    for field in required:
        if field not in payload or not payload[field]:
            errors.append(f"Missing required field: {field}")
    
    # Validate slang density
    slang_density = payload.get("slang_density")
    if slang_density:
        valid_slang = ["Low", "Medium", "High"]
        if isinstance(slang_density, str) and slang_density not in valid_slang:
            # Check if it's numeric format
            if not any(c.isdigit() for c in slang_density):
                errors.append(f"Invalid slang_density: {slang_density}. Must be Low, Medium, High, or numeric (0-10)")
    
    # Validate energy
    energy = payload.get("energy")
    if energy:
        valid_energy = ["Low", "Medium", "High", "Medium-Low", "Medium-High"]
        if energy not in valid_energy:
            errors.append(f"Invalid energy: {energy}. Must be one of {valid_energy}")
    
    return (len(errors) == 0, errors if errors else None)


def validate_response(response: Dict[str, Any]) -> tuple[bool, Optional[List[str]]]:
    """
    Validate GPT response structure.
    
    Args:
        response: GPT response dictionary
        
    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []
    
    # Check for lyrics
    if "lyrics" not in response:
        errors.append("Response missing 'lyrics' field")
    elif not response["lyrics"]:
        errors.append("Lyrics field is empty")
    
    # Check structure
    required_fields = ["lyrics", "phonetics", "qa_log", "metadata"]
    for field in required_fields:
        if field not in response:
            errors.append(f"Response missing '{field}' field")
    
    # Validate lyrics structure if it's a dict
    if "lyrics" in response and isinstance(response["lyrics"], dict):
        lyrics = response["lyrics"]
        if not lyrics.get("verse_1") and not lyrics.get("full_text"):
            errors.append("Lyrics missing verse_1 or full_text")
        if not lyrics.get("chorus"):
            errors.append("Lyrics missing chorus section")
    
    return (len(errors) == 0, errors if errors else None)


def validate_structure_compliance(lyrics: Dict[str, Any], expected_structure: str) -> tuple[bool, Optional[str]]:
    """
    Validate that lyrics follow expected structure.
    
    Args:
        lyrics: Lyrics dictionary
        expected_structure: Expected structure string (e.g., "[verse 1] → [chorus] → ...")
        
    Returns:
        Tuple of (is_compliant, error_message)
    """
    if not isinstance(lyrics, dict):
        return (False, "Lyrics must be a dictionary")
    
    # Parse expected structure
    import re
    sections = re.findall(r'\[([^\]]+)\]', expected_structure)
    
    # Normalize section names
    section_map = {
        "verse 1": "verse_1",
        "verse 2": "verse_2",
        "verse 2 / chanteo": ["verse_2", "chanteo"],
        "pre-chorus": "pre_chorus",
        "chorus": "chorus",
        "bridge": "bridge",
        "outro": "outro",
        "intro": "intro",
        "chanteo": "chanteo"
    }
    
    missing = []
    for section in sections:
        normalized = section_map.get(section.lower())
        if isinstance(normalized, list):
            # One of these must exist
            if not any(lyrics.get(n) for n in normalized):
                missing.append(section)
        elif normalized:
            if not lyrics.get(normalized):
                missing.append(section)
    
    if missing:
        return (False, f"Missing required sections: {', '.join(missing)}")
    
    return (True, None)
