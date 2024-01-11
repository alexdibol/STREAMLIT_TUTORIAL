import streamlit as st

import streamlit as st

def main():
    st.title('Image Embedding in Streamlit')
    image_url = "https://www.tripsavvy.com/thmb/YKRDxBOXpPbyG36okPP_qAIMb0M=/5496x3690/filters:no_upscale():max_bytes(150000):strip_icc()/king-s-college-chapel--cambridge-186707375-5ee669af8f6543d7847575b5a644d2bd.jpg"
    st.image(image_url, caption='King\'s College Chapel, Cambridge')

if __name__ == "__main__":
    main()

