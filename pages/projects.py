import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Projects | My Portfolio",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
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

st.title('My Projects')

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🚀 Project 1
    **Machine Learning Application**
    
    Developed a predictive analytics tool using scikit-learn and streamlit.
    - Achieved 95% accuracy
    - Deployed to production
    - Used by 1000+ users
    
    [View Project](https://github.com)
    """)
    
with col2:
    st.markdown("""
    ### 💻 Project 2
    **Web Application**
    
    Built a full-stack web application using Flask and React.
    - RESTful API
    - User Authentication
    - Real-time updates
    
    [View Project](https://github.com)
    """)

# Footer
st.markdown("---")
st.markdown("© 2025")