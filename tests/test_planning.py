import unittest

class TestPlanningScoring(unittest.TestCase):

    def test_basic_planning(self):
        self.assertEqual(planning_score_calculator(100), expected_score)

    def test_planning_with_edge_case(self):
        self.assertEqual(planning_score_calculator(0), edge_case_score)

    def test_planning_with_negative(self):
        self.assertGreater(planning_score_calculator(-10), 0)

if __name__ == '__main__':
    unittest.main()