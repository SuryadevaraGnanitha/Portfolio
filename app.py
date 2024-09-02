import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests
from PIL import Image


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file not found: {file_name}")
    except Exception as e:
        st.error(f"Error loading CSS file: {str(e)}")


st.set_page_config(layout="wide")
# Load CSS file from the same directory
local_css("./style.css")

lottie_contact = load_lottieurl(
    "https://lottie.host/f6213881-ec5d-492b-ae84-bd0cc18145cc/gUGgrBbGMO.json"
)

st.title("Portfolio website")
st.header("Gnanitha Suryadevara")
st.subheader("Hey Guys :wave:")
st.write("---")

selected = option_menu(
    menu_title=None,
    options=["About", "Project", "Contact"],
    icons=["person", "code-slash", "chat-left-text-fill"],
    orientation="horizontal",
)

if selected == "About":
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("I am Gnanitha Suryadevara")
            st.title("Undergrad at Hyderabad Institute Of Technology and Management")
        with col2:
            st.image("pp.jpeg", caption="Gnanitha Suryadevara", width=500)
    st.write("---")

    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader(
                """
                        Education
                        - HITAM
                            - Bachelor of Engineering-Computer science (Artificial Intelligence and Machine learning)
                        - Chaitanya Junior College
                            - Intermediate
                        - Ravindra Bharathi School
                            - Xth
                        """
            )
        with col4:
            st.subheader(
                """
                        Experience
                        - IBM skill build Project-Based internship
                            - 6 weeks
                            - online
                        - BASKETHUNT Pvt Lim (IT AND Web development) internship
                            - 2 months
                            - online"""
            )
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


                     


if selected == "Project":
    with st.container():
        st.header("My Projects")
        st.write("##")
        # Language Detection Project with a drop-down
        with st.expander("Language Detection"):
            st.write(
                """
                **Description:**
                The Language Detection project is a machine learning-based project that identifies the language of a given text. 
                The model was trained on a largex dataset consisting of text samples from various languages. 
                It utilizes natural language processing techniques to classify the language with high accuracy.
                """
            )


if selected == "Contact":
    st.header("Get In Touch")
    st.write("##")
    st.write("##")

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
        st.lottie(lottie_contact, height=300)
