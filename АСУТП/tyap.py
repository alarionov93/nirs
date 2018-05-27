import uuid
from random import *

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, age, group, subjects):
		super(Student, self).__init__()
		self.id = str(uuid.uuid4())[:8]
		self.name = name
		self.age = age
		self.group = group
		self.subjects = subjects

	@property
	def score(self):
		mark_sum = 0
		avg = 0
		for s in self.subjects:
			mark_sum += s.mark
		if len(self.subjects) > 0:
			avg = mark_sum/len(self.subjects)
		return avg

	def __str__(self):
		return '%s %s %s %s' % (self.id, self.name, self.group, self.score)


class Group(object):
	"""docstring for Group"""
	def __init__(self, name):
		super(Group, self).__init__()
		self.name = name

	def __str__(self):
		return self.name
		


class Subject(object):
	"""docstring for Subject"""
	def __init__(self, name, mark):
		super(Subject, self).__init__()
		self.name = name
		self.mark = mark
		

if __name__=='__main__':

	v = Student('Vasya', 18, Group('ACY-16'), [Subject('a', 5), Subject('b', 5), Subject('c', 4)])
	p = Student('Petya', 19, Group('ACY-14'), [Subject('a', 5), Subject('b', 3), Subject('c', 4)])
	g = Student('Grisha', 20, Group('ACY-16'), [Subject('a', 3), Subject('b', 3), Subject('c', 4)])
	l = Student('Lena', 19, Group('ACY-16'), [Subject('a', 4), Subject('b', 5), Subject('c', 4), Subject('d', 5)])

	students = [v,p,g,l]

	for s in students:
		print('%s\t| %s' % (s.name, s.score))

