from CSVfile import CSVfile
from NumericalCSVFile import NumericalCSVFile
from incrementalModel import IncrementModel

# csvFile = CSVfile('./shampoo_sales.csv')
# try:
#     numericalCSV = NumericalCSVFile('./shampoo_sales.csv')
#     print(numericalCSV.get_data())
# except Exception as e:
#     print("Expection: {}".format(str(e)))

incModl = IncrementModel()
print(incModl.predict([50, 52, 60]))

