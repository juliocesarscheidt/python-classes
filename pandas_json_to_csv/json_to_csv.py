import os
import json
import pandas as pd

if __name__ == '__main__':
  result_dataset = []
  
  with open('sample.json', 'r') as f:
    content = json.loads(f.read())
    # print(content)
    result_dataset = content

  df = pd.DataFrame(data=result_dataset)
  print(df.head(10))
  print(df.describe())

  # generate a csv from dataset
  df.to_csv(
    f"sample.csv",
    index=False,
    sep=",",
    encoding="utf-8",
  )
