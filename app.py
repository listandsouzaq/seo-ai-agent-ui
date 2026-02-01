import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI SEO Priority Analysis",
    page_icon="🔍",
    layout="centered"
)

# Custom CSS for cleaner, minimal design
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .priority-box {
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .technical-seo {
        background-color: #ff6b6b;
        color: white;
    }
    .content-seo {
        background-color: #4ecdc4;
        color: white;
    }
    .onpage-seo {
        background-color: #ffd93d;
        color: #333;
    }
    .offpage-seo {
        background-color: #6c5ce7;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# App title
st.title("🔍 AI SEO Priority Analysis")
st.markdown("### Identify what to fix first to improve your search rankings")
st.markdown("---")

# Create form
with st.form("seo_analysis_form"):
    # Website URL
    url = st.text_input(
        "Website URL",
        placeholder="https://example.com",
        help="Enter the full URL of the page you want to analyze"
    )
    
    # Two columns for yes/no inputs
    col1, col2 = st.columns(2)
    
    with col1:
        indexed = st.radio(
            "Is the page indexed?",
            options=["Yes", "No"],
            help="Check if the page appears in Google search results"
        )
        
        has_title = st.radio(
            "Has title tag?",
            options=["Yes", "No"],
            help="Does the page have a proper title tag?"
        )
    
    with col2:
        has_meta = st.radio(
            "Has meta description?",
            options=["Yes", "No"],
            help="Does the page have a meta description?"
        )
        
        content_length = st.number_input(
            "Content length (words)",
            min_value=0,
            value=500,
            step=50,
            help="Approximate word count of the page content"
        )
    
    # PageSpeed score
    pagespeed = st.slider(
        "PageSpeed Score",
        min_value=0,
        max_value=100,
        value=75,
        help="Google PageSpeed Insights score (0-100)"
    )
    
    # Submit button
    submitted = st.form_submit_button("Analyze SEO Priority")

# Analysis logic
if submitted:
    if not url:
        st.error("Please enter a website URL")
    else:
        # Initialize variables
        priority = None
        reason = ""
        action = ""
        priority_class = ""
        
        # Priority analysis logic
        if indexed == "No":
            priority = "Technical SEO"
            reason = "Your page is not indexed by search engines, which is the most critical issue."
            action = "**Action:** Check your robots.txt file, ensure the page is not set to 'noindex', submit your sitemap to Google Search Console, and verify there are no crawl errors."
            priority_class = "technical-seo"
        
        elif content_length < 800:
            priority = "Content Priority"
            reason = f"Your content is only {content_length} words, which is below the recommended minimum of 800 words."
            action = "**Action:** Expand your content with valuable, relevant information. Aim for at least 800-1000 words to provide comprehensive coverage of your topic and improve rankings."
            priority_class = "content-seo"
        
        elif has_title == "No" or has_meta == "No":
            priority = "On-Page SEO"
            missing = []
            if has_title == "No":
                missing.append("title tag")
            if has_meta == "No":
                missing.append("meta description")
            reason = f"Your page is missing {' and '.join(missing)}, which are essential for search engine optimization."
            action = "**Action:** Add a compelling title tag (50-60 characters) and meta description (150-160 characters) that includes your target keywords and encourages clicks."
            priority_class = "onpage-seo"
        
        elif pagespeed < 50:
            priority = "Technical SEO"
            reason = f"Your PageSpeed score is {pagespeed}/100, which is below the acceptable threshold."
            action = "**Action:** Optimize images, minify CSS/JavaScript, enable caching, use a CDN, and consider upgrading your hosting. Fast loading speeds are crucial for both user experience and SEO."
            priority_class = "technical-seo"
        
        else:
            priority = "Off-Page SEO"
            reason = "Your on-page and technical SEO are in good shape. Focus on building authority."
            action = "**Action:** Build quality backlinks from reputable websites, create shareable content, engage on social media, and consider guest posting on industry-relevant sites."
            priority_class = "offpage-seo"
        
        # Display results
        st.markdown("---")
        st.markdown("## 📊 Analysis Results")
        
        # Priority box with custom styling
        st.markdown(f"""
            <div class="priority-box {priority_class}">
                <h2 style="margin-top: 0;">🎯 Priority: {priority}</h2>
                <p style="font-size: 1.1rem; margin: 1rem 0;"><strong>Why:</strong> {reason}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Action recommendations
        st.markdown("### 💡 Recommended Actions")
        st.markdown(action)
        
        # Additional info
        st.markdown("---")
        st.info("💡 **Tip:** Address the highest priority issues first for maximum impact on your search rankings.")
        
        # Summary box
        with st.expander("📋 Analysis Summary"):
            st.write(f"**URL:** {url}")
            st.write(f"**Indexed:** {indexed}")
            st.write(f"**Content Length:** {content_length} words")
            st.write(f"**Title Tag:** {has_title}")
            st.write(f"**Meta Description:** {has_meta}")
            st.write(f"**PageSpeed Score:** {pagespeed}/100")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 0.9rem;'>"
    "Built with Streamlit | AI SEO Priority Analysis Tool"
    "</p>",
    unsafe_allow_html=True
)
