from incrementalModel import IncrementModel

class FitIncrementalModle(IncrementModel):


    def fit(self, dataframe):
        return super().avgIncrease(dataframe)

    def predict(self,dataframe, current):
        avg_increment = self.fit(dataframe)
        currentAverageIncrease = super().avgIncrease(current)
        return current[-1] + ((avg_increment + currentAverageIncrease) / 2)



