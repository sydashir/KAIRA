"""
Utility functions for the lyrics generator application.
"""
import json
from typing import Dict, Any


def build_json_payload(
    genre: str,
    song_type: str,
    vibe: str,
    energy: str,
    language: str,
    slang_density: int,
    structure: str,
    chanteo: bool,
    bridge: bool,
    phonetics: bool,
    notes: str,
    lyrics_part: str
) -> Dict[str, Any]:
    """
    Build a JSON payload from the user's selections.
    
    Args:
        genre: Music genre selection
        song_type: Type of song
        vibe: Emotional vibe
        energy: Energy level
        language: Language selection
        slang_density: Slang density level (0-10)
        structure: Song structure
        chanteo: Whether to include chanteo
        bridge: Whether to include bridge
        phonetics: Whether to include phonetics
        notes: Additional notes from user
        lyrics_part: Which part of lyrics to generate
        
    Returns:
        Dictionary containing all parameters
    """
    payload = {
        "genre": genre,
        "type": song_type,
        "vibe": vibe,
        "energy": energy,
        "language": language,
        "slang_density": slang_density,
        "structure": structure,
        "chanteo": chanteo,
        "bridge": bridge,
        "phonetics": phonetics,
        "notes": notes,
        "lyrics_part": lyrics_part
    }
    return payload


def get_system_prompt() -> str:
    """
    Get the system prompt for the OpenAI API.
    
    Returns:
        System prompt string
    """
    return """You are an expert Spanish/Latin Pop and Urban music lyricist specializing in reggaeton, 
dembow, trap latino, bachata urbana, and similar genres. You understand the cultural nuances, 
slang, phonetic patterns, and melodic structures of Latin urban music.

Your task is to generate authentic, culturally-aware lyrics based on the provided parameters.

When generating lyrics:
1. Match the specified genre, vibe, energy, and structure
2. Use appropriate slang density (0=formal, 10=heavy street slang)
3. Include chanteo sections if requested (catchy repetitive hooks)
4. Include bridge sections if requested
5. Provide phonetic transcriptions if requested (showing how to pronounce difficult phrases)
6. Follow the specified song structure
7. Generate only the requested lyrics part (intro, verse, chorus, etc.)

Format your response as JSON with the following structure:
{
    "lyrics": "The generated lyrics with line breaks",
    "phonetics": "Phonetic guidance for difficult words/phrases (if requested)",
    "qa_log": "Quality assurance notes explaining your creative choices, cultural references used, and any important context"
}

Be creative, authentic, and culturally sensitive. Make sure the lyrics flow naturally and match the energy/vibe requested."""


def parse_response(response_text: str) -> Dict[str, str]:
    """
    Parse the OpenAI API response.
    
    Args:
        response_text: Raw response text from OpenAI
        
    Returns:
        Dictionary with lyrics, phonetics, and qa_log
    """
    try:
        # Try to parse as JSON
        data = json.loads(response_text)
        return {
            "lyrics": data.get("lyrics", ""),
            "phonetics": data.get("phonetics", ""),
            "qa_log": data.get("qa_log", "")
        }
    except json.JSONDecodeError:
        # If not valid JSON, return the raw text as lyrics
        return {
            "lyrics": response_text,
            "phonetics": "",
            "qa_log": "Response was not in JSON format"
        }


def format_download_txt(lyrics: str, phonetics: str, qa_log: str, payload: Dict[str, Any]) -> str:
    """
    Format content for TXT download.
    
    Args:
        lyrics: Generated lyrics
        phonetics: Phonetic guidance
        qa_log: QA log notes
        payload: Original request payload
        
    Returns:
        Formatted text string
    """
    txt_content = "=" * 50 + "\n"
    txt_content += "SPANISH/LATIN LYRICS GENERATION\n"
    txt_content += "=" * 50 + "\n\n"
    
    txt_content += "PARAMETERS:\n"
    txt_content += f"Genre: {payload['genre']}\n"
    txt_content += f"Type: {payload['type']}\n"
    txt_content += f"Vibe: {payload['vibe']}\n"
    txt_content += f"Energy: {payload['energy']}\n"
    txt_content += f"Language: {payload['language']}\n"
    txt_content += f"Slang Density: {payload['slang_density']}/10\n"
    txt_content += f"Structure: {payload['structure']}\n"
    txt_content += f"Chanteo: {'Yes' if payload['chanteo'] else 'No'}\n"
    txt_content += f"Bridge: {'Yes' if payload['bridge'] else 'No'}\n"
    txt_content += f"Phonetics: {'Yes' if payload['phonetics'] else 'No'}\n"
    txt_content += f"Lyrics Part: {payload['lyrics_part']}\n"
    if payload['notes']:
        txt_content += f"Notes: {payload['notes']}\n"
    txt_content += "\n" + "=" * 50 + "\n\n"
    
    txt_content += "LYRICS:\n"
    txt_content += "-" * 50 + "\n"
    txt_content += lyrics + "\n\n"
    
    if phonetics:
        txt_content += "=" * 50 + "\n"
        txt_content += "PHONETICS:\n"
        txt_content += "-" * 50 + "\n"
        txt_content += phonetics + "\n\n"
    
    if qa_log:
        txt_content += "=" * 50 + "\n"
        txt_content += "QA LOG:\n"
        txt_content += "-" * 50 + "\n"
        txt_content += qa_log + "\n"
    
    return txt_content


def format_download_json(lyrics: str, phonetics: str, qa_log: str, payload: Dict[str, Any]) -> str:
    """
    Format content for JSON download.
    
    Args:
        lyrics: Generated lyrics
        phonetics: Phonetic guidance
        qa_log: QA log notes
        payload: Original request payload
        
    Returns:
        JSON string
    """
    json_content = {
        "parameters": payload,
        "output": {
            "lyrics": lyrics,
            "phonetics": phonetics,
            "qa_log": qa_log
        }
    }
    return json.dumps(json_content, indent=2, ensure_ascii=False)
