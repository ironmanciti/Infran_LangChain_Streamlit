import streamlit as st 
from PIL import Image

# 이 스크립트는 Streamlit을 사용하여 이미지, 비디오, 오디오와 같은 미디어 파일을 표시하는 예제입니다.

# 이미지 파일 열기
img = Image.open("data/banana.jpg")  

# 이미지를 원래의 크기로 표시합니다.
st.image(img)  

# 이미지가 컨테이너 너비에 맞게 자동으로 조정됩니다.
st.image(img, use_container_width=True)  

# URL에서 이미지를 불러와 너비를 200픽셀로 설정하여 표시합니다.
url = "https://cdn.britannica.com/92/13192-050-6644F8C3/bananas-bunch.jpg"
st.image(url, width=200)  

# 로컬 비디오 파일을 읽어옵니다.
video_file = open("data/AI_artist_news.mp4", "rb").read()  

# 비디오 파일을 Streamlit 앱에 표시합니다.
st.video(video_file)  

# 로컬 오디오 파일을 읽어옵니다.
audio_file = open("data/song.mp3", "rb").read()  

# 오디오 파일을 100초부터 재생합니다.
st.audio(audio_file, start_time=100)
