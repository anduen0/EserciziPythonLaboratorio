class CSVfile:
    try:
        def __init__(self, name, start=0, end=-1):
            if type(start) != int and type(end) != int and type(name) != str :
                raise Exception("Params not supported")
            else:
                self.name = name
                self.start = start
                self.end = end
    except Exception as e:
        print("Expection: {}".format(str(e)))

    def get_data(self):

        try:
            my_file = open(self.name, 'r')
        except:
            print('Il file "{}" non esiste!'.format(self.name))
            return -1

        data = []

        for index, line in enumerate(my_file):
            if index >= self.start and (index <= self.end and self.end != -1):
                if 'Date' in line:
                    continue

                data.append(line.split(','))

        my_file.close()
        return data
