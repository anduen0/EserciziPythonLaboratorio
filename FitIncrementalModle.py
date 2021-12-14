from incrementalModel import IncrementModel

class FitIncrementalModle(IncrementModel):


    def fit(self, dataset):
        return super().avgIncrease(dataset)

    def predict(self, dataset, current):
        avg_increment = self.fit(dataset)
        currentAverageIncrease = super().avgIncrease(current)
        return current[-1] + ((avg_increment + currentAverageIncrease) / 2)



