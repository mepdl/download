import streamlit as st
from pytube import YouTube, Playlist

st.title("Download de YouTube")

url = st.text_input("Insira a URL do vídeo, áudio ou playlist:")

options = ["Áudio", "Vídeo", "Playlist"]
download_type = st.selectbox("Selecione o tipo de download:", options)

if st.button("Baixar"):
    if url:
        try:
            if download_type == "Playlist":
                playlist = Playlist(url)
                for video_url in playlist.video_urls:
                    yt = YouTube(video_url)
                    if download_type == "Áudio":
                        stream = yt.streams.filter(only_audio=True).first()
                    else:
                        stream = yt.streams.get_highest_resolution()
                    stream.download()
                st.success("Playlist baixada com sucesso!")
            else:
                yt = YouTube(url)
                if download_type == "Áudio":
                    stream = yt.streams.filter(only_audio=True).first()
                else:
                    stream = yt.streams.get_highest_resolution()
                stream.download()
                st.success(f"{download_type} baixado com sucesso!")
        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")
    else:
        st.warning("Por favor, insira uma URL.")
