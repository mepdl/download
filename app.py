import streamlit as st
from pytube import YouTube, Playlist
import os

# Função para baixar vídeo
def download_video(url, output_path='downloads'):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path)
    return stream.default_filename

# Função para baixar áudio
def download_audio(url, output_path='downloads'):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(output_path)
    return stream.default_filename

# Função para baixar playlist
def download_playlist(url, output_path='downloads'):
    playlist = Playlist(url)
    for video in playlist.videos:
        video.streams.first().download(output_path)
    return playlist.title

# Interface do Streamlit
st.title("Baixar Vídeos, Áudios e Playlists do YouTube")

# Campo para inserir a URL
url = st.text_input("Insira a URL do YouTube:")

# Menu para escolher o tipo de download
option = st.selectbox("Escolha o tipo de download:", ["Vídeo", "Áudio", "Playlist"])

# Botão para realizar o download
if st.button("Baixar"):
    if url:
        try:
            if option == "Vídeo":
                filename = download_video(url)
                st.success(f"Vídeo baixado com sucesso: {filename}")
            elif option == "Áudio":
                filename = download_audio(url)
                st.success(f"Áudio baixado com sucesso: {filename}")
            elif option == "Playlist":
                playlist_title = download_playlist(url)
                st.success(f"Playlist '{playlist_title}' baixada com sucesso!")
        except Exception as e:
            st.error(f"Erro ao baixar: {e}")
    else:
        st.warning("Por favor, insira uma URL válida.")