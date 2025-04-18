import streamlit as st
from PIL import Image

def get_server_ip():
    host = st.context.headers.get("host", None)
    
    if host:
        return host.split(':')[0]  # Remove port if present
    
    # Fallback to local IP
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception:
        return 'localhost'
    
def main():
    # Streamlit UI setup
    st.set_page_config(layout="wide")
    st.title("RoboTF LLM Tools for LocalAI usage!")
    st.logo("images/robotf-small.png", size="large", icon_image="images/robotf-small.png")

    try:
        image = Image.open("images/robotf-tools.jpg")
        st.image(image, width=300, caption="RoboTF LLM Tools")
    except FileNotFoundError as e:
        st.error(f"The image file 'robot-tools.jpg' was not found: {e}")
    except Exception as e:
        st.error(f"Failed to load image: {e}")
        
    st.write("What does this suite of tools do so far:")
    st.write("  * Docker Command Runner")
    st.write("  * Docker Dashboard")
    st.write("  * HuggingFace Downloader")
    st.write("  * LLM Token Estimator for open source models")
    st.write("  * Model Config Editor for LocalAI")
    st.write("Choose your selection from the left hand menu")
    
    st.write("Other Application Links in RoboTF AI Suite (must be running)")
    server_ip = get_server_ip()
    application_links = f"""
    [LocalAI](http://{server_ip}:8080) | 
    [ComfyUI](http://{server_ip}:8188) | 
    [Open WebUI](http://{server_ip}:3000) | 
    [Flowise](http://{server_ip}:3001) | 
    [n8n](http://{server_ip}:5678) | 
    [Postgres](http://{server_ip}:5432) | 
    [ChromaDB](http://{server_ip}:8000) | 
    [Unstructured API](http://{server_ip}:8003)
    """
    st.markdown(application_links.replace('\n', ' '), unsafe_allow_html=True)
    
    st.divider()

    # Social Media Icons and Links
    social_media_links = """
    [![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@RoboTFAI)
    [![Reddit](https://img.shields.io/badge/Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=white)](https://www.reddit.com/user/RoboTF-AI/)
    [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/kkacsh321)
    [![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/RoboTF)
    [![X](https://img.shields.io/badge/X-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/RoboTF_AI)
    [![Email](https://img.shields.io/badge/Email-008000?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxIDEgMTAwIj48cG9seWdvbiBwb2ludHM9IjUwLDAgMTAwLDUwIDUwLDEwMCAwLDUwIiBmaWxsPSIjMDA4MDBGIi8+PC9zdmc+&logoColor=white)](mailto:robot@robotf.ai)
    [![Website](https://img.shields.io/badge/Website-00B4D8?style=for-the-badge&logo=web&logoColor=white)](https://robotf.ai)
    """
    st.markdown(social_media_links.replace('\n', ' '), unsafe_allow_html=True)
    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("custom_configs/style.css")

    # Add footer with copyright information
    st.write("Copyright © 2025 RoboTF.ai. All Rights Reserved.")
        
if __name__ == "__main__":
    main()