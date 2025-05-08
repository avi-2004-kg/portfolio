import streamlit as st
from PIL import Image

st.set_page_config(page_title="My Interactive Portfolio", layout="wide")

# Top Navigation Bar
st.markdown("""
<style>
.navbar {
    background: linear-gradient(to right, #673ab7, #3f51b5);
    padding: 12px 0;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    position: sticky;
    top: 0;
    z-index: 1000;
}
.navbar a {
    color: white;
    font-weight: 600;
    text-decoration: none;
    margin: 0 20px;
    font-size: 1rem;
}
.navbar a:hover {
    color: #c5cae9;
}
.badge {
    display: inline-block;
    margin-top: 14px;
    background: linear-gradient(to right, #7e57c2, #5c6bc0);
    color: white;
    padding: 8px 18px;
    border-radius: 50px;
    font-weight: bold;
    font-size: 0.95rem;
}
</style>

<div class="navbar">
    <a href="#about">About</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center; color: #3f51b5;'>My Interactive Portfolio</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Explore my skills, projects, and reach out to collaborate!</p>", unsafe_allow_html=True)
st.markdown('<p class="badge" style="text-align:center; display:block;">Web & AI Developer</p>', unsafe_allow_html=True)

# About Section
st.markdown('<a name="about"></a>', unsafe_allow_html=True)
st.markdown("## About Me")
st.write("I’m a developer passionate about combining web development with AI to build smart, user-friendly applications. I love working with multilingual NLP, generative models, and real-time interactions.")

# Skills Section
st.markdown('<a name="skills"></a>', unsafe_allow_html=True)
st.markdown("## Skills")
cols = st.columns(6)
skills = ["HTML", "CSS", "JavaScript", "Python", "Flask", "TensorFlow"]
for i, skill in enumerate(skills):
    with cols[i]:
        st.button(skill, key=skill)

# Projects Section
st.markdown('<a name="projects"></a>', unsafe_allow_html=True)
st.markdown("## Projects")

# Load images
img1 = Image.open("m1.png")
img2 = Image.open("m2.png")
img3 = Image.open("m3.png")

# Project 1
st.image(img1, caption="Multilanguage Chatbot", use_column_width=True)
st.write("**Multilanguage Chatbot**  \nSupports multiple languages with AI tools for loan guidance and document checks.  \n[View Project](https://github.com/avi-2004-kg/Multilanguage-chatbot)")

# Project 2
st.image(img2, caption="Handwritten-to-Image Converter", use_column_width=True)
st.write("**Handwritten-to-Image Converter**  \nAI model that converts text into visual content using generative tools.  \n[Try Demo](https://github.com/avi-2004-kg/Handwritten-To-image-converter)")

# Project 3
st.image(img3, caption="Portfolio Website", use_column_width=True)
st.write("**Portfolio Website**  \nFully responsive personal portfolio to showcase skills and projects.  \n[View Site](#)")

# Contact Section
st.markdown('<a name="contact"></a>', unsafe_allow_html=True)
st.markdown("## Contact")
st.write("📧 Email: [kgavinash0@gmail.com](mailto:kgavinash0@gmail.com)  \n📞 Phone: [9902174350](tel:+1234567890)")

# Footer
st.markdown("<hr><p style='text-align: center;'>&copy; 2025 My Portfolio</p>", unsafe_allow_html=True)
