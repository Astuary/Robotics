import numpy as np
import matplotlib.pyplot as plt
import math

K = 16
m = 0.05
l = 0.04

I = m*l*l
#B = 2*math.sqrt(K*I)
#B = 0.2
B_arr = [0.005, 0.035, 2*math.sqrt(K*I), 0.150, 0.2]
theta = np.zeros((5, 100))
count = 0

for B in B_arr:
    zeta = B/(2*math.sqrt(K*I))
    #zeta = 0.5
    print(zeta)
    omega = math.sqrt(K/I)
    print(omega)

    a = 1
    b = 2*zeta*omega
    c = omega*omega

    discriminant = (b * b) - (4 * a * c)

    if(discriminant > 0):
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Two Distinct Real Roots Exists: root1 = %.2f and root2 = %.2f" %(root1, root2))
        print(count)

        for i in range(100):
            t = i/1000
            theta[count][i] = - (math.pi/2)*(root2/(root2 - root1))*(math.e**(root1*t)) - (math.pi/2)*(root1/(root1 - root2))*(math.e**(root2*t))
            #theta[count][i] = -(math.pi*root2*math.e**(root1*t))/(2*(root2-root1))-(math.pi*root1*math.e**(root2*t))/(2*(root1-root2))

    elif(discriminant == 0):
        root1 = root2 = -b / (2 * a)
        print("Two Equal and Real Roots Exists: root1 = %.2f and root2 = %.2f" %(root1, root2))
        print(count)

        for i in range(100):
            t = i/1000
            theta[count][i] = (- (math.pi/2) - (math.pi/2)*omega*t)*(math.e**(-omega*t))

    elif(discriminant < 0):
        root1 = -b / (2 * a)
        imaginary = math.sqrt(-discriminant) / (2 * a)
        print("Two Distinct Complex Roots Exists: root1 = %.2f+%.2f and root2 = %.2f-%.2f" %(root1, imaginary, root1, imaginary))
        print(count)

        for i in range(100):
            t = i/1000
            theta[count][i] = (math.pi/2)*(math.e**(t*root1))*(root1*math.sin(imaginary*t)/imaginary - math.cos(imaginary*t))

    count = count + 1

print(theta)
fig1 = plt.gcf()
plt.plot(range(100), theta[0], 'r--', label='0.005')
plt.plot(range(100), theta[1], 'mo', label='0.040')
plt.plot(range(100), theta[2], 'g-.', label=round(2*math.sqrt(K*I), 3))
plt.plot(range(100), theta[3], 'c.', label='0.150')
plt.plot(range(100), theta[4], 'b:', label='0.200')
plt.xlabel(r'Time $t\; [ms]$', fontsize=22)
plt.ylabel(r'Error $\theta - \theta_{ref}$ $[rad]$', fontsize=22)
#plt.yticks(np.arange(0, max(power_output)+10, 5))
plt.title(r'Error vs. Time for a $\pi/2$ rotation (eye): $K = 16.0 [Nm]$', fontsize=22)
plt.legend(title=r'Values of $B$ in $[kg\cdot m^2/s]$', fontsize='xx-large')
mng = plt.get_current_fig_manager()
mng.window.showMaximized()
plt.grid()
plt.show()
fig1.savefig('eye_2.png')
