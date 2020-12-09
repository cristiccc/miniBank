#!usr/env/bin
import os

#empty card generator
def generateEmptyCard():
	global emptyCard
	emptyCard = dict()
	emptyCard['customerID'] = '000'
	emptyCard['cardNumber'] = ['0000', '0000', '0000', '0000']
	emptyCard['fullName'] = 'John Doe'
	emptyCard['expirationDate'] = ['00', '00']
	emptyCard['cvvCode'] = '000'


generateEmptyCard()
print('Empty card : ' + str(emptyCard))
