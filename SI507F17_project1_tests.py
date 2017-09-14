## Do not change import statements.
import unittest
from SI507F17_project1_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########
class test_Cards_variables(unittest.TestCase):

	def test_1(self):
		x = Card()
		self.assertEqual(type(x.suit_names), type([]), "testing type of suit_names")
	def test_2(self):
		y = Card()
		self.assertEqual(type(y.rank_levels), type([]), "testing type of rank_levels")
	def test_3(self):
		z = Card()
		self.assertEqual(type(z.faces), type({}), "testing type of key-value pairs")
	def test_4(self):
		c = Card(1,"Ace")
		self.assertEqual(c.faces, (1) "testing certain key pairs with string")

# class test_Deck
	# def test_4(self):
		
unittest.main(verbosity=2)