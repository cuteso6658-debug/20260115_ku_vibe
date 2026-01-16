"""
1단계: Streamlit 소개 및 첫 번째 앱
학습 목표: Streamlit의 기본 구조 이해하기
"""

import streamlit as st

# 브라우저창 텝을 보면 아이콘과 페이지 타이틀이 바뀌어있는것을 볼 수 있다.
st.set_page_config(
    page_title="스트림릿과의 만남",
    page_icon="🎨",
    layout="wide"  # "centered" 또는 "wide"
)

# 제목 표시
st.title("🎉 나의 첫 Streamlit 앱")

# 간단한 텍스트 출력
st.write("안녕하세요! Streamlit에 오신 것을 환영합니다.")

# 구분선
st.divider()

# 자기소개 섹션
st.header("자기소개")
st.write("이름: 홍길동")
st.write("직업: 데이터 분석가")
st.write("관심사: 데이터 시각화, 머신러닝")

# 구분선
st.divider()

# 간단한 인터랙션
st.subheader("버튼을 눌러보세요!")
if st.button("인사하기"):
    st.balloons()  # 풍선 애니메이션
else:
    st.success("반갑습니다! 🎊")


# 정보 박스
st.info("💡 팁: 코드를 수정하고 저장하면 자동으로 새로고침됩니다!")

# ============================================
# 실습 과제
# ============================================
st.divider()
st.header("📝 실습 과제")
st.markdown("""
1. 제목을 자신의 이름으로 변경해보세요
2. 자기소개 내용을 본인의 정보로 바꿔보세요
3. 새로운 버튼을 추가하고, 클릭 시 다른 메시지가 나오도록 해보세요
4. `st.warning()` 또는 `st.error()` 함수를 사용해보세요
""")

import streamlit as st

# 1. 제목을 자신의 이름으로 변경
st.title("홍길동의 Streamlit 앱")  # 👉 여기를 본인 이름으로 변경하세요

# 2. 자기소개 내용을 본인의 정보로 변경
st.header("자기소개")
st.write("""
안녕하세요, 저는 홍길동입니다.  
데이터 분석과 파이썬 프로그래밍에 관심이 많고,  
웹 대시보드를 Streamlit으로 만드는 것을 좋아합니다.
""")  # 👉 본인 소개로 수정

# 3. 새로운 버튼 추가 + 클릭 시 다른 메시지 출력
st.subheader("버튼 예제")

if st.button("안녕하세요 버튼"):
    st.success("안녕하세요! 반갑습니다 😊")  # 첫 번째 버튼 메시지

if st.button("오늘 기분 버튼"):
    st.info("오늘도 좋은 하루 보내세요! 🚀")  # 두 번째(새로운) 버튼 메시지

# 4. st.warning() 또는 st.error() 사용
st.subheader("알림 메시지 예제")

st.warning("주의: 이 기능은 아직 테스트 중입니다.")  # 경고 메시지
st.error("에러: 서버와의 연결에 문제가 발생했습니다.")  # 에러 메시지

