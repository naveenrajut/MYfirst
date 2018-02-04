class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print "Name:", self.lastName + ",", self.firstName
		print "ID:", self.idNumber

class Student(Person):
    def __init__(self,firstName,lastName,idNumber,scores):
        Person.__init__(self,firstName,lastName,idNumber)
        self.scores=scores
    def calculate(self):
        self.result=0
        for i in range(numScores):
            self.result=self.result+scores[i]
        self.ans=self.result/numScores
        if self.ans>=90 and self.ans<=100:
            return'O'
        elif self.ans>=80 and self.ans<90:
            return'E'
        elif self.ans>=70 and self.ans<80:
            return'A'
        elif self.ans>=55 and self.ans<70:
            return'P'
        elif self.ans>=40 and self.ans<55:
            return'D'
        else:
            return'T'


line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input()) # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()