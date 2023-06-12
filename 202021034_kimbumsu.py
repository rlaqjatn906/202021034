import streamlit as st
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import control

st.markdown("<h1 style='color: red; font-size: 30px;'>202021034 김범수 제어공학</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: blue;'>기말고사</h2>", unsafe_allow_html=True)
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
st.subheader("응답곡선")
st.pyplot(fig1)

# 주파수 응답 계산
w, mag, phase = control.bode(feedback_tf)

# 보드선도 그리기 (이득)
fig2 = plt.figure()
plt.semilogx(w, mag)
plt.title('Bode Plot (Magnitude)')
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Magnitude [dB]')
plt.grid(True)
st.subheader("보드선도 (이득)")
st.pyplot(fig2)

# 보드선도 그리기 (위상)
fig3 = plt.figure()
plt.semilogx(w, phase)
plt.title('Bode Plot (Phase)')
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Phase [degrees]')
plt.grid(True)
st.subheader("보드선도 (위상)")
st.pyplot(fig3)
