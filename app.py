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
from core import GPTClient, PromptBuilder, ResponseParser, validate_payload
from utils import build_json_payload, format_download_txt, format_download_json

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="KAIRA 2025 — MAINSTREAM Songwriting Assistant",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #FF6B6B;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #4ECDC4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.3rem;
        font-weight: bold;
        color: #45B7D1;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF6B6B;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #FF5252;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<div class="main-header">🎧 KAIRA 2025 — MAINSTREAM</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Professional Bilingual Songwriting Assistant for Latin Pop & Urban Music</div>', unsafe_allow_html=True)

st.markdown("""
<div style="background-color: #f0f2f6; padding: 1rem; border-radius: 10px; margin-bottom: 2rem;">
    <p style="margin: 0; color: #333;">
        <strong>MAINSTREAM</strong> is a hybrid voice blending global pop melody, urban groove, and the natural tone 
        of a Latin songwriter from 2017–2025. Generate authentic, singable, emotionally believable lyrics with 
        phonetic rhythm and cultural authenticity.
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar configuration
st.sidebar.header("🎵 Configuration")
st.sidebar.markdown("---")

# Model selection
st.sidebar.subheader("🤖 AI Model")
model_options = ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "gpt-4"]
selected_model = st.sidebar.selectbox(
    "Model",
    model_options,
    index=0,
    help="GPT-4o recommended for best results. GPT-4o-mini is faster and cheaper."
)

st.sidebar.markdown("---")

# Core Parameters
st.sidebar.subheader("🎼 Core Parameters")

genre = st.sidebar.selectbox(
    "Genre",
    GENRES,
    index=1,  # Default to Reggaeton
    help="Music genre for the lyrics"
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
st.sidebar.subheader("🎤 Singer Profile (Optional)")

singer_gender = st.sidebar.selectbox(
    "Gender",
    ["", "Female", "Male", "Non-binary"],
    index=0,
    help="Singer's gender"
)

singer_nationality = st.sidebar.text_input(
    "Nationality",
    placeholder="e.g., Colombian, Puerto Rican, Mexican",
    help="Singer's nationality for regional flavor"
)

singer_vocal_style = st.sidebar.text_input(
    "Vocal Style",
    placeholder="e.g., Smooth, Raspy, Powerful",
    help="Singer's vocal characteristics"
)

st.sidebar.markdown("---")

# Structure & Elements
st.sidebar.subheader("🎹 Structure & Elements")

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
    help="Add flow-driven rhythmic section (between singing and rapping)"
)

include_bridge = st.sidebar.checkbox(
    "Include Bridge",
    value=False,
    help="Add emotional twist or closure section (4-6 lines)"
)

include_phonetics = st.sidebar.checkbox(
    "Include Phonetics",
    value=True,
    help="Show phonetic breakdowns for difficult phrases"
)

st.sidebar.markdown("---")

# Lyrics Part
st.sidebar.subheader("📝 Lyrics Part")

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
    st.markdown('<div class="section-header">✍️ Additional Instructions</div>', unsafe_allow_html=True)
    
    # Notes field
    notes = st.text_area(
        "Notes & Concepts",
        placeholder="""Enter specific details:
• Scenes or settings (e.g., "beach sunset", "late night drive")
• Objects or symbols (e.g., "red dress", "old photograph")
• Emotions or themes
• Any specific requirements

Example: "Visual scenes, emotional but not melodramatic, Caribbean vibes"
""",
        height=150,
        help="Provide specific creative direction, themes, scenes, or requirements"
    )
    
    # Keywords
    keywords = st.text_input(
        "Keywords to Include",
        placeholder="e.g., playa, recuerdo, mirada, noche",
        help="Comma-separated keywords to include in lyrics"
    )
    
    # Forbidden words
    forbidden_words = st.text_input(
        "Forbidden Words",
        placeholder="e.g., corazón, alma (words to avoid)",
        help="Comma-separated words to NOT use"
    )

with col2:
    st.markdown('<div class="section-header">⚙️ Current Settings</div>', unsafe_allow_html=True)
    
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
        "🎤 Generate Lyrics",
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
        
        # Generate lyrics
        with st.spinner("🎵 KAIRA is writing your lyrics..."):
            try:
                # Initialize GPT client
                client = GPTClient(model=selected_model)
                
                # Build prompts
                system_prompt = PromptBuilder.get_system_prompt()
                user_prompt = PromptBuilder.build_user_prompt(payload)
                
                # Generate with retry
                response = client.generate_with_retry(
                    system_prompt=system_prompt,
                    user_prompt=user_prompt,
                    max_retries=3
                )
                
                # Parse response
                parsed = ResponseParser.parse(json.dumps(response) if isinstance(response, dict) else response)
                
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
    st.markdown('<div class="section-header">🎵 Generated Output</div>', unsafe_allow_html=True)
    
    # Create tabs for different outputs
    tab1, tab2, tab3, tab4 = st.tabs(["📝 Lyrics", "🗣️ Phonetics", "📊 QA Log", "ℹ️ Metadata"])
    
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
    
    # Download section
    st.markdown("---")
    st.markdown('<div class="section-header">📥 Download Options</div>', unsafe_allow_html=True)
    
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
            label="📄 Download as TXT",
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
            label="📋 Download as JSON",
            data=json_content,
            file_name="kaira_lyrics.json",
            mime="application/json",
            use_container_width=True
        )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p><strong>KAIRA 2025 — MAINSTREAM Songwriting Assistant</strong></p>
    <p>Professional bilingual lyrics for Latin Pop & Urban Music (2017-2025 Era)</p>
    <p style='font-size: 0.9em;'>Powered by OpenAI GPT-4+ | Built with Streamlit</p>
    <p style='font-size: 0.8em; margin-top: 10px;'>
        Based on KAIRA DNA specifications: Hook-first logic, phonetic rhythm, 
        visual storytelling, and authentic 2025 Gen-Z Spanish tone.
    </p>
</div>
""", unsafe_allow_html=True)

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
