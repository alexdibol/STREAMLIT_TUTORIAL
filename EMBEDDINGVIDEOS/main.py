import streamlit as st

def main():
    st.title('Image and Video Embedding in Streamlit')

    # Embedding the image
    image_url = "https://www.tripsavvy.com/thmb/YKRDxBOXpPbyG36okPP_qAIMb0M=/5496x3690/filters:no_upscale():max_bytes(150000):strip_icc()/king-s-college-chapel--cambridge-186707375-5ee669af8f6543d7847575b5a644d2bd.jpg"
    st.image(image_url, caption='King\'s College Chapel, Cambridge')

    # Embedding the YouTube video
    video_url = "https://youtu.be/isP3lspL644"
    st.video(video_url)

if __name__ == "__main__":
    main()

