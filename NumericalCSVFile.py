from CSVfile import CSVfile


class NumericalCSVFile(CSVfile):
    def get_data(self):
        elements = super().get_data()
        data = []

        for i in range(len(elements)):
            try:
                if i == 0:
                    dato = elements[i][1].strip()
                    if not dato.isdigit():
                        raise Exception(" '{}' it's not a digit".format(dato))
                else:
                    dato = float(elements[i][1])
                    data.append([elements[i][0], dato])
            except Exception as e:
                print("Errore verificato: " + str(e))
                continue
        return data
