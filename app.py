import streamlit as st
from lib.tokenizer import Tokenizer

tokenizer = Tokenizer()
colors = ['#FFADAD', '#FFD6A5', '#FDFFB6', '#CAFFBF']

st.title("星火 Tokenizer 工具")

text = st.text_area("Text to tokenize", "Type your text here", height=200)

# Tokenization
if st.button("Tokenize"):
    tokens = tokenizer.encode(text)

    # 循环使用四种颜色渲染Tokens
    tokens_html = ''.join(
        f'<span style="background-color:{colors[i % 4]};">{token if token.strip() != "" else "[空格]"}</span>&nbsp;'
        for i, token in enumerate(tokens.decodes)
    )
    # 循环使用四种颜色渲染Token IDs
    token_ids_html = ''.join(
        f'<span style="background-color:{colors[i % 4]};">{id_}</span>&nbsp;' for i, id_ in enumerate(tokens.encodes))

    # 使用Markdown渲染带有背景色的结果
    st.markdown("Tokens:", unsafe_allow_html=True)
    st.markdown(
        f"<p style='background-color:#f0f2f6; padding:10px;'>{tokens_html}</p>", unsafe_allow_html=True)
    st.markdown("Token IDs:", unsafe_allow_html=True)
    st.markdown(
        f"<p style='background-color:#f0f2f6; padding:10px;'>{token_ids_html}</p>", unsafe_allow_html=True)
    st.markdown("Token Size:", unsafe_allow_html=True)
    st.markdown(
        f"<p style='background-color:#f0f2f6; padding:10px;'>{tokens.size}</p>", unsafe_allow_html=True)

footer = """<style>
.a {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: white;
    color: grey;
    text-align: center;
    padding: 10px;
    font-size: 16px;
}
</style>
<div class='a'>© 2024 MJ <在国内部署请看 app.py 修改备案号> | <a href="https://www.beian.miit.gov.cn/" target="_blank">备案号：粤ICP备XXXXXX号-1</a></div>
"""
st.markdown(footer, unsafe_allow_html=True)
