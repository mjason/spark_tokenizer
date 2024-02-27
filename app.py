import streamlit as st
from lib.tokenizer import Tokenizer
import os

tokenizer = Tokenizer()
colors = ['#FFADAD', '#FFD6A5', '#FDFFB6', '#CAFFBF']

# 对暗黑模式进行优化，确保文本颜色对比度
text_color = "#000000"  # 黑色文本，适用于亮色背景
border_color = "#ffffff"  # 白色边框，增强暗色模式下的对比度


company_name = os.getenv('COMPANY_NAME', '如果需要在中国使用环境变量COMPANY_NAME成你公司的名字')
icp_number = os.getenv('ICP_NUMBER', '在中国公网使用记得设置备案号，环境变量为ICP_NUMBER')
show_icp_info = os.getenv('SHOW_ICP_INFO', 'false').lower() == 'true'

st.set_page_config(page_title="星火 Tokenizer 工具")
st.title("星火 Tokenizer 工具")

text = st.text_area("Text to tokenize", "Type your text here", height=200)

if st.button("Tokenize"):
    tokens = tokenizer.encode(text)

    # 循环使用四种颜色渲染Tokens，增加文本颜色和边框样式
    tokens_html = ''.join(
        f'<span style="background-color:{colors[i % 4]}; color:{text_color}; border:1px solid {border_color};">{token if token.strip() != "" else "[空格]"}</span>&nbsp;'
        for i, token in enumerate(tokens.decodes)
    )
    # 循环使用四种颜色渲染Token IDs，增加文本颜色和边框样式
    token_ids_html = ''.join(
        f'<span style="background-color:{colors[i % 4]}; color:{text_color}; border:1px solid {border_color};">{id_}</span>&nbsp;' for i, id_ in enumerate(tokens.encodes))

    # 使用Markdown渲染带有背景色、文本颜色和边框的结果
    st.markdown("Tokens:", unsafe_allow_html=True)
    st.markdown(
        f"<p style='padding:10px;'>{tokens_html}</p>", unsafe_allow_html=True)
    st.markdown("Token IDs:", unsafe_allow_html=True)
    st.markdown(
        f"<p style='padding:10px;'>{token_ids_html}</p>", unsafe_allow_html=True)
    st.markdown("Token Size:", unsafe_allow_html=True)
    st.markdown(
        f"<p style='padding:10px;'>{tokens.size}</p>", unsafe_allow_html=True)

# 添加页脚备案信息，适配暗黑模式，并调整样式
footer = f"""
    <style>
        .footer {{
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            font-size: 0.8rem;
            padding: 5px;
            z-index: 100;
        }}
        .footer a {{
            color: grey;
        }}
    </style>
    <script>
        // 根据Streamlit的主题动态设置页脚颜色
        const footerStyle = document.createElement('style');
        const theme = window.parent.document.body.getAttribute('data-theme');
        if (theme === 'dark') {{
            footerStyle.innerHTML = '.footer {{background-color: #0e1117; color: grey;}} .footer a {{ color: grey; }}';
        }} else {{
            footerStyle.innerHTML = '.footer {{background-color: #fff; color: grey;}} .footer a {{ color: grey; }}';
        }}
        document.head.appendChild(footerStyle);
    </script>
    <footer class="footer">© 2024 {company_name} | <a href="https://www.beian.miit.gov.cn/" target="_blank">{icp_number}</a></footer>
"""
if show_icp_info:
    st.markdown(footer, unsafe_allow_html=True)
