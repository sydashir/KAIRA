"""
Song structure templates for KAIRA 2025.
Based on KAIRA DNA: Fixed structure unless overridden.
"""

# Default MAINSTREAM structure from KAIRA DNA
DEFAULT_STRUCTURE = "[verse 1] → [chorus] → [verse 2 / chanteo] → [pre-chorus] → [chorus]"

STRUCTURES = {
    "Mainstream Default": "[verse 1] → [chorus] → [verse 2 / chanteo] → [pre-chorus] → [chorus]",
    "Classic Pop": "[verse 1] → [pre-chorus] → [chorus] → [verse 2] → [pre-chorus] → [chorus] → [bridge] → [chorus]",
    "Urban Simple": "[verse 1] → [chorus] → [verse 2] → [chorus]",
    "Trap Flow": "[intro] → [verse 1] → [chorus] → [verse 2] → [bridge] → [chorus]",
    "Bachata Classic": "[intro] → [verse 1] → [pre-chorus] → [chorus] → [verse 2] → [pre-chorus] → [chorus] → [outro]",
    "Reggaeton Party": "[intro] → [verse 1] → [chorus] → [chanteo] → [chorus] → [outro]",
    "Ballad": "[intro] → [verse 1] → [chorus] → [verse 2] → [chorus] → [bridge] → [chorus]",
    "Freestyle": "No fixed structure - creative flow",
    "Custom": "User-defined structure"
}

# Line count specifications from KAIRA DNA
SECTION_LINE_COUNTS = {
    "verse": {
        "lines": 8,
        "description": "Sets the scene with conversational, cinematic tone. Short enough to groove, long enough to carry emotion."
    },
    "pre-chorus": {
        "lines": 4,
        "description": "Builds tension; energy rises melodically. Bridge or anticipation to the hook."
    },
    "chorus": {
        "lines": 8,
        "description": "4 + 4 structure: First 4 = one clear emotional phrase (hook). Next 4 = echo, answer, or variation."
    },
    "chanteo": {
        "lines": [8, 12, 16],
        "description": "Flow-driven rhythmic phrasing. 8 if pre-chorus is 8, 12 if section is 4-bar, 16 if no pre-chorus."
    },
    "bridge": {
        "lines": [4, 5, 6],
        "description": "Emotional twist or closure; same rhythmic pulse. Only when requested."
    },
    "outro": {
        "lines": [4, 5, 6],
        "description": "Closing section, fade-out or final statement."
    },
    "intro": {
        "lines": [2, 4],
        "description": "Opening hook or atmospheric setup."
    }
}

# Structure validation rules
STRUCTURE_RULES = {
    "never_start_with": ["pre-chorus", "bridge", "outro"],
    "must_include": ["verse", "chorus"],
    "optional_sections": ["intro", "pre-chorus", "chanteo", "bridge", "outro"],
    "chorus_repetition": "allowed"
}
