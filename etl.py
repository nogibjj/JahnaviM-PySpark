'''Use ETL to Extract, Transform, Load and Query election data'''

from mylib.extract import extract
from mylib.transform_load import trans_load
from mylib.query import query

# Extract
extract()

# Transform and Load
trans_load()

# Query
query()
