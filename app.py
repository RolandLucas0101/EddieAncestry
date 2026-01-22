import streamlit as st
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
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Lora:wght@400;500&display=swap');
    
    .main-header {
        font-family: 'Cinzel', serif;
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        color: #1a472a;
        margin-bottom: 0.5rem;
    }
    
    .sub-header {
        font-family: 'Lora', serif;
        font-size: 1.3rem;
        text-align: center;
        color: #2d5016;
        margin-bottom: 2rem;
        font-style: italic;
    }
    
    .section-header {
        font-family: 'Cinzel', serif;
        font-size: 1.8rem;
        color: #1a472a;
        border-bottom: 2px solid #c9a66b;
        padding-bottom: 0.5rem;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
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
    
    .image-placeholder {
        background: linear-gradient(135deg, #e8dfc8 0%, #d4c9a6 100%);
        border: 2px dashed #c9a66b;
        border-radius: 8px;
        padding: 2rem;
        text-align: center;
        margin: 1.5rem 0;
        font-family: 'Lora', serif;
        color: #666;
    }
    
    .download-btn {
        background: linear-gradient(to right, #1a472a, #2d5016);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 5px;
        font-family: 'Lora', serif;
        font-size: 1rem;
        cursor: pointer;
        transition: all 0.3s ease;
        display: inline-block;
        text-decoration: none;
    }
    
    .download-btn:hover {
        background: linear-gradient(to right, #2d5016, #1a472a);
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# ==================== PDF GENERATION FUNCTION ====================
def generate_pdf_content():
    """Generate HTML content for PDF conversion"""
    today = datetime.now().strftime("%B %d, %Y")
    
    content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>The Burns Family Story - Genealogical Report</title>
        <style>
            body {{ font-family: 'Arial', sans-serif; line-height: 1.6; margin: 0; padding: 20px; color: #333; }}
            .header {{ text-align: center; border-bottom: 3px solid #1a472a; padding-bottom: 20px; margin-bottom: 30px; }}
            .main-title {{ color: #1a472a; font-size: 28px; margin-bottom: 10px; }}
            .subtitle {{ color: #2d5016; font-size: 18px; font-style: italic; }}
            .section {{ margin-bottom: 25px; }}
            .section-title {{ color: #1a472a; border-bottom: 2px solid #c9a66b; padding-bottom: 5px; margin-bottom: 15px; font-size: 22px; }}
            .evidence-box {{ background: #f9f3e9; border-left: 4px solid #c9a66b; padding: 15px; margin: 15px 0; }}
            .timeline-year {{ font-weight: bold; color: #c9a66b; }}
            .footer {{ margin-top: 40px; padding-top: 20px; border-top: 1px solid #ddd; text-align: center; color: #666; font-size: 12px; }}
            .image-caption {{ font-style: italic; color: #666; text-align: center; margin: 10px 0; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1 class="main-title">A Journey Home: The Burns Family Story</h1>
            <p class="subtitle">A Genealogical Gift for Eddie Byrnes</p>
            <p><em>Presented on {today}</em></p>
        </div>
        
        <div class="section">
            <h2 class="section-title">Core Discovery</h2>
            <div class="evidence-box">
                <strong>Edward J. Burns (1936-2004) is your biological father.</strong><br><br>
                <strong>Key Evidence:</strong><br>
                • Married your mother, Virginia Gonzalez, in <strong>1957</strong><br>
                • Lived with you as a family in <strong>Brooklyn & Manhattan (1958-1960)</strong><br>
                • Named you as his son in his <strong>2004 obituary</strong><br>
                • Timeline and geography align perfectly<br><br>
                <strong>Confidence Level: 95%+</strong>
            </div>
        </div>
        
        <div class="section">
            <h2 class="section-title">Family Timeline</h2>
            <p><span class="timeline-year">1936</span> - Edward J. Burns born January 4 in Brooklyn, NY</p>
            <p><span class="timeline-year">1940</span> - Living at 1057 Fox Street, Bronx with parents James & Catherine</p>
            <p><span class="timeline-year">1950</span> - Family upheaval: Edward (14) in Los Angeles; Catherine widowed in Bronx</p>
            <p><span class="timeline-year">1957</span> - Marries Virginia A. Gonzalez (November 16) in NYC</p>
            <p><span class="timeline-year">1958</span> - Eddie Byrnes born January 27 in Brooklyn</p>
            <p><span class="timeline-year">1959-1960</span> - Family moves to Amsterdam Avenue, Manhattan</p>
            <p><span class="timeline-year">1960s-1990s</span> - Truck driver for Consolidated Freightways, 30-year career</p>
            <p><span class="timeline-year">2004</span> - Passes away May 12 in Belleville, NJ; Obituary names "Edward 'Eddie' Byrnes" as his son</p>
        </div>
        
        <div class="section">
            <h2 class="section-title">Family Tree</h2>
            <pre style="background: #f5f5f5; padding: 15px; border-radius: 5px; font-family: monospace;">
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
            </pre>
        </div>
        
        <div class="section">
            <h2 class="section-title">Documented Evidence</h2>
            <h3>U.S. Census Records</h3>
            <p><strong>1940 Census (1057 Fox St, Bronx)</strong><br>
            • Edward Burns, age 4<br>
            • Parents: James & Catherine Burns (both born Ireland)<br>
            • James: Machinist in auto plant</p>
            
            <p><strong>1950 Census (Multiple Locations)</strong><br>
            • Edward Burns, age 14, Los Angeles, CA<br>
            • Living with Sara Burns & siblings<br>
            • Catherine Burns (widowed), age 50, 1075 Tiffany St, Bronx</p>
            
            <h3>Vital Records</h3>
            <p><strong>Social Security Death Index</strong><br>
            • Edward J. Burns: Born Jan 4, 1936 - Died May 12, 2004</p>
            
            <p><strong>Marriage Index</strong><br>
            • Edward J. Burns to Virginia A. Gonzalez: Nov 16, 1957, NYC</p>
            
            <h3>Next Steps for Verification</h3>
            <ol>
                <li>Order Eddie's birth certificate (NYC Vital Records)</li>
                <li>Order marriage certificate (Edward & Virginia, 1957)</li>
                <li>DNA testing (AncestryDNA, 23andMe)</li>
                <li>Contact Greco Funeral Home (Lyndhurst, NJ)</li>
            </ol>
        </div>
        
        <div class="section">
            <h2 class="section-title">Historical Context</h2>
            <p><strong>Irish Roots:</strong> James (born ~1896) and Catherine (born ~1900) Burns lived through the 
            1916 Easter Rising, Irish War of Independence (1919-1921), and Civil War (1922-1923). 
            They emigrated to America in the mid-to-late 1920s.</p>
            
            <p><strong>Key Locations:</strong><br>
            • 1057 Fox St, Bronx (1940)<br>
            • 1075 Tiffany St, Bronx (1950s)<br>
            • Brooklyn & Manhattan (1958-1960)<br>
            • Belleville, NJ (2004)</p>
            
            <p class="image-caption">[Historical images: Irish immigrants boarding ship, Ellis Island, 1940s American family]</p>
        </div>
        
        <div class="section">
            <div class="evidence-box">
                <h3>Birthday Message</h3>
                <p>This presentation represents months of research through historical archives, 
                census records, and public documents—all to answer the question of your paternal lineage.</p>
                
                <p><em>"My grandparents survived the birth of a nation and the Great Depression. 
                My father survived a childhood fracture and crossed a continent twice. 
                Through it all, they held onto family. I am the living proof of that hold."</em></p>
                
                <p><strong>Sláinte agus beannachtaí</strong><br>
                (Health and blessings)</p>
                
                <p style="text-align: right;">With all our love,<br>Your Sibling</p>
            </div>
        </div>
        
        <div class="footer">
            <p>Sources: 1940 & 1950 U.S. Census • NYC Marriage Index • Social Security Death Index • Newark Star-Ledger Obituary</p>
            <p>Presented as a birthday gift • Generated on {today}</p>
        </div>
    </body>
    </html>
    """
    
    return content

def create_download_link(content, filename="burns_family_story.html"):
    """Create a downloadable HTML file"""
    b64 = base64.b64encode(content.encode()).decode()
    href = f'data:text/html;base64,{b64}'
    return href

# ==================== IMAGE HANDLING ====================
def display_historical_placeholder(image_key, caption):
    """Display a styled placeholder for historical images"""
    st.markdown(f"""
    <div class="image-placeholder">
        <div style="font-size: 2.5rem; margin-bottom: 1rem;">🏞️</div>
        <div style="font-family: 'Cinzel', serif; font-size: 1.1rem; color: #1a472a; margin-bottom: 0.5rem;">
            Historical Image
        </div>
        <div style="font-family: 'Lora', serif; color: #666;">
            {caption}
        </div>
        <div style="margin-top: 0.5rem; font-size: 0.9rem; color: #888;">
            (Image from historical archives)
        </div>
    </div>
    """, unsafe_allow_html=True)

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
    
    # PDF Download Button
    st.markdown("### 📥 Download Report")
    if st.button("Download Full Report (HTML)", key="download_pdf"):
        pdf_content = generate_pdf_content()
        download_link = create_download_link(pdf_content, "burns_family_story.html")
        st.markdown(f'<a href="{download_link}" download="burns_family_story.html" class="download-btn">⬇️ Download Now</a>', unsafe_allow_html=True)
        st.info("The report has been generated as an HTML file. You can print it directly from your browser or convert it to PDF.")
    
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
    
    # Important Locations
    st.markdown("### 📍 Key Locations")
    st.markdown("""
    • 1057 Fox St, Bronx (1940)  
    • 1075 Tiffany St, Bronx (1950s)  
    • Brooklyn & Manhattan (1958-1960)  
    • Belleville, NJ (2004)
    """)
    
    st.markdown("---")
    st.markdown("*A genealogical gift for Eddie*")

# ==================== PAGE 1: INTRODUCTION ====================
if page == "🎁 Introduction":
    st.markdown('<div class="main-header">A Journey Home</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">The Burns Family Story: A Genealogical Gift for Eddie Byrnes</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="gift-message">', unsafe_allow_html=True)
        st.markdown("""
        This is more than a genealogy report. This is your origin story—a testament to resilience, 
        woven through the lives of ordinary people facing extraordinary times. 
        
        This presentation documents the search for your biological father, **Edward J. Burns**, 
        and reveals your Irish-American heritage.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-header">The Core Discovery</div>', unsafe_allow_html=True)
        
        st.success("""
        **Edward J. Burns (1936-2004) is your biological father.**
        
        **Key Evidence:**
        • Married your mother, Virginia Gonzalez, in **1957**
        • Lived with you as a family in **Brooklyn & Manhattan (1958-1960)**
        • Named you as his son in his **2004 obituary**
        • Timeline and geography align perfectly
        """)
        
        st.markdown("**Confidence Level: 95%+**")
        
        st.markdown('<div class="section-header">Quick Facts</div>', unsafe_allow_html=True)
        st.markdown("""
        • **Father:** Edward J. Burns  
        • **Grandparents:** James & Catherine Burns (Ireland)  
        • **Uncles:** John (Bronx), James (FL), Michael (PA)  
        • **Aunt:** Catherine Ryan (Staten Island)
        """)
    
    with col2:
        # Historical image placeholder
        display_historical_placeholder("1940s_family", "An American family, 1940s")
        
        # Quick download option
        st.markdown("### Quick Download")
        if st.button("Get Summary PDF", key="intro_download"):
            summary_content = generate_pdf_content()
            download_link = create_download_link(summary_content, "burns_family_summary.html")
            st.markdown(f'<a href="{download_link}" download="burns_family_summary.html" class="download-btn">📄 Download Summary</a>', unsafe_allow_html=True)

# ==================== PAGE 2: IRISH ROOTS ====================
elif page == "🇮🇪 Irish Roots":
    st.markdown('<div class="main-header">The Irish Roots</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Your Grandparents: James & Catherine Burns</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        James (born ~1896) and Catherine (born ~1900) came of age in an Ireland 
        being torn apart and reborn:
        
        • **Historical Context:** Lived through the 1916 Easter Rising, Irish War of 
          Independence (1919-1921), and Civil War (1922-1923)
        • **Daily Life:** Economic hardship, political turmoil, deep Catholic faith
        • **The Decision:** By the mid-1920s, emigration was the path forward for 
          a young couple seeking to build a family
        
        They carried Ireland within them—its strength, faith, and perseverance—as 
        they prepared for their journey to America.
        """)
        
        st.markdown('<div class="section-header">Ireland in the 1920s</div>', unsafe_allow_html=True)
        st.markdown("""
        • Population: About 3 million  
        • Major event: Irish Free State established (1922)  
        • Economic reality: Agricultural, limited opportunities  
        • Emigration wave: Over 220,000 left between 1921-1930
        """)
        
        st.markdown('<div class="gift-message">', unsafe_allow_html=True)
        st.markdown("""
        "They didn't leave because they didn't love Ireland. 
        They left because they loved the idea of a future enough 
        to risk everything for it."
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Historical image placeholder
        display_historical_placeholder("irish_immigrants", "Irish immigrants boarding a ship at Cork, c. 1851")
        
        st.markdown('<div class="section-header">Life in Ireland</div>', unsafe_allow_html=True)
        st.markdown("""
        • **Agriculture:** Most families worked small farms  
        • **Religion:** Catholic faith central to community life  
        • **Politics:** Transition from British rule to independence  
        • **Economy:** Limited industrial development, high unemployment
        """)

# ==================== PAGE 3: JOURNEY TO AMERICA ====================
elif page == "🛳️ Journey to America":
    st.markdown('<div class="main-header">Journey to America</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">The Leap Across the Atlantic (c. 1924-1929)</div>', unsafe_allow_html=True)
    
    # Historical image placeholder
    display_historical_placeholder("ellis_island", "Ellis Island, New York, c. 1902")
    
    st.markdown("""
    Sometime in the mid-to-late 1920s, James and Catherine boarded a crowded transatlantic 
    steamer from Cork or Dublin. After about a week's voyage, they arrived at **Ellis Island**.
    
    ### Their First Years in America
    
    **Initial Challenges:**
    • Relied on Irish immigrant networks in New York  
    • James found work as a laborer, dockworker, or machinist  
    • Catherine managed a tenement apartment, possibly working as a domestic servant  
    • Faced the Great Depression starting in 1929
    
    **The 1940 Census finds them settled:**
    """)
    
    st.info("""
    **1057 Fox Street, Bronx, New York**
    • James Burns (44) – Machinist, born Ireland  
    • Catherine Burns (40) – Homemaker, born Ireland  
    • **Edward Burns (4)** – Your father, born New York
    """)
    
    st.markdown("### Life in the Bronx")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        They had planted their roots in America, surviving economic hardship through 
        the same grit that sustained them in Ireland.
        
        **Neighborhood Life:**
        • Irish immigrant communities in the Bronx  
        • Catholic parishes as community centers  
        • Factory work and manual labor  
        • Tenement housing with shared facilities
        """)
    
    with col2:
        display_historical_placeholder("bronx_street", "Bronx street scene, 1920s")

# ==================== PAGE 4: FAMILY TIMELINE ====================
elif page == "📅 Family Timeline":
    st.markdown('<div class="main-header">Family Timeline</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">The Life of Edward J. Burns & Family</div>', unsafe_allow_html=True)
    
    # Timeline
    timeline_data = [
        {"year": "1936", "event": "Edward J. Burns born January 4 in Brooklyn, NY"},
        {"year": "1940", "event": "Living at 1057 Fox Street, Bronx with parents James & Catherine"},
        {"year": "1950", "event": "Family upheaval: Edward (14) in Los Angeles; Catherine widowed in Bronx"},
        {"year": "1957", "event": "Marries Virginia A. Gonzalez (November 16) in NYC"},
        {"year": "1958", "event": "• Eddie Byrnes born January 27 in Brooklyn\n• Family lives on South Portland Street, Brooklyn"},
        {"year": "1959-1960", "event": "Family moves to Amsterdam Avenue, Manhattan"},
        {"year": "1960s-1990s", "event": "Truck driver for Consolidated Freightways, 30-year career"},
        {"year": "2004", "event": "• Passes away May 12 in Belleville, NJ\n• Obituary names 'Edward \"Eddie\" Byrnes' as his son"}
    ]
    
    for item in timeline_data:
        st.markdown(f"**{item['year']}**")
        st.markdown(f"{item['event']}")
        st.markdown("---")
    
    st.markdown('<div class="section-header">Your Burns Family Tree</div>', unsafe_allow_html=True)
    
    st.code("""
    James BURNS (Ireland) + Catherine (Ireland)
            |
            ├── Edward J. BURNS (1936-2004) = Virginia GONZALEZ
            │               │
            │               └── Edward "Eddie" BYRNES (You)
            │
            ├── John Burns (Bronx)
            ├── James Burns (Florida)
            ├── Michael Burns (Pennsylvania)
            └── Catherine Ryan (Staten Island)
    """, language="text")
    
    display_historical_placeholder("truck_1950s", "1950s truck delivery - similar to Edward's work")

# ==================== PAGE 5: EVIDENCE ====================
elif page == "🔍 Evidence":
    st.markdown('<div class="main-header">Documented Evidence</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Research Sources & Verification</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["📋 Census Records", "📚 Directories", "📜 Vital Records", "🔬 Next Steps"])
    
    with tab1:
        st.markdown("### U.S. Census Records")
        st.markdown("""
        **1940 Census (1057 Fox St, Bronx)**
        • Edward Burns, age 4  
        • Parents: James & Catherine Burns (both born Ireland)  
        • James: Machinist in auto plant
        
        **1950 Census (Multiple Locations)**
        • Edward Burns, age 14, Los Angeles, CA  
        • Living with Sara Burns & siblings  
        • Catherine Burns (widowed), age 50, 1075 Tiffany St, Bronx
        """)
        
        st.markdown('<div class="gift-message">', unsafe_allow_html=True)
        st.markdown("""
        **Why this matters:** Census records are official government documents 
        that provide snapshots of families at specific moments in time.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### NYC Directories")
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
        st.markdown("### Vital Records")
        st.markdown("""
        **Social Security Death Index**
        • Edward J. Burns: Born Jan 4, 1936 - Died May 12, 2004
        
        **Marriage Index**
        • Edward J. Burns to Virginia A. Gonzalez: Nov 16, 1957, NYC
        
        **Obituary (Newark Star-Ledger, May 14, 2004)**
        • "Survived by his beloved wife, Virginia (Gonzalez) Burns; his loving son, Edward 'Eddie' Byrnes..."  
        • Lists brothers: John (Bronx), James (Florida), Michael (Pennsylvania)
        """)
    
    with tab4:
        st.markdown("### How to Verify Absolutely")
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
        
        # Download button in evidence section
        st.markdown("---")
        st.markdown("### Download Full Report")
        if st.button("Generate Complete Report", key="evidence_download"):
            pdf_content = generate_pdf_content()
            download_link = create_download_link(pdf_content, "burns_family_complete_report.html")
            st.markdown(f'<a href="{download_link}" download="burns_family_complete_report.html" class="download-btn">📑 Download Complete Report</a>', unsafe_allow_html=True)
            st.success("Report generated successfully! Click the button above to download.")

# ==================== PAGE 6: BIRTHDAY MESSAGE ====================
else:  # Birthday Message
    st.markdown('<div class="main-header">Happy Birthday, Eddie</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="gift-message">', unsafe_allow_html=True)
        st.markdown("""
        This presentation represents months of research through historical archives, 
        census records, and public documents—all to answer the question of your paternal lineage.
        
        What we found is more than names and dates. We found a story of resilience:
        
        • **From Ireland:** The strength of James and Catherine who survived war and depression  
        • **From the Bronx:** The toughness of a New York Irish-American family  
        • **From Your Father:** The perseverance of a man who crossed a continent twice 
          and always acknowledged you
        
        Your story is not simple—it's real. It's gritty. It's human. And it's yours to claim.
        """)
        
        st.markdown("""
        <div style="border-left: 4px solid #c9a66b; padding-left: 1.5rem; margin: 1.5rem 0; font-style: italic;">
        "My grandparents survived the birth of a nation and the Great Depression. 
        My father survived a childhood fracture and crossed a continent twice. 
        Through it all, they held onto family. I am the living proof of that hold."
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        This is your foundation. The next chapter—connecting with uncles, cousins, 
        and perhaps even the town in Ireland where it all began—is yours to write.
        
        <div style="text-align: center; margin-top: 2rem; font-family: 'Cinzel', serif;">
        <i>Sláinte agus beannachtaí</i><br>
        (Health and blessings)
        </div>
        
        <div style="text-align: right; margin-top: 3rem; font-family: 'Lora', serif;">
        With all our love,<br>
        Your Sibling
        </div>
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Historical family image placeholder
        display_historical_placeholder("1940s_family", "An American family, 1940s")
        
        # Final download option
        st.markdown('<div class="section-header">Preserve This Story</div>', unsafe_allow_html=True)
        if st.button("Download Keepsake Report", key="final_download"):
            pdf_content = generate_pdf_content()
            download_link = create_download_link(pdf_content, "burns_family_keepsake.html")
            st.markdown(f'<a href="{download_link}" download="burns_family_keepsake.html" class="download-btn">💝 Download Keepsake</a>', unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; margin-top: 2rem; padding: 1rem; background: #f9f3e9; border-radius: 8px;">
            <div style="font-size: 2.5rem;">🎂</div>
            <div style="font-family: 'Cinzel', serif; font-size: 1.2rem;">Happy Birthday</div>
            <div style="font-family: 'Lora', serif; color: #666; margin-top: 0.5rem;">
                January 27, 1958
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==================== FOOTER ====================
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**Sources**")
    st.markdown("• 1940 & 1950 U.S. Census")
    st.markdown("• NYC Marriage Index")
with col2:
    st.markdown("**Research Methods**")
    st.markdown("• Genealogical research")
    st.markdown("• Historical context")
with col3:
    st.markdown("**Presented**")
    st.markdown(f"• {datetime.now().strftime('%B %d, %Y')}")
    st.markdown("• A birthday gift")

st.markdown(
    "<div style='text-align: center; color: #666; font-size: 0.9rem; margin-top: 2rem;'>"
    "This digital presentation was created with Streamlit"
    "</div>", 
    unsafe_allow_html=True
)

# ==================== SESSION STATE ====================
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
