import streamlit as st
import requests
st.title("Video Section")

toggle = st.toggle("Enable Youtube Video Question Answering")

if not toggle:
    st.set_page_config(page_title="Video Summarization", page_icon="🎥")
    st.subheader("Video Summarization")

    uploaded_file = st.file_uploader(
        'Upload a video file',
        type=["mp4", "mov", "avi", "mkv"]
    )

    if uploaded_file is not None:
        with st.spinner('Processing video...'):
            try:
                response = requests.post(
                    'http://127.0.0.1:8000/video-summarize',
                    files={
                        "video_file": (
                            uploaded_file.name,
                            uploaded_file.getvalue(),
                            uploaded_file.type
                        )
                    }
                )

                if response.status_code == 200:
                        data = response.json()
                        st.success('Answer:')
                        summary_text = data['answer']
                        st.write(summary_text)
                else:
                    st.error(f"Error: {response.json().get('detail')}")

            except Exception as e:
                st.error(f"Connection error: {e}")
else:
    st.set_page_config(page_title="YouTube Q&A", page_icon="🎥")
    st.subheader("YouTube Q&A")
    st.write("Ask questions about any YouTube video")

    video_url = st.text_input("Enter YouTube URL")
    query = st.text_input("Enter your question")

    if st.button("Get Answer"):
        if not video_url or not query:
            st.warning("Please enter both URL and question.")
        else:
            with st.spinner("Processing video..."):
                try:
                    response = requests.post(
                        'http://127.0.0.1:8000/youtube-qna',
                        json={
                            'url': video_url,
                            'query': query
                        }
                    )

                    if response.status_code == 200:
                        data = response.json()
                        st.success('Answer:')
                        st.write(data['answer'])
                    else:
                        st.error(f"Error: {response.json().get('detail')}")

                except Exception as e:
                    st.error(f"Connection error: {e}")