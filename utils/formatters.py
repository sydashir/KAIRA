"""
Formatters for KAIRA 2025.
Handles TXT and JSON download formatting.
"""

import json
from typing import Dict, Any
from datetime import datetime


def format_download_txt(
    lyrics: Dict[str, Any],
    phonetics: Dict[str, Any],
    qa_log: Dict[str, Any],
    metadata: Dict[str, Any],
    payload: Dict[str, Any]
) -> str:
    """
    Format content for TXT download.
    
    Args:
        lyrics: Lyrics dictionary
        phonetics: Phonetics dictionary
        qa_log: QA log dictionary
        metadata: Metadata dictionary
        payload: Original request payload
        
    Returns:
        Formatted text string
    """
    lines = []
    lines.append("=" * 70)
    lines.append("KAIRA 2025 — MAINSTREAM LYRICS GENERATION")
    lines.append("=" * 70)
    lines.append("")
    
    # Timestamp
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    
    # Parameters
    lines.append("PARAMETERS:")
    lines.append("-" * 70)
    lines.append(f"Genre: {payload.get('genre', 'N/A')}")
    lines.append(f"Type: {payload.get('type', 'N/A')}")
    lines.append(f"Vibe: {payload.get('vibe', 'N/A')}")
    lines.append(f"Energy: {payload.get('energy', 'N/A')}")
    lines.append(f"Language: {payload.get('language', 'N/A')}")
    lines.append(f"Slang Density: {payload.get('slang_density', 'N/A')}")
    
    if payload.get('singer'):
        singer = payload['singer']
        lines.append(f"Singer: {singer.get('gender', '')} - {singer.get('nationality', '')}")
    
    lines.append(f"Structure: {metadata.get('structure', 'Default MAINSTREAM')}")
    lines.append(f"Include Chanteo: {'Yes' if payload.get('include_chanteo') else 'No'}")
    lines.append(f"Include Bridge: {'Yes' if payload.get('include_bridge') else 'No'}")
    lines.append(f"Include Phonetics: {'Yes' if payload.get('include_phonetics') else 'No'}")
    
    if payload.get('notes'):
        lines.append(f"\nNotes: {payload['notes']}")
    
    lines.append("")
    lines.append("=" * 70)
    lines.append("")
    
    # Lyrics
    lines.append("LYRICS:")
    lines.append("-" * 70)
    lines.append("")
    
    if isinstance(lyrics, dict):
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
                lines.append(f"[{label}]")
                lines.append(lyrics[key])
                lines.append("")
    elif isinstance(lyrics, str):
        lines.append(lyrics)
        lines.append("")
    
    # Phonetics
    if phonetics and payload.get('include_phonetics'):
        lines.append("=" * 70)
        lines.append("PHONETICS:")
        lines.append("-" * 70)
        lines.append("")
        
        if "difficult_phrases" in phonetics and phonetics["difficult_phrases"]:
            for phrase_data in phonetics["difficult_phrases"]:
                if isinstance(phrase_data, dict):
                    lines.append(f"Phrase: {phrase_data.get('phrase', '')}")
                    lines.append(f"PHON: {phrase_data.get('phonetic', '')}")
                    if phrase_data.get('note'):
                        lines.append(f"Note: {phrase_data['note']}")
                    lines.append("")
        
        if "rhythm_notes" in phonetics:
            lines.append("Rhythm Notes:")
            lines.append(phonetics["rhythm_notes"])
            lines.append("")
    
    # QA Log
    if qa_log:
        lines.append("=" * 70)
        lines.append("QA LOG:")
        lines.append("-" * 70)
        lines.append("")
        
        if isinstance(qa_log, dict):
            if "creative_choices" in qa_log:
                lines.append("Creative Choices:")
                lines.append(qa_log["creative_choices"])
                lines.append("")
            
            if "cultural_references" in qa_log:
                lines.append("Cultural References:")
                lines.append(qa_log["cultural_references"])
                lines.append("")
            
            if "slang_used" in qa_log and qa_log["slang_used"]:
                lines.append(f"Slang Used: {', '.join(qa_log['slang_used'])}")
                lines.append("")
            
            if "structure_notes" in qa_log:
                lines.append("Structure Notes:")
                lines.append(qa_log["structure_notes"])
                lines.append("")
        elif isinstance(qa_log, str):
            lines.append(qa_log)
            lines.append("")
    
    # Metadata
    if metadata:
        lines.append("=" * 70)
        lines.append("METADATA:")
        lines.append("-" * 70)
        lines.append(f"Total Lines: {metadata.get('total_lines', 'N/A')}")
        lines.append(f"Structure: {metadata.get('structure', 'N/A')}")
        lines.append(f"Slang Density: {metadata.get('slang_density', 'N/A')}")
        lines.append(f"Model Used: {metadata.get('model_used', 'N/A')}")
        if metadata.get('estimated_duration'):
            lines.append(f"Estimated Duration: {metadata['estimated_duration']}")
        lines.append("")
    
    lines.append("=" * 70)
    lines.append("Generated by KAIRA 2025 — MAINSTREAM Songwriting Assistant")
    lines.append("Powered by OpenAI GPT-4+")
    lines.append("=" * 70)
    
    return "\n".join(lines)


def format_download_json(
    lyrics: Dict[str, Any],
    phonetics: Dict[str, Any],
    qa_log: Dict[str, Any],
    metadata: Dict[str, Any],
    payload: Dict[str, Any]
) -> str:
    """
    Format content for JSON download.
    
    Args:
        lyrics: Lyrics dictionary
        phonetics: Phonetics dictionary
        qa_log: QA log dictionary
        metadata: Metadata dictionary
        payload: Original request payload
        
    Returns:
        JSON string
    """
    output = {
        "kaira_version": "2025 MAINSTREAM",
        "generated_at": datetime.now().isoformat(),
        "parameters": payload,
        "output": {
            "lyrics": lyrics,
            "phonetics": phonetics,
            "qa_log": qa_log
        },
        "metadata": metadata
    }
    
    return json.dumps(output, indent=2, ensure_ascii=False)
