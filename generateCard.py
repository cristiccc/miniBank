#!usr/env/bin
import os
import random
import datetime
from dateutil import relativedelta
import textwrap

#generate customerID
def generateID():
	n = random.random()
	n *= 10000
	n = int(n)
	return str(n)

#generate card number and cvv code
def generateCardNumber():
	n = random.random()
	m = pow(10, 16)
	n *= m
	n = int(n)
	n = str(n)
	list = textwrap.wrap(n, 4)
	return list

#generate full name
def generateFullName():
	firstName = input()
	lastName = input()
	return str(firstName), str(lastName)

#generate expiration date
def generateExpirationDate():
	nextYear = datetime.date.today() + relativedelta.relativedelta(months=12)
	nextYear = str(nextYear)
	splittedExpirationDate = nextYear.split('-')
	#returns month and year, in this order
	return str(splittedExpirationDate[1]), str(splittedExpirationDate[0])

#generate cvv code
def generateCvvCode():
	n = random.random()
	n *= 1000
	n = int(n)
	return str(n)

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

newCard = dict()
newCard = emptyCard
newCard['customerID'] = generateID()
newCard['cardNumber'] = generateCardNumber()
newCard['fullName'] = generateFullName()
newCard['expirationDate'] = generateExpirationDate()
newCard['cvvCode'] = generateCvvCode()
print('NEW CARD IS : ' + str(newCard))
