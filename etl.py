'''Use ETL to Extract, Transform, Load and Query election data'''

from pyspark.sql import SparkSession
from mylib.extract import extract
from mylib.transform_load import trans_load
from mylib.query import query

# Create a Spark session
spark = SparkSession.builder.appName("Election").getOrCreate()

# Extract
extract()

# Transform and Load
election_df = trans_load(spark)

# Query
query(spark, election_df)

# Stop the Spark session
spark.stop()
