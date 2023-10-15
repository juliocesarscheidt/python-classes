# pip install importlib_metadata pydantic

# https://docs.pydantic.dev/latest/
# https://docs.pydantic.dev/latest/why/#json-schema

from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, ValidationError

class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]

m1 = Delivery(timestamp='2020-10-31T03:04:05Z', dimensions=['10', '20'])

print(m1)
# timestamp=datetime.datetime(2020, 10, 31, 3, 4, 5, tzinfo=TzInfo(UTC)) dimensions=(10, 20)

print(repr(m1.timestamp))
# datetime.datetime(2020, 10, 31, 3, 4, 5, tzinfo=TzInfo(UTC))

print(m1.dimensions)
# (10, 20)

print(m1.model_dump())  
# {'timestamp': datetime.datetime(2020, 10, 31, 3, 4, 5, tzinfo=TzInfo(UTC)), 'dimensions': (10, 20)}


external_data = {'timestamp': '2023-01-31T12:59:59Z', 'dimensions': ['50', '60']}  

try:
    m2 = Delivery(**external_data)

    print(m2.model_dump())
    # {'timestamp': datetime.datetime(2023, 1, 31, 12, 59, 59, tzinfo=TzInfo(UTC)), 'dimensions': (50, 60)}
    
    print(m2.model_json_schema())
    # {'properties': {'timestamp': {'format': 'date-time', 'title': 'Timestamp', 'type': 'string'}, 'dimensions': {'maxItems': 2, 'minItems': 2, 'prefixItems': [{'type': 'integer'}, {'type': 'integer'}], 'title': 'Dimensions', 'type': 'array'}}, 'required': ['timestamp', 'dimensions'], 'title': 'Delivery', 'type': 'object'}

except ValidationError as e:
    print(e.errors())
