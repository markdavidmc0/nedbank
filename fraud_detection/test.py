#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from fraud_detection import FraudDetector
import time


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

    def test_days_equals_expenditure(self) -> None:
        """Tests cases where number of trailing days equals number of expenditure days"""

        days = 2
        expenditure = [1, 4]

        run = FraudDetector()
        output = run.detector(days, expenditure)
        self.assertEqual(output, 0)

    def test_one_day(self) -> None:
        """Tests one day entry"""

        days = 1
        expenditure = [150]

        run = FraudDetector()
        output = run.detector(days, expenditure)
        self.assertEqual(output, 0)

    def test_less_than_one(self) -> None:
        """Tests less than one day entry"""

        days = 0
        expenditure = []

        run = FraudDetector()
        with self.assertRaises(ValueError):
            run.detector(days, expenditure)

    def test_negative_days(self) -> None:
        """Tests negative days"""

        days = -5
        expenditure = []

        run = FraudDetector()
        with self.assertRaises(ValueError):
            run.detector(days, expenditure)

    def test_days_larger_than_expense(self) -> None:
        """Tests days larger than expense"""

        days = 5
        expenditure = [2, 6, 7, 5]

        run = FraudDetector()
        with self.assertRaises(ValueError):
            run.detector(days, expenditure)

    def test_days_larger_than_10_power_5(self) -> None:
        """Tests larger than 10^5 days"""

        days = 10**6
        expenditure = [2, 6, 7, 5, 7, 8, 9]

        run = FraudDetector()
        with self.assertRaises(ValueError):
            run.detector(days, expenditure)

    def test_expense_larger_than_200(self) -> None:
        """Tests larger than 200 foe expense"""

        days = 4
        expenditure = [0, 6, 7, 5, 7, 8, 400]

        run = FraudDetector()
        with self.assertRaises(ValueError):
            run.detector(days, expenditure)

    def test_large_case_1(self) -> None:
        """Tests 10000 trailing days with unique expenditure"""

        # initial time
        t1 = time.time()

        days = 10000
        # read in expenditure list from file
        with open('fraud_detection/P2-input1.csv', newline='') as f:
            expenditure = f.read()
            expenditure = expenditure.split(' ')
            expenditure = list(map(lambda x: int(x), expenditure))

        print('Processing lerge test case 1...')
        run = FraudDetector()
        output = run.detector(days, expenditure)
        self.assertEqual(output, 406)

        # user output info
        print('Number of messages to be sent:{}'.format(output))
        t2 = time.time()
        print('Time taken to run test: {}s'.format(t2 - t1))

    def test_large_case_2(self) -> None:
        """Tests 80000 trailing days with unique expenditure"""

        # initial time
        t1 = time.time()

        days = 80000
        # read in expenditure list from file
        with open('fraud_detection/P2-input2.csv', newline='') as f:
            expenditure = f.read()
            expenditure = expenditure.split(' ')
            expenditure = list(map(lambda x: int(x), expenditure))

        print('Processing lerge test case 2...')
        run = FraudDetector()
        output = run.detector(days, expenditure)
        self.assertEqual(output, 3)

        # user output info
        print('Number of messages to be sent: {}'.format(output))
        t2 = time.time()
        print('Time taken to run test: {}s'.format(t2 - t1))


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
