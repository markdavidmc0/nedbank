#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from fraud_detection import FraudDetector


class FraudDetectionTest(unittest.TestCase):
    """Tests anomaly cases for fraud detection on transaction spending"""

    def test_trailing_case_01(self) -> None:
        """Tests 5 trailing days with unique expenditure"""

        days = 5
        expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]

        run = FraudDetector()
        output = run.detector(days, expenditure)
        self.assertEqual(output, 2)

    def test_trailing_case_02(self) -> None:
        """Tests 4 trailing days with unique expenditure"""

        days = 4
        expenditure = [1, 2, 3, 4, 4]

        run = FraudDetector()
        output = run.detector(days, expenditure)
        self.assertEqual(output, 0)

    # def test_trailing_case_03(self) -> None:
    #     """Tests 100000 trailing days with unique expenditure"""
    #
    #     days = 100000
    #     with open('P2-input1.csv', newline='') as f:
    #         expenditure = f.read()
    #         expenditure = expenditure.split(' ')
    #         expenditure = list(map(lambda x: int(x), expenditure))
    #
    #     run = FraudDetector()
    #     output = run.detector(days, expenditure)
    #     self.assertEqual(output, 0)
    #
    # def test_trailing_case_04(self) -> None:
    #     """Tests 190000 trailing days with unique expenditure"""
    #
    #     days = 190000
    #     with open('P2-input2.csv', newline='') as f:
    #         expenditure = f.read()
    #         expenditure = expenditure.split(' ')
    #         expenditure = list(map(lambda x: int(x), expenditure))
    #
    #     run = FraudDetector()
    #     output = run.detector(days, expenditure)
    #     self.assertEqual(output, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
