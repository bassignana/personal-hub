import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Skills | My Portfolio",
    page_icon="💡",
    layout="wide"
)

# Navigation links
st.page_link("main.py", label="Home", icon="🏠")
st.page_link("pages/projects.py", label="Projects", icon="🚀")
st.page_link("pages/skills.py", label="Skills", icon="💡")
st.page_link("pages/contact.py", label="Contact", icon="📧")

st.title('Skills & Expertise')

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Technical Skills")
    skills_data = {
        'Skill': ['Python', 'JavaScript', 'SQL', 'Machine Learning', 'AWS'],
        'Level': [90, 85, 80, 85, 75]
    }
    df = pd.DataFrame(skills_data)
    st.dataframe(df, hide_index=True)

with col2:
    st.markdown("### Certifications")
    st.markdown("""
    - AWS Certified Solutions Architect
    - Google Cloud Professional Data Engineer
    - Microsoft Azure Developer Associate
    """)

# Footer
st.markdown("---")
st.markdown("© 2024 My Portfolio. Built with Streamlit.")