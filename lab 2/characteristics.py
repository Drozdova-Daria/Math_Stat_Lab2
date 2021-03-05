from enum import Enum


class Characteristics(Enum):
    SAMPLE_AVERAGE = 1
    SAMPLE_MEDIAN = 2
    HALF_SUM_EXTREME_SAMPLE_ELEMENTS = 3
    HALF_SUM_GUARTILES = 4
    TRUNCATED_AVERAGE = 5
    SAMPLE_VARIANCE = 6

    @staticmethod
    def in_str(characteristic):
        if characteristic == Characteristics.SAMPLE_AVERAGE:
            return 'Sample average'
        elif characteristic == Characteristics.SAMPLE_MEDIAN:
            return 'Sample median'
        elif characteristic == Characteristics.HALF_SUM_EXTREME_SAMPLE_ELEMENTS:
            return 'Half-sum extreme sample elements'
        elif characteristic == Characteristics.HALF_SUM_GUARTILES:
            return 'Half-sum guartiles'
        elif characteristic == Characteristics.TRUNCATED_AVERAGE:
            return 'Truncated average'
        elif characteristic == Characteristics.SAMPLE_VARIANCE:
            return 'Sample variance'
        else:
            return ''

