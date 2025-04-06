import streamlit as st
from PIL import Image
from autotiktokenizer import AutoTikTokenizer


def main():
    st.set_page_config(page_title="LLM Token Estimator", layout="wide", page_icon="images/favicon.ico")

    try:
        image = Image.open("images/robot_token.jpg")
        st.image(image, width=400)
    except FileNotFoundError as e:
        st.error(f"The image file 'robot_token.jpg' was not found: {e}")
    except Exception as e:
        st.error(f"Failed to load image: {e}")

    st.logo("images/robotf-small.png", size="large", link="https://robotf.ai", icon_image="images/robotf-small.png")

    # Title and description
    st.title("RoboTF LLM Token Estimator")
    st.write("Enter text below to count the number of tokens for your specific LLM Model.")
    
    # Provide example model names and link to Hugging Face
    st.write("Example model names: `mistralai/Mistral-7B-Instruct-v0.3`, `deepseek-ai/DeepSeek-Coder-V2-Instruct-0724`, `Qwen/Qwen2.5-Coder-32B-Instruct`")
    st.markdown("[Browse models on Hugging Face Hub](https://huggingface.co/models) 🤗")
    st.markdown("Should support any model with a `tokenizer.json` in the HuggingFace repo")
    st.markdown("If using a quant, or re-train, point at original model repo with `tokenizer.json`")
    st.markdown("This is only an estimator based on [autotiktokenizer](https://github.com/bhavnicksm/autotiktokenizer) project - Go Support them")
    st.markdown("---")
    st.markdown("How this works:")
    st.markdown("You enter the user/model-repo-name that contains a `tokenizer.json` from huggingface")
    st.markdown("It removes any newline characters in the input")
    st.markdown("We use autotiktokenizer to take your prompt input and estimate the tokens for that model")
    st.markdown("For private Huggingface repos you will need to set the ")
    st.markdown("Hope you find useful and can find the Github project here: [RoboTF LLM Token Estimator](https://github.com/kkacsh321/robotf-llm-token-estimator)")

    # Function to load tokenizer with caching
    @st.cache_resource
    def load_tokenizer(model_name):
        return AutoTikTokenizer.from_pretrained(model_name)
    
    # Create a form for the inputs and button
    with st.form(key='token_count_form'):
        # Text input for the model name
        model_name = st.text_area(
            "Enter the Hugging Face model name: (org/model_name)",
            placeholder="mistralai/Mistral-7B-Instruct-v0.3", height=68  # Default model name
        )
        
        # Text area for the user's input text
        user_input = st.text_area("Your text:", height=200)
        
        # Submit button
        submit_button = st.form_submit_button(label='Count Tokens')
    
    # When the form is submitted
    if submit_button:
        if model_name:
            # Initialize the tokenizer
            try:
                tokenizer = load_tokenizer(model_name)
            except Exception as e:
                st.error(f"Error loading tokenizer for model '{model_name}': {e}")
                st.stop()
            
            if user_input:
                # Replace newlines with spaces in the user input
                cleaned_input = user_input.replace('\n', ' ')
                
                # Tokenize the cleaned input text
                tokens = tokenizer.encode(cleaned_input)
                token_count = len(tokens)
                
                # Display results
                st.subheader("Results")
                st.write(f"**Model:** {model_name}")
                st.write(f"**Estimated Token count:** {token_count}")
                st.write(f"**Original Text Length:** {len(user_input)} characters")
                st.write(f"**Cleaned Text Length:** {len(cleaned_input)} characters")
                
            else:
                st.warning("Please enter some text to count tokens.")
        else:
            st.warning("Please enter a model name to proceed.")

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
