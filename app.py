"""
KAIRA 2025 — MAINSTREAM Songwriting Assistant
Enhanced Streamlit Application

A professional bilingual songwriting system for Latin Pop & Urban music.
Based on KAIRA DNA specifications (2017-2025 post-Despacito era).
"""

import streamlit as st
from dotenv import load_dotenv
import sys
import json
from pathlib import Path
"""
KAIRA 2025 — MAINSTREAM Songwriting Assistant
Enhanced Streamlit Application

A professional bilingual songwriting system for Latin Pop & Urban music.
Based on KAIRA DNA specifications (2017-2025 post-Despacito era).
"""

import streamlit as st
from dotenv import load_dotenv
import sys
import json
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent))

# Import configurations
from config import GENRES, SONG_TYPES, VIBES, STRUCTURES, DEFAULT_STRUCTURE
from core import LLMClient, PromptBuilder, ResponseParser, validate_payload
from utils import build_json_payload, format_download_txt, format_download_json

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="KAIRA 2025 — MAINSTREAM",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Music-Themed Design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');

    /* Global Theme - Purple & Cyan Music Vibes */
    .stApp {
        background: linear-gradient(135deg, #1a0b2e 0%, #16213e 50%, #0f3460 100%);
        color: #FFFFFF;
        font-family: 'Poppins', sans-serif;
    }

    /* All text elements bright white */
    p, span, div, label, .stMarkdown {
        color: #FFFFFF !important;
    }

    /* Headers - Vibrant & Visible */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        color: #FFFFFF !important;
    }

    .main-header {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #FF10F0, #00D9FF, #FFD700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 3px;
        animation: glow 2s ease-in-out infinite alternate;
    }

    @keyframes glow {
        from { filter: drop-shadow(0 0 10px #FF10F0); }
        to { filter: drop-shadow(0 0 20px #00D9FF); }
    }

    .sub-header {
        font-size: 1.2rem;
        color: #FFD700;
        text-align: center;
        margin-bottom: 3rem;
        font-weight: 400;
        letter-spacing: 2px;
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
    }

    .section-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #00D9FF !important;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 3px solid #FF10F0;
        padding-bottom: 0.5rem;
        text-shadow: 0 0 10px rgba(0, 217, 255, 0.5);
    }

    /* Glassmorphism Containers with Neon Glow */
    .glass-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 16, 240, 0.3);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(255, 16, 240, 0.2), 0 0 20px rgba(0, 217, 255, 0.1);
    }

    /* Buttons - Vibrant Neon */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #FF10F0, #FF007F, #FF5252);
        color: #FFFFFF !important;
        font-weight: 700;
        border-radius: 15px;
        padding: 1rem 2rem;
        border: 2px solid #FF10F0;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 1.1rem;
        box-shadow: 0 0 20px rgba(255, 16, 240, 0.5);
    }

    .stButton>button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 15px 30px rgba(255, 0, 127, 0.5), 0 0 30px rgba(255, 16, 240, 0.8);
        background: linear-gradient(135deg, #FF007F, #FF10F0, #FFD700);
    }

    /* Inputs - Bright & Visible */
    .stTextInput>div>div>input, 
    .stTextArea>div>div>textarea {
        background-color: rgba(10, 10, 40, 0.9) !important;
        color: #FFFFFF !important;
        border-radius: 10px;
        border: 2px solid rgba(0, 217, 255, 0.6) !important;
        font-size: 1.05rem;
        padding: 0.5rem;
    }
    
    .stTextInput>div>div>input:focus, 
    .stTextArea>div>div>textarea:focus {
        border-color: #FF10F0 !important;
        box-shadow: 0 0 15px rgba(255, 16, 240, 0.6) !important;
        background-color: rgba(20, 10, 50, 0.95) !important;
    }

    /* Selectbox - Dark background with white text */
    .stSelectbox {
        color: #FFFFFF !important;
    }
    
    .stSelectbox > div > div {
        background-color: rgba(10, 10, 40, 0.9) !important;
        color: #FFFFFF !important;
        border: 2px solid rgba(0, 217, 255, 0.6) !important;
        border-radius: 10px;
    }
    
    .stSelectbox label {
        color: #00D9FF !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
    }
    
    /* Selectbox input (the selected value) */
    .stSelectbox input {
        color: #FFFFFF !important;
    }
    
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: rgba(10, 10, 40, 0.9) !important;
        color: #FFFFFF !important;
        border: 2px solid rgba(0, 217, 255, 0.6) !important;
    }
    
    /* Dropdown menu options */
    [data-baseweb="menu"] {
        background-color: rgba(10, 10, 40, 0.98) !important;
        border: 2px solid #FF10F0 !important;
        box-shadow: 0 8px 30px rgba(255, 16, 240, 0.4) !important;
    }
    
    [data-baseweb="menu"] li {
        background-color: rgba(10, 10, 40, 0.95) !important;
        color: #FFFFFF !important;
    }
    
    [data-baseweb="menu"] li:hover {
        background-color: rgba(255, 16, 240, 0.3) !important;
        color: #FFD700 !important;
    }
    
    /* Selected option in dropdown */
    [role="option"][aria-selected="true"] {
        background-color: rgba(0, 217, 255, 0.3) !important;
        color: #FFFFFF !important;
    }
    
    /* MultiSelect */
    .stMultiSelect {
        color: #FFFFFF !important;
    }
    
    .stMultiSelect > div > div {
        background-color: rgba(10, 10, 40, 0.9) !important;
        border: 2px solid rgba(0, 217, 255, 0.6) !important;
        border-radius: 10px;
    }
    
    .stMultiSelect span {
        color: #FFFFFF !important;
    }
    
    .stMultiSelect div[data-baseweb="tag"] {
        background-color: rgba(255, 16, 240, 0.6) !important;
        color: #FFFFFF !important;
    }

    /* Sidebar - Dark with Neon Accents */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0e27 0%, #16213e 100%);
        border-right: 2px solid rgba(255, 16, 240, 0.3);
    }
    
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }

    /* Tabs - Neon Style */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: rgba(0, 0, 0, 0.3);
        padding: 10px;
        border-radius: 15px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        color: #FFFFFF !important;
        font-weight: 600;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #FF10F0, #00D9FF);
        color: #FFFFFF !important;
        border: 2px solid #FFD700;
        box-shadow: 0 0 20px rgba(255, 16, 240, 0.6);
    }

    /* Sliders */
    .stSlider {
        padding: 10px 0;
    }
    
    .stSlider > div > div > div > div {
        background-color: #FF10F0 !important;
    }
    
    .stSlider label {
        color: #00D9FF !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
    }
    
    .stSlider [role="slider"] {
        background-color: #FFD700 !important;
    }
    
    .stSlider div[data-baseweb="slider"] {
        background-color: rgba(10, 10, 40, 0.5) !important;
    }

    /* Number Input */
    .stNumberInput > div > div > input {
        background-color: rgba(10, 10, 40, 0.9) !important;
        color: #FFFFFF !important;
        border: 2px solid rgba(0, 217, 255, 0.6) !important;
        border-radius: 10px;
        font-size: 1.1rem;
    }
    
    .stNumberInput label {
        color: #00D9FF !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
    }

    /* Radio Buttons */
    .stRadio > div {
        background-color: rgba(10, 10, 40, 0.5) !important;
        padding: 15px;
        border-radius: 10px;
        border: 2px solid rgba(0, 217, 255, 0.3);
    }
    
    .stRadio label {
        color: #FFFFFF !important;
        font-size: 1.05rem !important;
    }
    
    .stRadio > label {
        color: #00D9FF !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
    }
    
    .stRadio div[role="radiogroup"] label {
        color: #FFFFFF !important;
    }

    /* Checkboxes */
    .stCheckbox {
        background-color: rgba(10, 10, 40, 0.5);
        padding: 10px;
        border-radius: 8px;
        border: 1px solid rgba(0, 217, 255, 0.2);
    }
    
    .stCheckbox label {
        color: #FFFFFF !important;
        font-size: 1.05rem !important;
    }
    
    .stCheckbox span {
        color: #FFFFFF !important;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background-color: rgba(10, 10, 40, 0.7);
        color: #FFFFFF !important;
        border: 2px solid rgba(0, 217, 255, 0.5);
        border-radius: 10px;
        font-weight: 600;
    }
    
    .streamlit-expanderHeader:hover {
        background-color: rgba(255, 16, 240, 0.2);
        border-color: #FF10F0;
    }
    
    .streamlit-expanderContent {
        background-color: rgba(10, 10, 40, 0.3);
        border: 1px solid rgba(0, 217, 255, 0.2);
        border-radius: 0 0 10px 10px;
    }

    /* Success/Error Messages */
    .stSuccess {
        background-color: rgba(0, 255, 127, 0.2);
        color: #00FF7F !important;
        border: 2px solid #00FF7F;
        border-radius: 10px;
    }

    .stError {
        background-color: rgba(255, 0, 0, 0.2);
        color: #FF4444 !important;
        border: 2px solid #FF4444;
        border-radius: 10px;
    }

    /* Download Buttons */
    .stDownloadButton>button {
        background: linear-gradient(135deg, #00D9FF, #00FF7F);
        color: #000000 !important;
        font-weight: 700;
        border-radius: 12px;
        border: 2px solid #00FF7F;
        box-shadow: 0 0 15px rgba(0, 217, 255, 0.5);
    }

    .stDownloadButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(0, 255, 127, 0.5);
    }

    /* Text Areas for Lyrics Display */
    .stTextArea textarea {
        font-family: 'Courier New', monospace;
        font-size: 1.1rem;
        line-height: 1.8;
        color: #FFFFFF !important;
        background-color: rgba(0, 0, 0, 0.4) !important;
        border: 2px solid rgba(255, 16, 240, 0.4) !important;
    }

    /* JSON Display (Signal Flow) */
    .stJson {
        background-color: rgba(10, 10, 40, 0.95) !important;
        border: 2px solid #00D9FF !important;
        border-radius: 12px;
        padding: 20px !important;
        box-shadow: 0 0 20px rgba(0, 217, 255, 0.3);
    }
    
    .stJson pre {
        color: #FFFFFF !important;
        font-size: 1.05rem !important;
        background-color: transparent !important;
    }
    
    .stJson code {
        color: #FFFFFF !important;
        background-color: transparent !important;
    }
    
    /* JSON syntax highlighting */
    .stJson .token.property {
        color: #FFD700 !important;
    }
    
    .stJson .token.string {
        color: #00FF7F !important;
    }
    
    .stJson .token.number {
        color: #FF10F0 !important;
    }
    
    .stJson .token.boolean {
        color: #00D9FF !important;
    }
    
    .stJson .token.punctuation {
        color: #FFFFFF !important;
    }

    /* Labels - Consistent Neon Cyan for all form labels */
    label[data-testid="stWidgetLabel"] {
        color: #00D9FF !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        text-shadow: 0 0 8px rgba(0, 217, 255, 0.4);
        letter-spacing: 0.5px;
    }
    
    /* Secondary labels (like options) */
    label:not([data-testid="stWidgetLabel"]) {
        color: #FFFFFF !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
    }
    
    /* Specific input type labels */
    .stTextInput label, 
    .stTextArea label,
    .stSelectbox label,
    .stMultiSelect label,
    .stSlider label,
    .stNumberInput label {
        color: #00D9FF !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        text-shadow: 0 0 8px rgba(0, 217, 255, 0.4);
    }

