"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np
import json

class Patient:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def get_body_mass_index(self):
        """ Compute body mass index: weight_in_kg / height_in_meters**2 """

        return self.weight / self.height ** 2

def load_json(filename):
    """Load a numpy array from a JSON document.
    
    Expected format:
    [
      {
        "observations": [0, 1]
      },
      {
        "observations": [0, 2]
      }    
    ]
    :param filename: Filename of CSV to load
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data_as_json = json.load(file)
        return [np.array(entry['observations']) for entry in data_as_json]

def load_csv(filename):  
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data:np.array) -> np.array:
    """Calculate the daily mean of a 2d inflammation data array.

    :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days)
    :return: mean of data per column
    """    
    return np.mean(data, axis=0)


def daily_max(data:np.array) -> np.array:
    """Calculate the daily max of a 2d inflammation data array.

    :param data: 2d inflammation data array
    :return: max of data per column
    """   
    return np.max(data, axis=0)


def daily_min(data:np.array) -> np.array:
    """Calculate the daily min of a 2d inflammation data array.

    :param data: 2d inflammation data array
    :return: min of data per column
    """    
    return np.min(data, axis=0)

