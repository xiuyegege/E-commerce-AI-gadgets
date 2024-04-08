import streamlit as st
import seller_text_utils


import os

image_path = os.path.join("img", "maijiaxiu.png")
st.image(image_path)

st.header("秀叶·买家秀文案生成器")

with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API密钥：", type="password")
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")

st.markdown("---")
product_features = st.text_area("请输入产品的卖点信息：", height=200, max_chars=2800)

with st.expander("怎么写卖点信息"):
    st.write("##### 小商家不知道怎么写卖点？")
    st.write("""
    - 在平台上找到销量比较高的竞品
- 把竞品的标题复制出来
- 在竞品的产品页面把卖点提取出来
- 把竞品的海报、主图用图片提取文字的工具提取出来（qq截图功能就有）
- 然后把这些信息整理一下就可以填进去了
    """)

st.markdown("---")
user_QA = st.text_area("请输入自己或竞品的问大家信息：", height=200, max_chars=3200)
with st.expander("问大家怎么获取"):
    st.write("##### 问大家一条一条的复制太费时？")
    st.write("""
    - 可以使用 xparth 工具在网页上爬取
    - 我会在稍后把 Xpath 工具的使用方法录一个视频传到这里
    - 时间允许的话，还会做一个爬取大家信息的工具，我会放在这里供大家使用
    - 如果你想快一点用上，也可以打赏我哦
    """)
st.markdown("---")
creativity = st.slider("✨ 填写文案创造力（参数越小，文案越参考问大家信息，参数越大，AI 越放飞自我）",
                       min_value=0.0, max_value=1.5, value=0.4, step=0.1)

st.markdown("---")

submit = st.button("开始创作：“客户看了就要下单”的买家秀评价文案吧")

if submit and not openai_api_key:
    st.info("请输入你的OpenAI API密钥")
    st.stop()
if submit and not product_features:
    st.info("请输入参考爆款笔记的主题")
    st.stop()
if submit and not user_QA:
    st.info("请输入爆款主题的文案")
    st.stop()

if submit:
    with st.spinner("AI正在努力创作中，请稍等..."):
        result = seller_text_utils.generate_seller_text(product_features, user_QA, openai_api_key, creativity)
    st.divider()
    st.markdown("#### 评价文案")
    st.write(result.seller_assess[0])
    st.write(result.seller_assess[1])
    st.write(result.seller_assess[2])
    st.write(result.seller_assess[3])
    st.write(result.seller_assess[4])
    st.write(result.seller_assess[5])
    st.write(result.seller_assess[6])
    st.write(result.seller_assess[7])
    st.write(result.seller_assess[8])
    st.write(result.seller_assess[9])




