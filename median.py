"""
Created on Feb 26, 2016

@author: michael.f.koegel
"""


def median(values):
    """
    :param values: 
    :return: 
    """
    values = sorted(values)
    length = len(values)
    index = ((length - 1) // 2)
    
    if length % 2 == 0:
        return values[index]
    else:
        return (values[index] + values[index + 1]) / 2.0

median([2, 7, 1, 4, 9, 3])
