import unittest
from your_module import calculate_liquidity_score

class TestLiquidityScoring(unittest.TestCase):
    
    def test_liquidity_score_high(self):
        # Assuming a high liquidity scenario
        result = calculate_liquidity_score(current_assets=100000, current_liabilities=50000)
        self.assertEqual(result, 2.0)  # Example expected score for high liquidity
    
    def test_liquidity_score_low(self):
        # Assuming a low liquidity scenario
        result = calculate_liquidity_score(current_assets=30000, current_liabilities=90000)
        self.assertEqual(result, 0.33)  # Example expected score for low liquidity
    
    def test_liquidity_score_equal(self):
        # Current assets equal to current liabilities
        result = calculate_liquidity_score(current_assets=50000, current_liabilities=50000)
        self.assertEqual(result, 1.0)  # Example expected score when equal

    def test_liquidity_score_zero(self):
        # Ensure function handles zero correctly
        result = calculate_liquidity_score(current_assets=0, current_liabilities=10000)
        self.assertEqual(result, 0)  # Score should be zero

if __name__ == '__main__':
    unittest.main()