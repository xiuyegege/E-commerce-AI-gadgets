import streamlit as st

import qa_utils
from hongshu_utils import generate_xiaohongshu

import os

image_path = os.path.join("img", "xiaohongshu.png")
st.image(image_path)

st.header("秀叶·问大家文案生成器")

st.write("这个生成器会模拟用户提问和用户回答，生成10条新用户的提问和老客户的回答文案")

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

submit = st.button("开始创作：“客户看了就要下单的”问大家文案吧")

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
        result = qa_utils.generate_cunstomer_qa(product_features, user_QA, openai_api_key, creativity)
    st.divider()

    st.markdown("#### 问大家的问1：")
    st.write(result.customer_questions[0])
    st.markdown("#### 问大家的答1：")
    st.write(result.customer_answer[0])
    st.markdown("---")

    st.markdown("#### 问大家的问2：")
    st.write(result.customer_questions[1])
    st.markdown("#### 问大家的答2：")
    st.write(result.customer_answer[1])
    st.markdown("---")

    st.markdown("#### 问大家的问3：")
    st.write(result.customer_questions[2])
    st.markdown("#### 问大家的答3：")
    st.write(result.customer_answer[2])
    st.markdown("---")

    st.markdown("#### 问大家的问4：")
    st.write(result.customer_questions[3])
    st.markdown("#### 问大家的答4：")
    st.write(result.customer_answer[3])
    st.markdown("---")

    st.markdown("#### 问大家的问5：")
    st.write(result.customer_questions[4])
    st.markdown("#### 问大家的答5：")
    st.write(result.customer_answer[4])
    st.markdown("---")

    st.markdown("#### 问大家的问6：")
    st.write(result.customer_questions[5])
    st.markdown("#### 问大家的答6：")
    st.write(result.customer_answer[5])
    st.markdown("---")

    st.markdown("#### 问大家的问7：")
    st.write(result.customer_questions[6])
    st.markdown("#### 问大家的答7：")
    st.write(result.customer_answer[6])
    st.markdown("---")

    st.markdown("#### 问大家的问8：")
    st.write(result.customer_questions[7])
    st.markdown("#### 问大家的答8：")
    st.write(result.customer_answer[7])
    st.markdown("---")

    st.markdown("#### 问大家的问9：")
    st.write(result.customer_questions[8])
    st.markdown("#### 问大家的答9：")
    st.write(result.customer_answer[8])
    st.markdown("---")

    st.markdown("#### 问大家的问10：")
    st.write(result.customer_questions[9])
    st.markdown("#### 问大家的答10：")
    st.write(result.customer_answer[9])



