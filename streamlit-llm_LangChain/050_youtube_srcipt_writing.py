# .env 파일에서 환경 변수를 읽어옵니다.
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# DuckDuckGo 검색 툴
from langchain.tools import DuckDuckGoSearchResults

# Button Style 지정
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#FFFFFF;
}
</style>""", unsafe_allow_html=True)

# 현재 라인에 두 개의 열을 생성
col1, col2 = st.columns([1, 4])

# 첫 번째 열에 YouTube 이미지를 추가
col1.image('./Youtube.jpg', width=150)
# 두 번째 열에 "동영상 대본 생성기" 텍스트를 추가
col2.write("# 동영상 대본 생성기")

# -------------------
# 동영상 대본 생성 함수 (LCEL 파이프라인 방식)
# -------------------
def generate_script(prompt, video_length, creativity):
    
    llm = ChatOpenAI(temperature=creativity, model="gpt-4o-mini") 
    
    # 1. Title 생성용 Prompt
    title_prompt = ChatPromptTemplate.from_messages([
        ("user", "YouTube 동영상의 제목을 정해주세요: {subject}.")
    ])
    # 2. Script 생성용 Prompt
    script_prompt = ChatPromptTemplate.from_messages([
        ("user", 
         "이 제목을 바탕으로 YouTube 동영상용 대본을 만들어 보세요. "
         "{search_results} 검색 데이터를 이용하여 "
         "제목: {title}인 {duration}분 분량의 동영상 대본을 한글로 작성해 주세요.")
    ])

    # 3. Title 및 Script 생성을 위한 체인 구성
    title_chain = (
        title_prompt 
        | llm
        | StrOutputParser()
    )

    script_chain = (
        script_prompt
        | llm
        | StrOutputParser()
    )

    # 4. DuckDuckGo 검색 결과
    search_tool = DuckDuckGoSearchResults()

    # 5. Title 생성
    title = title_chain.invoke({"subject": prompt})
    
    # 6. DuckDuckGo 검색 결과를 가져옴
    search_results = search_tool.run(prompt)
    
    # 7. Script 생성
    script = script_chain.invoke({
        "search_results": search_results,
        "title": title,
        "duration": video_length
    })

    return search_results, title, script

# 사용자 입력 받기
prompt = st.text_input('동영상의 주제를 입력하세요.', key="prompt")
video_length = st.text_input('예상 시간 🕒 (분)', key="video_length")
creativity = st.slider('Temperature - (0 LOW || 1 HIGH)', 0.0, 1.0, 0.2, step=0.1)

# 대본 생성 버튼
submit = st.button("대본을 생성합니다.")

if submit:
    # 대본 생성 함수 호출
    search_results, title, script = generate_script(prompt, video_length, creativity)
    st.success('생성이 완료 되었습니다. 만족하시기기 바랍니다. ❤️')

    # 제목 표시
    st.subheader("제목:")
    st.write(title)

    # 동영상 대본 표시
    st.subheader("동영상 대본:📝")
    st.write(script)

    # 검색 결과 표시
    st.subheader("검토 - DuckDuckGo Search 결과:🔍")
    with st.expander('Show me 👀'):
        st.info(search_results)
