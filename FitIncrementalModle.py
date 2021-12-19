from incrementalModel import IncrementModel

class FitIncrementalModle(IncrementModel):
    def __str__(self):
        return 'FitIncrementModel'

    def fit(self, fit_data):
        self.global_avg_increment = self.avgIncrease(fit_data)

    def predict(self, predict_data):
        parent_prediction = super().predict(predict_data)

        parent_predict_increment = parent_prediction - predict_data[-1]

        prediction_increment = (self.global_avg_increment + parent_predict_increment) / 2

        prediction = predict_data[-1] + prediction_increment

        return prediction


