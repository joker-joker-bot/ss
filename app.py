import streamlit as st

# 1. 设置页面标题
st.set_page_config(page_title="视频播放器", page_icon="🎬")

st.title("🎬 视频播放测试")
st.write("正在尝试使用原生 HTML 播放 video.mp4...")

# 2. 核心代码：原生 HTML 播放器
# 注意：这里直接引用同目录下的 video.mp4
video_html = """
<video width="100%" height="auto" controls autoplay>
  <source src="video.mp4" type="video/mp4">
  您的浏览器不支持视频标签。
</video>
"""

# 3. 在页面上显示
st.markdown(video_html, unsafe_allow_html=True)

# 调试信息
st.info("如果上方是一片空白，说明找不到 video.mp4 文件。")