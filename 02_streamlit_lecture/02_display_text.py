"""
2단계: 텍스트 출력 함수들
학습 목표: 다양한 방식으로 텍스트 출력하기
"""

import streamlit as st

# ============================================
# 1. 제목과 헤더
# ============================================
st.title("📝 텍스트 출력 함수 배우기")
st.header("1. 제목과 헤더")
st.subheader("이것은 소제목입니다")

st.write("""
Streamlit은 다양한 방식으로 텍스트를 출력할 수 있습니다.  
각 함수의 용도를 이해하고 적절히 사용하는 것이 중요합니다.
""")

# ============================================
# 2. 일반 텍스트
# ============================================
st.divider()
st.header("2. 일반 텍스트")

st.text("이것은 st.text() 함수입니다.")
st.write("이것은 st.write() 함수입니다. - 가장 많이 사용됩니다!")

# st.write는 마크다운도 지원합니다
st.write("**굵은 글씨**, *기울임*, ~~취소선~~")

# ============================================
# 3. 마크다운
# ============================================
st.divider()
st.header("3. 마크다운")

st.markdown("""
### 마크다운으로 작성한 소제목

마크다운을 사용하면 더 풍부한 서식을 사용할 수 있습니다:
- **굵은 글씨**
- *기울임*
- `코드 강조`
- [링크](https://streamlit.io)

#### 리스트
1. 첫 번째
2. 두 번째
3. 세 번째
""")

# ============================================
# 4. 코드 블록
# ============================================
st.divider()
st.header("4. 코드 블록")

st.code("""
def hello():
    print("Hello, Streamlit!")
    return "안녕하세요"
""", language="python")

# 다른 언어도 가능합니다
st.code("""
SELECT * FROM users
WHERE age > 20
ORDER BY name;
""", language="sql")

# ============================================
# 5. 수식 (LaTeX)
# ============================================
st.divider()
st.header("5. 수식")

st.latex(r"""
E = mc^2
""")

st.latex(r"""
\sum_{i=1}^{n} x_i = x_1 + x_2 + ... + x_n
""")

# ============================================
# 6. 상태 메시지
# ============================================
st.divider()
st.header("6. 상태 메시지")

st.success("✅ 성공 메시지 - 작업이 성공적으로 완료되었습니다!")
st.info("ℹ️ 정보 메시지 - 유용한 정보를 제공합니다.")
st.warning("⚠️ 경고 메시지 - 주의가 필요합니다.")
st.error("❌ 에러 메시지 - 문제가 발생했습니다.")

# ============================================
# 7. 기타 유용한 함수
# ============================================
st.divider()
st.header("7. 기타 유용한 함수")

st.caption("이것은 작은 설명 텍스트입니다 (캡션)")

# 인용문
st.markdown("> 누구나 코딩을 할 수 있다. - 박태근")

# 인터넷상 이미지
st.caption("인터넷상 이미지 표시")
st.image("data:image/jpeg;base64,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", use_container_width=True)

# 이미지 사이즈를 화면에 맞추고싶다면? 강제로 늘릴 수 있음
st.image("https://placehold.co/300x300")
# st.image("https://placehold.co/300x300", use_container_width=True)

# 로컬 이미지
st.caption("내 컴퓨터의 이미지 표시")
st.image('image/sample1.jpg')

# ============================================
# 실습 과제
# ============================================
st.divider()
st.header("📝 실습 과제")

st.markdown("""
### 과제: 뉴스 기사 만들기

다음 요소들을 포함한 가상의 뉴스 기사를 만들어보세요:
1. `st.title()`로 기사 제목
2. `st.caption()`으로 작성자와 날짜
3. `st.image()`로 이미지 (URL 사용 가능)
4. `st.markdown()`으로 본문 내용
5. `st.info()`로 관련 정보 박스
6. `st.code()`로 코드나 데이터 예시
""")

# 예시 답안 (접어두기)
with st.expander("💡 예시 답안 보기"):
    st.title("🚀 AI 기술의 새로운 돌파구")
    st.caption("작성자: 홍길동 | 2026-01-15")
    
    st.image("https://placehold.co/600x400", caption="AI 연구소")
    
    st.markdown("""
    최근 연구진이 새로운 AI 알고리즘을 개발했다고 발표했습니다.
    
    이 기술은 기존 방식보다 **50% 더 빠른** 처리 속도를 보여줍니다.
    """)
    
    st.info("이 기술은 2027년 상용화될 예정입니다.")

import streamlit as st

