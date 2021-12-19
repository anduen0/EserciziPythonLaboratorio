from CSVfile import CSVfile
from NumericalCSVFile import NumericalCSVFile
from incrementalModel import IncrementModel
from FitIncrementalModle import FitIncrementalModle

# csvFile = CSVfile('./shampoo_sales.csv')
# try:
#     numericalCSV = NumericalCSVFile('./shampoo_sales.csv')
#     print(numericalCSV.get_data())
# except Exception as e:
#     print("Expection: {}".format(str(e)))

# test_fit_data = [8,19,31,41]
# test_predict_data = [50,52,60]
#
# increment_model = IncrementModel()
# prediction = increment_model.predict(test_predict_data)
# if not prediction == 65:
#     raise Exception('IncrementModel sul dataset di test non mi torna 65 ma "{}"'.format(prediction))
# else:
#     print('IncrementModel test passed')
#
# fit_increment_model = FitIncrementalModle()
# fit_increment_model.fit(test_fit_data)
# prediction = fit_increment_model.predict(test_predict_data)
# if not prediction == 68:
#     raise Exception('FitIncrementModel sul dataset di test non mi torna 68 ma "{}"'.format(prediction))
# else:
#     print('FitIncrementModel test passed')

# Linea vuota

shampoo_sales = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]

eval_months = 12
cutoff_month = len(shampoo_sales) - eval_months

increment_model = IncrementModel()
fit_increment_model = FitIncrementalModle()

fit_increment_model.fit(shampoo_sales[:cutoff_month])

models = [increment_model, fit_increment_model]

for model in models:

    error = 0
    print('Evaluating model "{}"'.format(model))

    # Predizioni sul dataset di "valutazione" ovvero le vendite
    # dello shampoo dal mese di cutoff in poi
    predictions = []
    for i in range(eval_months):
        predict_data = shampoo_sales[cutoff_month + i - 3 - 1:cutoff_month + i - 1]
        prediction = model.predict(predict_data)
        real = shampoo_sales[cutoff_month + i]
        print('"{}" (pred) vs "{}" (real)'.format(int(prediction), int(real)))

        # Aggiungo se volessi poi plottare
        predictions.append(prediction)

        error += abs(prediction - real)

    error = error / eval_months

    print('Average error: "{}"\n'.format(error))
