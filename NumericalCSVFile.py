from CSVfile import CSVfile


class NumericalCSVFile(CSVfile):
    def get_data(self):
        elements = super().get_data()
        data = []
        print(elements)

        for i in range(len(elements)):
            dato = 0
            try:
                if i == 0:
                    dato = elements[i][1].strip()
                    # if not float(dato).is_integer() :
                    try:
                        float(dato)
                    except Exception as e:
                        raise Exception(" '{}' it's not a digit".format(e))
                else:
                    dato = float(elements[i][1])

                data.append([elements[i][0], dato])
            except Exception as e:
                print("Errore verificato: " + str(e))
                continue
        return data