# 1. 제목: st.title()
st.title("AI 데이터 분석, 프로 스포츠 전략에 혁신을 불러오다")

# 2. 작성자와 날짜: st.caption()
st.caption("작성자: 이승민 | 2026-01-16 · 스포츠 테크 전문 기자")

# 3. 이미지: st.image() (URL 사용)
st.image(
    "https://images.pexels.com/photos/1405355/pexels-photo-1405355.jpeg",
    caption="데이터 분석이 적용된 프로 축구 경기 장면 (이미지 출처: Pexels)",
    use_column_width=True
)

# 4. 본문 내용: st.markdown()
st.markdown(
"""
프로 스포츠 현장에서 **AI 기반 데이터 분석**이 전술과 선수 관리의 핵심 도구로 자리 잡고 있다.  
국내 주요 프로 축구·야구 구단들은 이미 수 년 전부터 선수의 움직임, 체력 소모, 부상 위험도 등을
실시간으로 수집·분석하는 시스템을 도입했다.

코칭스태프는 이 데이터를 바탕으로 **최적의 라인업 구성**, **교체 타이밍 결정**,  
상대 팀의 **공격 패턴 분석**까지 세밀하게 준비할 수 있게 됐다.  
특히 최근에는 경기 중에도 태블릿과 대시보드를 통해 실시간 AI 분석 결과를 확인하며
전술을 즉각적으로 수정하는 모습이 자주 포착되고 있다.

전문가들은 AI가 기존의 경험·감(감각)에 의존하던 전략 수립 과정을 **정량화**하고,  
선수 개개인의 **퍼포먼스 관리**를 극대화할 수 있을 것으로 기대하고 있다.  
반면, 데이터 의존도가 지나치게 높아질 경우, **예측 불가한 변수**와  
선수의 멘탈, 경기 흐름과 같은 **정성적 요소**가 간과될 수 있다는 우려도 제기된다.

국내 프로야구 한 구단의 데이터 분석 담당자는  
“AI가 답을 주는 것이 아니라, 더 나은 질문을 던지도록 도와주는 도구”라며  
“결국 결정은 사람이 내리되, AI는 그 결정을 더 똑똑하게 만들어 주는 역할을 한다”고 말했다.
"""
)

# 5. 관련 정보 박스: st.info()
st.info(
"""
**관련 스포츠 테크 동향**  
- K리그 일부 구단은 선수의 움직임을 추적하는 **트래킹 데이터 시스템**을 도입해  
  경기당 스프린트 횟수, 평균 속도, 회복 속도 등을 분석하고 있음.  
- 프로야구에서는 투수의 **구종·구속·회전수(Spin Rate)** 데이터와  
  타자의 **타구 발사각·타구 속도** 데이터를 활용해 맞춤형 훈련 프로그램을 설계.  
- 유럽 주요 축구 리그는 AI를 활용해 **부상 위험 예측 모델**을 구축,  
  특정 선수의 주당 출전 시간과 훈련 강도를 자동으로 조절하는 시스템을 시험 중.
"""
)

# 6. 코드나 데이터 예시: st.code()
st.subheader("스포츠 경기 데이터 분석 예시 코드")

st.code(
"""
import pandas as pd

# 예시: 축구 경기에서 선수별 이동 거리를 분석하는 간단한 코드

# 가상의 트래킹 데이터 (CSV) 예시
# columns: [player_id, player_name, total_distance_m, high_intensity_runs, max_speed_kmh]
df = pd.read_csv("match_tracking_sample.csv")

# 경기에서 가장 많이 뛴 선수 TOP 5
top_runners = df.sort_values("total_distance_m", ascending=False).head(5)

print("경기 중 가장 많이 뛴 선수 TOP 5")
print(top_runners[["player_name", "total_distance_m"]])

# 고강도 질주(high_intensity_runs)가 많은 선수 TOP 5
top_sprinters = df.sort_values("high_intensity_runs", ascending=False).head(5)

print("\\n고강도 스프린트 횟수가 가장 많은 선수 TOP 5")
print(top_sprinters[["player_name", "high_intensity_runs"]])

# 특정 선수의 부하 관리 지표 예시
player_name = "홍길동"
player_row = df[df["player_name"] == player_name].iloc[0]

load_score = (
    player_row["total_distance_m"] * 0.001  # km 단위
    + player_row["high_intensity_runs"] * 0.5
    + player_row["max_speed_kmh"] * 0.2
)

print(f"\\n{player_name}의 경기 부하 점수(예시): {load_score:.2f}")
""",
    language="python"
)
