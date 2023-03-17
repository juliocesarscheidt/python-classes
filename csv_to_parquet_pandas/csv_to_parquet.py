import os
import time
import json
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

import pandas as pd
import pyarrow.parquet as pq

# read from csv file
df_csv = pd.read_csv('customer.csv', sep=',')
df_csv['c_login'].fillna(value="", inplace=True)

print(df_csv.head(10))
print(df_csv.describe())
print(df_csv.columns)

# creating final df from csv df
body_df_final = []
now = date.today()

for index, row in df_csv.iterrows():
  print(row['c_customer_id'], row['c_email_address'],
        row['c_first_name'], row['c_last_name'],
        row['c_birth_day'], row['c_birth_month'], row['c_birth_year'])

  birth_date = datetime.strptime(str(row['c_birth_year']) + '-' + \
                                 str(row['c_birth_month']) + '-' + \
                                 str(row['c_birth_day']), '%Y-%m-%d').date()
  print('birth_date', birth_date)
  rdelta = relativedelta(now, birth_date)
  print('years', rdelta.years)

  body_df_final.append({
    'id': row['c_customer_id'],
    'name': (row['c_first_name'].strip() + ' ' + row['c_last_name'].strip()).capitalize(),
    'email': row['c_email_address'].strip().lower(),
    'age': rdelta.years
  })

df_final = pd.DataFrame(data=body_df_final)
print(df_final.head(10))

# save to parquet file
df_final.to_parquet(path='./customer.gz.parquet', index=True, compression='gzip')
# df_final.to_parquet(path='./customer.snappy.parquet', index=True, compression='snappy')

# read from parquet file
df_parquet = pq.ParquetDataset('./customer.gz.parquet').read_pandas().to_pandas()

print(df_parquet.head(10))
print(df_parquet.describe())
