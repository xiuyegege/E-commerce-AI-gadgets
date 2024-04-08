import streamlit as st
from hongshu_utils import generate_xiaohongshu

import os

image_path = os.path.join("img", "xiaohongshu.png")
st.image(image_path)

# st.image("../img/xiaohongshu.png")

st.header("秀叶·AI小红书爆款笔记仿写工具")
with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API密钥：", type="password")
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")

# 分割线
st.write("---")

st.write("#### 第一步应该先找到你的对标笔记")

column1,column2,column3 = st.columns(3)
with column1:
    st.write("""
    - 起号阶段：
    - 【参考粉丝数不过万的博主，找到她笔记中点赞数、收藏数较高的帖子。】""")

with column2:
    st.write(""" - 运营号：
- 【参考粉丝数和自己差不多的博主，
找到她笔记中点赞数、收藏数较高的帖子。】
""")

with column3:
    st.write("""- 不要去找和自己粉丝数差别太大的大博主；
- 具体参考的数据要从自己所在细分领域去查看
""")

# 分割线
st.write("---")

Reference_Topic = st.text_input("复制参考爆款笔记的主题")

Reference_Text = paragraph = st.text_area("复制参考爆款笔记的正文", height=200, max_chars=2800)

# 分割线
st.write("---")
st.write("""我们这里不是简单的仿写，还是会加入一个新主题，这个主题可以是近期热点、热搜。
另外尽量要和你仿写的文案有一定关系，你要没关系也可以，那就得让AI自己多发挥了。
""")

theme = st.text_input(" 填写你的主题")

creativity = st.slider("✨ 填写文案创造力（参数越小，文案越参考原文，参数越大，AI 越放飞自我）",
                       min_value=0.0, max_value=1.5, value=0.4, step=0.1)

manner_speaking = st.selectbox("要求写作的语气：（点击单选）",[
    "参考文：和案例文案一样的情感",
    "喜悦的：描述开心、愉快的情绪",
    "悲伤的：表达伤心、难过之情",
    "平静的：传达内心的安宁与平和",
    "愤怒的：表示强烈的不满或愤怒",
    "焦虑的：体现担忧、不安的心情",
    "恐惧的：描述害怕、恐惧的感受",
    "自信的：展现对自身的信心与肯定",
    "自卑的：表示自我怀疑或不自信",
    "满足的：传达一种满意、知足的状态",
    "孤独的：形容独处、寂寞的情感",
    "好奇的：表现对事物的兴趣和探求欲",
    "感恩的：表达对他人的感激之情",
    "浪漫的：营造浪漫、温馨的氛围",
    "忧郁的：显示出一种愁苦、郁闷的情绪",
    "激动的：形容情绪激昂、兴奋",
    "无奈的：表示对某种情况的无力感",
    "乐观的：传递积极、向上的心态",
    "沮丧的：体现失望、灰心的心情"])

submit = st.button("点击开始我惊天地泣鬼神的创作吧！")

if submit and not openai_api_key:
    st.info("请输入你的OpenAI API密钥")
    st.stop()
if submit and not Reference_Topic:
    st.info("请输入参考爆款笔记的主题")
    st.stop()
if submit and not Reference_Text:
    st.info("请输入爆款主题的文案")
    st.stop()
if submit and not theme:
    st.info("请输入生成你想要的主题，如果不知道，就从参考爆款主题里提取，或直接复制爆款主题")
    st.stop()
if submit:
    with st.spinner("AI正在努力创作中，请稍等..."):
        result = generate_xiaohongshu(theme,manner_speaking,Reference_Topic,Reference_Text, openai_api_key,creativity)
    st.divider()
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("##### 小红书标题1")
        st.write(result.titles[0])
        st.markdown("##### 小红书标题2")
        st.write(result.titles[1])
        st.markdown("##### 小红书标题3")
        st.write(result.titles[2])
        st.markdown("##### 小红书标题4")
        st.write(result.titles[3])
        st.markdown("##### 小红书标题5")
        st.write(result.titles[4])
    with right_column:
        st.markdown("##### 小红书正文")
        st.write(result.content)

