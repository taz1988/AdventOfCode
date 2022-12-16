import unittest
import calorie

class MaxCalorieTestCase(unittest.TestCase):

    input="""1000
    2000
    3000

    4000

    5000
    6000

    7000
    8000
    9000

    10000"""

    def test_find_biggest_calorie(self):
        self.assertEqual(calorie.max_calorie(self.input.split("\n")), 24000, 'incorrect max callorie')

    def test_find_all_calories(self):
        self.assertEqual(calorie.all_elves_calories(self.input.split("\n")), [6000, 4000, 11000, 24000, 10000], 'incorrect all elves callories')

    def test_find_top_three_calories_sum(self):
        self.assertEqual(calorie.top_three_calories_total(self.input.split("\n")), 45000, 'incorrect top three elves sum callories')
