import numpy as np
from scipy.stats import cauchy, laplace, poisson, uniform
from distribution import Distribution
from characteristics import Characteristics
import csv


def selection(mu, sigma, size, distribution):
    if distribution == Distribution.NORMAL:
        return np.random.normal(mu, sigma, size)
    elif distribution == Distribution.CAUCHY:
        return cauchy.rvs(mu, sigma, size)
    elif distribution == Distribution.LAPLACE:
        return laplace.rvs(mu, sigma, size)
    elif distribution == Distribution.POISSON:
        return poisson.rvs(mu, size=size)
    elif distribution == Distribution.UNIFORM:
        return uniform.rvs(mu, sigma, size)
    else:
        return None


def sample_average(sel: list, size):
    return sum(sel) / size


def sample_median(sel: list, size):
    sel.sort()
    if size % 2 == 0:
        return (sel[int(size / 2 - 1)] + sel[int(size / 2)]) / 2
    else:
        return sel[int((size - 1) / 2)]


def half_sum_extreme_sample_elements(sel: list, size):
    sel.sort()
    return (sel[0] + sel[size - 1]) / 2


def sample_guartile(sel: list, size, order):
    if size * order == round(size * order):
        return sel[int(size * order) - 1]
    else:
        return sel[int(round(size * order))]


def half_sum_quartiles(sel: list, size):
    sel.sort()
    return (sample_guartile(sel, size, 0.25) + sample_guartile(sel, size, 0.75)) / 2


def truncated_average(sel: list, size):
    sel.sort()
    r = round(size / 4)
    sel_sum = sum(sel[r: (size - r - 1):])
    return sel_sum / (size - 2 * r)


def sample_variance(sel: list, size):
    value_of_sample_average = sample_average(sel, size)
    value_of_sample_variance = 0
    for i in range(len(sel)):
        value_of_sample_variance = value_of_sample_variance + (sel[i] - value_of_sample_average) ** 2
    return value_of_sample_variance / size


def average_of_characteristic(a, b, size, distribution, characteristic, count):
    average_characteristic = 0
    average_characteristic_in_sqrt = 0
    values_of_characteristic = {
        Characteristics.SAMPLE_AVERAGE: sample_average,
        Characteristics.SAMPLE_MEDIAN: sample_median,
        Characteristics.HALF_SUM_EXTREME_SAMPLE_ELEMENTS: half_sum_extreme_sample_elements,
        Characteristics.HALF_SUM_GUARTILES: half_sum_quartiles,
        Characteristics.TRUNCATED_AVERAGE: truncated_average
    }
    for _ in range(count):
        sel = selection(a, b, size, distribution).tolist()
        value_of_characteristic = values_of_characteristic[characteristic](sel, size)
        average_characteristic += value_of_characteristic
        average_characteristic_in_sqrt = average_characteristic_in_sqrt + values_of_characteristic[characteristic]([s*s for s in sel], size) - value_of_characteristic ** 2
    return average_characteristic / count, average_characteristic_in_sqrt / count


size = [10, 100, 1000]
a_parameters = [0, 0, 0, 10, -np.sqrt(3)]
b_parameters = [1, 1, np.sqrt(2), 0, np.sqrt(3)]
distributions = [Distribution.NORMAL,
                 Distribution.CAUCHY,
                 Distribution.LAPLACE,
                 Distribution.POISSON,
                 Distribution.UNIFORM]
characteristics = [Characteristics.SAMPLE_AVERAGE,
                   Characteristics.SAMPLE_MEDIAN,
                   Characteristics.HALF_SUM_EXTREME_SAMPLE_ELEMENTS,
                   Characteristics.HALF_SUM_GUARTILES,
                   Characteristics.TRUNCATED_AVERAGE]


count = 1000
with open('results.csv', mode='w', encoding='utf-8') as file:
    file_writer = csv.writer(file)
    for a, b, distribution in zip(a_parameters, b_parameters, distributions):
        for n in size:
            file_writer.writerow((Distribution.in_str(distribution), str(n)))
            for characteristic in characteristics:
                value_one, value_two = average_of_characteristic(a, b, n, distribution, characteristic, count)
                file_writer.writerow((Characteristics.in_str(characteristic), str(round(value_one, 5)) , str(round(value_two, 5))))
file.close()
