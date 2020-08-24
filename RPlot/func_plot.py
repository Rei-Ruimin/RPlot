import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
from mpl_toolkits.axes_grid1 import make_axes_locatable


def plot_and_save_func(func_str, x1_i, x2_i, y1_i, y2_i, t1_i, t2_i, tnum, save_dir):

    '''
    def add_np(text):
        for ch in ['sin', 'sinh', 'arcsin',
                   'cos', 'cosh', 'arccos',
                   'tan', 'tanh', 'arctan']:
            if ch in text:
                text = text.replace(ch, 'np.' + ch)
        return text

    mathfunc = add_np(func_str)
    '''

    f = lambda x, y, t: eval(func_str)

    fig, ax = plt.subplots(figsize=(5, 5))
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.ticklabel_format(style='scientific', axis='both', scilimits=(0, 0))
    # I like to position my colorbars this way, but you don't have to
    div = make_axes_locatable(ax)
    cax = div.append_axes('right', '5%', '5%')
    Xmin = eval(x1_i)
    Xmax = eval(x2_i)
    Ymin = eval(y1_i)
    Ymax = eval(y2_i)
    Tmin = eval(t1_i)
    Tmax = eval(t2_i)
    Tnum = eval(tnum)

    x = np.linspace(Xmin, Xmax, 500)
    y = np.linspace(Ymin, Ymax, 500)
    X, Y = np.meshgrid(x, y)
    t_list = np.linspace(Tmin, Tmax, Tnum)

    # This is now a list of arrays rather than a list of artists
    frames = []
    for t in t_list:
        curVals = f(X, Y, t)
        frames.append(curVals)

    cv0 = frames[0]
    im = ax.imshow(cv0, origin='lower', cmap="GnBu", extent=[x.min(), x.max(), y.min(), y.max()],
                   aspect="auto")  # Here make an AxesImage rather than contour
    cb = fig.colorbar(im, cax=cax)
    cb.set_label("value of z")
    tx = ax.set_title('Time = 0')

    def fmt(x):
        a, b = '{:.2e}'.format(x).split('e')
        b = int(b)
        return r'${} * 10^{{{}}}$'.format(a, b)

    def animate(i):
        arr = frames[i]
        vmax = np.max(arr)
        vmin = np.min(arr)
        im.set_data(arr)
        im.set_clim(vmin, vmax)
        tx.set_text('Time = {}'.format(fmt(t_list[i])))
        # In this version you don't have to do anything to the color bar,
        # it updates itself when the mappable it watches (im) changes

    ani = animation.FuncAnimation(fig, animate, frames=Tnum, interval=500)

    # create folders
    os.chdir(save_dir)
    os.makedirs('Output')
    os.chdir("Output")
    ani.save('video.mp4')
    os.chdir(save_dir)


if __name__ == '__main__':
    plot_and_save_func("2*np.sin(800*(x+y-5000*t)) + 3*np.cos(1000*(x+2*y-4000*t))", "-0.01", "0.01", "0", "0.03", "0", "1/250000", "10", "C:/Users/11602/Desktop/PyQt5-GUI")