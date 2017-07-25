import unittest
import mutated_underperformers as un

# Note: this test suite does not contain a complete set of test cases.

class TestCollectUnderperformers(unittest.TestCase):

    def test_underperformers_low_threshold(self):
        """ Test collect_underperformers with a threshold for which there
        are no underperformers."""
        
        perf_list = [4, 5, 6]
        actual = un.collect_underperformers(perf_list, 1)
        mutated_perf_list = []
        self.assertEqual(perf_list, mutated_perf_list)
        #The next check is optional. You can have a seperate test case for that.
        self.assertEqual(actual, None)

        
if __name__ == '__main__':
    unittest.main(exit = False)
        
        
