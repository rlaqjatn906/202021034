import streamlit as st
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import control

st.title("202021034 김범수 제어공학")
st.header("기말고사")

# 전달함수 정의
num = [100]
den = [1, 5, 6]
sys_tf = control.TransferFunction(num, den)

# 폐루프 전달함수 계산
feedback_tf = control.feedback(sys_tf)

# 폐루프 전달함수 출력
st.subheader("폐루프 전달함수")
st.text(feedback_tf)

# unit step 입력에 대한 응답곡선 계산
t, y = control.step_response(feedback_tf)

# 응답곡선 그리기
fig1 = plt.figure()
plt.plot(t, y)
plt.title('Step Response')
plt.xlabel('Time [s]')
plt.ylabel('Output')
plt.grid(True)

# 주파수 응답 계산
w, mag, phase = control.bode(feedback_tf)

# 보드선도 그리기
fig2 = plt.figure()
plt.semilogx(w, mag)
plt.title('Bode Plot')
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Magnitude [dB]')
plt.grid(True)

# 그래프를 Streamlit 애플리케이션에 표시
st.pyplot(fig1)
st.pyplot(fig2)
