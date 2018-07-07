import matplotlib.pyplot as plt
import numpy as np

from math import sqrt


def latexify(fig_width=None, fig_height=None, columns=1):
    """Set up matplotlib's RC params for LaTeX plotting.
    Call this before plotting a figure.

    Parameters
    ----------
    fig_width : float, optional, inches
    fig_height : float,  optional, inches
    columns : {1, 2}
    """

    # code adapted from http://www.scipy.org/Cookbook/Matplotlib/LaTeX_Examples

    # Width and max height in inches for IEEE journals taken from
    # computer.org/cms/Computer.org/Journal%20templates/transactions_art_guide.pdf

    assert(columns in [1, 2])

    if fig_width is None:
        fig_width = 3.39 if columns == 1 else 6.9  # Width in inches

    if fig_height is None:
        golden_mean = (sqrt(5)-1.0)/2.0     # Aesthetic ratio
        fig_height = fig_width*golden_mean  # height in inches

    MAX_HEIGHT_INCHES = 8.0
    if fig_height > MAX_HEIGHT_INCHES:
        print("WARNING: fig_height too large:" + fig_height +
              "so will reduce to" + MAX_HEIGHT_INCHES + "inches.")
        fig_height = MAX_HEIGHT_INCHES

    params = {'backend': 'ps',
              'text.latex.preamble': [r'\usepackage{gensymb}',
                                      r'\usepackage{eurosym}'],
              'axes.labelsize': 8,   # fontsize for x and y labels (was 10)
              'axes.titlesize': 8,
              'font.size': 8,        # was 10
              'legend.fontsize': 8,  # was 10
              'xtick.labelsize': 8,
              'ytick.labelsize': 8,
              'text.usetex': True,
              'figure.figsize': [fig_width, fig_height],
              'font.family': 'serif'
              }

    return params


def format_axes(ax, right=False):

    SPINE_COLOR = 'gray'

    side = 'left' if right else 'right'
    for spine in ['top', side]:
        ax.spines[spine].set_visible(False)

    side = 'right' if right else 'left'
    for spine in [side, 'bottom']:
        ax.spines[spine].set_color(SPINE_COLOR)
        ax.spines[spine].set_linewidth(0.5)

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position(side)

    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_tick_params(direction='out', color=SPINE_COLOR)

    return ax


def paper_mode(fig, ax, rcParams, right_ax=None, fig_width=None,
               fig_height=None, columns=1, path=None):
    """Enable paper mode for figures.

    Call this to generate a paper sized figure. It can be saved directly to the
    folder of the paper ('path' argument) for direct integration.
    """

    params = latexify(fig_width, fig_height, columns)
    rcParams.update(params)
    fig.tight_layout()
    format_axes(ax)
    # Optional right axis
    if right_ax is not None:
        format_axes(right_ax, right=True)
    # Specify path to figure in latex folder for automatic integration
    if path is not None:
        fig.savefig(path)


def ccdf(data, xlabel='', title='', scalemax=14, histogram=False):
    print('{:<8} {:>7.2f}'.format('Min:', np.min(data)))
    print('{:<8} {:>7.2f}'.format('Max:', np.max(data)))
    print('{:<8} {:>7.2f}'.format('Mean:', np.mean(data)))
    print('{:<8} {:>7.2f}'.format('Median:', np.median(data)))
    print('{:<8} {:>7.2f}'.format('Std:', np.std(data)))

    # CCDF
    plt.hist(data,
             bins=np.logspace(0, scalemax, 50, base=2),
             cumulative=-1,
             normed=True,
             log=True,
             histtype="step")
    plt.gca().set_xscale("log")
    plt.xlabel(xlabel)
    plt.title(title)
    plt.grid()
    plt.show()

    if histogram:
        plt.hist(data, log=True, bins=100)
        plt.show()
