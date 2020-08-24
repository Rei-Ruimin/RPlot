import os
import shutil

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import FuncFormatter


def plot_and_save_scatter(data_file, timeparam_file, save_dir,
                          utime, uaxis, ptitle,
                          data_ver, save_v, save_i):
    # create folders
    os.chdir(save_dir)

    os.makedirs('Output')
    os.chdir("Output")

    os.makedirs('original data')
    os.chdir("original data")
    shutil.copy(data_file, os.getcwd())
    shutil.copy(timeparam_file, os.getcwd())
    os.chdir("..")

    # read data
    df = pd.read_csv(data_file, delim_whitespace=True, engine='python')
    if not data_ver:
        df = df.T

    cols = pd.read_csv(timeparam_file, delim_whitespace=True, engine='python')
    df.columns = ['X', 'Y'] + list(cols)
    zVals = df.iloc[:, 2:]

    # plot
    fig, ax = plt.subplots()
    plt.xlabel('x axis ({})'.format(uaxis))
    plt.ylabel('y axis ({})'.format(uaxis))
    plt.ticklabel_format(style='sci', scilimits=(0, 0))

    im = plt.scatter(df['X'], df['Y'], c=df[zVals.columns[0]], cmap='jet', marker=',')
    plt.xlim(df['X'].min(), df['X'].max())
    plt.ylim(df['Y'].min(), df['Y'].max())
    plt.clim(zVals.to_numpy().min(), zVals.to_numpy().max())

    def fmt(x, pos):
        a, b = '{:.2e}'.format(x).split('e')
        b = int(b)
        return r'${} * 10^{{{}}}$'.format(a, b)

    cb = plt.colorbar(im, format=FuncFormatter(fmt))
    f_title = '{}\n t = {}{}'.format(ptitle, zVals.columns[0], utime)
    tx = ax.set_title(f_title)

    # animate
    def animate(i):
        im.set_array(zVals.iloc[:, i])
        tx.set_text('{}\n t = {}{}'.format(ptitle, zVals.columns[i], utime))
        if save_i:
            plt.savefig('figure{}.png'.format(i), bbox_inches='tight')

    ani = FuncAnimation(fig, animate, frames=len(zVals.columns), interval=100)
    # save figures and video
    os.makedirs('figures')
    os.chdir("figures")
    if save_v:
        ani.save('animation.mp4')

    os.chdir(save_dir)


if __name__ == '__main__':
    plot_and_save_scatter("C:/Users/11602/Desktop/JupyterLab/sample_data/Displacement_V.txt",
                          "C:/Users/11602/Desktop/JupyterLab/sample_data/cols_V.txt",
                          "C:/Users/11602/Desktop/PyQt5-GUI",
                          "S", "M", "TESTTT!", True, True, True)
