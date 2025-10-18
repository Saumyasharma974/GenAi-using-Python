import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import re

# Load environment variables
load_dotenv()

# Initialize model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

st.title("🎥 YouTube Video Summarizer")
st.caption("Paste a YouTube video link and get a clean AI-generated summary!")

# Input field
video_url = st.text_input("🔗 Paste YouTube Video URL here:")

def extract_video_id(url):
    """Extract video ID from YouTube URLs"""
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    return match.group(1) if match else None

if st.button("✨ Generate Summary"):
    video_id = extract_video_id(video_url)

    if not video_id:
        st.error("❌ Invalid YouTube URL. Please check and try again.")
    else:
        try:
            with st.spinner("⏳ Fetching transcript..."):
                ytt_api = YouTubeTranscriptApi()
                fetched_transcript = ytt_api.fetch(video_id, languages=['en', 'hi'])

                # ✅ Convert snippets to text
                text = " ".join([snippet.text for snippet in fetched_transcript]).strip()

            # ✅ Split into chunks
            splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=200)
            chunks = splitter.split_text(text)

            st.info(f"📄 Transcript split into {len(chunks)} parts. Summarizing...")

            summaries = []
            for i, chunk in enumerate(chunks, 1):
                with st.spinner(f"🧠 Summarizing part {i}/{len(chunks)}..."):
                    response = model.invoke(f"Summarize this part clearly:\n{chunk}")
                    summaries.append(response.content)

            final_summary = model.invoke(
                "Combine these summaries into one final detailed yet concise summary:\n"
                + " ".join(summaries)
            )

            st.subheader("🧾 Final Summary")
            st.write(final_summary.content)

        except TranscriptsDisabled:
            st.error("🚫 This video has transcripts disabled.")
        except Exception as e:
            st.error(f"❌ Error: {e}")
