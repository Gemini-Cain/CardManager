#@Date 2015/09/15
#@Author Xin Du
#coding:utf-8

import json
import card

class Handler(object):
	"""Json处理"""
	def __init__(self, file_name):
		super(Handler, self).__init__()
		self.file_name = file_name
	
	def __read_json_file__(self):
		content = []
		file = open(self.file_name)
		while True:
			line = file.readline()
			if not line:
				break
			print '-'*30
			print line
			text = json.loads(line)
			content.append(text)
		return content
 	
 	def __writeJsonFile__(self, content):
 		file = open(self.file_name, 'w')
		for line in content:
			print "%s:%s" %(__name__, line)
			text = json.dumps(line)
			file.write(text + "\n")
		file.close()


	def get_cards(self):
		cards = []
		for line in self.__read_json_file__():
			item = card.Card()
			for key in line.keys():
				# if key == "id":
				# 	if isinstance(line[key], unicode):
				# 		item.set_id(line[key])
				# 	else:
				# 		raise TypeError
				if key == "numnber":
					if isinstance(line[key], unicode):
						item.set_number(line[key])
					else:
						raise TypeError
				elif key == "name":
					if isinstance(line[key], unicode):
						item.set_name(line[key])
					else:
						raise TypeError
				elif key == "bank":
					if isinstance(line[key], unicode):
						item.set_bank(line[key])
					else:
						raise TypeError
				elif key == "month_times":
					if isinstance(line[key], int):
						item.set_month_times(line[key])
					else:
						raise TypeError
				elif key == "year_times":
					if isinstance(line[key], int):
						item.set_year_times(line[key])
					else:
						raise TypeError
				elif key == "billing_date":
					if isinstance(line[key], int):
						item.set_billing_date(line[key])
					else:
						raise TypeError
				elif key == "payment_due_date_month":
					if isinstance(line[key], unicode):
						item.set_payment_due_date_month(line[key])
					else:
						raise TypeError
				elif key == "payment_due_date_type":
					if isinstance(line[key], unicode):
						item.set_payment_due_date_type(line[key])
					else:
						raise TypeError
				elif key == "payment_due_date":
					if isinstance(line[key], int):
						item.set_payment_due_date(line[key])
					else:
						raise TypeError
				else:
					continue
			cards.append(item)
		return cards

	def save_cards(self, cards):
		content = []
		for item in cards:
			line = {}
			line["number"] = item.get_number();
			line["name"] = item.get_name();
			line["bank"] = item.get_bank();
			line["month_times"] = item.get_month_times();
			line["year_times"] = item.get_year_times();
			line["billing_date"] = item.get_billing_date();
			line["payment_due_date_month"] = item.get_payment_due_date_month();
			line["payment_due_date_type"] = item.get_payment_due_date_type();
			line["payment_due_date"] = item.get_payment_due_date();
			content.append(line)
		self.__writeJsonFile__(content)


def test():
	json = Handler("D:\\Code\\CardManager\\card.txt")
	for item in json.get_cards():
		item.show_card()
	# temp = card.Card("8444", str("中信信用卡").decode("utf-8"), str("中信").decode("utf-8"), 0, 0, 13, "current", "fixed", 2)
	# cards = json.get_cards()
	# cards.append(temp)
	# json.save_cards(cards)

if __name__ == '__main__':
	test()