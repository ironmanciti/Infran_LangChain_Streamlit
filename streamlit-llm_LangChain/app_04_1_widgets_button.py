import streamlit as st 

# 이 스크립트는 Streamlit을 사용하여 버튼, 라디오 버튼, 체크박스, 셀렉트 박스, 슬라이더와 같은 다양한 UI 위젯을 표시하는 예제입니다.

# 버튼 위젯을 생성합니다.
st.button('버튼 위젯')

# 버튼을 클릭하면 이름을 출력합니다.
name = "김길동"
if st.button("Submit"):
    st.write("이름: {}".format(name))
    
# 라디오 버튼으로 상태를 선택합니다.
status = st.radio("선택", ("활성화", "비활성화"))
if status == "활성화":
    st.success("활성화 되었습니다.")
else:
    st.warning("비활성화 되었습니다.")
    
# 체크박스를 선택하여 텍스트를 표시하거나 숨깁니다.
if st.checkbox("show/hide"):
    st.text("Showing something")
    
# 셀렉트 박스를 사용해 언어를 선택합니다.
languages = ["Python", "Java", "C++", "C#"]
choice = st.selectbox("언어 선택", languages)
st.write("{}을 선택하셨습니다.".format(choice))

# 멀티 셀렉트를 사용해 여러 언어를 선택합니다.
my_languages = st.multiselect("내가 아는 언어들", languages, default="Java")
st.write(my_languages)

# 슬라이더를 사용해 나이를 선택합니다.
age = st.slider("나이", 1, 100, 50)
st.write("나이는 {}입니다.".format(age))
