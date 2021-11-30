class CSVfile:
	def __init__(self, name):
		self.name = name
	
	def get_data(self):
        my_file = open(self.name, 'r')

		data=[] 

		for line in my_file:
			
			if 'Date' in line:
				continue

			data.append(line.split(','))
		
		my_file.close()

		return data