import unittest
import underperformers as un
#Doing import <module name> as <short name> allows us to use
#this short_name when referring to this module.

# Note: this test suite does not contain a complete set of test cases.

class TestCollectUnderperformers(unittest.TestCase):

    def test_underperformers_low_threshold(self):
        """ Test collect_underperformers with a threshold for which there
        are no underperformers."""

        actual = un.collect_underperformers([4, 5, 6], 1)
        expected = []
        self.assertEqual(actual, expected)


    def test_underperformers_high_threshold(self):
        """ Test collect_underperformers with a threshold for which all items
        are underperformers."""
        
        actual = un.collect_underperformers([2, 4, 6], 8)
        expected = [2, 4, 6]
        self.assertEqual(actual, expected)


        
    def test_underperformers_mutation(self):
        """ Confirm that collect_underperformers does not mutate the 
        list it's given."""
        
        perf_list = [3, 5, 2]
        perf_list_expected = perf_list[:]
        actual = un.collect_underperformers(perf_list, 4)
        self.assertEqual(perf_list, perf_list_expected)

	#Two things to be careful about:
	#(1) If you do perf_list_expected = perf_list, then both
	#refer to the same object so you will not be able to catch a mutation.
	#(2) Use an example where not all the list elements are underperformers. 
	#In that case the list wouldn't change so you cannot tell if the code mutates the list or not.
        

        
if __name__ == '__main__':
    unittest.main(exit = False)
        
        
