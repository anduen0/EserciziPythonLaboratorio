from models import Model


class IncrementModel(Model):
    def avgIncrease(self, data):
        averageIncrease = 0
        length = len(data)
        for item in range(length):
            if item < length - 1:
                averageIncrease += data[item + 1] - data[item]

        return averageIncrease / (length-1)

    def predict(self, data):
        avgIncrease = self.avgIncrease(data)
        return data[-1] + avgIncrease
