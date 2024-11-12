'''Takes a csv and loads it as a spark df'''

from pyspark.sql import SparkSession

PATH = 'data/election-results.csv'

def trans_load(spark, path = PATH):
    '''Takes the csv file and loads at as a Spark df'''
    # Load Data
    df = spark.read.csv(path, header=True, inferSchema=True)
    return df

if __name__ == '__main__':
    spark = SparkSession.builder.appName("Election").getOrCreate()
    output = trans_load(spark)
    print('Number of columns:', len(output.columns))
    spark.stop()