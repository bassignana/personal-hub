import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# Page Configuration
st.set_page_config(
    page_title="Contact | My Portfolio",
    page_icon="📧",
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

def send_email(name, email, message):
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "your-email@gmail.com"
        sender_password = "your-app-password"
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = sender_email
        msg['Subject'] = f"Portfolio Contact from {name}"
        
        body = f"""
        Name: {name}
        Email: {email}
        Message: {message}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, sender_email, text)
        server.quit()
        return True
    except Exception as e:
        st.error(f"Error sending email: {str(e)}")
        return False

st.title('Contact Me')

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Get in Touch
    Feel free to reach out to me for any questions or opportunities.
    """)
    
    with st.form(key='contact_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send Message")
        
        if submit:
            if name and email and message:
                if send_email(name, email, message):
                    st.success("Message sent successfully!")
            else:
                st.warning("Please fill in all fields.")

with col2:
    st.markdown("""
    ### Connect with Me
    - [LinkedIn](https://linkedin.com)
    - [GitHub](https://github.com)
    - [Twitter](https://twitter.com)
    """)

# Footer
st.markdown("---")
st.markdown("© 2025")