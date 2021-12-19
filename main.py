from CSVfile import CSVfile
from NumericalCSVFile import NumericalCSVFile
from incrementalModel import IncrementModel
from FitIncrementalModle import FitIncrementalModle

# csvFile = CSVfile('./shampoo_sales.csv')
# try:
#     numericalCSV = NumericalCSVFile('./shampoo_sales.csv')
#     print(numericalCSV.get_data())
# except Exception as e:
#     print("Expection: {}".format(str(e)))

incModl = IncrementModel()
fitModl = FitIncrementalModle()
dataset = [8, 19, 31, 41]
current = [50, 52, 60]



print(incModl.predict(current))



print(fitModl.predict(dataset, current))

