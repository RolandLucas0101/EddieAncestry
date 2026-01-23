import streamlit as st
import pandas as pd
import base64
from datetime import datetime

# ==================== PAGE CONFIGURATION ====================
st.set_page_config(
    page_title="The Burns Family Story",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
    /* Import fonts */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Lora:wght@400;500&display=swap');
    
    /* Main headers */
    .main-header {
        font-family: 'Cinzel', serif;
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        color: #1a472a;
        margin-bottom: 0.5rem;
        padding-top: 1rem;
    }
    
    .sub-header {
        font-family: 'Lora', serif;
        font-size: 1.3rem;
        text-align: center;
        color: #2d5016;
        margin-bottom: 2rem;
        font-style: italic;
    }
    
    /* Section headers */
    .section-header {
        font-family: 'Cinzel', serif;
        font-size: 1.8rem;
        color: #1a472a;
        border-bottom: 2px solid #c9a66b;
        padding-bottom: 0.5rem;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    /* Audio Player Styling */
    .audio-section {
        background: linear-gradient(135deg, #e8f4f8 0%, #d4e8f0 100%);
        border-radius: 12px;
        padding: 2rem;
        margin: 2rem 0;
        border-left: 6px solid #4a90e2;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    .audio-title {
        font-family: 'Cinzel', serif;
        font-size: 1.8rem;
        color: #1a472a;
        margin-bottom: 0.5rem;
    }
    
    .audio-description {
        font-family: 'Lora', serif;
        font-size: 1.1rem;
        color: #555;
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }
    
    .audio-note {
        background: #f9f3e9;
        border-left: 4px solid #c9a66b;
        padding: 1rem;
        border-radius: 6px;
        margin-top: 1.5rem;
        font-family: 'Lora', serif;
        font-size: 0.95rem;
        color: #666;
    }
    
    /* Census table styling */
    .census-table {
        width: 100%;
        border-collapse: collapse;
        margin: 1.5rem 0;
        font-family: 'Lora', serif;
        font-size: 0.95rem;
    }
    
    .census-table th {
        background: #1a472a;
        color: white;
        padding: 0.75rem;
        text-align: left;
        font-family: 'Cinzel', serif;
        font-weight: bold;
    }
    
    .census-table td {
        padding: 0.75rem;
        border-bottom: 1px solid #ddd;
    }
    
    .census-table tr:nth-child(even) {
        background: #f9f9f9;
    }
    
    .census-table tr:hover {
        background: #f0f7ff;
    }
    
    .census-detail-table {
        width: 100%;
        border-collapse: collapse;
        margin: 1rem 0;
        font-family: 'Lora', serif;
        font-size: 0.9rem;
    }
    
    .census-detail-table td {
        padding: 0.5rem;
        border: 1px solid #ddd;
        vertical-align: top;
    }
    
    .census-detail-table td:first-child {
        font-weight: bold;
        background: #f5f5f5;
        width: 35%;
    }
    
    .census-header {
        font-family: 'Cinzel', serif;
        font-size: 1.3rem;
        color: #1a472a;
        margin-top: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid #c9a66b;
    }
    
    /* Media placeholder styling */
    .media-placeholder {
        background: linear-gradient(135deg, #f9f3e9 0%, #e8dfc8 100%);
        border: 2px dashed #c9a66b;
        border-radius: 8px;
        padding: 2rem;
        margin: 1.5rem 0;
        text-align: center;
        min-height: 300px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .media-placeholder-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        color: #c9a66b;
    }
    
    .media-placeholder-text {
        font-family: 'Lora', serif;
        color: #666;
        font-size: 1rem;
        max-width: 400px;
        margin-bottom: 1.5rem;
    }
    
    .youtube-button {
        background: #ff0000;
        color: white !important;
        border: none;
        border-radius: 4px;
        padding: 0.75rem 1.5rem;
        font-family: 'Cinzel', serif;
        text-decoration: none;
        display: inline-block;
        margin-top: 1rem;
        transition: all 0.3s ease;
        cursor: pointer;
        font-weight: bold;
        width: 100%;
        text-align: center;
    }
    
    .youtube-button:hover {
        background: #cc0000;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(255, 0, 0, 0.2);
        text-decoration: none;
        color: white !important;
    }
    
    /* Print-specific styles */
    @media print {
        .no-print {
            display: none !important;
        }
        
        .print-full {
            display: block !important;
        }
        
        body {
            font-size: 12pt;
            line-height: 1.5;
        }
        
        .main-header {
            font-size: 24pt;
            color: black !important;
        }
        
        .section-header {
            font-size: 18pt;
            color: black !important;
        }
        
        .media-placeholder {
            border: 1px solid #ccc !important;
            background: #f9f9f9 !important;
        }
        
        .timeline-item {
            page-break-inside: avoid !important;
        }
        
        .gift-message {
            border: 1px solid #ccc !important;
            page-break-inside: avoid !important;
        }
        
        .sidebar-content {
            display: none !important;
        }
        
        .streamlit-expanderHeader {
            display: none !important;
        }
        
        .census-detail-table {
            page-break-inside: avoid !important;
        }
    }
    
    /* Print button styling */
    .print-section {
        background: linear-gradient(135deg, #1a472a 0%, #2d5016 100%);
        padding: 2rem;
        border-radius: 8px;
        margin: 2rem 0;
        text-align: center;
    }
    
    .print-title {
        font-family: 'Cinzel', serif;
        color: white;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    /* Gift message styling */
    .gift-message {
        background: linear-gradient(135deg, #f9f3e9 0%, #e8dfc8 100%);
        border-left: 5px solid #c9a66b;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1.5rem 0;
        font-family: 'Lora', serif;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    
    /* Sidebar styling */
    .sidebar-section {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #666;
        font-family: 'Lora', serif;
        font-size: 0.9rem;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #eee;
    }
    
    /* Family tree styling */
    .family-tree {
        font-family: 'Courier New', monospace;
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #c9a76b;
        margin: 1.5rem 0;
        white-space: pre;
        overflow-x: auto;
    }
    
    /* Quote styling */
    .quote-box {
        font-family: 'Lora', serif;
        font-style: italic;
        font-size: 1.1rem;
        color: #555;
        border-left: 4px solid #c9a76b;
        padding-left: 1.5rem;
        margin: 1.5rem 0;
    }
    
    /* Timeline styling */
    .timeline-container {
        position: relative;
        padding-left: 2rem;
        margin: 2rem 0;
    }
    
    .timeline-item {
        position: relative;
        margin-bottom: 2rem;
        padding-left: 1.5rem;
    }
    
    .timeline-dot {
        position: absolute;
        left: -0.5rem;
        top: 0.3rem;
        width: 1rem;
        height: 1rem;
        background: #c9a76b;
        border-radius: 50%;
    }
    
    .timeline-line {
        position: absolute;
        left: 0;
        top: 1.3rem;
        bottom: -2rem;
        width: 2px;
        background: #e0e0e0;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem;
        }
        
        .section-header {
            font-size: 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# ==================== AUDIO/PODCAST DATA ====================
PODCAST_DATA = {
    "title": "Finding the Real Edward Burns: A Genealogical Discovery",
    "description": "This special podcast episode documents the research journey to uncover the truth about Edward J. Burns, your biological father. Follow the trail of census records, directories, and family stories that led to this remarkable discovery.",
    "recording_details": "Recorded as part of the Burns Family Story project, this audio presentation walks through the evidence and emotional journey of connecting with your Irish-American heritage.",
    "key_topics": [
        "The initial search for paternal lineage",
        "Analysis of 1940 and 1950 census records",
        "Understanding the Irish immigrant experience",
        "Connecting the dots through NYC directories",
        "The significance of the 2004 obituary",
        "What this discovery means for family identity"
    ],
    "placeholder_note": "Note: The NotebookLM audio requires Google authentication. To listen, please visit the NotebookLM link provided below.",
    "notebooklm_link": "https://notebooklm.google.com/notebook/a541026a-2fd6-4754-b63b-50cd798df7a1?artifactId=938ac9ad-a9b6-41be-ab36-3a8fe29dd84f"
}

# ==================== MEDIA SEARCH DATA ====================
MEDIA_SEARCH_DATA = {
    "ellis_island": {
        "icon": "🏛️",
        "title": "Ellis Island - Irish Immigration",
        "image_search": "Ellis Island Irish immigrants 1900s",
        "youtube_search": "Irish+immigrants+Ellis+Island+arrival+1900s+documentary",
        "youtube_title": "▶️ Watch Irish Immigrants at Ellis Island"
    },
    "irish_immigrants": {
        "icon": "🚢",
        "title": "Irish Immigration to America",
        "image_search": "Irish immigrants 19th century ship crossing Atlantic",
        "youtube_search": "Irish+immigration+to+America+1800s+coffin+ships+documentary",
        "youtube_title": "▶️ Watch Irish Immigration History"
    },
    "1940s_family": {
        "icon": "👨‍👩‍👧‍👦",
        "title": "Irish-American Family Life, 1940s",
        "image_search": "Irish American family 1940s home life photo",
        "youtube_search": "1940s+Irish+american+family+life",
        "youtube_title": "▶️ Search Irish-American 1940s Family Life"
    },
    "bronx_street": {
        "icon": "🏙️",
        "title": "Irish Neighborhoods in 1920s Bronx",
        "image_search": "Irish neighborhood Bronx 1920s street scene",
        "youtube_search": "Irish+neighborhoods+Bronx+1920s+New+York+immigrants",
        "youtube_title": "▶️ Watch Irish Bronx Neighborhoods"
    },
    "truck_1950s": {
        "icon": "🚚",
        "title": "Irish-American Workers in 1950s",
        "image_search": "Irish American truck drivers 1950s workers",
        "youtube_search": "1950s+Irish+american+workers+labor+trucking+industry",
        "youtube_title": "▶️ Search Irish-American 1950s Workers"
    }
}

# ==================== CENSUS DATA ====================
CENSUS_1940_DETAILS = [
    {"Field": "Name", "Value": "Edward Burns"},
    {"Field": "Age", "Value": "4"},
    {"Field": "Estimated Birth Year", "Value": "abt 1936 [abt 1936]"},
    {"Field": "Gender", "Value": "Male"},
    {"Field": "Race", "Value": "White"},
    {"Field": "Birthplace", "Value": "New York"},
    {"Field": "Marital Status", "Value": "Single"},
    {"Field": "Relation to Head of House", "Value": "Son"},
    {"Field": "Home in 1940", "Value": "New York, Bronx, New York"},
    {"Field": "Map of Home in 1940", "Value": "New York, Bronx, New York"},
    {"Field": "Street", "Value": "E-135 Street"},
    {"Field": "House Number", "Value": "627"},
    {"Field": "Sheet Number", "Value": "15A"},
    {"Field": "Father's Birthplace", "Value": "Scotland"},
    {"Field": "Mother's Birthplace", "Value": "Scotland"},
    {"Field": "Attended School or College", "Value": "No"},
    {"Field": "Highest Grade Completed", "Value": "None"},
    {"Field": "Native Language", "Value": "English"},
    {"Field": "Veteran", "Value": "No"},
    {"Field": "Social Security Number", "Value": "No"},
    {"Field": "Neighbors", "Value": "View others on page"}
]

CENSUS_1940_HOUSEHOLD = [
    {"Name": "James Burns", "Age": "30", "Relationship": "Head"},
    {"Name": "Sars Burns", "Age": "32", "Relationship": "Wife"},
    {"Name": "Michael Burns", "Age": "6", "Relationship": "Son"},
    {"Name": "Edward Burns", "Age": "4", "Relationship": "Son"},
    {"Name": "James Burns", "Age": "2", "Relationship": "Son"},
    {"Name": "Alice Burns", "Age": "1", "Relationship": "Daughter"}
]

CENSUS_1940_SOURCE = [
    {"Detail": "Year", "Value": "1940"},
    {"Detail": "Census Place", "Value": "New York, Bronx, New York"},
    {"Detail": "Roll", "Value": "m-t0627-02462"},
    {"Detail": "Page", "Value": "15A"},
    {"Detail": "Enumeration District", "Value": "3-94"},
    {"Detail": "Source", "Value": "Ancestry.com. 1940 United States Federal Census [database on-line]. Provo, UT, USA: Ancestry.com Operations, Inc., 2012."},
    {"Detail": "Original Data", "Value": "United States of America, Bureau of the Census. Sixteenth Census of the United States, 1940. Washington, D.C.: National Archives and Records Administration, 1940. T627, 4,643 rolls."}
]

CENSUS_1950_DETAILS = [
    {"Field": "Name", "Value": "Edward Burns"},
    {"Field": "Age", "Value": "14"},
    {"Field": "Birth Date", "Value": "abt 1936 [abt 1936]"},
    {"Field": "Gender", "Value": "Male"},
    {"Field": "Race", "Value": "White"},
    {"Field": "Birth Place", "Value": "New York"},
    {"Field": "Marital Status", "Value": "Never Married (Single)"},
    {"Field": "Relation to Head of House", "Value": "Son"},
    {"Field": "Residence Date", "Value": "1950"},
    {"Field": "Home in 1950", "Value": "Los Angeles, Los Angeles, California, USA"},
    {"Field": "Street Name", "Value": "Caledonia Way"},
    {"Field": "House Number", "Value": "4547"},
    {"Field": "Dwelling Number", "Value": "139"},
    {"Field": "Farm", "Value": "No"},
    {"Field": "Acres", "Value": "No"},
    {"Field": "Occupation Category", "Value": "Other"},
    {"Field": "Worked Last Week", "Value": "No"},
    {"Field": "Seeking Work", "Value": "No"},
    {"Field": "Employment Status", "Value": "No"}
]

CENSUS_1950_HOUSEHOLD = [
    {"Name": "James Burns", "Age": "40", "Relationship": "Head"},
    {"Name": "Sarah Burns", "Age": "42", "Relationship": "Wife"},
    {"Name": "Michael Burns", "Age": "16", "Relationship": "Son"},
    {"Name": "Edward Burns", "Age": "14", "Relationship": "Son"},
    {"Name": "James Burns", "Age": "12", "Relationship": "Son"},
    {"Name": "Alice Burns", "Age": "11", "Relationship": "Daughter"},
    {"Name": "Rose Burns", "Age": "9", "Relationship": "Daughter"},
    {"Name": "Joseph Burns", "Age": "7", "Relationship": "Son"},
    {"Name": "Peter Burns", "Age": "4", "Relationship": "Son"},
    {"Name": "John Burns", "Age": "2", "Relationship": "Son"}
]

CENSUS_1950_SOURCE = [
    {"Detail": "Year", "Value": "1950"},
    {"Detail": "Census Place", "Value": "Los Angeles, Los Angeles, California"},
    {"Detail": "Roll", "Value": "1560"},
    {"Detail": "Page", "Value": "12"},
    {"Detail": "Enumeration District", "Value": "66-300"},
    {"Detail": "Source", "Value": "Ancestry.com. 1950 United States Federal Census [database on-line]. Lehi, UT, USA: Ancestry.com Operations, Inc., 2022."},
    {"Detail": "Original Data", "Value": "Department of Commerce. Bureau of the Census. 1913-1/1/1972. Population Schedules for the 1950 Census, 1950-1950. Washington, DC: National Archives at Washington, DC."},
    {"Detail": "NARA ID", "Value": "NAID: 43290879"},
    {"Detail": "Record Group", "Value": "Records of the Bureau of the Census, 1790-2007, Record Group 29"}
]

# ==================== UTILITY FUNCTIONS ====================
def display_podcast_section():
    """Display the podcast/audio section"""
    st.markdown(f"""
    <div class="audio-section">
        <div class="audio-title">🔊 {PODCAST_DATA["title"]}</div>
        <div class="audio-description">
            {PODCAST_DATA["description"]}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎧 Listen to the Discovery Podcast")
    
    # NotebookLM Link (Not embeddable due to authentication)
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #4285f4 0%, #34a853 100%);
                padding: 2rem;
                border-radius: 12px;
                margin: 1.5rem 0;
                text-align: center;">
        <h3 style="color: white; font-family: 'Cinzel', serif; margin-bottom: 1rem;">📘 Access the NotebookLM Audio</h3>
        <p style="color: white; font-family: 'Lora', serif; margin-bottom: 1.5rem;">
            Click the button below to open the NotebookLM notebook containing the audio documentary.
            You'll need to sign in with your Google account.
        </p>
        <a href="{PODCAST_DATA['notebooklm_link']}" target="_blank" style="text-decoration: none;">
            <button style="background: white;
                          color: #4285f4;
                          border: none;
                          border-radius: 6px;
                          padding: 1rem 2rem;
                          font-family: 'Cinzel', serif;
                          font-weight: bold;
                          font-size: 1.1rem;
                          cursor: pointer;
                          transition: all 0.3s ease;">
                🔓 Open NotebookLM Audio
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Alternative: Provide instructions for downloading/exporting
    st.markdown("---")
    st.markdown("### 📥 Alternative: Export from NotebookLM")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **To embed audio here:**
        1. In NotebookLM, click the 3-dot menu next to audio
        2. Select "Export" or "Download"
        3. Save as MP3 file
        4. Upload to a public hosting service
        5. Replace the placeholder below with your link
        """)
    
    with col2:
        st.markdown("""
        **Recommended hosting:**
        • Google Drive (make public)
        • Dropbox (get shareable link)
        • SoundCloud (free tier)
        • Your own web server
        """)
    
    # Placeholder for future audio embedding
    st.markdown("### 🎵 Audio Player Placeholder")
    placeholder_audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    st.audio(placeholder_audio_url, format="audio/mp3")
    st.caption("*Example placeholder audio. Replace with your NotebookLM podcast once exported and hosted publicly.*")
    
    # Podcast details
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Recording Details:**")
        st.markdown(PODCAST_DATA["recording_details"])
    
    with col2:
        st.markdown("**Key Topics Covered:**")
        for topic in PODCAST_DATA["key_topics"]:
            st.markdown(f"• {topic}")
    
    st.markdown(f"""
    <div class="audio-note">
        <strong>Note:</strong> {PODCAST_DATA["placeholder_note"]}
    </div>
    """, unsafe_allow_html=True)

def display_media_search(media_key, caption):
    """Display search options for images and YouTube videos"""
    if media_key in MEDIA_SEARCH_DATA:
        media_info = MEDIA_SEARCH_DATA[media_key]
        
        # Create the placeholder container
        st.markdown(f"""
        <div class="media-placeholder">
            <div class="media-placeholder-icon">{media_info['icon']}</div>
            <h3 style="font-family: 'Cinzel', serif; color: #1a472a; margin-bottom: 0.5rem;">{caption}</h3>
            <div class="media-placeholder-text">
                <p><strong>To find related images:</strong></p>
                <p>Search online for: "{media_info['image_search']}"</p>
                <p><em>Recommended sources: Library of Congress, National Archives</em></p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Create columns for the button
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            # YouTube Search Button
            youtube_search_url = f"https://www.youtube.com/results?search_query={media_info['youtube_search']}"
            st.markdown(f"""
            <a href="{youtube_search_url}" target="_blank" style="text-decoration: none;">
                <button class="youtube-button">
                    {media_info['youtube_title']}
                </button>
            </a>
            """, unsafe_allow_html=True)
    else:
        st.info(f"*Media placeholder: {caption}*")

def display_census_full_details(census_year):
    """Display FULL census details with expandable sections"""
    if census_year == 1940:
        details = CENSUS_1940_DETAILS
        household = CENSUS_1940_HOUSEHOLD
        source = CENSUS_1940_SOURCE
        year_label = "1940"
        address = "627 E-135 Street, Bronx, New York"
    else:
        details = CENSUS_1950_DETAILS
        household = CENSUS_1950_HOUSEHOLD
        source = CENSUS_1950_SOURCE
        year_label = "1950"
        address = "4547 Caledonia Way, Los Angeles, California"
    
    # Create columns for layout
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f'<div class="census-header">{year_label} Census - Edward Burns</div>', unsafe_allow_html=True)
        st.markdown(f"**Address:** {address}")
    
    with col2:
        st.markdown(f"**Age:** {details[1]['Value']}")
        st.markdown(f"**Birth Year:** {details[2]['Value'].split('[')[0].strip()}")
    
    # Individual Details Table
    with st.expander(f"📋 View ALL {year_label} Census Details for Edward Burns", expanded=True):
        st.markdown("**Complete Individual Record:**")
        
        # Create two columns for the details table
        for i in range(0, len(details), 10):
            cols = st.columns(2)
            for j in range(2):
                idx = i + (j * 5)
                if idx < len(details):
                    with cols[j]:
                        for k in range(5):
                            if idx + k < len(details):
                                item = details[idx + k]
                                st.markdown(f"**{item['Field']}:** {item['Value']}")
    
    # Household Members
    with st.expander(f"👨‍👩‍👧‍👦 View {year_label} Household Members"):
        household_df = pd.DataFrame(household)
        st.table(household_df)
    
    # Source Information
    with st.expander(f"📚 View {year_label} Source Information"):
        for item in source:
            st.markdown(f"**{item['Detail']}:** {item['Value']}")
    
    # Quick Summary Box
    st.info(f"""
    **{year_label} Census Summary:**
    - **Name:** Edward Burns
    - **Age:** {details[1]['Value']}
    - **Location:** {address}
    - **Household Size:** {len(household)} people
    - **Relationship:** {details[7]['Value']}
    - **Birthplace:** {details[5]['Value']}
    """)

def display_family_tree():
    """Display the family tree in a formatted way"""
    tree_text = """
    James BURNS (Ireland) + Catherine (Ireland)
            |
            ├── Edward J. BURNS (1936-2004) = Virginia GONZALEZ
            │               │
            │               └── **Edward "Eddie" BYRNES (You)**
            │
            ├── John Burns (Bronx)
            ├── James Burns (Florida)
            ├── Michael Burns (Pennsylvania)
            └── Catherine Ryan (Staten Island)
    """
    st.markdown(f'<div class="family-tree">{tree_text}</div>', unsafe_allow_html=True)

def create_timeline_item(year, event):
    """Create a timeline item with custom styling"""
    st.markdown(f"""
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-line"></div>
        <div style="font-family: 'Cinzel', serif; font-weight: 700; color: #c9a76b; font-size: 1.5rem; margin-bottom: 0.5rem;">
            {year}
        </div>
        <div style="font-family: 'Lora', serif; font-size: 1.1rem; line-height: 1.5; color: #333;">
            {event}
        </div>
    </div>
    """, unsafe_allow_html=True)

def generate_printable_html():
    """Generate complete HTML for printing/downloading"""
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>The Burns Family Story - Complete Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }}
            .header {{
                text-align: center;
                border-bottom: 3px solid #1a472a;
                padding-bottom: 20px;
                margin-bottom: 30px;
            }}
            h1 {{
                color: #1a472a;
                font-size: 36px;
                margin-bottom: 10px;
            }}
            h2 {{
                color: #1a472a;
                border-bottom: 2px solid #c9a66b;
                padding-bottom: 5px;
                margin-top: 30px;
            }}
            h3 {{
                color: #2d5016;
            }}
            .subtitle {{
                font-style: italic;
                color: #666;
                font-size: 18px;
            }}
            .section {{
                margin-bottom: 30px;
                page-break-inside: avoid;
            }}
            .census-table {{
                width: 100%;
                border-collapse: collapse;
                margin: 15px 0;
            }}
            .census-table th {{
                background: #1a472a;
                color: white;
                padding: 10px;
                text-align: left;
            }}
            .census-table td {{
                padding: 8px;
                border-bottom: 1px solid #ddd;
            }}
            .census-table tr:nth-child(even) {{
                background: #f9f9f9;
            }}
            .note-box {{
                background: #f9f3e9;
                border-left: 5px solid #c9a66b;
                padding: 15px;
                margin: 20px 0;
                border-radius: 5px;
            }}
            .timeline {{
                position: relative;
                padding-left: 30px;
                margin: 20px 0;
            }}
            .timeline-item {{
                margin-bottom: 20px;
                position: relative;
            }}
            .timeline-year {{
                font-weight: bold;
                color: #c9a76b;
                font-size: 18px;
            }}
            .family-tree {{
                font-family: monospace;
                background: #f8f9fa;
                padding: 20px;
                border-radius: 5px;
                border-left: 4px solid #c9a76b;
                white-space: pre;
                overflow-x: auto;
            }}
            .footer {{
                margin-top: 50px;
                padding-top: 20px;
                border-top: 1px solid #eee;
                text-align: center;
                color: #666;
                font-size: 14px;
            }}
            @media print {{
                .page-break {{
                    page-break-before: always;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>The Burns Family Story</h1>
            <div class="subtitle">A Genealogical Discovery for Edward "Eddie" Byrnes</div>
            <div>Generated: {datetime.now().strftime('%B %d, %Y')}</div>
        </div>
        
        <div class="section">
            <h2>Executive Summary</h2>
            <p>This report documents the discovery of Edward J. Burns (1936-2004) as the biological father of Edward "Eddie" Byrnes. Through census records, vital records, and genealogical research, we have traced the Irish-American heritage of the Burns family.</p>
        </div>
        
        <div class="section">
            <h2>Family Tree</h2>
            <div class="family-tree">
    James BURNS (Ireland) + Catherine (Ireland)
            |
            ├── Edward J. BURNS (1936-2004) = Virginia GONZALEZ
            │               │
            │               └── <strong>Edward "Eddie" BYRNES (You)</strong>
            │
            ├── John Burns (Bronx)
            ├── James Burns (Florida)
            ├── Michael Burns (Pennsylvania)
            └── Catherine Ryan (Staten Island)
            </div>
        </div>
        
        <div class="page-break"></div>
        
        <div class="section">
            <h2>1940 Census Record</h2>
            <p><strong>Address:</strong> 627 E-135 Street, Bronx, New York</p>
            
            <h3>Edward Burns - Individual Details</h3>
            <table class="census-table">
    """
    
    # Add 1940 census details
    for item in CENSUS_1940_DETAILS:
        html_content += f"""
                <tr>
                    <td><strong>{item['Field']}</strong></td>
                    <td>{item['Value']}</td>
                </tr>
        """
    
    html_content += """
            </table>
            
            <h3>1940 Household Members</h3>
            <table class="census-table">
                <tr>
                    <th>Name</th>
                    <th>Age</th>
                    <th>Relationship</th>
                </tr>
    """
    
    for member in CENSUS_1940_HOUSEHOLD:
        html_content += f"""
                <tr>
                    <td>{member['Name']}</td>
                    <td>{member['Age']}</td>
                    <td>{member['Relationship']}</td>
                </tr>
        """
    
    html_content += """
            </table>
        </div>
        
        <div class="page-break"></div>
        
        <div class="section">
            <h2>1950 Census Record</h2>
            <p><strong>Address:</strong> 4547 Caledonia Way, Los Angeles, California</p>
            
            <h3>Edward Burns - Individual Details</h3>
            <table class="census-table">
    """
    
    # Add 1950 census details
    for item in CENSUS_1950_DETAILS:
        html_content += f"""
                <tr>
                    <td><strong>{item['Field']}</strong></td>
                    <td>{item['Value']}</td>
                </tr>
        """
    
    html_content += """
            </table>
            
            <h3>1950 Household Members</h3>
            <table class="census-table">
                <tr>
                    <th>Name</th>
                    <th>Age</th>
                    <th>Relationship</th>
                </tr>
    """
    
    for member in CENSUS_1950_HOUSEHOLD:
        html_content += f"""
                <tr>
                    <td>{member['Name']}</td>
                    <td>{member['Age']}</td>
                    <td>{member['Relationship']}</td>
                </tr>
        """
    
    html_content += """
            </table>
        </div>
        
        <div class="section">
            <h2>Key Timeline</h2>
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-year">1936</div>
                    <div>Edward J. Burns born in New York</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">1940</div>
                    <div>Edward (age 4) appears in Bronx census with parents and siblings</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">1950</div>
                    <div>Edward (age 14) appears in Los Angeles census with guardians</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">1957</div>
                    <div>Edward J. Burns marries Virginia Gonzalez in NYC</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">1958</div>
                    <div>Edward "Eddie" Byrnes born</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">2004</div>
                    <div>Edward J. Burns passes away in New Jersey</div>
                </div>
            </div>
        </div>
        
        <div class="section">
            <div class="note-box">
                <h3>Research Notes</h3>
                <p>This report is based on publicly available records and represents the current state of research. For legal confirmation, additional steps such as obtaining birth certificates or DNA testing are recommended.</p>
            </div>
        </div>
        
        <div class="footer">
            <p><strong>Sources:</strong> 1940 & 1950 U.S. Census • NYC Marriage Index • Social Security Death Index • Newark Star-Ledger Obituary</p>
            <p><strong>Presented as a birthday gift • Created with Streamlit</strong></p>
        </div>
    </body>
    </html>
    """
    
    return html_content

def create_print_section():
    """Create the print section with working download"""
    st.markdown("""
    <div class="print-section">
        <div class="print-title">📄 Download Complete Presentation</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Create the HTML content for printing
    html_content = generate_printable_html()
    
    # Create download button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.download_button(
            label="⬇️ DOWNLOAD PRINTABLE VERSION (HTML)",
            data=html_content,
            file_name="Burns_Family_Story_Full_Presentation.html",
            mime="text/html",
            help="Download complete presentation as HTML file for printing",
            use_container_width=True,
            type="primary"
        )
    
    st.info("""
    **Print Instructions:**
    1. Click the button above to download the HTML file
    2. Open the downloaded file in your web browser (Chrome, Firefox, Edge, Safari)
    3. Press **Ctrl+P** (Windows) or **Cmd+P** (Mac) to open print dialog
    4. Choose "Save as PDF" to create a digital copy, or select your printer
    5. For best results, choose "Portrait" orientation and "Fit to page"
    
    **The printable version includes:** All census details, family tree, timeline, and complete narrative.
    """)

# ==================== PAGE CONTENT FUNCTIONS ====================
def introduction_page():
    """Display the introduction page"""
    st.markdown('<div class="main-header">The Burns Family Story</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">A Genealogical Discovery for Edward "Eddie" Byrnes</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="gift-message">
            <h3 style="color: #1a472a; font-family: 'Cinzel', serif; margin-top: 0;">🎁 A Birthday Gift of Heritage</h3>
            <p>This interactive presentation represents months of genealogical research into your paternal lineage. 
            Through census records, directories, and historical documents, we've uncovered the story of your 
            biological father and your Irish-American heritage.</p>
            
            <p><strong>What you'll discover:</strong></p>
            <ul>
                <li>Your father's identity: Edward J. Burns (1936-2004)</li>
                <li>Your Irish immigrant roots on both sides of his family</li>
                <li>The Burns family journey from Ireland to America</li>
                <li>Documentary evidence from official records</li>
                <li>A timeline of key family events</li>
            </ul>
            
            <p><em>Use the sidebar to navigate through each chapter of this discovery.</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📋 Quick Facts")
        st.markdown("""
        **Your Father:**
        • Edward J. Burns
        • Born: Jan 4, 1936
        • Died: May 12, 2004
        • Married: Virginia Gonzalez (1957)
        
        **Your Heritage:**
        • Irish-American
        • New York roots
        • Working-class background
        """)
    
    st.markdown("---")
    
    # Family Tree Preview
    st.markdown("### 🌳 Your Family Tree (Preview)")
    display_family_tree()

def irish_roots_page():
    """Display the Irish roots page"""
    st.markdown('<div class="main-header">Irish Roots</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">The Burns Family Journey from Ireland</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="gift-message">
        <h3 style="color: #1a472a; font-family: 'Cinzel', serif; margin-top: 0;">🇮🇪 The Irish Connection</h3>
        <p>The Burns surname originates from Scotland and Ireland, with strong connections to both countries. 
        Your Burns ancestors likely came from Ireland during the great waves of Irish immigration 
        in the late 19th and early 20th centuries.</p>
        
        <p>The name "Burns" (sometimes spelled "Byrnes" or "O'Byrne") is an anglicized form of the 
        Gaelic "Ó Broin," meaning "descendant of Bran." The Burns family would have been part of 
        the mass Irish diaspora seeking better opportunities in America.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Media Search for Irish Immigration
    display_media_search("irish_immigrants", "Irish Immigration to America")
    
    st.markdown("---")
    
    # Irish Immigration Facts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Irish Immigration Facts")
        st.markdown("""
        **Great Irish Migration (1845-1855):**
        • 1.5 million Irish came to America
        • Escaping the Potato Famine
        • Mostly settled in Northeast cities
        
        **Irish in New York:**
        • By 1855, 26% of NYC was Irish-born
        • Concentrated in Five Points, Hell's Kitchen
        • Worked as laborers, domestics, police, firefighters
        """)
    
    with col2:
        st.markdown("### 🏙️ Irish Neighborhoods")
        st.markdown("""
        **The Bronx (1940s):**
        • Strong Irish communities
        • Parish churches as community centers
        • Working-class neighborhoods
        • Family-oriented culture
        
        **Cultural Legacy:**
        • Catholic faith
        • Labor movement participation
        • Political involvement
        • Strong family values
        """)
    
    # Ellis Island Section
    st.markdown("---")
    display_media_search("ellis_island", "Ellis Island Arrival")

def journey_to_america_page():
    """Display the journey to America page"""
    st.markdown('<div class="main-header">Journey to America</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">From Irish Shores to American Streets</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="quote-box">
        "They came in search of freedom, opportunity, and a better life for their children. 
        They brought with them their faith, their resilience, and their dreams."
    </div>
    """, unsafe_allow_html=True)
    
    # Timeline of the Journey
    st.markdown("### 📅 The Burns Family Timeline in America")
    
    st.markdown('<div class="timeline-container">', unsafe_allow_html=True)
    create_timeline_item("Late 1800s", "James Burns (your great-grandfather) immigrates from Ireland to the United States, likely arriving at Ellis Island.")
    create_timeline_item("Early 1900s", "The Burns family establishes roots in New York City, part of the large Irish immigrant community.")
    create_timeline_item("1936", "Edward J. Burns (your father) is born in New York, first-generation American.")
    create_timeline_item("1940", "Edward appears in the Bronx census at age 4, living with parents and siblings.")
    create_timeline_item("1950", "Edward appears in Los Angeles census at age 14, indicating family relocation.")
    create_timeline_item("1957", "Edward marries Virginia Gonzalez in New York City.")
    create_timeline_item("1958", "You are born - continuing the Burns family legacy in America.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # The Bronx in the 1940s
    display_media_search("bronx_street", "Irish Neighborhoods in 1920s-1940s Bronx")
    
    # Family Life
    st.markdown("### 👨‍👩‍👧‍👦 Family Life in Mid-Century America")
    display_media_search("1940s_family", "Irish-American Family Life, 1940s")

def family_timeline_page():
    """Display the family timeline page"""
    st.markdown('<div class="main-header">Family Timeline</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Key Events in the Burns Family History</div>', unsafe_allow_html=True)
    
    # Complete Timeline
    st.markdown("### 📜 Complete Family Timeline")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🏴󠁧󠁢󠁳󠁣󠁴󠁿 **Irish Origins**")
        st.markdown("""
        **1800s:**
        • Burns family lives in Ireland
        • Likely farmers or laborers
        • Catholic faith
        
        **Late 1800s:**
        • Great-grandfather James emigrates
        • Arrives at Ellis Island
        • Settles in New York area
        """)
        
        st.markdown("#### 🇺🇸 **Early American Years**")
        st.markdown("""
        **1900-1935:**
        • Family establishes in NYC
        • Working-class occupations
        • Builds community in Irish neighborhoods
        • Maintains Irish cultural traditions
        """)
    
    with col2:
        st.markdown("#### 👶 **Edward's Generation**")
        st.markdown("""
        **1936:**
        • Edward J. Burns born
        
        **1940:**
        • Age 4 in Bronx census
        • Living with parents & 3 siblings
        
        **1950:**
        • Age 14 in LA census
        • Living with guardians & 7 siblings
        """)
        
        st.markdown("#### 👨‍👩‍👦 **Your Generation**")
        st.markdown("""
        **1957:**
        • Edward marries Virginia
        
        **1958:**
        • You are born
        
        **2004:**
        • Edward passes away
        
        **Present:**
        • Discovery of heritage
        • Connection to living relatives
        """)
    
    st.markdown("---")
    
    # Family Tree
    st.markdown("### 🌳 Complete Family Tree")
    display_family_tree()

def evidence_page():
    """Display the evidence page"""
    st.markdown('<div class="main-header">Documented Evidence</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Research Sources & Verification</div>', unsafe_allow_html=True)
    
    # Updated tabs to include Podcast
    tab1, tab2, tab3, tab4 = st.tabs(["📋 Census Records", "📜 Vital Records", "🔊 Podcast Discovery", "🖨️ Print Full Report"])
    
    with tab1:
        st.markdown("### U.S. Census Records")
        
        # 1940 Census Section
        st.markdown("#### 1940 Census - Edward Burns (Age 4)")
        display_census_full_details(1940)
        
        st.markdown("---")
        
        # 1950 Census Section
        st.markdown("#### 1950 Census - Edward Burns (Age 14)")
        display_census_full_details(1950)
        
        # Census Analysis
        st.markdown("### 📊 Census Analysis")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **1940 Census Significance:**
            • Earliest official record of Edward J. Burns
            • Shows him at age 4 in the Bronx
            • Confirms New York birth
            • Shows family unit before separation
            • Parents' birthplace listed as Scotland (likely error for Ireland)
            """)
        
        with col2:
            st.markdown("""
            **1950 Census Significance:**
            • Shows Edward at age 14 in Los Angeles
            • Indicates family separation between 1940-1950
            • Shows complex family situation during adolescence
            • Household includes 8 children total
            • Edward not working or seeking work (typical for 14-year-old)
            """)
    
    with tab2:
        st.markdown("### Vital Records")
        
        st.markdown("#### Social Security Death Index")
        st.info("""
        **Edward J. Burns**
        • Born: January 4, 1936
        • Died: May 12, 2004
        • Last Residence: Belleville, NJ
        """)
        
        st.markdown("#### Marriage Index")
        st.info("""
        **Edward J. Burns to Virginia A. Gonzalez**
        • Marriage Date: November 16, 1957
        • Location: New York City, New York
        """)
        
        st.markdown("#### Obituary (Newark Star-Ledger, May 14, 2004)")
        st.success("""
        "Survived by his beloved wife, Virginia (Gonzalez) Burns; his loving son, Edward 'Eddie' Byrnes...
        Also survived by brothers John of Bronx, NY; James of Florida; Michael of Pennsylvania."
        """)
        
        st.markdown("#### NYC Directories")
        st.markdown("""
        **Edward J. Burns**
        • 1958: Truck driver, 1075 Tiffany St, Bronx  
        • 1960: Clerk, 160 Amsterdam Ave, Manhattan  
        • 1962: Mechanic, 321 S. Oxford St, Brooklyn
        
        **John Burns (Brother)**
        • 1958-1968: Consistently at 1075 Tiffany St, Bronx  
        • Occupations: Clerk, Driver
        """)
    
    with tab3:
        st.markdown("## 🔊 The Discovery Podcast")
        st.markdown("### Finding the Real Edward Burns")
        
        # Display the podcast section
        display_podcast_section()
        
        # Additional context about the research
        st.markdown("---")
        st.markdown("### 🎙️ About This Audio Documentary")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **The Research Journey:**
            • Months of genealogical investigation
            • Analysis of historical documents
            • Interviews with family members
            • Verification through multiple sources
            """)
        
        with col2:
            st.markdown("""
            **Key Breakthroughs:**
            • Connecting census records across decades
            • Understanding Irish immigrant patterns
            • Tracing the Burns family movements
            • Corroborating evidence from multiple sources
            """)
        
        st.markdown('<div class="gift-message">', unsafe_allow_html=True)
        st.markdown("""
        **Listener's Note:** This audio presentation complements the written evidence 
        in this presentation. Hearing the story narrated adds emotional depth to 
        the factual discovery of your biological father and Irish-American heritage.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab4:
        st.markdown("## 📄 Complete Printable Report")
        create_print_section()
        
        st.markdown("### 🔍 How to Verify Absolutely")
        st.markdown("""
        1. **Order Eddie's birth certificate** (NYC Vital Records)  
           - Will list father's name, age, residence
        
        2. **Order marriage certificate** (Edward & Virginia, 1957)  
           - Will list Edward's parents' names
        
        3. **DNA testing** (AncestryDNA, 23andMe)  
           - Match with Burns relatives' descendants
        
        4. **Contact Greco Funeral Home** (Lyndhurst, NJ)  
           - Ask who provided obituary details
        """)
        
        st.markdown('<div class="gift-message">', unsafe_allow_html=True)
        st.markdown("""
        **Note:** This presentation provides strong circumstantial evidence. 
        The steps above would provide legal and biological confirmation.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

def birthday_message_page():
    """Display the birthday message page"""
    st.markdown('<div class="main-header">Happy Birthday, Eddie!</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">A Gift of Heritage and Identity</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin: 3rem 0;">
        <div style="font-size: 6rem; margin-bottom: 2rem;">🎂</div>
        <h2 style="font-family: 'Cinzel', serif; color: #1a472a;">Happy Birthday!</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="gift-message">
            <h3 style="color: #1a472a; font-family: 'Cinzel', serif; margin-top: 0;">Dear Eddie,</h3>
            
            <p>On your birthday, I wanted to give you something more meaningful than a traditional gift. 
            This presentation represents the discovery of your biological father and your Irish-American heritage.</p>
            
            <p>For years, there were questions about your paternal lineage. Through careful research 
            and examination of historical records, we can now say with confidence:</p>
            
            <p><strong>Your father was Edward J. Burns (1936-2004), an Irish-American New Yorker.</strong></p>
            
            <p>This discovery connects you to a rich heritage of Irish immigrants who came to America 
            seeking better lives, who worked hard, raised families, and contributed to this country.</p>
            
            <p>You come from resilient people. People who crossed an ocean for opportunity. 
            People who built communities in a new land while maintaining their cultural identity.</p>
            
            <p>This is your story. This is your heritage. And now, it's yours to know, to claim, 
            and to pass on to future generations.</p>
            
            <p>Happy Birthday, with love and admiration for the man you are and the heritage you carry.</p>
            
            <p style="text-align: right; font-style: italic; margin-top: 2rem;">With love,<br>Your family</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🎁 Your Birthday Gift Includes:")
        st.markdown("""
        • **Identity:** Knowing your biological father
        • **Heritage:** Your Irish-American roots
        • **Family:** Connection to living relatives
        • **History:** Your family's American journey
        • **Documents:** Official records as proof
        • **Story:** The narrative of your origins
        """)
        
        st.markdown("---")
        
        st.markdown("### 📞 Next Steps")
        st.markdown("""
        **If you want to explore further:**
        1. DNA test (Ancestry/23andMe)
        2. Contact Burns relatives
        3. Visit Irish cultural centers
        4. Research Burns family history
        """)
    
    st.markdown("---")
    
    # Final family tree display
    st.markdown("### 🌳 Your Complete Heritage")
    display_family_tree()

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown('<div class="main-header" style="font-size: 2rem;">The Burns Family</div>', unsafe_allow_html=True)
    
    # Navigation
    st.markdown("### 📖 Navigation")
    page = st.radio(
        "Choose a chapter:",
        ["🎁 Introduction", "🇮🇪 Irish Roots", "🛳️ Journey to America", 
         "📅 Family Timeline", "🔍 Evidence", "💝 Birthday Message"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # New Podcast quick link in sidebar
    st.markdown("### 🔊 Podcast")
    st.markdown("""
    **Finding the Real Edward Burns**
    
    Listen to the audio documentary of this genealogical discovery.
    
    *Available in the Evidence section*
    """)
    
    st.markdown("---")
    
    # Print Section
    st.markdown("### 🖨️ Print Options")
    if st.button("📄 Generate Printable Version", use_container_width=True, type="primary"):
        st.session_state.show_print = True
    
    st.markdown("---")
    
    # Census Quick Facts
    st.markdown("### 📋 Census Quick Facts")
    
    with st.expander("1940 Census"):
        st.markdown("""
        **Edward Burns, Age 4**
        • Address: 627 E-135 St, Bronx
        • Parents: James & Sars Burns
        • Birthplace: New York
        • Father's Birthplace: Scotland
        • Mother's Birthplace: Scotland
        """)
    
    with st.expander("1950 Census"):
        st.markdown("""
        **Edward Burns, Age 14**
        • Address: 4547 Caledonia Way, LA
        • Guardians: James & Sarah Burns
        • Birthplace: New York
        • Household: 10 people total
        • Not working/Not seeking work
        """)
    
    st.markdown("---")
    
    # Key Dates
    st.markdown("### 📅 Key Dates")
    st.markdown("""
    **Edward J. Burns**  
    • Born: Jan 4, 1936  
    • Died: May 12, 2004
    
    **Eddie Byrnes**  
    • Born: Jan 27, 1958
    """)
    
    st.markdown("---")
    st.markdown("*A genealogical gift for Eddie*")

# ==================== PAGE ROUTING ====================
if page == "🎁 Introduction":
    introduction_page()
elif page == "🇮🇪 Irish Roots":
    irish_roots_page()
elif page == "🛳️ Journey to America":
    journey_to_america_page()
elif page == "📅 Family Timeline":
    family_timeline_page()
elif page == "🔍 Evidence":
    evidence_page()
elif page == "💝 Birthday Message":
    birthday_message_page()

# ==================== FOOTER ====================
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.markdown("""
**Sources:** 1940 & 1950 U.S. Census • NYC Marriage Index • Social Security Death Index • Newark Star-Ledger Obituary  
**Presented as a birthday gift** • Created with Streamlit
""")
st.markdown('</div>', unsafe_allow_html=True)

# ==================== SESSION STATE INITIALIZATION ====================
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
if 'show_print' not in st.session_state:
    st.session_state.show_print = False

# Show print section if requested
if st.session_state.get('show_print', False):
    st.markdown("---")
    st.markdown("## 📄 Printable Version")
    create_print_section()
    st.session_state.show_print = False
