#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from statistics import median

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


class FraudDetector:
    """Detects potential fraudulant transactions through aggregation

    Previous trailing days double medians are indicators of fraud and are used
    to count warning messages."""

    def __init__(self):
        pass

    def detector(self, trailing_days, expenditure: list) -> int:
        """Calculates number of fraud warnings based on historical expense data

        Trailing days and expense items are given as inputs, used to calculate
        twice mean anomalies and return the number of times these anomalies are detected.
        Algorithm runs with n^2*log(n) complexity

        :param trailing_days: number of data collection days before calculation initailised
        :param expenditure: daily expense transactions
        :return: number of fraud warnings per user
        """
        # enforce problem constraints
        self.check_constraints(trailing_days, expenditure)

        messages = 0
        current_day = 0
        lower_range = 0

        while current_day < len(expenditure):

            # increase lower range only when calculation day reached
            if current_day > trailing_days:
                lower_range += 1

            # median calculation range shifts with iterations
            trailing_expenses = expenditure[lower_range:current_day]

            # calculate median only when enough data is available
            if len(trailing_expenses) == trailing_days:
                middle_val = median(trailing_expenses)

                if expenditure[current_day] >= 2 * middle_val:
                    messages += 1  # increase message count when anomaly experienced

            current_day += 1

            # test progress time counter
            if current_day % 10000 == 0:
                print('Processing, currently at day {}'.format(current_day))

            # problem constraint for max trailing days
            if current_day > 100000:
                return messages

        return messages

    @staticmethod
    def check_constraints(trailing_days, expenditure: list) -> None:
        """Checks for boundary constraints

        :param trailing_days: number of data collection days before calculation initailised
        :param expenditure: daily expense transactions
        """
        if trailing_days < 1 or trailing_days > 10**5 or trailing_days > len(expenditure)\
                or expenditure is []:
            raise ValueError('Constraints out of bounds.')

        for purchase in expenditure:
            if purchase > 200:
                raise ValueError('Constraints out of bounds.')
