class X(object):
	"""docstring for X"""
	def __init__(self, *args):
		super(X, self).__init__()
		self.args = args

	def __str__(self):
		return str(self.args[0])

x = X(1, 2, 3)
print(x)