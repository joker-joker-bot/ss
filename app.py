import streamlit as st
import base64

st.title("我的视频播放器")

# --- 方法：使用 HTML 标签直接播放 ---

# 1. 读取视频文件
video_file = open('video.mp4', 'rb')
video_bytes = video_file.read()

# 2. 把视频转换成浏览器能看懂的格式 (base64)
video_base64 = base64.b64encode(video_bytes).decode('utf-8')

# 3. 用 HTML 强行播放
st.markdown(f'''
    <video width="100%" height="auto" controls autoplay>
        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        您的浏览器不支持视频标签。
    </video>
''', unsafe_allow_html=True)