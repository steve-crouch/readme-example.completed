#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""

import os
import argparse

from inflammation import models, views


def main(args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    in_files = args.infiles
    if not isinstance(in_files, list):
        in_files = [args.infiles]

    for filename in in_files:
        inflammation_data = models.load_csv(filename)

        view_data = {
            'average': models.daily_mean(inflammation_data),
            'max': models.daily_max(inflammation_data),
            'min': models.daily_min(inflammation_data),
            'stddev': models.daily_stddev(inflammation_data)
        }

        # Create output filepath from input filepath
        inputfilebase = os.path.basename(filename)
        inputfilename = os.path.splitext(inputfilebase)[0]
        outputfile = os.path.join(args.outputdir, inputfilename + '.png')

        views.generate_plot(view_data, outputfile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic patient inflammation plot generator')

    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing inflammation series for each patient')

    parser.add_argument(
        '--outputdir',
        required=True,
        help='Directory to put output plot images')

    args = parser.parse_args()

    main(args)
