import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests
from PIL import Image

# Function to load Lottie animation from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Function to apply local CSS
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file not found: {file_name}")
    except Exception as e:
        st.error(f"Error loading CSS file: {str(e)}")

# Set page configuration
st.set_page_config(layout="wide")

# Load CSS file
local_css("style.css")

# Load Lottie animation
lottie_contact = load_lottieurl("https://lottie.host/16479003-a806-40f7-99da-ae866bdf44b4/FuDw7bC6RU.json")

# Main content of the portfolio
st.write("##")
st.title("Portfolio")
st.header("Gnanitha Suryadevara")
st.subheader("Hey Guys :wave:")
st.write("---")

# Option Menu
with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About', 'Projects', 'Contact'],
        icons=['person', 'code-slash', 'chat-left-text-fill'],
        orientation='horizontal'
    )

# About Section
if selected == 'About':
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Gnanitha Suryadevara")
            st.title("Undergrad at Hyderabad Institute Of Technology and Management")
            # Add Download Resume Button
            with open("gnanitha_suryadevara_resume.pdf", "rb") as file:
                st.download_button(
                    label="Download Resume",
                    data=file,
                    file_name="./gnanitha_suryadevara_resume.pdf",
                    mime="application/pdf"


                )
            st.markdown(
                """
                <a href="https://www.linkedin.com/in/gnanitha-suryadevara-8686b624b" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/e/e9/Linkedin_icon.svg" alt="LinkedIn" style="width:25px; margin-right:10px;">
                    Connect on LinkedIn
                </a>
                """, unsafe_allow_html=True)
        with col2:
            st.image("pp.jpeg", caption="Gnanitha Suryadevara", width=500)
    st.write("---")

    # Education and Experience Section
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("""
                        Education
                        - HITAM
                            - Bachelor of Engineering-Computer science (Artificial Intelligence and Machine learning)
                        - Chaitanya Junior College
                            - Intermediate
                        - Ravindra Bharathi School
                            - Xth
                        """)
        with col4:
            st.subheader("""
                        Experience
                        - IBM skill build Project-Based internship
                            - 6 weeks
                            - online
                        - BASKETHUNT Pvt Lim (IT AND Web development) internship
                            - 2 months
                            - online""")
    st.write("---")
    with st.container():
        col5, col6 = st.columns(2)
        with col6:
            st.subheader(
                """
                        SKILLS
                        - python
                        - ML
                        - NLP
                        - Data Visualization using EXCEL
                        """
            )
        with col5:
            
            st.header("CERTIFICATIONS")          
            with st.expander("NPTEL Programming, Data Structures And Algorithms Using Python,"):
                st.image("./NPTEL_DS.jpeg")
            with st.expander("IBM skill build Artificial Intelligence in practice"):
                st.image("./IBM_SKILLBUILD.jpeg")
            with st.expander("NPTEL PROGRAMMING IN JAVA"):
                st.image("./NPTEL_JAVA.jpg")

# Project Section
if selected == 'Projects':
    with st.container():
        st.header("My Projects")
        st.write("##")

        with st.expander("Emotion Detection"):
            st.write("""
                    Description:
                    An Emotion Detection Project is aimed at identifying and interpreting human emotions from various inputs such as facial expressions, text, speech, or physiological signals. 
                     The project involves leveraging artificial intelligence (AI) and machine learning (ML) techniques to analyze and classify emotions into predefined categories, such as happiness, sadness, anger, fear, surprise, and others.   
                    """)
                     

        # Language Detection Project with a drop-down
        with st.expander("Language Detection"):
            st.write("""
                Description:
                The Language Detection project is a machine learning-based project that identifies the language of a given text. 
                The model was trained on a large dataset of 16GB consisting of audio samples from various languages. 
                It utilizes natural language processing techniques and basic cnn model to classify the language with high accuracy of 89%.
                """)
        


# Contact Section
if selected == "Contact":
    st.header("Get In Touch")

    contact_form = """ 
    <form action="https://formsubmit.co/gnanitha_s@outlook.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="your name" required>
        <input type="email" name="email" placeholder="your mail id" required>
        <textarea name="message" placeholder="your message" required></textarea>
        <button type="submit">Send</button>
    </form>"""

    left_col, right_col = st.columns((2, 1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st.lottie(lottie_contact, height=200)
        st.markdown(
            """
            <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                <h2>CONTACT US</h2>
            </div>
            """, 
            unsafe_allow_html=True
        )