</style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<div class="main-header">🎵 KAIRA 2025 🎵</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">⚡ MAINSTREAM // LATIN POP & URBAN SONGWRITING SYSTEM ⚡</div>', unsafe_allow_html=True)

st.markdown("""
<div class="glass-container">
    <p style="margin: 0; color: #FFFFFF; font-size: 1.2rem; line-height: 1.8; text-align: center;">
        <strong style="color: #FF10F0;">CORE IDENTITY:</strong> A hybrid voice blending global pop melody, urban groove, and the natural tone 
        of a Latin songwriter (2017–2025). Generates authentic, singable, emotionally believable lyrics with 
        <strong style="color: #00D9FF;">phonetic rhythm</strong> and <strong style="color: #FFD700;">Gen-Z Spanish</strong> authenticity. 🔥
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar configuration
st.sidebar.markdown('<h2 style="color: #FF10F0; text-shadow: 0 0 10px rgba(255, 16, 240, 0.5);">🎛️ STUDIO CONTROLS</h2>', unsafe_allow_html=True)
st.sidebar.markdown("---")

# Model selection
st.sidebar.subheader("🤖 AI ENGINE")

provider = st.sidebar.selectbox(
    "Provider",
    ["OpenAI", "Anthropic", "Google"],
    index=0,
    help="Select AI provider"
)

if provider == "OpenAI":
    model_options = ["gpt-4o", "o1-preview", "o1-mini", "gpt-4-turbo"]
    default_ix = 0
elif provider == "Anthropic":
    model_options = ["claude-3-5-sonnet-latest", "claude-3-5-haiku-latest", "claude-3-opus-latest"]
    default_ix = 0
else:  # Google
    model_options = ["gemini-1.5-pro-002", "gemini-1.5-flash-002"]
    default_ix = 0

selected_model = st.sidebar.selectbox(
    "Model",
    model_options,
    index=default_ix,
    help=f"Select model for {provider}"
)

st.sidebar.markdown("---")

# Core Parameters
st.sidebar.subheader("🎼 TRACK DNA")

genre = st.sidebar.selectbox(
    "Genre",
    GENRES,
    index=1,  # Default to Reggaeton
)

song_type = st.sidebar.selectbox(
    "Type",
    SONG_TYPES,
    index=0,  # Default to Romantic
    help="Emotional/thematic type of the song"
)

vibe = st.sidebar.selectbox(
    "Vibe",
    VIBES,
    index=5,  # Default to Sensual
    help="Emotional atmosphere and mood"
)

energy_options = ["Low", "Medium-Low", "Medium", "Medium-High", "High"]
energy = st.sidebar.selectbox(
    "Energy",
    energy_options,
    index=2,  # Default to Medium
    help="Energy level and intensity"
)

language_options = ["Spanish", "English", "Spanglish"]
language = st.sidebar.selectbox(
    "Language",
    language_options,
    index=0,  # Default to Spanish
    help="Primary language for lyrics"
)

slang_options = ["Low (0-3)", "Medium (4-6)", "High (7-10)"]
slang_density = st.sidebar.selectbox(
    "Slang Density",
    slang_options,
    index=1,  # Default to Medium
    help="Amount of slang and street language"
)

st.sidebar.markdown("---")

# Singer Profile
st.sidebar.subheader("🎤 ARTIST PROFILE")

singer_gender = st.sidebar.selectbox(
    "Gender",
    ["", "Female", "Male", "Non-binary"],
    index=0,
    help="Singer's gender"
)

singer_nationality = st.sidebar.text_input(
    "Nationality",
    placeholder="e.g., Colombian, Puerto Rican",
    help="Singer's nationality for regional flavor"
)

singer_vocal_style = st.sidebar.text_input(
    "Vocal Style",
    placeholder="e.g., Smooth, Raspy, Powerful",
    help="Singer's vocal characteristics"
)

st.sidebar.markdown("---")

# Structure & Elements
st.sidebar.subheader("🎹 ARRANGEMENT")

structure_options = list(STRUCTURES.keys())
structure_selection = st.sidebar.selectbox(
    "Structure",
    structure_options,
    index=0,  # Default to Mainstream Default
    help="Song structure template"
)

structure_override = STRUCTURES[structure_selection] if structure_selection != "Custom" else ""

if structure_selection == "Custom":
    structure_override = st.sidebar.text_input(
        "Custom Structure",
        value="[verse 1] → [chorus] → [verse 2] → [chorus]",
        help="Define your own structure"
    )

include_chanteo = st.sidebar.checkbox(
    "Include Chanteo",
    value=False,
    help="Add flow-driven rhythmic section"
)

include_bridge = st.sidebar.checkbox(
    "Include Bridge",
    value=False,
    help="Add emotional twist or closure section"
)

include_phonetics = st.sidebar.checkbox(
    "Include Phonetics",
    value=True,
    help="Show phonetic breakdowns for difficult phrases"
)

st.sidebar.markdown("---")

# Lyrics Part
st.sidebar.subheader("📝 SESSION SCOPE")

lyrics_part_options = [
    "Full Song",
    "Verse 1 Only",
    "Chorus Only",
    "Verse 2 Only",
    "Pre-Chorus Only",
    "Chanteo Only",
    "Bridge Only",
    "Custom Selection"
]

lyrics_part = st.sidebar.selectbox(
    "Part to Generate",
    lyrics_part_options,
    index=0,
    help="Which part of the song to generate"
)

length_options = ["Short", "Medium", "Long"]
length = st.sidebar.selectbox(
    "Length",
    length_options,
    index=1,
    help="Overall length preference"
)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="section-header">✍️ CREATIVE BRIEF</div>', unsafe_allow_html=True)
    
    # Notes field
    notes = st.text_area(
        "Notes & Concepts",
        placeholder="""Enter specific details:
• Scenes (e.g., "beach sunset", "late night drive")
• Objects (e.g., "red dress", "old photograph")
• Emotions (e.g., "nostalgia", "desire")

Example: "Visual scenes, emotional but not melodramatic, Caribbean vibes"
""",
        height=150,
        help="Provide specific creative direction"
    )
    
    # Keywords
    keywords = st.text_input(
        "Keywords to Include",
        placeholder="e.g., playa, recuerdo, mirada, noche",
        help="Comma-separated keywords"
    )
    
    # Forbidden words
    forbidden_words = st.text_input(
        "Forbidden Words",
        placeholder="e.g., corazón, alma (words to avoid)",
        help="Comma-separated words to NOT use"
    )

with col2:
    st.markdown('<div class="section-header">⚙️ SIGNAL FLOW</div>', unsafe_allow_html=True)
    
    # Build preview payload
    preview_payload = {
        "genre": genre,
        "type": song_type,
        "vibe": vibe,
        "energy": energy,
        "language": language,
        "slang": slang_density.split()[0],
        "structure": structure_override or DEFAULT_STRUCTURE
    }
    
    st.json(preview_payload)

# Generate button
st.markdown("---")

col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

with col_btn2:
    generate_button = st.button(
        "🎤 GENERATE LYRICS",
        type="primary",
        use_container_width=True
    )

# Generation logic
if generate_button:
    # Extract slang density value
    slang_value = slang_density.split()[0]  # "Low", "Medium", or "High"
    
    # Build payload
    payload = build_json_payload(
        genre=genre,
        song_type=song_type,
        vibe=vibe,
        energy=energy,
        language=language,
        slang_density=slang_value,
        singer_gender=singer_gender,
        singer_nationality=singer_nationality,
        singer_vocal_style=singer_vocal_style,
        include_chanteo=include_chanteo,
        include_bridge=include_bridge,
        include_phonetics=include_phonetics,
        structure_override=structure_override,
        lyrics_part=lyrics_part,
        notes=notes,
        length=length,
        keywords=keywords,
        forbidden_words=forbidden_words
    )
    
    # Validate payload
    is_valid, errors = validate_payload(payload)
    
    if not is_valid:
        st.error("❌ Invalid configuration:")
        for error in errors:
            st.error(f"• {error}")
    else:
        # Store payload in session state
        st.session_state.payload = payload
        
        with st.spinner("🎵 Generating lyrics... This may take 30-60 seconds."):
            try:
                # Initialize client
                client = LLMClient(provider=provider, model=selected_model)
                
                # Build prompts
                system_prompt = PromptBuilder.get_system_prompt()
                user_prompt = PromptBuilder.build_user_prompt(payload)
                
                # Generate lyrics
                response = client.generate_lyrics(
                    system_prompt=system_prompt,
                    user_prompt=user_prompt,
                    temperature=0.8,
                    max_tokens=2500
                )
                
                # Parse response
                parsed = ResponseParser.parse(response)
                
                # Store results in session state
                st.session_state.lyrics = parsed.get("lyrics", {})
                st.session_state.phonetics = parsed.get("phonetics", {})
                st.session_state.qa_log = parsed.get("qa_log", {})
                st.session_state.metadata = parsed.get("metadata", {})
                st.session_state.generated = True
                
                st.success("✅ Lyrics generated successfully! 🎉")
                st.balloons()
                
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
                st.error("Please check your API key and try again.")
                st.session_state.generated = False

# Display results
if st.session_state.get('generated', False):
    st.markdown("---")
    st.markdown('<div class="section-header">🎵 MASTER OUTPUT</div>', unsafe_allow_html=True)
    
    # Create tabs for different outputs
    tab1, tab2, tab3, tab4 = st.tabs(["📝 LYRICS", "🗣️ PHONETICS", "📊 QA LOG", "ℹ️ METADATA"])
    
    with tab1:
        st.subheader("Generated Lyrics")
        lyrics = st.session_state.get('lyrics', {})
        
        if lyrics:
            # Format for display
            formatted_lyrics = ResponseParser.format_lyrics_display(lyrics)
            st.text_area(
                "Lyrics",
                value=formatted_lyrics,
                height=500,
                key="lyrics_display"
            )
        else:
            st.warning("No lyrics generated.")
    
    with tab2:
        st.subheader("Phonetics Guide")
        phonetics = st.session_state.get('phonetics', {})
        
        if phonetics and st.session_state.payload.get('include_phonetics'):
            formatted_phonetics = ResponseParser.format_phonetics_display(phonetics)
            st.text_area(
                "Phonetics",
                value=formatted_phonetics,
                height=400,
                key="phonetics_display"
            )
        else:
            st.info("No phonetics generated. Enable 'Include Phonetics' to get pronunciation guidance.")
    
    with tab3:
        st.subheader("Quality Assurance Log")
        qa_log = st.session_state.get('qa_log', {})
        
        if qa_log:
            formatted_qa = ResponseParser.format_qa_log_display(qa_log)
            st.text_area(
                "QA Log",
                value=formatted_qa,
                height=400,
                key="qa_log_display"
            )
        else:
            st.info("No QA log available.")
    
    with tab4:
        st.subheader("Metadata")
        metadata = st.session_state.get('metadata', {})
        
        if metadata:
            st.json(metadata)
        else:
            st.info("No metadata available.")

    # Translation Feature
    st.markdown("---")
    st.subheader("🌍 TRANSLATION")
    
    if st.button("Translate Lyrics to English", key="translate_btn"):
        lyrics_text = ResponseParser.format_lyrics_display(st.session_state.get('lyrics', {}))
        if lyrics_text:
            with st.spinner("Translating..."):
                try:
                    client = LLMClient(provider=provider, model=selected_model)
                    translation = client.translate_text(lyrics_text)
                    st.session_state.translation = translation
                    st.success("Translation complete!")
                except Exception as e:
                    st.error(f"Translation failed: {str(e)}")
        else:
            st.warning("No lyrics to translate.")
            
    if st.session_state.get('translation'):
        st.text_area(
            "English Translation",
            value=st.session_state.translation,
            height=400
        )
    
    # Download section
    st.markdown("---")
    st.markdown('<div class="section-header">📥 EXPORT</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # TXT download
        txt_content = format_download_txt(
            st.session_state.get('lyrics', {}),
            st.session_state.get('phonetics', {}),
            st.session_state.get('qa_log', {}),
            st.session_state.get('metadata', {}),
            st.session_state.get('payload', {})
        )
        st.download_button(
            label="📄 DOWNLOAD TXT",
            data=txt_content,
            file_name="kaira_lyrics.txt",
            mime="text/plain",
            use_container_width=True
        )
    
    with col2:
        # JSON download
        json_content = format_download_json(
            st.session_state.get('lyrics', {}),
            st.session_state.get('phonetics', {}),
            st.session_state.get('qa_log', {}),
            st.session_state.get('metadata', {}),
            st.session_state.get('payload', {})
        )
        st.download_button(
            label="📋 DOWNLOAD JSON",
            data=json_content,
            file_name="kaira_lyrics.json",
            mime="application/json",
            use_container_width=True
        )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p><strong>KAIRA 2025 — MAINSTREAM</strong></p>
    <p style='font-size: 0.8em; color: #444;'>
        POWERED BY {model}
    </p>
</div>
""".format(model=selected_model), unsafe_allow_html=True)

