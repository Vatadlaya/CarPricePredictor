import pandas as pd
df = pd.read_csv('car_cleaned_data.csv')
df.head()

df.columns

X= df[['Present_Price', 'Kms_Driven', 'Car_Age', 'Fuel_Type_CNG', 'Fuel_Type_Diesel', 'Fuel_Type_Petrol', 'Transmission_Automatic',
        'Transmission_Manual']]
y = df['Selling_Price']
print(X)
print(y)

#  Fitting Random Forest Regression to the Training set
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(X,y)

import pickle
#  This line imports the built-in Python library that provides the functionality for object serialization.
# Serialization means saving a Python object, for example, an ML, model, to a binary file named rf_model.pkl using the pickle module
with open('rf_model.pkl', 'wb') as model_file:
# This part assigns the opened file object to the variable model_file, which is then used within the with block. 
# The with statement ensures the file is automatically closed when the block is exited, even if errors occur.
    pickle.dump(model, model_file)
# This function serializes the Python object model (e.g., a trained scikit-learn random forest classifier)
# and writes the resulting byte stream to the file object model_file. 