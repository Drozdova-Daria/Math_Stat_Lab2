from enum import Enum


class Distribution(Enum):
    NORMAL = 1
    CAUCHY = 2
    LAPLACE = 3
    POISSON = 4
    UNIFORM = 5

    @staticmethod
    def in_str(distribution):
        if distribution == Distribution.NORMAL:
            return 'Normal'
        elif distribution == Distribution.CAUCHY:
            return 'Cauchy'
        elif distribution == Distribution.LAPLACE:
            return 'Laplace'
        elif distribution == Distribution.POISSON:
            return 'Poisson'
        elif distribution == Distribution.UNIFORM:
            return 'Uniform'
        else:
            return ''