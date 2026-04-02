import streamlit as st

# 1. 设置网页的基本信息（标题、图标、布局）
st.set_page_config(
    page_title="我的私人影院", 
    page_icon="🎬", 
    layout="centered"
)

# 2. 写网页内容（像写普通 Python 脚本一样）

# 显示大标题
st.title("🎬 我的私人视频影院")

# 显示一段介绍文字
st.write("这是一个使用 Python Streamlit 快速搭建的视频播放页面。")
video_url = "https://www.w3schools.com/html/mov_bbb.mp4"

# 3. 核心功能：播放视频
# 只需要一行代码，Streamlit 会自动处理播放器的样式
st.video("video_url")

# 4. 添加一点互动（比如侧边栏）
st.sidebar.header("设置")
st.sidebar.info("这里可以放播放列表或者简介。")