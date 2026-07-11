import streamlit as st

# 1. 웹앱 타이틀 및 학생 정보 입력창
st.title("🏃‍♂️ 고등학교 학년별/성별 맞춤형 PAPS 평가 프로그램")
st.markdown("학년, 성별과 기록을 입력하면 공인 기준에 맞춘 운동 처방 리포트가 생성됩니다.")

student_name = st.text_input("학생 이름을 입력하세요:", "홍길동")

# 학년 선택 기능과 성별 선택 기능을 직관적인 라디오 버튼으로 배치
student_grade = st.radio("학년을 선택하세요:", ["1학년", "2학년", "3학년"])
gender = st.radio("성별을 선택하세요:", ["남학생", "여학생"])

st.subheader("📋 PAPS 측정 기록 입력")

# 2. 디지털 데이터 입력창 생성
shuttle_run = st.number_input("1. 왕복오래달리기 (회) 입력:", min_value=0, value=40)
long_jump = st.number_input("2. 제자리멀리뛰기 (cm) 입력:", min_value=0, value=180)
sit_and_reach = st.number_input("3. 유연성: 앉아윗몸앞으로굽히기 (cm) 입력:", value=10.0)
grip_strength = st.number_input("4. 악력 (kg) 입력:", min_value=0.0, value=30.0)

# 3. 분석 버튼을 누르면 조건문 실행
if st.button("📊 PAPS 분석 및 운동 처방 리포트 보기"):
    st.markdown(f"### 📑 {student_name} 학생({student_grade} {gender})의 분석 결과")
    
    # [알고리즘 분기] 각 학년 및 성별에 따른 4~5등급(저체력 경고) 국가공인 커트라인 수치 자동 세팅
    # 교육부 학교건강검사규칙 필수평가 기준표 데이터 엄격 적용
    if student_grade == "1학년":
        if gender == "남학생":
            shuttle_cut, jump_cut, reach_cut, grip_cut = 40, 186, 3.0, 30.0
        else:
            shuttle_cut, jump_cut, reach_cut, grip_cut = 24, 131, 6.0, 18.0
            
    elif student_grade == "2학년":
        if gender == "남학생":
            shuttle_cut, jump_cut, reach_cut, grip_cut = 42, 195, 4.0, 33.0
        else:
            shuttle_cut, jump_cut, reach_cut, grip_cut = 24, 133, 6.5, 19.0
            
    elif student_grade == "3학년":
        if gender == "남학생":
            shuttle_cut, jump_cut, reach_cut, grip_cut = 45, 200, 5.0, 35.0
        else:
            shuttle_cut, jump_cut, reach_cut, grip_cut = 24, 135, 7.0, 20.0

    # 4. 설정된 커트라인 변수값들을 활용하여 대소 비교 및 피드백 출력 자동화
    # [왕복오래달리기 평가]
    if shuttle_run < shuttle_cut:
        st.error(f"- [심폐지구력 경고]: 현재 학년 기준({shuttle_cut}회 미만)보다 심폐지구력이 매우 취약합니다. 주 3회 30분 이상 조깅을 추천합니다.")
    else:
        st.success("- [심폐지구력 양호]: 현재 학년 기준을 충족합니다. 우수한 유산소 능력을 꾸준히 유지하세요.")

    # [제자리멀리뛰기 평가]
    if long_jump < jump_cut:
        st.error(f"- [순발력 경고]: 현재 학년 기준({jump_cut}cm 미만)보다 순발력이 다소 부족합니다. 스쿼트 점프 등으로 하체 폭발력을 기르세요.")
    else:
        st.success("- [순발력 양호]: 현재 학년 기준을 충족합니다. 하체의 순간적인 힘 발휘 능력이 좋습니다.")

    # [유연성 평가]
    if sit_and_reach < reach_cut:
        st.error(f"- [유연성 경고]: 현재 학년 기준({reach_cut}cm 미만)보다 가동 범위가 좁아 부상 위험이 있습니다. 매일 스트레칭을 하세요.")
    else:
        st.success("- [유연성 양호]: 현재 학년 기준을 충족합니다. 관절 상태를 잘 유지하고 있습니다.")

    # [악력 평가]
    if grip_strength < grip_cut:
        st.error(f"- [근력 경고]: 현재 학년 기준({grip_cut}kg 미만)보다 악력이 약합니다. 철봉 매달리기나 악력기를 이용해 힘을 기르세요.")
    else:
        st.success("- [근력 양호]: 현재 학년 기준을 충족합니다. 상체 근력과 신체 지지 능력이 안정적입니다.")
           



