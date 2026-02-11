import unittest

def calculate_debt_score(total_debt, income):
    # Sample function to calculate debt score
    if total_debt < 0 or income < 0:
        return -1  # Indicating invalid input
    if total_debt == 0:
        return 0
    return max(0, income - total_debt)  # Simple debt score calculation

class TestDebtScoring(unittest.TestCase):

    def test_positive_debt_score(self):
        # Example test case for a positive debt score
        score = calculate_debt_score(10000, 5000)  # Example values
        self.assertGreater(score, 0)

    def test_zero_debt_score(self):
        # Example test case for zero debt score
        score = calculate_debt_score(0, 0)  # Example values
        self.assertEqual(score, 0)

    def test_negative_debt_score(self):
        # Example test case for negative debt score (if applicable)
        score = calculate_debt_score(-5000, 2000)  # Example values
        self.assertLess(score, 0)

if __name__ == '__main__':
    unittest.main()