import streamlit as st
from PIL import Image
import base64

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

st.title('Welcome to My Portfolio')

# Profile section
col1, col2 = st.columns([1, 2])
with col1:
    # Hard-coded profile picture
    # Replace this URL with your actual image URL or base64 string
    profile_image_url = "https://your-image-url.com/profile.jpg"
    st.image(profile_image_url, width=250, caption="John Doe")
    
    # Hard-coded GIF
    # Replace this URL with your actual GIF URL or base64 string
    gif_url = "https://your-gif-url.com/animation.gif"
    st.image(gif_url, caption="Featured Work", use_column_width=True)

    # Alternative method using base64 (uncomment and replace with your image data)
    """
    # For profile picture
    profile_image_base64 = "your-base64-encoded-image-string"
    st.markdown(f'<img src="data:image/jpeg;base64,{profile_image_base64}" alt="Profile Picture" class="profile-img" width="250">', unsafe_allow_html=True)
    
    # For GIF
    gif_base64 = "your-base64-encoded-gif-string"
    st.markdown(f'<img src="data:image/gif;base64,{gif_base64}" alt="Featured Work" class="gif-container" width="100%">', unsafe_allow_html=True)
    """

with col2:
    st.markdown("""
    # John Doe
    ### Software Developer | Data Scientist
    
    I'm a passionate developer with expertise in Python, Machine Learning, and Web Development.
    With 5 years of experience in building scalable applications and implementing data-driven solutions.
    
    [GitHub](https://github.com) | [LinkedIn](https://linkedin.com)
    """)

# Footer
st.markdown("---")
st.markdown("© 2025")