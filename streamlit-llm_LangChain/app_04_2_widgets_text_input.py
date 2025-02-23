import streamlit as st 

# 이 스크립트는 Streamlit을 사용하여 텍스트 입력, 비밀번호 입력, 텍스트 영역, 숫자 입력, 날짜 입력 위젯을 표시하는 예제입니다.

# 텍스트 입력 필드를 생성합니다.
name = st.text_input("이름을 입력하세요.")
st.write(name)

# 비밀번호 입력 필드를 생성합니다.
password = st.text_input("비밀번호를 입력하세요.", type="password")
st.write(password)

# 사용자가 여러 줄의 텍스트를 입력할 수 있습니다.
message = st.text_area("메시지를 입력하세요.", height=100)
st.write(message)

# 숫자 입력 필드를 생성합니다.
number = st.number_input("숫자를 입력하세요.")
st.write(number)

# 날짜 선택 필드를 생성합니다.
appointment_date = st.date_input("약속 일자를 입력하세요.")
st.write(appointment_date)
