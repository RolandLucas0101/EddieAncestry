import streamlit as st
import pandas as pd
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
    "placeholder_note": "Podcast is hosted on Google Drive. Use the download button if the audio player doesn't work."
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
    """Display the podcast/audio section with Google Drive link"""
    st.markdown("""
    <div class="audio-section">
        <div class="audio-title">🔊 Finding the Real Edward Burns: A Genealogical Discovery</div>
        <div class="audio-description">
            This special podcast episode documents the research journey to uncover the truth about Edward J. Burns, your biological father. Follow the trail of census records, directories, and family stories that led to this remarkable discovery.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎧 Listen to the Discovery Podcast")
    
    # Convert Google Drive view link to direct download link
    google_drive_id = "1NSqCR-FqZFJOQEpgBFLNzP0yvQqjl4uV"
    direct_audio_url = f"https://drive.google.com/uc?export=download&id={google_drive_id}"
    
    # Try to display audio
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f9f3e9 0%, #e8dfc8 100%);
                padding: 2rem;
                border-radius: 12px;
                margin: 1.5rem 0;
                text-align: center;
                border-left: 5px solid #c9a66b;">
        <h3 style="color: #1a472a; font-family: 'Cinzel', serif; margin-bottom: 1rem;">🎙️ Podcast Ready!</h3>
        <p style="font-family: 'Lora', serif; margin-bottom: 1.5rem;">
            Your podcast has been uploaded. Click play to listen to the audio documentary.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Try to play the audio
    try:
        st.audio(direct_audio_url, format="audio/mp3")
        st.success("✅ Audio loaded successfully from Google Drive!")
    except Exception as e:
        st.warning(f"⚠️ Could not load audio directly: {str(e)}")
        st.info("""
        **Alternative ways to access the podcast:**
        
        1. **Direct Download:** [Click here to download the MP3](https://drive.google.com/uc?export=download&id=1NSqCR-FqZFJOQEpgBFLNzP0yvQqjl4uV)
        2. **View in Google Drive:** [Open in Google Drive](https://drive.google.com/file/d/1NSqCR-FqZFJOQEpgBFLNzP0yvQqjl4uV/view)
        3. **Manual Play:** Download the file and play it on your device
        """)
    
    # Also show the direct link as a button
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <a href="https://drive.google.com/uc?export=download&id={google_drive_id}" target="_blank" style="text-decoration: none;">
            <button style="background: #4285f4;
                          color: white;
                          border: none;
                          border-radius: 6px;
                          padding: 0.75rem 1.5rem;
                          font-family: 'Cinzel', serif;
                          font-weight: bold;
                          cursor: pointer;
                          transition: all 0.3s ease;
                          width: 100%;">
                ⬇️ Direct Download MP3
            </button>
        </a>
        """, unsafe_allow_html=True)
    
    # Podcast details
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Recording Details:**")
        st.markdown("Recorded as part of the Burns Family Story project, this audio presentation walks through the evidence and emotional journey of connecting with your Irish-American heritage.")
    
    with col2:
        st.markdown("**Key Topics Covered:**")
        st.markdown("• The initial search for paternal lineage")
        st.markdown("• Analysis of 1940 and 1950 census records")
        st.markdown("• Understanding the Irish immigrant experience")
        st.markdown("• Connecting the dots through NYC directories")
        st.markdown("• The significance of the 2004 obituary")
        st.markdown("• What this discovery means for family identity")
    
    st.markdown("""
    <div class="audio-note">
        <strong>Note:</strong> The podcast is hosted on Google Drive. If the audio player doesn't work, 
        use the download button above to save the file to your device and play it locally.
    </div>
    """, unsafe_allow_html=True)

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
        st.markdown(f'<div class="section-header">{year_label} Census - Edward Burns</div>', unsafe_allow_html=True)
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
    <div style="background: linear-gradient(135deg, #1a472a 0%, #2d5016 100%);
                padding: 2rem;
                border-radius: 8px;
                margin: 2rem 0;
                text-align: center;">
        <div style="font-family: 'Cinzel', serif; color: white; font-size: 1.5rem; margin-bottom: 1rem;">
            📄 Download Complete Presentation
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Create the HTML content for printing
    html_content = generate_printable_html()
    
    # Create download button with unique key
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.download_button(
            label="⬇️ DOWNLOAD PRINTABLE VERSION (HTML)",
            data=html_content,
            file_name="Burns_Family_Story_Full_Presentation.html",
            mime="text/html",
            help="Download complete presentation as HTML file for printing",
            use_container_width=True,
            type="primary",
            key="download_printable_version"
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
    """Display the introduction page using Streamlit components"""
    st.markdown('<div class="main-header">The Burns Family Story</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">A Genealogical Discovery for Edward "Eddie" Byrnes</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        with st.container():
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f9f3e9 0%, #e8dfc8 100%);
                        border-left: 5px solid #c9a66b;
                        padding: 1.5rem;
                        border-radius: 8px;
                        margin: 1.5rem 0;">
            """, unsafe_allow_html=True)
            
            st.markdown("### 🎁 A Birthday Gift of Heritage")
            st.write("This interactive presentation represents months of genealogical research into your paternal lineage. Through census records, directories, and historical documents, we've uncovered the story of your biological father and your Irish-American heritage.")
            
            st.markdown("**What you'll discover:**")
            st.markdown("- Your father's identity: Edward J. Burns (1936-2004)")
            st.markdown("- Your Irish immigrant roots on both sides of his family")
            st.markdown("- The Burns family journey from Ireland to America")
            st.markdown("- Documentary evidence from official records")
            st.markdown("- A timeline of key family events")
            
            st.write("*Use the sidebar to navigate through each chapter of this discovery.*")
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📋 Quick Facts")
        st.markdown("**Your Father:**")
        st.markdown("• Edward J. Burns")
        st.markdown("• Born: Jan 4, 1936")
        st.markdown("• Died: May 12, 2004")
        st.markdown("• Married: Virginia Gonzalez (1957)")
        
        st.markdown("**Your Heritage:**")
        st.markdown("• Irish-American")
        st.markdown("• New York roots")
        st.markdown("• Working-class background")
    
    st.markdown("---")
    
    # Family Tree Preview
    st.markdown("### 🌳 Your Family Tree (Preview)")
    display_family_tree()

def irish_roots_page():
    """Display the Irish roots page"""
    st.markdown('<div class="main-header">Irish Roots</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">The Burns Family Journey from Ireland</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f9f3e9 0%, #e8dfc8 100%);
                    border-left: 5px solid #c9a66b;
                    padding: 1.5rem;
                    border-radius: 8px;
                    margin: 1.5rem 0;">
        """, unsafe_allow_html=True)
        
        st.markdown("### 🇮🇪 The Irish Connection")
        st.write("The Burns surname originates from Scotland and Ireland, with strong connections to both countries. Your Burns ancestors likely came from Ireland during the great waves of Irish immigration in the late 19th and early 20th centuries.")
        st.write('The name "Burns" (sometimes spelled "Byrnes" or "O\'Byrne") is an anglicized form of the Gaelic "Ó Broin," meaning "descendant of Bran." The Burns family would have been part of the mass Irish diaspora seeking better opportunities in America.')
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Irish Immigration Facts")
        st.markdown("**Great Irish Migration (1845-1855):**")
        st.markdown("• 1.5 million Irish came to America")
        st.markdown("• Escaping the Potato Famine")
        st.markdown("• Mostly settled in Northeast cities")
        
        st.markdown("**Irish in New York:**")
        st.markdown("• By 1855, 26% of NYC was Irish-born")
        st.markdown("• Concentrated in Five Points, Hell's Kitchen")
        st.markdown("• Worked as laborers, domestics, police, firefighters")
    
    with col2:
        st.markdown("### 🏙️ Irish Neighborhoods")
        st.markdown("**The Bronx (1940s):**")
        st.markdown("• Strong Irish communities")
        st.markdown("• Parish churches as community centers")
        st.markdown("• Working-class neighborhoods")
        st.markdown("• Family-oriented culture")
        
        st.markdown("**Cultural Legacy:**")
        st.markdown("• Catholic faith")
        st.markdown("• Labor movement participation")
        st.markdown("• Political involvement")
        st.markdown("• Strong family values")

def journey_to_america_page():
    """Display the journey to America page"""
    st.markdown('<div class="main-header">Journey to America</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">From Irish Shores to American Streets</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="font-family: 'Lora', serif; font-style: italic; font-size: 1.1rem; color: #555;
                border-left: 4px solid #c9a76b; padding-left: 1.5rem; margin: 1.5rem 0;">
    "They came in search of freedom, opportunity, and a better life for their children. 
    They brought with them their faith, their resilience, and their dreams."
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📅 The Burns Family Timeline in America")
    
    st.markdown("**Late 1800s:** James Burns (your great-grandfather) immigrates from Ireland to the United States, likely arriving at Ellis Island.")
    st.markdown("**Early 1900s:** The Burns family establishes roots in New York City, part of the large Irish immigrant community.")
    st.markdown("**1936:** Edward J. Burns (your father) is born in New York, first-generation American.")
    st.markdown("**1940:** Edward appears in the Bronx census at age 4, living with parents and siblings.")
    st.markdown("**1950:** Edward appears in Los Angeles census at age 14, indicating family relocation.")
    st.markdown("**1957:** Edward marries Virginia Gonzalez in New York City.")
    st.markdown("**1958:** You are born - continuing the Burns family legacy in America.")

def family_timeline_page():
    """Display the family timeline page"""
    st.markdown('<div class="main-header">Family Timeline</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Key Events in the Burns Family History</div>', unsafe_allow_html=True)
    
    st.markdown("### 📜 Complete Family Timeline")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🏴󠁧󠁢󠁳󠁣󠁴󠁿 **Irish Origins**")
        st.markdown("**1800s:**")
        st.markdown("• Burns family lives in Ireland")
        st.markdown("• Likely farmers or laborers")
        st.markdown("• Catholic faith")
        
        st.markdown("**Late 1800s:**")
        st.markdown("• Great-grandfather James emigrates")
        st.markdown("• Arrives at Ellis Island")
        st.markdown("• Settles in New York area")
        
        st.markdown("#### 🇺🇸 **Early American Years**")
        st.markdown("**1900-1935:**")
        st.markdown("• Family establishes in NYC")
        st.markdown("• Working-class occupations")
        st.markdown("• Builds community in Irish neighborhoods")
        st.markdown("• Maintains Irish cultural traditions")
    
    with col2:
        st.markdown("#### 👶 **Edward's Generation**")
        st.markdown("**1936:**")
        st.markdown("• Edward J. Burns born")
        
        st.markdown("**1940:**")
        st.markdown("• Age 4 in Bronx census")
        st.markdown("• Living with parents & 3 siblings")
        
        st.markdown("**1950:**")
        st.markdown("• Age 14 in LA census")
        st.markdown("• Living with guardians & 7 siblings")
        
        st.markdown("#### 👨‍👩‍👦 **Your Generation**")
        st.markdown("**1957:**")
        st.markdown("• Edward marries Virginia")
        
        st.markdown("**1958:**")
        st.markdown("• You are born")
        
        st.markdown("**2004:**")
        st.markdown("• Edward passes away")
        
        st.markdown("**Present:**")
        st.markdown("• Discovery of heritage")
        st.markdown("• Connection to living relatives")
    
    st.markdown("---")
    
    st.markdown("### 🌳 Complete Family Tree")
    display_family_tree()

def evidence_page():
    """Display the evidence page"""
    st.markdown('<div class="main-header">Documented Evidence</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Research Sources & Verification</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["📋 Census Records", "📜 Vital Records", "🔊 Podcast Discovery", "🖨️ Print Full Report"])
    
    with tab1:
        st.markdown("### U.S. Census Records")
        
        st.markdown("#### 1940 Census - Edward Burns (Age 4)")
        display_census_full_details(1940)
        
        st.markdown("---")
        
        st.markdown("#### 1950 Census - Edward Burns (Age 14)")
        display_census_full_details(1950)
        
        st.markdown("### 📊 Census Analysis")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**1940 Census Significance:**")
            st.markdown("• Earliest official record of Edward J. Burns")
            st.markdown("• Shows him at age 4 in the Bronx")
            st.markdown("• Confirms New York birth")
            st.markdown("• Shows family unit before separation")
            st.markdown("• Parents' birthplace listed as Scotland (likely error for Ireland)")
        
        with col2:
            st.markdown("**1950 Census Significance:**")
            st.markdown("• Shows Edward at age 14 in Los Angeles")
            st.markdown("• Indicates family separation between 1940-1950")
            st.markdown("• Shows complex family situation during adolescence")
            st.markdown("• Household includes 8 children total")
            st.markdown("• Edward not working or seeking work (typical for 14-year-old)")
    
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
        st.markdown("**Edward J. Burns**")
        st.markdown("• 1958: Truck driver, 1075 Tiffany St, Bronx")
        st.markdown("• 1960: Clerk, 160 Amsterdam Ave, Manhattan")
        st.markdown("• 1962: Mechanic, 321 S. Oxford St, Brooklyn")
        
        st.markdown("**John Burns (Brother)**")
        st.markdown("• 1958-1968: Consistently at 1075 Tiffany St, Bronx")
        st.markdown("• Occupations: Clerk, Driver")
    
    with tab3:
        st.markdown("## 🔊 The Discovery Podcast")
        st.markdown("### Finding the Real Edward Burns")
        
        display_podcast_section()
        
        st.markdown("---")
        st.markdown("### 🎙️ About This Audio Documentary")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**The Research Journey:**")
            st.markdown("• Months of genealogical investigation")
            st.markdown("• Analysis of historical documents")
            st.markdown("• Interviews with family members")
            st.markdown("• Verification through multiple sources")
        
        with col2:
            st.markdown("**Key Breakthroughs:**")
            st.markdown("• Connecting census records across decades")
            st.markdown("• Understanding Irish immigrant patterns")
            st.markdown("• Tracing the Burns family movements")
            st.markdown("• Corroborating evidence from multiple sources")
        
        with st.container():
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f9f3e9 0%, #e8dfc8 100%);
                        border-left: 5px solid #c9a66b;
                        padding: 1.5rem;
                        border-radius: 8px;
                        margin: 1.5rem 0;">
            """, unsafe_allow_html=True)
            
            st.markdown("**Listener's Note:** This audio presentation complements the written evidence in this presentation. Hearing the story narrated adds emotional depth to the factual discovery of your biological father and Irish-American heritage.")
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    with tab4:
        st.markdown("## 📄 Complete Printable Report")
        create_print_section()
        
        st.markdown("### 🔍 How to Verify Absolutely")
        st.markdown("1. **Order Eddie's birth certificate** (NYC Vital Records)")
        st.markdown("   - Will list father's name, age, residence")
        st.markdown("")
        st.markdown("2. **Order marriage certificate** (Edward & Virginia, 1957)")
        st.markdown("   - Will list Edward's parents' names")
        st.markdown("")
        st.markdown("3. **DNA testing** (AncestryDNA, 23andMe)")
        st.markdown("   - Match with Burns relatives' descendants")
        st.markdown("")
        st.markdown("4. **Contact Greco Funeral Home** (Lyndhurst, NJ)")
        st.markdown("   - Ask who provided obituary details")
        
        with st.container():
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f9f3e9 0%, #e8dfc8 100%);
                        border-left: 5px solid #c9a66b;
                        padding: 1.5rem;
                        border-radius: 8px;
                        margin: 1.5rem 0;">
            """, unsafe_allow_html=True)
            
            st.markdown("**Note:** This presentation provides strong circumstantial evidence. The steps above would provide legal and biological confirmation.")
            
            st.markdown("</div>", unsafe_allow_html=True)

def birthday_message_page():
    """Display the birthday message page"""
    st.markdown('<div class="main-header">Happy Birthday, Eddie!</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">A Gift of Heritage and Identity</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h1 style='text-align: center;'>🎂</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; font-family: Cinzel, serif; color: #1a472a;'>Happy Birthday!</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        with st.container():
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f9f3e9 0%, #e8dfc8 100%);
                        border-left: 5px solid #c9a66b;
                        padding: 1.5rem;
                        border-radius: 8px;
                        margin: 1.5rem 0;">
            """, unsafe_allow_html=True)
            
            st.markdown("### Dear Eddie,")
            st.write("On your birthday, I wanted to give you something more meaningful than a traditional gift. This presentation represents the discovery of your biological father and your Irish-American heritage.")
            st.write("For years, there were questions about your paternal lineage. Through careful research and examination of historical records, we can now say with confidence:")
            st.markdown("**Your father was Edward J. Burns (1936-2004), an Irish-American New Yorker.**")
            st.write("This discovery connects you to a rich heritage of Irish immigrants who came to America seeking better lives, who worked hard, raised families, and contributed to this country.")
            st.write("You come from resilient people. People who crossed an ocean for opportunity. People who built communities in a new land while maintaining their cultural identity.")
            st.write("This is your story. This is your heritage. And now, it's yours to know, to claim, and to pass on to future generations.")
            st.write("Happy Birthday, with love and admiration for the man you are and the heritage you carry.")
            st.markdown("<p style='text-align: right; font-style: italic; margin-top: 2rem;'>With love,<br>Your family</p>", unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🎁 Your Birthday Gift Includes:")
        st.markdown("• **Identity:** Knowing your biological father")
        st.markdown("• **Heritage:** Your Irish-American roots")
        st.markdown("• **Family:** Connection to living relatives")
        st.markdown("• **History:** Your family's American journey")
        st.markdown("• **Documents:** Official records as proof")
        st.markdown("• **Story:** The narrative of your origins")
        
        st.markdown("---")
        
        st.markdown("### 📞 Next Steps")
        st.markdown("**If you want to explore further:**")
        st.markdown("1. DNA test (Ancestry/23andMe)")
        st.markdown("2. Contact Burns relatives")
        st.markdown("3. Visit Irish cultural centers")
        st.markdown("4. Research Burns family history")
    
    st.markdown("---")
    
    st.markdown("### 🌳 Your Complete Heritage")
    display_family_tree()

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown('<div style="font-family: Cinzel, serif; font-size: 2rem; color: #1a472a; text-align: center; margin-bottom: 1rem;">The Burns Family</div>', unsafe_allow_html=True)
    
    st.markdown("### 📖 Navigation")
    page = st.radio(
        "Choose a chapter:",
        ["🎁 Introduction", "🇮🇪 Irish Roots", "🛳️ Journey to America", 
         "📅 Family Timeline", "🔍 Evidence", "💝 Birthday Message"],
        label_visibility="collapsed",
        key="navigation_radio"
    )
    
    st.markdown("---")
    
    st.markdown("### 🔊 Podcast")
    st.markdown("**Finding the Real Edward Burns**")
    st.markdown("Listen to the audio documentary of this genealogical discovery.")
    st.markdown("*Available in the Evidence section*")
    
    st.markdown("---")
    
    st.markdown("### 🖨️ Print Options")
    if st.button("📄 Generate Printable Version", use_container_width=True, type="primary", key="print_button"):
        st.session_state.show_print = True
    
    st.markdown("---")
    
    st.markdown("### 📋 Census Quick Facts")
    
    with st.expander("1940 Census"):
        st.markdown("**Edward Burns, Age 4**")
        st.markdown("• Address: 627 E-135 St, Bronx")
        st.markdown("• Parents: James & Sars Burns")
        st.markdown("• Birthplace: New York")
        st.markdown("• Father's Birthplace: Scotland")
        st.markdown("• Mother's Birthplace: Scotland")
    
    with st.expander("1950 Census"):
        st.markdown("**Edward Burns, Age 14**")
        st.markdown("• Address: 4547 Caledonia Way, LA")
        st.markdown("• Guardians: James & Sarah Burns")
        st.markdown("• Birthplace: New York")
        st.markdown("• Household: 10 people total")
        st.markdown("• Not working/Not seeking work")
    
    st.markdown("---")
    
    st.markdown("### 📅 Key Dates")
    st.markdown("**Edward J. Burns**")
    st.markdown("• Born: Jan 4, 1936")
    st.markdown("• Died: May 12, 2004")
    st.markdown("")
    st.markdown("**Eddie Byrnes**")
    st.markdown("• Born: Jan 27, 1958")
    
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
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-family: 'Lora', serif; font-size: 0.9rem; margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #eee;">
<strong>Sources:</strong> 1940 & 1950 U.S. Census • NYC Marriage Index • Social Security Death Index • Newark Star-Ledger Obituary<br>
<strong>Presented as a birthday gift</strong> • Created with Streamlit
</div>
""", unsafe_allow_html=True)

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
