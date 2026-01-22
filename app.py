import streamlit as st

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
    
    /* Timeline styling */
    .timeline-year {
        font-family: 'Cinzel', serif;
        font-weight: 700;
        color: #c9a66b;
        font-size: 1.5rem;
        margin-bottom: 0.2rem;
    }
    
    .timeline-event {
        font-family: 'Lora', serif;
        font-size: 1.1rem;
        line-height: 1.5;
        color: #333;
        margin-bottom: 1.2rem;
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
    
    /* Image container */
    .image-container {
        border-radius: 8px;
        overflow: hidden;
        margin: 1.5rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    .image-caption {
        font-family: 'Lora', serif;
        font-size: 0.9rem;
        color: #666;
        text-align: center;
        padding: 0.5rem;
        background: #f8f9fa;
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

# ==================== IMAGE URLS ====================
# Direct image URLs that will work with st.image()
HISTORICAL_IMAGES = {
    "irish_immigrants": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Irish_immigrants_boarding_a_ship_at_Cork_%281851%29.jpg/1280px-Irish_immigrants_boarding_a_ship_at_Cork_%281851%29.jpg",
    "ellis_island": "https://upload.wikimedia.org/wikipedia/commons/5/55/Ellis_island_1902.jpg",
    "1940s_family": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/American_family_1940s.jpg/1280px-American_family_1940s.jpg",
    "bronx_street": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Bronx_Street_Scene_1920s.jpg/1280px-Bronx_Street_Scene_1920s.jpg",
    "truck_1950s": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/1950s_truck_delivery.jpg/1280px-1950s_truck_delivery.jpg"
}

# ==================== UTILITY FUNCTIONS ====================
def display_historical_image(image_key, caption):
    """Display historical image directly from URL"""
    try:
        if image_key in HISTORICAL_IMAGES:
            st.image(
                HISTORICAL_IMAGES[image_key],
                caption=caption,
                width="stretch"  # Fixed: Replaced use_column_width with width parameter
            )
        else:
            st.warning(f"Image '{image_key}' not found in collection.")
    except Exception as e:
        st.info(f"*Historical image: {caption}*")
        st.caption(f"(Image temporarily unavailable)")

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
        # Family tree symbol and image
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🌳</div>
            <div style="font-family: 'Cinzel', serif; font-size: 1.2rem;">Family Heritage</div>
        </div>
        """, unsafe_allow_html=True)
        
        display_historical_image("1940s_family", "An American family, 1940s")

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
        
        st.markdown('<div class="quote-box">', unsafe_allow_html=True)
        st.markdown("""
        "They didn't leave because they didn't love Ireland. 
        They left because they loved the idea of a future enough 
        to risk everything for it."
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Historical image
        display_historical_image("irish_immigrants", "Irish immigrants boarding a ship at Cork, c. 1851")
        
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
    
    # Ellis Island image
    display_historical_image("ellis_island", "Ellis Island, New York, c. 1902")
    
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
        display_historical_image("bronx_street", "Bronx street scene, 1920s")

# ==================== PAGE 4: FAMILY TIMELINE ====================
elif page == "📅 Family Timeline":
    st.markdown('<div class="main-header">Family Timeline</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">The Life of Edward J. Burns & Family</div>', unsafe_allow_html=True)
    
    # Timeline with custom styling
    st.markdown('<div class="timeline-container">', unsafe_allow_html=True)
    
    timeline_items = [
        {"year": "1936", "event": "Edward J. Burns born January 4 in Brooklyn, NY"},
        {"year": "1940", "event": "Living at 1057 Fox Street, Bronx with parents James & Catherine"},
        {"year": "1950", "event": "Family upheaval: Edward (14) in Los Angeles; Catherine widowed in Bronx"},
        {"year": "1957", "event": "Marries Virginia A. Gonzalez (November 16) in NYC"},
        {"year": "1958", "event": "• Eddie Byrnes born January 27 in Brooklyn<br>• Family lives on South Portland Street, Brooklyn"},
        {"year": "1959-1960", "event": "Family moves to Amsterdam Avenue, Manhattan"},
        {"year": "1960s-1990s", "event": "Truck driver for Consolidated Freightways, 30-year career"},
        {"year": "2004", "event": "• Passes away May 12 in Belleville, NJ<br>• Obituary names 'Edward \"Eddie\" Byrnes' as his son"}
    ]
    
    for item in timeline_items:
        create_timeline_item(item["year"], item["event"])
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Your Burns Family Tree</div>', unsafe_allow_html=True)
    
    display_family_tree()
    
    display_historical_image("truck_1950s", "1950s truck delivery - similar to Edward's work")

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
        
        st.markdown('<div class="gift-message">', unsafe_allow_html=True)
        st.markdown("""
        **Note:** This presentation provides strong circumstantial evidence. 
        The steps above would provide legal and biological confirmation.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

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
        <div class="quote-box">
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
        # Historical family image
        display_historical_image("1940s_family", "An American family, 1940s")
        
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
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.markdown("""
**Sources:** 1940 & 1950 U.S. Census • NYC Marriage Index • Social Security Death Index • Newark Star-Ledger Obituary  
**Presented as a birthday gift** • Created with Streamlit • Historical images from Wikimedia Commons
""")
st.markdown('</div>', unsafe_allow_html=True)

# ==================== SESSION STATE INITIALIZATION ====================
if 'initialized' not in st.session_state:
    st.session_state.initialized = True