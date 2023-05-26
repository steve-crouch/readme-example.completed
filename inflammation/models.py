"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains
inflammation data for a single patient taken over a number of days
and each column represents a single day across all patients.
"""

from functools import reduce
import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array for each day.

    :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days).
    :returns: An array of mean values of measurements for each day.
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily maximum of a 2D inflammation data array for each day.

    :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days).
    :returns: An array of max values of measurements for each day.
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily minimum of a 2D inflammation data array for each day.

    :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days).
    :returns: An array of minimum values of measurements for each day.
    """
    return np.min(data, axis=0)


def daily_stddev(data):
    """Calculate the standard deviation of a 2D inflammation data array for each day.

    :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days).
    :returns: An array of standard deviation values of measurements for each day.
    """
    return np.std(data, axis=0)


def daily_median(data):
    """Calculate the daily median of a 2D inflammation data array for each day.

    :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days).
    :returns: An array of median values of measurements for each day.
    """
    return np.median(data, axis=0)


def patient_normalise(data):
    """
    Normalise patient data between 0 and 1 of a 2D inflammation data array.

    Any NaN values are ignored, and normalised to 0

    :param data: 2D array of inflammation data
    :type data: ndarray

    """
    if not isinstance(data, np.ndarray):
        raise TypeError('data input should be ndarray')
    if len(data.shape) != 2:
        raise ValueError('inflammation array should be 2-dimensional')
    if np.any(data < 0):
        raise ValueError('inflammation values should be non-negative')
    max_data = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max_data[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    return normalised


def daily_above_threshold(patient_num, data, threshold):
    """Count how many days a given patient's inflammation exceeds a given threshold.

    :param patient_num: The patient row number
    :param data: A 2D data array with inflammation data
    :param threshold: An inflammation threshold to check each daily value against
    :returns: An integer representing the number of days a patient's inflammation is over a given threshold
    """

    above_threshold = map(lambda x: x > 5, data[patient_num])
    return reduce(lambda a, b: a + 1 if b else a, above_threshold, 0)


def daily_above_threshold2(patient_num, data, threshold):
    """Count how many days a given patient's inflammation exceeds a given threshold.

    :param patient_num: The patient row number
    :param data: A 2D data array with inflammation data
    :param threshold: An inflammation threshold to check each daily value against
    :returns: An integer representing the number of days a patient's inflammation is over a given threshold
    """
    def count_above_threshold(a, b):
        if b:
            return a + 1
        else:
            return a

    above_threshold = map(lambda x: x > 5, data[patient_num])
    return reduce(count_above_threshold, above_threshold, 0)
