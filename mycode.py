import pandas as pd
import os

data = {'Name ': ['Alice','Bob','Charlie'],'Age': [23,34,31] , 'City' : ['NewYork','Los Angeles','Chicago']}

df = pd.DataFrame(data)




data_dir = 'data' ## name of directory
os.makedirs(data_dir,exist_ok=True) ## creates the data folder
## if the folder already exists , exists_ok = True  rewrites 



file_path = os.path.join(data_dir,'sample_data.csv')
## this creates a file sample_data.csv in data directory


df.to_csv(file_path,index=False)
## copies the above data into sample_data.csv
## index = False tells pandas not to include the row inde numbers in csv file


print(f'csv file saved to {file_path}')