import streamlit as st


import os

image_path = os.path.join("img", "bobo.png")
st.image(image_path)

with st.sidebar:
    st.write("""
    - 这个工具的后端还在开发中
    - 敬请期待
    - 如果你对这方面有具体的需求和想法
    - 可以给我发邮件
    - （464864419@qq.com）
    - 我将参考你的需求来改进功能
    """)

st.markdown("---")

st.markdown("## 直播话术的template_text还在总结中，请耐心等待")

st.write("#### 等待期间，先看看美女图片吧")

st.markdown("---")
st.write("#### 以下是使用Stable Diffusion 进行换脸的图")

column1,column2 = st.columns(2)

with column1:
    st.write("这张是原图")
    image_path = os.path.join("img", "C-face (0).png")
    st.image(image_path, width=300)

with column2:
    st.write("这边是换脸之后")
    image_path = os.path.join("img", "C-face (1).png")
    st.image(image_path, width=300)
    image_path = os.path.join("img", "C-face (2).png")
    st.image(image_path, width=300)
    image_path = os.path.join("img", "C-face (3).png")
    st.image(image_path, width=300)
    image_path = os.path.join("img", "C-face (4).png")
    st.image(image_path, width=300)


