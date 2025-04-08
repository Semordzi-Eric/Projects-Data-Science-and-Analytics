import streamlit as st
import whisper 
import tempfile  # To handle uploaded files safely

# Load Whisper model once (outside function to optimize performance)
model = whisper.load_model("base")

st.title("Speech AI App")
st.write("Upload an audio file to transcribe.")

audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

if audio_file:
    st.audio(audio_file)
    st.write("Processing...")

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        temp_file.write(audio_file.read())  # Write file content
        temp_path = temp_file.name  # Get saved file path

    # Transcribe audio using Whisper
    result = model.transcribe(temp_path)

    # Display Transcription
    st.subheader("Transcription:")
    st.write(result['text'])

