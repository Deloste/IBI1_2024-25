import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("D:")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
dalys_data.head(5)
dalys_data.info()
dalys_data.describe()
print(dalys_data.iloc[0:10, 0:3])
#the 10th year for which DALYs were recorded in Afghanistan is 1999
dalys_1990 = dalys_data.loc[dalys_data['Year'] == 1990, 'DALYs']
data_1990 = dalys_data.loc[dalys_data['Year'] == 1990, :]
print(data_1990)
uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
plt.plot(uk.Year, uk.DALYs, 'bo')
plt.xticks(uk.Year,rotation=-90)
fr = dalys_data.loc[dalys_data.Entity=="France", ["DALYs", "Year"]]
uk.describe() #mean=23319.016333
fr.describe() #mean=21474.627000
#mean DALYs for UK is bigger than France
# Filter rows where DALYs > 650,000
high_dalys = dalys_data[dalys_data['DALYs'] > 650000]
# Extract unique country names
countries_high_dalys = high_dalys['Entity'].unique()
print("Countries with DALYs > 650,000 in at least one year:")
print(countries_high_dalys)
