"""
Configuration package for KAIRA 2025.
Contains genre, type, vibe, and structure definitions.
"""

from .genres import GENRES, GENRE_DESCRIPTIONS
from .types import SONG_TYPES, TYPE_DESCRIPTIONS
from .vibes import VIBES, VIBE_DESCRIPTIONS
from .structures import STRUCTURES, DEFAULT_STRUCTURE

__all__ = [
    'GENRES',
    'GENRE_DESCRIPTIONS',
    'SONG_TYPES',
    'TYPE_DESCRIPTIONS',
    'VIBES',
    'VIBE_DESCRIPTIONS',
    'STRUCTURES',
    'DEFAULT_STRUCTURE'
]
