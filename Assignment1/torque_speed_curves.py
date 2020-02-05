import numpy as np
import matplotlib.pyplot as plt

no_load_speed = 122.2
no_load_current = 0.12
stall_torque = 2.7
torque_constant = 0.163
V_in = 24

slope = no_load_speed/stall_torque
stall_current = no_load_current + (stall_torque/torque_constant)

load = np.zeros(101)
motor_current = np.zeros(101)
motor_speed = np.zeros(101)
power_output = np.zeros(101)
efficiency = np.zeros(101)

for i in range(101):
    load[i] = stall_torque*i/100

    motor_current[i] = no_load_current + (load[i]/torque_constant)

    power_input = V_in * motor_current[i]

    motor_speed[i] = no_load_speed - slope*load[i]

    power_output[i] = load[i]*motor_speed[i]

    efficiency[i] = power_output[i]/power_input

fig1 = plt.gcf()
plt.plot(load, motor_current, color="#0095B6", label='Current')
plt.xlabel(r'Motor Load Torque $\tau [N\cdot m]$', fontsize=22)
plt.ylabel(r'Motor Current $[A]$', fontsize=22)
plt.xticks(np.arange(0,stall_torque+0.1, 0.1))
plt.yticks(np.arange(0, max(motor_current)+0.5, 0.5))
plt.title('Current as a function of Motor Torque', fontsize=22)
mng = plt.get_current_fig_manager()
mng.window.showMaximized()
plt.grid()
plt.show()
fig1.savefig('current.png')

fig2 = plt.gcf()
plt.plot(load, motor_speed, color="#F47789", label='Speed')
plt.xlabel(r'Motor Load Torque $\tau [N\cdot m]$', fontsize=22)
plt.ylabel(r'Motor Speed $[rad/sec]$', fontsize=22)
plt.xticks(np.arange(0,stall_torque+0.1, 0.1))
plt.yticks(np.arange(0, motor_speed[0]+10, 5))
plt.title('Speed as a function of Motor Torque', fontsize=22)
mng = plt.get_current_fig_manager()
mng.window.showMaximized()
plt.grid()
plt.show()
fig2.savefig('speed.png')

fig3 = plt.gcf()
plt.plot(load, efficiency, color="#ED4F46", label='Efficiency')
plt.xlabel(r'Motor Load Torque $\tau [N\cdot m]$', fontsize=22)
plt.ylabel(r'Efficiency', fontsize=22)
plt.xticks(np.arange(0,stall_torque+0.1, 0.1))
plt.yticks(np.arange(0, max(efficiency)+0.1, 0.05))
plt.title('Efficiency as a function of Motor Torque', fontsize=22)
mng = plt.get_current_fig_manager()
mng.window.showMaximized()
plt.grid()
plt.show()
fig3.savefig('efficiency.png')

fig4 = plt.gcf()
plt.plot(load, power_output, color="#F38D29", label='Power')
plt.xlabel(r'Motor Load Torque $\tau [N\cdot m]$', fontsize=22)
plt.ylabel(r'Output Power $[W]$', fontsize=22)
plt.xticks(np.arange(0,stall_torque+0.1, 0.1))
plt.yticks(np.arange(0, max(power_output)+10, 5))
plt.title('Output Power as a function of Motor Torque', fontsize=22)
mng = plt.get_current_fig_manager()
mng.window.showMaximized()
plt.grid()
plt.show()
fig4.savefig('power.png')
