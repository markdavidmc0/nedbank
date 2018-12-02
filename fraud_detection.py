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

    @staticmethod
    def detector(trailing_days, expenditure: list) -> int:
        """Calculates number of fraud warnings based on historical expense data

        Trailing days and expense items are given as inputs, used to calculate
        twice mean anomolies and return the number of times these anomolies are detected

        :param trailing_days: number of data collection days before calculation initailised
        :param expenditure: daily expense transactions
        :return: number of fraud warnings per user
        """
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

        return messages


