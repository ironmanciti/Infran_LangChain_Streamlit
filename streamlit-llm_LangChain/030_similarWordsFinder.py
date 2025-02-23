# .env 파일에서 환경 변수를 읽어오기
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  

import streamlit as st
from langchain_openai import OpenAIEmbeddings

#FAISS는 Facebook AI Research에서 개발한 오픈소스 라이브러리로,
#최근접 이웃 검색 작업에 최적화된 인덱싱 구조와 알고리즘을 제공합
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import CSVLoader
import pandas as pd

# Streamlit 페이지 설정
st.set_page_config(page_title="Educate Kids")

# 웹 페이지 헤더
st.header("영어 단어 하나를 입력하시면 비슷한 단어들을 골라 드리겠습니다.")

#OpenAIEmbeddings 객체 초기화
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# CSVLoader 객체 초기화
loader = CSVLoader(file_path='similar_words.csv',
csv_args={
    'delimiter': ',',  # CSV 파일의 구분자 설정
    'quotechar': '"',  # CSV 파일의 텍스트 묶음 기호 설정
    'fieldnames': ['Words']  # CSV 필드 이름 설정
})

# CSV 파일 데이터를 Document 형식으로 로드
data = loader.load()

# Pandas를 이용해 CSV 파일 읽기 (데이터 확인용)
df = pd.read_csv('similar_words.csv')

# 데이터프레임을 Streamlit에 표시 (3줄만 표시되도록 설정)
st.dataframe(df, height=150)  

# FAISS 벡터 스토어를 생성
vector_store = FAISS.from_documents(data, embeddings)

#사용자로부터 입력을 받아 변수에 저장하는 함수
def get_text():
    # 텍스트 입력 필드 생성
    input_text = st.text_input("사용자: ")
    return input_text

# 사용자 입력 받기
user_input = get_text()
# 버튼 클릭 이벤트 설정
submit = st.button('비슷한 단어 고르기') 

# 버튼이 눌리고 입력값이 존재하는 경우 실행
if submit and user_input:
    # 사용자 입력을 사용해 유사도 검색 수행
    docs = vector_store.similarity_search(user_input)
    
    # 검색 결과 출력
    st.subheader("Top 5 Matches:")
    
    # 최대 5개의 검색 결과를 순서대로 출력
    for i in range(min(5, len(docs))):
        st.text(f"{i+1}st Match: {docs[i].page_content}")


