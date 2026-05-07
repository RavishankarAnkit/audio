import streamlit as st
import librosa
import numpy as np
import soundfile as sf
import wave
from pydub import AudioSegment
from scipy.io import wavfile
import tempfile

st.title("Audio WAV Converter and Player")

# Upload MP3 file
uploaded_file = st.file_uploader("Upload MP3 File", type=["mp3"])

if uploaded_file is not None:

    st.success("File Uploaded Successfully")

    # Save uploaded MP3 temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_mp3:
        tmp_mp3.write(uploaded_file.read())
        mp3_path = tmp_mp3.name

    # Convert MP3 to WAV
    audio = AudioSegment.from_mp3(mp3_path)

    wav_path = "test.wav"

    audio.export(wav_path, format="wav")

    st.success("Converted to WAV")

    # Read WAV file
    fs_wav, data_wav = wavfile.read(wav_path)

    # Display sample rate
    st.subheader("Sample Rate")
    st.write(fs_wav)

    # Display audio data
    st.subheader("Audio Data")
    st.write(data_wav)

    # Play audio
    st.subheader("Audio Player")

    audio_file = open(wav_path, "rb")

    st.audio(audio_file.read(), format="audio/wav")
