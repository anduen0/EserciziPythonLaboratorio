from CSVfile import CSVfile
from NumericalCSVFile import NumericalCSVFile

# csvFile = CSVfile('./shampoo_sales.csv')
numericalCSV = NumericalCSVFile('./shampoo_sales.csv')

print(numericalCSV.get_data())

