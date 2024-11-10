'''This script is to test the etl.py script'''

from mylib.query import create_record, read_db, update_ca, delete_ca
from mylib.extract import extract
from mylib.transform_load import trans_load
from pyspark.sql import SparkSession

def test_extract():
    '''tests if extract function works as expected'''
    output = extract()
    assert output == 'data/election-results.csv'

def test_transform_load():
    '''tests if transform_load function works as expected'''
    extract()
    spark = SparkSession.builder.appName("Election").getOrCreate()
    output = trans_load(spark)    
    assert len(output.columns) == 16
    spark.stop()

if __name__ == '__main__':
    test_extract()
    test_transform_load()
    print('\nAll tests passed')