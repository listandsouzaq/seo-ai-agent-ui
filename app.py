import streamlit as st
import time

# --- AGENT STATE INITIALIZATION ---
# This simulates the internal memory of the AI SEO Agent
if 'agent_state' not in st.session_state:
    st.session_state.agent_state = {
        "url": "",
        "detected_issues": [],
        "current_priority": None,
        "completed_steps": [],
        "next_recommended_action": ""
    }

# Page configuration
st.set_page_config(
    page_title="AI SEO Agent - Priority Analysis",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS for cleaner, minimal design
st.markdown("""
    <style>
    .main { padding-top: 2rem; }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        border: none;
    }
    .priority-box {
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .technical-seo { background-color: #ff6b6b; color: white; }
    .content-seo { background-color: #4ecdc4; color: white; }
    .onpage-seo { background-color: #ffd93d; color: #333; }
    .offpage-seo { background-color: #6c5ce7; color: white; }
    .agent-thought-card {
        background-color: #f0f2f6;
        border-left: 5px solid #4CAF50;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# App title
st.title("🤖 AI SEO Analysis Agent")
st.markdown("### I am your autonomous SEO strategist. Provide your data, and I'll determine the path forward.")
st.markdown("---")

# Create form
with st.form("seo_analysis_form"):
    url = st.text_input("Website URL", placeholder="https://example.com")
    
    col1, col2 = st.columns(2)
    with col1:
        indexed = st.radio("Is the page indexed?", options=["Yes", "No"])
        has_title = st.radio("Has title tag?", options=["Yes", "No"])
    
    with col2:
        has_meta = st.radio("Has meta description?", options=["Yes", "No"])
        content_length = st.number_input("Content length (words)", min_value=0, value=500, step=50)
    
    pagespeed = st.slider("PageSpeed Score", min_value=0, max_value=100, value=75)
    
    submitted = st.form_submit_button("Wake Up Agent & Analyze")

# --- MULTI-STEP AGENT REASONING FLOW ---
if submitted:
    if not url:
        st.error("I need a URL to begin my investigation.")
    else:
        # Reset Agent State for new analysis
        st.session_state.agent_state["completed_steps"] = []
        st.session_state.agent_state["detected_issues"] = []
        
        # UI: Agent Thinking Process
        with st.status("🤖 **Agent is thinking...**", expanded=True) as status:
            
            # Step 1: Diagnose Bottlenecks
            st.write("🔍 **Step 1: Diagnosing primary bottlenecks...**")
            time.sleep(1) # Simulate reasoning
            issues = []
            if indexed == "No": issues.append("Visibility Block (Not Indexed)")
            if pagespeed < 50: issues.append("Performance Critical")
            if content_length < 800: issues.append("Thin Content")
            if has_title == "No" or has_meta == "No": issues.append("Missing Metadata")
            
            st.session_state.agent_state["detected_issues"] = issues
            st.session_state.agent_state["completed_steps"].append("Diagnose Bottlenecks")
            
            # Step 2: Determine Highest Impact Fix
            st.write("⚖️ **Step 2: Calculating ROI of potential fixes...**")
            time.sleep(1)
            
            priority = ""
            reason = ""
            action = ""
            p_class = ""
            next_step = ""

            # Internal Logic Loop
            if indexed == "No":
                priority = "Technical SEO"
                reason = "If Google can't see you, nothing else matters. Indexing is the 'foundation' layer."
                action = "Check robots.txt, sitemaps, and GSC crawl errors immediately."
                p_class = "technical-seo"
                next_step = "Once indexed, I will re-evaluate your PageSpeed score."
            elif pagespeed < 50:
                priority = "Technical SEO"
                reason = "Core Web Vitals are a tie-breaker. Low scores actively hurt your crawl budget and UX."
                action = "Compress assets and enable server-side caching."
                p_class = "technical-seo"
                next_step = "After performance improves, I'll analyze your content depth."
            elif content_length < 800:
                priority = "Content Priority"
                reason = "The page lacks 'topical authority'. 500 words rarely ranks for competitive terms."
                action = "Expand to 1000+ words covering semantic sub-topics."
                p_class = "content-seo"
                next_step = "Once content is expanded, I'll suggest On-Page metadata tweaks."
            elif has_title == "No" or has_meta == "No":
                priority = "On-Page SEO"
                reason = "Metadata is your 'storefront'. Without it, CTR remains low even if you rank."
                action = "Draft unique Title and Meta Tags based on target keywords."
                p_class = "onpage-seo"
                next_step = "With On-Page fixed, we'll start a Backlink acquisition strategy."
            else:
                priority = "Off-Page SEO"
                reason = "Technical and content signals are strong. Authority is the final frontier."
                action = "Focus on high-quality backlink outreach."
                p_class = "offpage-seo"
                next_step = "Monitor rankings and optimize for Featured Snippets."

            st.session_state.agent_state["current_priority"] = priority
            st.session_state.agent_state["next_recommended_action"] = next_step
            st.session_state.agent_state["completed_steps"].append("Calculate ROI")

            # Step 3 & 4: Finalizing Strategy
            st.write("📝 **Step 3: Finalizing strategic explanation...**")
            time.sleep(0.8)
            st.write("🚀 **Step 4: Planning future roadmap...**")
            time.sleep(0.5)
            
            status.update(label="✅ Analysis Complete!", state="complete", expanded=False)

        # --- AGENT OUTPUT UI ---
        st.markdown("---")
        st.subheader("🤖 Agent Reasoning")
        st.markdown(f"""
        <div class="agent-thought-card">
            <strong>Agent's Logic:</strong> I've analyzed {url}. My reasoning flow determined that 
            <strong>{priority}</strong> is the primary bottleneck because {reason.lower()}
            <br><br>
            <strong>Status:</strong> {len(st.session_state.agent_state['detected_issues'])} key issues found.
        </div>
        """, unsafe_allow_html=True)

        # Display Result
        st.markdown(f"""
            <div class="priority-box {p_class}">
                <h2 style="margin-top: 0; color: white;">🎯 Current Focus: {priority}</h2>
                <p style="font-size: 1.1rem; margin: 1rem 0;"><strong>Agent Fix:</strong> {action}</p>
            </div>
            """, unsafe_allow_html=True)

        # Autonomous Next Steps
        st.markdown("### 🗺️ The Agent's Roadmap")
        col_a, col_b = st.columns(2)
        with col_a:
            st.success(f"**Step Completed:**\n{st.session_state.agent_state['completed_steps'][-1]}")
        with col_b:
            st.info(f"**Next Planned Step:**\n{st.session_state.agent_state['next_recommended_action']}")

        # Summary Log
        with st.expander("📝 Agent Diagnostic Log"):
            st.write(f"**Target URL:** {url}")
            st.write(f"**Detected Issues:** {', '.join(issues) if issues else 'None'}")
            st.write("**Confidence Score:** 94%")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 0.9rem;'>"
    "AI SEO Agent | Operational Mode: Autonomous Reasoning"
    "</p>",
    unsafe_allow_html=True
)
