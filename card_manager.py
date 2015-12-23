#@Date:2015-11-25
#@Author:Xin Du
#coding:utf-8

import time
import json_handler

class CardManager(object):
	"""docstring for CardManager"""
	def __init__(self, file):
		super(CardManager, self).__init__()
		self.handler = json_handler.Handler(file)

	def get_best_card(self, date):
		"""获取账期最长的卡"""
		year = date[0]
		month = date[1]
		day = date[3]
		cards = self.handler.get_cards()
		for x in cards:
			pass
		pass

	def get_all_card(self, date):
		"""获取账期最长的卡"""
		pass

	def show_cards(self, cards):
		pass

def test():
	
	cm = CardManager("D:\\Code\\CardManager\\card.txt")
	cm.get_best_card(time.localtime())
	
if __name__ == '__main__':
	test()#@Date:2015-11-25
#@Author:Xin Du
#coding:utf-8

import time
import json_handler.Handler

class CardManager(object):
	"""docstring for CardManager"""
	def __init__(self, file):
		super(CardManager, self).__init__()
		self.handler = Handler(file)

	def get_best_card(self, date):
		"""获取账期最长的卡"""
		year = date[0]
		month = date[1]
		day = date[3]
		cards = self.handler.get_cards()
		for x in cards:
			pass
		pass

	def get_all_card(self, date):
		"""获取账期最长的卡"""
		pass

	def show_cards(self, cards):
		pass

def test():
	
	cm = CardManager("D:\\Code\\CardManager\\card.txt")
	cm.get_best_card(time.localtime())
	
if __name__ == '__main__':
	test()