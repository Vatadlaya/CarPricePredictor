import pandas as pd
df = pd.read_csv(r"C:\Users\josephmuhlari\OneDrive\Desktop\CarPricePrediction\car_dataset (1).csv")

df['Selling_Price'] = df['Selling_Price']*100000
df['Present_Price'] = df['Present_Price']*100000
df.head()

# Create the date object of today's date:
from datetime import date
todays_date = date.today()
print(todays_date)

# Create car's age column:
df['Car_Age'] = todays_date.year - df['Year'] # Feature engineering
df.head()

# Drop Car name and Seller type
df = df.drop(columns=['Car_Name', 'Seller_Type'])
df.head()

# Encode the categorical columns using one-hot encoding:
df = pd.get_dummies(df,dtype=int)
# Note that categorical columns are divided into their types and columns are created for each type
# 0 is assigned if the new column type is not applicable, otherwise 1 is assigned
df.head()

# Change the df dataframe to a csv file
df.to_csv("car_cleaned_data.csv", index=False)
car_cleaned_data = pd.read_csv(r'car_cleaned_data.csv')
car_cleaned_data.head()