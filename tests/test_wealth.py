import unittest

class TestWealthScoring(unittest.TestCase):

    def test_calculate_wealth_score(self):
        # Assume calculate_wealth_score is a function in your application that calculates wealth score
        from your_module import calculate_wealth_score  # Adjust the import according to your module structure
        
        # Test case 1: Basic example
        score = calculate_wealth_score(income=50000, assets=200000, liabilities=50000)
        self.assertEqual(score, 200000)  # Example expected score
        
        # Test case 2: No assets
        score = calculate_wealth_score(income=30000, assets=0, liabilities=10000)
        self.assertEqual(score, 20000)  # Example expected score
        
        # Test case 3: Negative liabilities
        score = calculate_wealth_score(income=45000, assets=150000, liabilities=-20000)
        self.assertEqual(score, 170000)  # Example expected score

if __name__ == '__main__':
    unittest.main()