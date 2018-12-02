#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from fraud_detection import FraudDetector


class FraudDetectionTest(unittest.TestCase):
    """Tests anomaly cases for fraud detection on transaction spending"""

    @staticmethod
    def test_trailing_case_01() -> None:
        """Tests 5 trailing days with unique expenditure"""

        days = 5
        expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]

        run = FraudDetector()
        output = run.detector(days, expenditure)
        print(output)

    @staticmethod
    def test_trailing_case_02() -> None:
        """Tests 4 trailing days with unique expenditure"""

        days = 4
        expenditure = [1, 2, 3, 4, 4]

        run = FraudDetector()
        output = run.detector(days, expenditure)
        print(output)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
