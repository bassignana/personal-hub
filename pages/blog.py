import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Blog | My Portfolio",
    page_icon="📝",
    layout="wide"
)

# Custom CSS for blog layout
st.markdown("""
    <style>
    .blog-post {
        padding: 20px;
        border: 1px solid #f0f0f0;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .blog-date {
        color: #666;
        font-size: 0.9em;
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

st.title('Blog')

# Blog posts
posts = [
    {
        "title": "The Future of AI Development",
        "date": "February 15, 2025",
        "preview": "Exploring the latest trends in artificial intelligence and what they mean for developers...",
        "tags": ["AI", "Technology", "Development"],
        "read_time": "5 min read"
    },
    {
        "title": "Building Scalable Systems with Python",
        "date": "February 10, 2025",
        "preview": "A deep dive into architectural patterns for scaling Python applications...",
        "tags": ["Python", "Architecture", "Backend"],
        "read_time": "8 min read"
    },
    {
        "title": "Machine Learning in Production",
        "date": "February 5, 2025",
        "preview": "Best practices for deploying and maintaining machine learning models in production...",
        "tags": ["Machine Learning", "DevOps", "Production"],
        "read_time": "6 min read"
    }
]

# Blog post display
for post in posts:
    st.markdown(f"""
    <div class="blog-post">
        <h3>{post['title']}</h3>
        <p class="blog-date">{post['date']} • {post['read_time']}</p>
        <p>{post['preview']}</p>
        <p><i>Tags: {', '.join(post['tags'])}</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Add a "Read More" button for each post
    if st.button(f"Read More: {post['title']}"):
        # This is where you'd add logic to show the full post
        # For now, it's just a placeholder
        st.write("Full post content would go here...")

# Footer
st.markdown("---")
st.markdown("© 2025")