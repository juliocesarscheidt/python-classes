import os
import json

filename = "output.txt"

# writing
with open(filename, "w") as file:
  file.write(json.dumps({"message": "Hello World"}))
  # file.close() # no need to call close

# reading
with open(filename, "r") as file:
  content = json.loads(file.read())
  print(content)
  # {'message': 'Hello World'}
  print(content["message"])
  # Hello World
  # file.close() # no need to call close

try:
  print(os.stat(filename))
except Exception as e:
  pass
