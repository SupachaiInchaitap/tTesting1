import unittest

def assess_health(x, y):
    if x <= 120 and 100 <= y < 125:
        return "Normal"
    elif 120 < x <= 138 and 100 <= y < 125:
        return "Risk"
    elif 140 <= x < 159 and 125 <= y < 154:
        return "High Risk level 1"
    elif 160 <= x < 179 and 155 <= y < 182:
        return "High Risk level 2"
    elif x >= 180 and y >= 183:
        return "High Risk level 3"
    else:
        return "Consider Visiting a Hospital"

class Health(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(assess_health(120,100),"Normal")
    def test_risk(self):
        self.assertEqual(assess_health(134,120),"Risk")
    def test_high_risk_level_1(self):
        self.assertEqual(assess_health(150,130),"High Risk level 1")
    def test_high_risk_level_2(self):
        self.assertEqual(assess_health(164,161),"High Risk level 2")
    def test_high_risk_level_3(self):
        self.assertEqual(assess_health(180,184),"High Risk level 3")
    def test_consider_visiting_hospital(self):
        self.assertEqual(assess_health(50,20),"Consider Visiting a Hospital")
if __name__ == '__main__':
    unittest.main()
