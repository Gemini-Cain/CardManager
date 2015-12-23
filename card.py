#@Date:2015-11-25
#@Author:Xin Du
#coding:utf-8

class Card(object):

	def __init__(self, number = None, name = None, bank = None, month_times = 0, year_times = 0, billing_date = 0, payment_due_date_month = "current", payment_due_date_type = "fixed", payment_due_date = 0):
		"""docstring for Card
		__number					卡号
		__name 						卡名称
		__bank						银行
		__month_times				月消费次数
		__year_times				年消费次数
		__billing_date				账单日
		__payment_due_date_month	还款期是否本月
		__payment_due_date_type		还款日类型
		__payment_due_date 			还款日
		"""
		super(Card, self).__init__()
		self.__number = number
		self.__name = name
		self.__bank = bank
		self.__month_times = month_times
		self.__year_times = year_times
		self.__billing_date = billing_date
		self.__payment_due_date_month = payment_due_date_month
		self.__payment_due_date_type = payment_due_date_type
		self.__payment_due_date = payment_due_date

	def get_number(self):
		return self.__number

	def set_number(self, number):
		self.__number = number

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name

	def get_bank(self):
		return self.__bank

	def set_bank(self, bank):
		self.__bank = bank

	def get_month_times(self):
		return self.__month_times

	def set_month_times(self, month_times):
		self.__month_times = month_times

	def get_year_times(self):
		return self.__year_times

	def set_year_times(self, year_times):
		self.__year_times = year_times

	def get_billing_date(self):
		return self.__billing_date

	def set_billing_date(self, billing_date):
		self.__billing_date = billing_date

	def get_payment_due_date_month(self):
		return self.__payment_due_date_month

	def set_payment_due_date_month(self, payment_due_date_month):
		self.__payment_due_date_month = payment_due_date_month

	def get_payment_due_date_type(self):
		return self.__payment_due_date_type

	def set_payment_due_date_type(self, payment_due_date_type):
		self.__payment_due_date_type = payment_due_date_type

	def get_payment_due_date(self):
		return self.__payment_due_date

	def set_payment_due_date(self, payment_due_date):
		self.__payment_due_date = payment_due_date

	def show_card(self):
		print "=" * 62
		print "%-30s%32s" % ("Type", "Content")
		print "-" * 62
		print "%-30s%32s" % ("[Number]", self.__number)
		print "%-30s%32s" % ("[Name]", self.__name.encode("gbk"))
		print "%-30s%32s" % ("[Bank]", self.__bank.encode("gbk"))
		print "%-30s%32s" % ("[Month Times]", str(self.__month_times) + "次".decode("utf-8").encode("gbk"))
		print "%-30s%32s" % ("[Year Times]", str(self.__year_times) + "次".decode("utf-8").encode("gbk"))
		print "%-30s%32s" % ("[Billing Date]", str(self.__billing_date) + "日".decode("utf-8").encode("gbk"))
		print "%-30s%32s" % ("[Payment Due Date Month]", str(self.__payment_due_date_month))
		print "%-30s%32s" % ("[Payment Due Date Type]", self.__payment_due_date_type)
		print "%-30s%32s" % ("[Payment Due Date]", str(self.__payment_due_date) + "日".decode("utf-8").encode("gbk"))
		print "-" * 62

def test():
	card = Card("8444", str("中信信用卡").decode("utf-8"), str("中信").decode("utf-8"), 0, 0, 13, "current", "fixed", 2)
	card.show_card()

if __name__ == '__main__':
	test()