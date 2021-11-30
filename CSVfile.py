
class CSVfile:
	def __init__(self, name):
		self.name = name

	def get_data(self):

		try:
			my_file = open(self.name, 'r')
		except:
			print('Il file "{}" non esiste!'.format(self.name))
			return -1

		data=[]

		for line in my_file:

			if'Date' in line:
				continue

			data.append(line.split(','))

		my_file.close()
		return data