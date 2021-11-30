from CSVfile import CSVfile

class NumericalCSVFile(CSVfile):
    def get_data(self):
        elements = super().get_data()
        data = []

        for i in range(len(elements)):
            if(i != 0): dato = float(elements[i][1])
            else: dato = elements[i][1]
            data.append([elements[i][0], dato])
        return data
