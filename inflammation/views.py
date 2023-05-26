"""Module containing code for plotting inflammation data."""

import os

from matplotlib import pyplot as plt


def generate_plot(data_dict, outputfile):
    """Display and save plots of basic statistical properties of the inflammation data.

    :param data_dict: Dictionary of name -> data to plot
    """

    num_plots = len(data_dict)
    fig = plt.figure(figsize=((3 * num_plots) + 1, 3.0))

    for i, (name, data) in enumerate(data_dict.items()):
        axes = fig.add_subplot(1, num_plots, i + 1)

        axes.set_ylabel(name)
        axes.set_xlabel('Days')
        axes.plot(data)

    fig.tight_layout()

    fig.savefig(outputfile)
