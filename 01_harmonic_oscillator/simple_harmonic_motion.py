# - *- coding utf- 8 - *-

import math
import matplotlib.pyplot as plt
from matplotlib import animation

"""
w**2 = k/m
X(t) = x0*cos(wt) + (v0/w)*sin(wt)
V(t) = v0*cos(wt) - x0*w*sin(wt)
"""

x0 = 1
v0 = 0
k = 1
m = 1
w = k / m
frame_rate = 30

fig, ax = plt.subplots()


def animate(i):
    ax.clear()

    plt.xlim(-2.0, 2.0)
    plt.ylim(-2.0, 2.0)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    t = i/frame_rate
    x = x0*math.cos(w * t) + (v0/w)*math.sin(w * t)
    v = v0*math.cos(w * t) - x0*w*math.sin(w * t)
    # centre = x, 0.0
    bottom_left = (x-0.5/2, -0.5/2)

    plt.text(x, 0.5, 'v:{0}\n x:{1}'.format(v, x),
             fontdict={'size': 10, 'color': 'b'})

    rect = plt.Rectangle(bottom_left, 0.5, 0.5)
    return ax.add_patch(rect)


ani = animation.FuncAnimation(fig=fig, func=animate, interval=1000/frame_rate, blit=False)

plt.show()
