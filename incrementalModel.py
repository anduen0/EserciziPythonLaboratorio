from models import Model


class IncrementModel(Model):
    def predict(self, data):
        prediction = 0
        length = len(data)
        for item in range(length):
            if item < length-1:
                prediction += abs(data[item] - data[item + 1])
        return prediction/(length-1) + data[length-1]
