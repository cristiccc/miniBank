import random
import datetime
from dateutil import relativedelta
import textwrap

class createUser:
	def __init__(self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName

	#generate customerID
	def generateID(self):
		n = random.random()
		n *= 10000
		n = int(n)
		self.id = str(n)
		#return str(n)



class createRONAccount(createUser):
	def __init__(self, firstName, lastName):
		createUser.__init__(self, firstName, lastName)
		#super().__init__(self, firstName, lastName)

	#generate card number and cvv code
	def generateRONCardNumber(self):
		n = random.random()
		m = pow(10, 16)
		n *= m
		n = int(n)
		n = str(n)
		n.strip('[,]')
		self.cardNumber = n
		#list = textwrap.wrap(n, 4)
		#return list

	#generate expiration date
	def generateExpirationDate(self):
		nextYear = datetime.date.today() + relativedelta.relativedelta(months=12)
		nextYear = str(nextYear)
		splittedExpirationDate = nextYear.split('-')
		self.month = splittedExpirationDate[1]
		self.year = splittedExpirationDate[0]
		#returns month and year, in this order
		#return str(splittedExpirationDate[1]), str(splittedExpirationDate[0])

	#generate cvv code
	def generateCvvCode(self):
		n = random.random()
		n *= 1000
		n = int(n)
		n = str(n)
		self.cvv = n

	def printRONAccount(self):
		print(self.firstName, self.lastName, self.id, self.cardNumber, self.month, self.year, self.cvv)



class createEURAccount(createUser):
	def __init__(self, firstName, lastName):
		createUser.__init__(self, firstName, lastName)
		#super().__init__(self, firstName, lastName)

	def printAccount(self):
		print(self.firstName, self.lastName)



class createUSDAccount(createUser):
	def __init__(self, firstName, lastName):
		createUser.__init__(self, firstName, lastName)
		#super().__init__(self, firstName, lastName)

	def printAccount(self):
		print(self.firstName, self.lastName)



class createRONDeposit(createUser):
	def __init__(self, firstName, lastName):
		createUser.__init__(self, firstName, lastName)
		#super().__init__(self, firstName, lastName)

	def addDeposit(self, amount):
		self.amount = amount

	def printDeposit(self):
		print(self.amount)



class createEURDeposit(createUser):
	def __init__(self, firstName, lastName):
		createUser.__init__(self, firstName, lastName)
		#super().__init__(self, firstName, lastName)

	def addDeposit(self, amount):
		self.amount = amount

	def printDeposit(self):
		print(self.amount)



class createUSDDeposit(createUser):
	def __init__(self, firstName, lastName):
		createUser.__init__(self, firstName, lastName)
		#super().__init__(self, firstName, lastName)

	def addDeposit(self, amount):
		self.amount = amount

	def printDeposit(self):
		print(self.amount)

x = createRONAccount('Cristi', 'Keseru')
x.generateID()
x.generateRONCardNumber()
x.generateExpirationDate()
x.generateCvvCode()
x.printRONAccount()