# Instructions expander
with st.expander("ℹ️ How to Use KAIRA MAINSTREAM"):
    st.markdown("""
    ### Quick Start Guide
    
    1. **Configure Core Parameters** (left sidebar):
       - Select Genre, Type, Vibe, Energy
       - Choose Language and Slang Density
    
    2. **Add Singer Profile** (optional):
       - Specify gender, nationality, vocal style
       - This helps tailor the lyrics to the artist
    
    3. **Choose Structure**:
       - Use Mainstream Default or select a preset
       - Enable Chanteo or Bridge if needed
       - Enable Phonetics for pronunciation help
    
    4. **Provide Instructions**:
       - Add notes with specific scenes, themes, emotions
       - Include keywords you want in the lyrics
       - List any forbidden words to avoid
    
    5. **Generate**:
       - Click "Generate Lyrics"
       - Review output in tabs (Lyrics, Phonetics, QA Log)
       - Download as TXT or JSON
    
    ### KAIRA DNA Principles
    
    - **Fixed Structure**: `[verse 1] → [chorus] → [verse 2] → [pre-chorus] → [chorus]`
    - **Line Counts**: Verse (8), Pre-Chorus (4), Chorus (8 in 4+4 pattern)
    - **Phonetic Rhythm**: Spanish sung phonetics with sinalefa and stressed vowels
    - **Visual Storytelling**: Movie-like scenes over abstract concepts
    - **Modern Spanish**: Conversational 2025 Gen-Z tone with subtle slang
    - **Emotional Honesty**: Real feelings, never melodramatic
    
    ### Tips for Best Results
    
    - **Be specific in notes**: "Beach sunset, nostalgic, red dress" > "Make it good"
    - **Match energy to genre**: High for Reggaeton/Dembow, Medium for Bachata
    - **Use appropriate slang**: Low (0-3) for mainstream, High (7-10) for underground
    - **Enable phonetics**: Especially for non-native Spanish speakers or complex phrases
    - **Try different models**: GPT-4o for best quality, GPT-4o-mini for speed
    """)

# Model info expander
with st.expander("🤖 AI Model Information"):
    st.markdown("""
    ### Supported Models
    
    - **GPT-4o** (Recommended): Latest multimodal model, excellent for creative writing
    - **GPT-4o-mini**: Faster and more affordable, good for experimentation
    - **GPT-4-turbo**: High-quality, reliable generation
    - **GPT-4**: Original GPT-4, stable and tested
    
    ### Coming Soon
    - GPT-5 and future OpenAI models (automatic support when released)
    
    ### Model Selection Tips
    - Use **GPT-4o** for production-quality lyrics
    - Use **GPT-4o-mini** for rapid iteration and testing
    - Higher temperature (0.8-0.9) for more creative, varied outputs
    """)
