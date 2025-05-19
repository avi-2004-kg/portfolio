import streamlit as st
from PIL import Image

st.set_page_config(page_title="My Interactive Portfolio", layout="wide")

# Load images
img1 = Image.open("m1.png")  # Multilanguage Chatbot
img2 = Image.open("m2.png")  # Handwritten-to-Image Converter
img3 = Image.open("m3.png")  # Portfolio Website
img4 = Image.open("m4.png")  # LangChain News Summarizer

# Font Awesome + Styling
st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        .stTabs [data-baseweb="tab-list"] {
            justify-content: center;
        }
        .stTabs [role="tab"] {
            font-size: 18px;
            padding: 10px 20px;
        }
        img {
            border-radius: 10px;
            max-height: 180px;
            object-fit: cover;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center; color: #3f51b5;'>🚀 My Interactive Portfolio</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Explore my work, skills, and projects below.</p>", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["👤 About", "⚙️ Skills", "📁 Projects", "📞 Contact"])

# About Tab
with tab1:
    st.markdown("## <i class='fas fa-user'></i> About Me", unsafe_allow_html=True)
    st.write("I’m a developer passionate about combining web development with AI to build smart, user-friendly applications.")
    st.write("I love working with multilingual NLP, generative models, and real-time interactions.")

# Skills Tab
with tab2:
    st.markdown("## <i class='fas fa-cogs'></i> Skills", unsafe_allow_html=True)
    cols = st.columns(6)
    skills = ["HTML", "CSS", "JavaScript", "Python", "Flask", "TensorFlow"]
    for i, skill in enumerate(skills):
        with cols[i]:
            st.button(skill, key=skill)

# Projects Tab
with tab3:
    st.markdown("## <i class='fas fa-project-diagram'></i> Projects", unsafe_allow_html=True)

    # First row
    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:
        st.image(img1, caption="Multilanguage Chatbot", use_container_width=True)
        st.markdown("""
        **Multilanguage Chatbot**  
        Supports multiple languages with AI tools for loan guidance and document checks.  
        [🔗 View Project](https://github.com/avi-2004-kg/Multilanguage-chatbot)
        """)

    with row1_col2:
        st.image(img2, caption="Handwritten-to-Image Converter", use_container_width=True)
        st.markdown("""
        **Handwritten-to-Image Converter**  
        AI model that converts text into visual content using generative tools.  
        [🔗 Try Demo](https://github.com/avi-2004-kg/Handwritten-To-image-converter)
        """)

    # Second row
    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:
        st.image(img3, caption="Portfolio Website", use_container_width=True)
        st.markdown("""
        **Portfolio Website**  
        Fully responsive personal portfolio to showcase skills and projects.  
        [🔗 View Site](#)
        """)

    with row2_col2:
        st.image(img4, caption="LangChain News Summarizer", use_container_width=True)
        st.markdown("""
        **LangChain-of-News-Summarizer-Translator**  
        Summarizes and translates latest news articles using LangChain and NLP tools.  
        [🔗 View Project](https://github.com/avi-2004-kg/LangChain-of-News-Summarizer-Translator)
        """)

# Contact Tab
with tab4:
    st.markdown("## <i class='fas fa-envelope'></i> Contact", unsafe_allow_html=True)
    st.write("📧 Email: [kgavinash0@gmail.com](mailto:kgavinash0@gmail.com)")
    st.write("📞 Phone: [+91 9902174350](tel:+919902174350)")
    st.write("💼 GitHub: [github.com/avi-2004-kg](https://github.com/avi-2004-kg)")

# Footer
st.markdown("<hr><p style='text-align: center;'>&copy; 2025 My Portfolio</p>", unsafe_allow_html=True)
