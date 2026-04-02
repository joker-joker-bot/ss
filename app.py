import gradio as gr

# 1. 定义一个简单的界面函数（虽然这里不需要输入，但Gradio习惯这样写）
def video_player():
    return "video.mp4"

# 2. 创建 Gradio 界面
with gr.Blocks() as demo:
    gr.Markdown("## 🎬 我的视频播放器")
    
    # 核心代码：使用 gr.Video 组件
    # 这里直接指定文件名，Gradio 会自动处理路径
    video = gr.Video(
        value="video.mp4", 
        label="视频预览", 
        autoplay=True, # 自动播放
    )

# 3. 启动应用
# server_name="0.0.0.0" 是为了让 Streamlit Cloud 能识别并运行它
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)