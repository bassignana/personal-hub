import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"  # This collapses the sidebar by default
)

# Hide Streamlit default elements
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    /* This hides specific Streamlit elements */
    .stDeployButton {
        display: none !important;
    }
    [data-testid="stToolbar"] {
        display: none !important;
    }
    /* Existing styles */
    .main {
        padding: 0rem 5rem;
    }
    .profile-img {
        border-radius: 50%;
        border: 5px solid #f0f0f0;
    }
    .gif-container {
        border: 2px solid #f0f0f0;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
    }
    .stButton > button {
        width: 100%;
    }
    div[data-testid="stHorizontalBlock"] {
        gap: 0px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Horizontal Navigation
col1, col2, col3, col4 = st.columns(4, gap="small")
with col1:
    st.page_link("main.py", label="Home", icon="🏠")
with col2:
    st.page_link("pages/projects.py", label="Projects", icon="🚀")
with col3:
    st.page_link("pages/blog.py", label="Blog", icon="📝")
with col4:
    st.page_link("pages/contact.py", label="Contact", icon="📧")

st.title('Welcome')

# Profile section
col1, col2 = st.columns([1, 2])
with col1:
    # Hard-coded profile picture
    profile_image_url = "static/profile_image.jpeg"
    st.image(profile_image_url, width=250, caption="Tommaso Bassignana's profile image.")
    
    # Hard-coded GIF
    gif_url = "https://your-gif-url.com/animation.gif"
    st.image(gif_url, caption="Featured Work", use_column_width=True)

with col2:
    st.markdown("""
    # Tommaso Bassignana
    ### Insert a very cool description here.
    
    Double digit years of experience in breaking stuff, understanding stuff and building useful things, sometimes.
    
    [GitHub](https://github.com) | [LinkedIn](https://linkedin.com)
    """)

# Footer
st.markdown("---")
st.markdown("© 2025")