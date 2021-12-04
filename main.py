from CSVfile import CSVfile
from NumericalCSVFile import NumericalCSVFile

# csvFile = CSVfile('./shampoo_sales.csv')
try:
    numericalCSV = NumericalCSVFile('./shampoo_sales.csv')
    print(numericalCSV.get_data())
except Exception as e:
    print("Expection: {}".format(str(e)))


