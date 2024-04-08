import streamlit as st


st.sidebar.title("秀叶电商AI应用小工具")
with st.sidebar:
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")


st.image("./img/banner_秀爷工具.jpg")

st.header("秀叶电商AI应用小工具")

st.write("##### 应用工具在左侧工具栏，依次点选")

# 分割线
st.markdown("---")

st.write("##### 这里分享的工具有限，如果你有需要解决的问题，或者有想要用AI替换的工作流，可以联系我，我来看看可以怎么使用AI来解决。")

st.markdown("## 秀叶介绍")
st.write("""- 标签：电商商家，AI设计师
- 秀叶是一个小众服装品牌主理人，和大家一样是电商商家。
- 通过不断的学习、寻找工具和自己开发一些AI应用来解决我们的一些电商经营中遇到的问题。
- 在这里分享自己开发的一些常用的AI小工具。""")

# 分割线
st.markdown("---")
st.write("""- 让我们一起：降低成本，提高电商运营效率，替换掉一些不必要的人工
- 上一个时代，我们借助人工帮我们赚钱，
- 下一个AI时代，我们一起学习借助人工智能帮我们赚钱。
""")

st.markdown("#### 常见疑问")

with st.expander("展开查看详细信息"):
    st.markdown("##### 费用？")
    st.write("""- 我这里的工具都开源，免费使用。
- 但是调用AI模型的API，会消耗费用。这个费用是OPAI收取，不是我收。
- 通常调用chatgpt_3.5写一篇小红书文案可能几毛钱左右，根据文章长度来计费的。
""")
    st.markdown("##### 什么是API")
    st.write("""- API是程序应用接口，
- 这里的AI是使用了OPENAI的接口。
- 需要到OPENAI的官网注册，并获取API_KEY
- 我这里的工具默认调用chat_gpt3.5
- 如果想使用更高级的gpt4，可以联系我帮忙修改模型设置

    """)
    st.markdown("##### 安装到自己电脑")
    st.write("""- 项目源码在GitHub
- 需要的伙伴自行下载
- 如果自己的公司没有AI工程师，可以联系我帮忙部署。
    """)
