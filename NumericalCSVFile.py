from CSVfile import CSVfile


class NumericalCSVFile(CSVfile):
    def get_data(self):
        elements = super().get_data()
        data = []

        for i in range(len(elements)):
            dato = 0
            try:
                if i == 0:
                    dato = elements[i][1].strip()

                    try:
                        float(dato)
                    except Exception as e:
                        data.append([elements[i][0], dato:="0.0"])
                        raise Exception(" '{}' it's not a digit".format(e))
                else:
                    try:
                        dato = float(elements[i][1])
                    except Exception as e:
                        data.append([elements[i][0], dato := 0.0])
                        raise Exception(" '{}' it's not a digit".format(e))

                data.append([elements[i][0], dato])
            except Exception as e:
                print("Errore verificato: " + str(e))
                continue
        return data
