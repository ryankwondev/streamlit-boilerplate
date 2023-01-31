import streamlit as st

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title('안녕하세요!')
st.write('대충 만들었어요')
# input
code = st.text_input('이거 필드 이름', '이건 샘플 텍스트')
# button
if st.button('버튼이름'):
    # show modal
    st.success('조회되었습니다.')
    # show INPUT + "이런거"
    st.write(code + "더해서")
