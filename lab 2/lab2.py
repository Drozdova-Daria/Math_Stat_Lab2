import numpy as np
from scipy.stats import cauchy, laplace, poisson, uniform
from distribution import Distribution
from characteristics import Characteristics
import csv
import math


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
    return sum(sel) / len(sel)


def sample_median(sel, size):
    return np.median(sel)


def half_sum_extreme_sample_elements(sel, size):
    return (sorted(sel)[0] + sorted(sel)[size - 1]) / 2


def sample_guartile(sel, size, order):
    if size * order == round(size * order):
        return sel[int(size * order) - 1]
    else:
        return sel[int(round(size * order))]


def half_sum_quartiles(sel, size):
    return (sample_guartile(sorted(sel), size, 0.25) + sample_guartile(sorted(sel), size, 0.75)) / 2


def truncated_average(sel: list, size):
    r = round(size / 4)
    sel_sum = sum(sorted(sel)[r: (size - r - 1):])
    return sel_sum / (size - 2 * r)


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
    values_list = []
    for _ in range(count):
        sel = selection(a, b, size, distribution)
        values_list.append(values_of_characteristic[characteristic](sel, size))
    return sample_average(values_list, count), abs(sample_average([v*v for v in values_list], count) - sample_average(values_list, count) ** 2)


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
                e = str(round(value_one, 5))
                d = str(round(value_two, 5))
                e_m_s_d = str(round((value_one - math.sqrt(math.fabs(value_two))), 5))
                e_p_s_d = str(round((value_one + math.sqrt(math.fabs(value_two))), 5))
                file_writer.writerow((Characteristics.in_str(characteristic), e, d, e_m_s_d, e_p_s_d))

