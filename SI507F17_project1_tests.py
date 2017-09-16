## Do not change import statements.
import unittest
from helper_functions import *
from SI507F17_project1_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########
class test_Cards_variables(unittest.TestCase):

	def test_1(self):
		x = Card(2,10)
		self.assertEqual(type(x.suit_names), type([]), "testing type of suit_names")
	def test_2(self):
		y = Card(0,4)
		self.assertEqual(type(y.rank_levels), type([]), "testing type of rank_levels")
	def test_3(self):
		z = Card(3,12)
		self.assertEqual(type(z.faces), type({}), "testing type of key-value pairs")
	def test_4(self):
		card = Card(2, 13)
		self.assertEqual(str(card), "King of Hearts", "testing if it returns the right output ")
	def test_5(self):
		card = Card(1,5)
		self.assertEqual(type(card.rank), int, "testing if it returns integer")

class test_Deck(unittest.TestCase):
	def test_6(self): # got help from the discussion session
		self.deck = Deck()
		for card_object in self.deck.cards:
			self.assertIsInstance(card_object, Card, "testing self.cards has instances of Card class")
	def test_7(self): # got help from the discussion session
		self.deck = Deck()
		d_string = str(self.deck)
		d_list = d_string.split('\n')
		len(d_list) == 52
		self.assertEqual(len(d_list), 52, "testing if it prints 52 lines")
	def test_8(self): 
		self.deck = Deck()
		self.assertEqual(type(self.deck.cards), type([]), "testing if the instances holds type of list")
	def test_9(self): # got help from the discussion session
		self.deck = Deck()
		for each_card in range(0,52):
			self.deck.pop_card()
		self.assertEqual(len(self.deck.cards), 0, "testing if the length of the cards that pop")
	def test_10(self): # gives you random decks
		self.deck = Deck()
		first = Deck()
		second = Deck()
		self.assertFalse(first.cards == second.cards, "testing if the two decks are different")
	# def test_14(self):


class test_Play_war_game(unittest.TestCase):
 	
 	def test_11(self):
 		war = play_war_game(testing=True)
 		self.assertEqual(type(war), tuple, "testing if output returns tuple")
 	def test_12(self):
 		war = play_war_game(testing=True)
 		self.assertEqual(type(war[0]), str, "testing if war[0] is a string")
 	def test_13(self):
 		war = play_war_game(testing=True)
 		self.assertEqual(type(war[1]), int, "testing if war[1] is a int")	


class test_Show_Song(unittest.TestCase):
	def test_14(self):
		any_song = show_song()
		self.assertIsInstance(any_song, Song, "testing if any_song is instance of class Song")
	def test_15(self):
		this_song = show_song("Lucky")
		self.assertTrue("Lucky" in str(this_song), "testing if lucky comes out in the search term")

		










unittest.main(verbosity=2)