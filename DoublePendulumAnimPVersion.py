import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import time

# set up initial state and global variables
pendulum = DPend.DoublePendulum([180., 0.0, -20., 0.0])
dt = 1./60 # 60 fps

#------------------------------------------------------------
# set up figure and animation
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(-2, 2), ylim=(-2, 2))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
timeText = ax.text(0.02, 0.95, '', transform=ax.transAxes)
energyText = ax.text(0.02, 0.90, '', transform=ax.transAxes)

def init():
    '''initialize animation'''
    line.set_data([], [])
    timeText.set_text('')
    energyText.set_text('')
    return line, timeText, energyText

def animate(i):
    '''perform animation step'''
    global pendulum, dt
    pendulum.Step(dt)
    
    line.set_data(*pendulum.Position())
    timeText.set_text('Time = {:.1f}'.format(pendulum.timeElapsed))
    energyText.set_text('Energy = {:.3f} J'.format(pendulum.Energy()))
    return line, timeText, energyText

# choose the interval based on dt and the time to animate one step
t0 = time.time()
animate(0)
t1 = time.time()
interval = 1000 * dt - (t1 - t0)

ani = animation.FuncAnimation(fig, animate, frames=300,
                              interval=interval, blit=True, init_func=init)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#ani.save('double_pendulum.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
