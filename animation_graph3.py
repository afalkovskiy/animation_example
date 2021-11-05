#Example of snow animation: AF, Nov 2021

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib.image as mpimg

plt.style.use('dark_background')

def check_bounds(xy, xmin, xmax, ymin, ymax):
    m = xy.shape[0]
    n = xy.shape[1]

    for i in range(m):

        if xy[i][0] < xmin:
            xy[i][0] = xmax
        if xy[i][0] > xmax:
            xy[i][0] = xmin

        if xy[i][1] < ymin:
            xy[i][1] = ymax
        if xy[i][1] > ymax:
            xy[i][1] = ymin
    return

# fig = plt.figure()
fig = plt.figure(figsize=(11, 7))
ax = plt.axes(xlim=(-5, 5), ylim=(0, 50))

ax = plt.gca()
plt.axis('off')
# plt.plot(x, y)
plt.xlim(-5, 5)
plt.ylim(0, 50)
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

line, = ax.plot([], [], lw=2, color='white')
fill = ax.fill_between([], 0, [], facecolor=line.get_color())

x2 = np.linspace(-5, 5, 100)
y2 = np.linspace(10, 50, 100)
scat = ax.scatter(x2, y2, s=32, lw=0.5, color='white')

xy = np.zeros((100, 2)) + 20*np.random.random_sample((100, 2))
xy[:, 0] = 2*xy[:, 0]
check_bounds(xy, -5, 5, 0, 50)

# print('xy:')
# print('xy', xy)
a1 = np.ones((100,2))
a1[:,0] = 5*a1[:,0]
a1[:,1] = 10*a1[:,1]

# print('a3:\n', a1)

text1 = ax.text(0.05, 0.6,  'My text',
                transform=ax.transAxes, color='gray', fontsize=150, family="fantasy", zorder=20)
text10 = ax.text(0.051, 0.58,  'My text',
                transform=ax.transAxes, color='navy', fontsize=152, family="fantasy", zorder=10)


text2 = ax.text(0.05, 0.2,  'My text',
                transform=ax.transAxes, color='gray', fontsize=150, family="fantasy", zorder=20)
text20 = ax.text(0.051, 0.18,  'My text',
                transform=ax.transAxes, color='navy', fontsize=152, family="fantasy", zorder=10)


# initialization function
def init():
    # creating an empty plot/frame
    line.set_data([], [])

    print('init: xy:')
    print('init: xy', xy)

    return line,

# lists to store x and y axis points
xdata, ydata = [], []

# animation function
def animate(i):
    global xy


    xdata = np.linspace(-2*np.pi, 2*np.pi, 100)
    ydata = 1*np.sin(xdata) + 2 + 0.5*np.sin(2*(xdata + 0.1*i)) + 0.5*i

    rdata = np.random.rand(100)
    # ydata = ydata + 0.1*rdata

    line.set_data(xdata, ydata)

    fill = ax.fill_between(xdata, 0, ydata, facecolor=line.get_color())


    r_arr = 0.2*np.random.random_sample((100, 2))

    r_arr[:,0] = 0.5*r_arr[:,0]
    r_arr[:,1] = 5*r_arr[:,1]

    xy = xy - r_arr

    check_bounds(xy, -5, 5, 0, 50)


    scat.set_offsets(xy)


    if i > 71 and i < 200:
        text1.set_text('Let it ')
    else:
        text1.set_text('')

    if i > 81 and i < 200:
        text2.set_text('Snow! ')
    else:
        text2.set_text('')

    if i > 91 and i < 121:
        text10.set_text('Let it ')
        text20.set_text('Snow!')
    else:
        text10.set_text('')
        text20.set_text('')


    return line, fill, scat, text1, text2, text10, text20,

# setting a title for the plot
plt.title('Simple graph2')
# hiding the axis details
plt.axis('off')

# call the animator
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

# save the animation as mp4 video file
anim.save('snow1.gif',writer='imagemagick')
plt.show()