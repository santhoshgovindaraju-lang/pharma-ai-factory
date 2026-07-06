import streamlit as st
import numpy as np
import time

# Executive styling and configuration
st.set_page_config(
    page_title="Agentic Pharma Production Engine", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Custom CSS theme injector for professional enterprise appearance
st.markdown("""
    <style>
    .main .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    .stAlert { border-left: 5px solid #2e7d32; }
    h1, h2, h3 { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #1e293b; }
    div[data-testid="stMetricValue"] { font-size: 2rem; color: #0f766e; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Application Master Header
st.title("🛡️ The Agentic Pharma Content Production Engine")
st.markdown("**Enterprise Content Transformation & Platform Migration Strategy** | *Operational Excellence & Delivery Leadership POV*")
st.write("---")

# Sidebar navigation control
st.sidebar.markdown("### ⚙️ Engine Control Room")
app_mode = st.sidebar.radio(
    "Select Briefing Module", 
    ["1. Executive Summary", "2. Core Strategic POV", "3. Workflow Swimlane", "4. ▶ LIVE DEMO PROTOTYPE"]
)

st.sidebar.write("---")
st.sidebar.markdown("""
**Operational Blueprint Summary:**
* **Scale Capability:** 1,000 Annual Assets
* **Optimised Headcount:** 16 Strategic FTEs
* **Turnaround Speed:** 24 - 48 Hours
* **Expected Cost Reduction:** 40%+
""")

# =========================================================================
# MODULE 1: EXECUTIVE SUMMARY
# =========================================================================
if app_mode == "1. Executive Summary":
    st.header("📋 Executive Summary: Shifting to Content Tech Partner")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        Our commercial promotional content factory is trapped in an expensive, headcount-dependent model. We pay premium creative agencies to design assets like **Interactive iPad iDetails** and **Veeva Approved Emails**, then pay an internal army of project managers, HTML developers, proofers, and QA specialists to pass those files across functional silos. This human-heavy assembly line causes severe **cost leakage, redundant validation steps, and prolonged campaign cycle times (2 to 3 weeks)**. 

        Compounding this friction, the life sciences industry is undergoing a massive technology migration. Legacy CRM infrastructure is sunsetting, forcing all top-tier pharma clients to choose a side over the next three years: migrating their entire content portfolios to **Veeva Vault CRM** or transitioning to the newly live **Salesforce Life Sciences Cloud**.
        """)
        st.info("💡 **The Strategic Pivot:** Implementing a lightweight **AI-Orchestration Wrapper** transforms our delivery center from a headcount-driven production vendor into an elite technology partner—reducing turnaround speeds to 24–48 hours, eliminating duplicated account teams, and expanding operational profit margins by over 40% without requiring massive software capital expenditures.")
    
    with col2:
        st.markdown("### Expected Roadmap Targets")
        st.metric(label="Day 30 Target: Ingestion Speed", value="50% Fast-Track", delta="Halves Setup Loops")
        st.metric(label="Day 60 Target: QA Cycle Time", value="75% Compression", delta="Zero Manual Backlog")
        st.metric(label="Day 90 Target: Operating Margin", value="40%+ Reduction", delta="Scales Headcount Free")

# =========================================================================
# MODULE 2: CORE STRATEGIC POV
# =========================================================================
elif app_mode == "2. Core Strategic POV":
    st.header("👁️ Detailed Point of View: The Four Portfolio Scenarios")
    st.write("Our AI-Engineered Production Engine provides 100% comprehensive operational coverage across the entire lifecycle of both tomorrow's new campaigns and yesterday's legacy content libraries.")
    
    scenario = st.tabs(["Scenario 1: Standalone", "Scenario 2: Client Platform", "Scenario 3: Legacy Manual", "Scenario 4: Platform Migration"])
    
    with scenario[0]:
        st.markdown("""
        ### New Assets – Standalone Open HTML Delivery
        *   **The Ground Reality:** Agencies drop unorganized raw packages (Adobe Cloud/Figma files) along with the approved baseline PDF into our collection system.
        *   **The AI Intervention:** The **AI Ingestion Agent** extracts all graphics, reads layout positions, and parses text copy blocks using Optical Character Recognition (OCR). Our **GenAI Code Compiler** takes these raw inputs and auto-injects them into our internal template core, generating clean, standard HTML code in seconds.
        *   **The Scale Benefit:** The compiler automatically applies relative typography rules and fluid CSS grids, ensuring the asset scales across every single iPad resolution and version without breaking or overlapping headings.
        """)
        
    with scenario[1]:
        st.markdown("""
        ### New Assets – Client Platform Mandate Integration
        *   **The Ground Reality:** The client requires production to occur directly within their owned enterprise content management systems—such as **Viseven (eWizard), Anthill, Shaman Go, or Adobe Experience Manager**.
        *   **The AI Intervention:** We connect our AI Ingestion Agent directly to the client’s software instance via public APIs. The AI skips standard HTML compilation and programmatically pushes the extracted visual layers, typography coordinates, and text blocks straight into the third-party platform’s workspace database, auto-assembling the slides inside their proprietary software environment.
        *   **The Scale Benefit:** Bypasses hours of manual asset dragging and dropping. Our **AI Template Engineers** handle platform-specific layout bugs directly within their software workspace, and validation scripts scrape live preview links for exact PDF visual checks.
        """)
        
    with scenario[2]:
        st.markdown("""
        ### Old Assets – Legacy Manual Code Refactoring
        *   **The Ground Reality:** The client presents a massive backlog of older, historical iDetails or emails built manually years ago by old vendors, containing rigid, non-responsive code layouts that break on modern iPads.
        *   **The AI Intervention:** Our **AI Reverse-Engineering Agent** deconstructs the old HTML packages, strips away broken layouts, and extracts the original high-resolution graphics and raw text strings. The text is matched word-for-word against historical approved PDFs to guarantee data integrity.
        *   **The Scale Benefit:** The clean components are automatically re-compiled into our modern, fluid layout core—upgrading the legacy asset to support responsive screen sizes and current device requirements in minutes.
        """)
        
    with scenario[3]:
        st.markdown("""
        ### Old Assets – Cross-Platform Migration & Upgrades
        *   **The Ground Reality:** The client needs to migrate their entire historical catalog of content out of an outdated software instance and move it into a newly adopted target destination like Veeva Vault CRM or Salesforce Life Sciences Cloud.
        *   **The AI Intervention:** The wrapper acts as a structural translator. It uses **Pluggable Deployment Adapters** to separate the core visual content layer from the legacy platform's system files. 
        *   **The Scale Benefit:** The engine automatically strips away outdated tracking configurations and dynamically appends modern analytics tags tailored to their new CRM endpoints, transforming a massive migration bottleneck into an automated, high-margin assembly line.
        """)

    st.markdown("### Process Phase Comparison Matrix")
    st.table([
        {"Production Phase": "Commercial Model", "Legacy Production Model": "Time & Materials (Hourly billing locks team counts high)", "Our AI Reimagined Factory": "Value / Asset-Based Pricing (Drives compounding internal profit)"},
        {"Production Phase": "Asset Ingestion", "Legacy Production Model": "Manual file parsing and tedious layout slicing across folders", "Our AI Reimagined Factory": "AI Ingestion Agent extracts copy strings and coordinates via vision rules"},
        {"Production Phase": "Quality Control", "Legacy Production Model": "Human proofers checking files page-by-page, prone to fatigue", "Our AI Reimagined Factory": "Visual QA Agent runs pixel-by-pixel mathematical overlay regression"},
        {"Production Phase": "Testing Loops", "Legacy Production Model": "Manual click-testing on physical iPads and scrolling screenshots", "Our AI Reimagined Factory": "Headless browser scripts (Playwright) and programmatic Litmus API checks"}
    ])

# =========================================================================
# MODULE 3: WORKFLOW SWIMLANE
# =========================================================================
elif app_mode == "3. Workflow Swimlane":
    st.header("🔀 Cross-Functional Swimlane Workflow")
    st.write("This operational blueprint outlines how tasks pass between systems, automated agents, and humans across all delivery execution phases.")
    
    st.markdown("""
    #### 🟢 [Lane 1] External Creative Agency
    *   **Action:** Drops raw, unorganized design asset packages (Figma, InDesign, Photoshop) and the final MLR-approved PDF baseline into our secure ingress platform.
    
    #### ⚙️ [Lane 2] AI Ingestion & Reverse-Engineering Agent (*Automation*)
    *   **Action:** Runs design files through **OpenCV/YOLO** to isolate visual layout bounding blocks. Performs an OCR text extraction scan on the MLR PDF to build a master approved text copy string matrix.
    
    #### ⚙️ [Lane 3] GenAI Code Compiler & API Injection Engine (*Automation*)
    *   *Standalone:* Auto-injects variables into our internal responsive template core, writing clean, relative HTML code.
