import unittest
import rock_paper_scissors

#python3 -m unittest rock_paper_scissors_test.py
class RockPaperScissorsTestCase(unittest.TestCase):

    input="""A Y
B X
C Z"""

    def test_calculate_score(self):
        self.assertEqual(rock_paper_scissors.calculate_score(self.input.split("\n")), 15, 'incorrect score')

    def test_calculate_score_with_suggested_output(self):
        self.assertEqual(rock_paper_scissors.calculate_score_with_suggested_output(self.input.split("\n")), 12, 'incorrect score')
