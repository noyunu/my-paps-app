import streamlit as st

st.title("🏃‍♂️ 고1 성별 맞춤형 PAPS 평가 프로그램")
st.markdown("성별과 기록을 입력하면 고1 공인 기준에 맞춘 운동 처방 리포트가 생성됩니다.")

student_name = st.text_input("학생 이름을 입력하세요:", "홍길동")
gender = st.selectbox("성별을 선택하세요:", ["남학생", "여학생"])

st.subheader("📋 PAPS 측정 기록 입력")

shuttle_run = st.number_input("1. 왕복오래달리기 (회) 입력:", min_value=0, value=40)
long_jump = st.number_input("2. 제자리멀리뛰기 (cm) 입력:", min_value=0, value=180)
sit_and_reach = st.number_input("3. 유연성: 앉아윗몸앞으로굽히기 (cm) 입력:", value=10.0)
grip_strength = st.number_input("4. 악력 (kg) 입력:", min_value=0.0, value=30.0)

if st.button("📊 PAPS 분석 및 운동 처방 리포트 보기"):
    st.markdown(f"### 📑 {student_name} 학생({gender})의 분석 결과")
    
    if gender == "남학생":
        if shuttle_run < 40: st.error("- [심폐지구력 경고]: 현재 심폐지구력이 매우 취약합니다. 주 3회 30분 이상 조깅을 추천합니다.")
        elif shuttle_run < 62: st.warning("- [심폐지구력 보통]: 보통 수준입니다. 페이스 조절을 연습하여 기록을 더 보완하세요.")
        else: st.success("- [심폐지구력 우수]: 최상위권입니다! 우수한 유산소 능력을 유지하세요.")

        if long_jump < 186: st.error("- [순발력 경고]: 순발력이 다소 부족합니다. 스쿼트 점프 등으로 하체 폭발력을 기르세요.")
        elif long_jump < 225: st.warning("- [순발력 보통]: 평균적인 수준입니다. 도약 시 상체 반동을 적극적으로 활용해 보세요.")
        else: st.success("- [순발력 우수]: 순발력이 아주 뛰어납니다. 하체의 순간적인 힘 발휘 능력이 좋습니다.")

        if sit_and_reach < 3.0: st.error("- [유연성 경고]: 가동 범위가 매우 좁아 부상 위험이 있습니다. 매일 스트레칭을 하세요.")
        elif sit_and_reach < 13.0: st.warning("- [유연성 보통]: 보통 수준입니다. 운동 전후로 고관절 and 햄스트링 스트레칭을 해주세요.")
        else: st.success("- [유연성 우수]: 유연성이 매우 뛰어납니다. 관절 상태를 잘 유지하고 있습니다.")

        if grip_strength < 30.0: st.error("- [근력 경고]: 악력이 약합니다. 철봉 매달리기나 악력기를 이용해 힘을 기르세요.")
        elif grip_strength < 42.0: st.warning("- [근력 보통]: 평범한 근력입니다. 푸시업이나 플랭크를 병행하여 보완하면 좋습니다.")
        else: st.success("- [근력 우수]: 상체 근력이 매우 우수합니다. 신체 지지 능력이 안정적입니다.")

    elif gender == "여학생":
        if shuttle_run < 24: st.error("- [심폐지구력 경고]: 현재 심폐지구력이 매우 취약합니다. 주 3회 빠른 걷기나 가벼운 조깅을 추천합니다.")
        elif shuttle_run < 41: st.warning("- [심폐지구력 보통]: 보통 수준입니다. 주당 달리는 거리를 조금씩 늘려보세요.")
        else: st.success("- [심폐지구력 우수]: 최상위권입니다! 우수한 유산소 능력을 유지하세요.")

        if long_jump < 131: st.error("- [순발력 경고]: 순발력이 부족합니다. 제자리 높이뛰기나 줄넘기 등으로 하체 힘을 기르세요.")
        elif long_jump < 166: st.warning("- [순발력 보통]: 평균 수준입니다. 점프 시 무릎을 가슴 쪽으로 당기는 연습을 해보세요.")
        else: st.success("- [순발력 우수]: 순발력이 아주 뛰어납니다. 순간적인 힘을 잘 활용합니다.")

        if sit_and_reach < 6.0: st.error("- [유연성 경고]: 몸이 다소 뻣뻣하여 부상 위험이 있습니다. 샤워 후 10분씩 스트레칭을 하세요.")
        elif sit_and_reach < 17.5: st.warning("- [유연성 보통]: 보통 수준입니다. 다리를 뻗고 상체를 숙이는 동작을 자주 연습하세요.")
        else: st.success("- [유연성 우수]: 유연성이 매우 뛰어납니다. 훌륭한 관절 가동 범위를 가졌습니다.")

        if grip_strength < 18.0: st.error("- [근력 경고]: 악력 및 상체 근력이 약합니다. 아령 운동이나 가벼운 밴드 운동을 추천합니다.")
        elif grip_strength < 26.5: report = st.warning("- [근력 보통]: 평범한 수준입니다. 무릎을 대고 하는 푸시업 등으로 상체 힘을 기르세요.")
        else: st.success("- [근력 우수]: 상체 근력이 매우 우수합니다. 신체 지지 능력이 안정적입니다.")



