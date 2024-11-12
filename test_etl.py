'''This script is to test the etl.py script'''

from pyspark.sql import SparkSession
from mylib.extract import extract
from mylib.transform_load import trans_load
from mylib.query import query

def test_extract():
    '''tests if extract function works as expected'''
    output = extract()
    assert output == 'data/election-results.csv'

def test_transform_load():
    '''tests if trans_load function works as expected'''
    extract()
    spark = SparkSession.builder.appName("Election").getOrCreate()
    output = trans_load(spark)    
    assert len(output.columns) == 16
    spark.stop()

def test_query():
    '''tests if query function works as expected'''
    spark = SparkSession.builder.appName("Election").getOrCreate()
    df = trans_load(spark)
    output = query(spark, df)
    assert len(output.columns) == 17
    spark.stop()

if __name__ == '__main__':
    test_extract()
    test_transform_load()
    test_query()
    print('All tests passed')