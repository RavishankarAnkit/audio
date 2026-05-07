import streamlit as st
import librosa
import librosa.display
import numpy as np
import soundfile as sf
import wave
from pydub import AudioSegment
from scipy.io import wavfile
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import tempfile

st.title("Audio Processing App")

# Upload MP3 file
uploaded_file = st.file_uploader("Upload MP3 File", type=["mp3"])

if uploaded_file is not None:

    st.success("File Uploaded Successfully")

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_mp3:
        tmp_mp3.write(uploaded_file.read())
        mp3_path = tmp_mp3.name

    # Convert MP3 to WAV
    audio = AudioSegment.from_mp3(mp3_path)

    wav_path = "test.wav"

    audio.export(wav_path, format="wav")

    st.success("Converted MP3 to WAV")

    # Read WAV file
    fs_wav, data_wav = wavfile.read(wav_path)

    # Show sampling frequency
    st.subheader("Sampling Frequency")
    st.write(fs_wav)

    # Show audio data shape
    st.subheader("Audio Shape")
    st.write(data_wav.shape)

    # If stereo audio take first channel
    if len(data_wav.shape) > 1:
        data = data_wav[:, 0]
    else:
        data = data_wav

    # Audio Player
    st.subheader("Audio Player")

    audio_file = open(wav_path, "rb")

    st.audio(audio_file.read(), format="audio/wav")

    # Load using librosa
    audio_signal, sample_rate = librosa.load(wav_path)

    # Waveform Plot
    st.subheader("Waveform")

    fig, ax = plt.subplots(figsize=(10,3))

    librosa.display.waveshow(audio_signal, sr=sample_rate, ax=ax)

    st.pyplot(fig)
