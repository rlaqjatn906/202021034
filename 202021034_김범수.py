import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import control

# 전달함수 정의
num = [100]
den = [1, 5, 6]
sys_tf = control.TransferFunction(num, den)

# 폐루프 전달함수 계산
feedback_tf = control.feedback(sys_tf)

# unit step 입력에 대한 응답곡선 계산
t, y = control.step_response(feedback_tf)

# 응답곡선 그리기
plt.figure()
plt.plot(t, y)
plt.title('Step Response')
plt.xlabel('Time [s]')
plt.ylabel('Output')
plt.grid(True)
plt.show()

# 주파수 응답 계산
w, mag, phase = control.bode(feedback_tf)

# 보드선도 그리기
plt.figure()
plt.semilogx(w, mag)
plt.title('Bode Plot')
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Magnitude [dB]')
plt.grid(True)
plt.show()