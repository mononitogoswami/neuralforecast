# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/data_dataset__plots.ipynb (unless otherwise specified).

__all__ = ['FONTSIZE', 'COLOR_PALLETE', 'draw_plot']

# Cell
import numpy as np
import matplotlib.pyplot as plt

import pylab as plt
from pylab import rcParams
plt.style.use('seaborn-whitegrid')

from matplotlib import rcParams
plt.rcParams['font.family'] = 'serif'

FONTSIZE = 22

COLOR_PALLETE = ['#C0D6CA', '#78ACA8', '#2D6B8F', '#235796',
                 '#E7C4C0', '#E3A39A', '#CA6F6A', '#7B3841',
                 '#D5BC67', '#20425B', '#E77A5B', '#9C9DB2']

# Cell
def draw_plot(x_plot: np.ndarray, y_plot: np.ndarray, title_str: str,
                x_axis_str: str, y_axis_str: str, ax: plt.axes,
                linewidth: float= 1.5, linecolor: str= '#628793') -> None:
    """
    Draw plot for time series data.

    Parameters
    ----------
    x_plot: np.ndarray
        Points to draw on x axis.
    y_plot: np.ndarray
        Points to draw on y axis.
        (Should be same size as x_plot)
    title_str: str
        Plot title.
    x_axis_str: str
        Label for x axis of plot.
    y_axis_str: str
        Label for x axis of plot.
    ax: plt.axes
        Pyplot object for drawing plots.
        (Can be plot or subplot object)
    linewidth: float
        Line width on plot.
    linecolor: str
        Line color on plot.
    """

    ax.plot(x_plot, y_plot, color=linecolor, linewidth=linewidth)
    ax.tick_params(labelsize=FONTSIZE-2)

    ax.set_xlabel(x_axis_str, fontsize=FONTSIZE)
    ax.set_ylabel(y_axis_str, fontsize=FONTSIZE)
    ax.set_title(title_str, fontsize=FONTSIZE)

    ax.set_ylim(np.min(y_plot), np.max(y_plot))
    ax.set_xlim(np.min(x_plot), np.max(x_plot))