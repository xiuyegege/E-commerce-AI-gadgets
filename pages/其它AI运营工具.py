import streamlit as st


import os

image_path = os.path.join("img", "yoyo.png")
st.image(image_path)

st.write("## 目前规划中依次要开发出来的小工具")
st.write("希望你也参与其中")

st.markdown("---")

st.markdown("### AI短视频脚本及AI视频生成器")
st.markdown("""
    > 直接从脚本到视频生成，
    然后对接发布到社交媒体平台
    """)

st.markdown("### AI电商数据爬取和分析")
st.markdown("""
> 从主要的电商平台和社交媒体平台获取数据，
然后进行数据分析和可视化，
自动监测高点击、高转化、供求关系不平衡的词和商品）
""")

st.markdown("### AI中国电商供应链爬取")
st.markdown("""
> 从上一个工具爬取爆款信息后,在这里自动从包括1688、拼多多等在内的所有以批发为主的电商平台上获取商品信息
自动生成供应链数据以便筛选比价
""")

st.markdown("---")

st.write("""
> 如果你在日常的运营中，有具体的需求和想法。欢迎和我沟通，我会尝试去实现这些AI运营工具。
  我的邮箱（464864419@qq.com)
""" )