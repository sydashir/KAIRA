"""
Genre definitions for KAIRA 2025.
Based on KAIRA DNA documents and current Latin music landscape.
"""

GENRES = [
    "Latin Pop",
    "Reggaeton",
    "Latin Trap",
    "Urban",
    "Afro-Latin",
    "Pop Balada",
    "Cumbia Urbana",
    "Bachata Urbana",
    "Dembow",
    "Corridos Tumbados",
    "Salsa Urbana",
    "Perreo",
    "Tropical Pop"
]

GENRE_DESCRIPTIONS = {
    "Latin Pop": "Melodic, radio-friendly with global appeal. Think Shakira, Enrique Iglesias",
    "Reggaeton": "Dembow rhythm, urban flavor. Post-Despacito era (2017-2025)",
    "Latin Trap": "Hip-hop influenced, darker production, street credibility",
    "Urban": "Hybrid of reggaeton, trap, and R&B elements",
    "Afro-Latin": "African rhythms blended with Latin sounds",
    "Pop Balada": "Emotional ballads with pop production",
    "Cumbia Urbana": "Traditional cumbia modernized with urban elements",
    "Bachata Urbana": "Dominican guitar-based with urban twist",
    "Dembow": "High-energy Dominican rhythm, party-focused",
    "Corridos Tumbados": "Mexican narrative style with trap/urban production",
    "Salsa Urbana": "Salsa rhythms with contemporary urban production",
    "Perreo": "Sensual, dancehall-influenced reggaeton subgenre",
    "Tropical Pop": "Caribbean vibes with pop sensibility"
}

# Genre-specific characteristics
GENRE_CHARACTERISTICS = {
    "Latin Pop": {
        "typical_energy": "Medium",
        "common_vibes": ["Romantic", "Uplifting", "Hopeful"],
        "slang_range": (0, 4),
        "language_preference": "Spanish or Spanglish"
    },
    "Reggaeton": {
        "typical_energy": "High",
        "common_vibes": ["Energetic", "Sensual", "Playful"],
        "slang_range": (5, 8),
        "language_preference": "Spanish or Spanglish"
    },
    "Latin Trap": {
        "typical_energy": "Medium-High",
        "common_vibes": ["Aggressive", "Dark", "Confident"],
        "slang_range": (7, 10),
        "language_preference": "Spanish"
    },
    "Bachata Urbana": {
        "typical_energy": "Medium",
        "common_vibes": ["Romantic", "Sensual", "Melancholic"],
        "slang_range": (3, 6),
        "language_preference": "Spanish"
    }
}
