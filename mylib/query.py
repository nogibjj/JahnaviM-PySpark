'''Use a query to analyze election data'''

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

def query(spark, election_df):
    '''Use a complex query to analyze election data'''

    # Data transformation: add column is_after_2000
    transformed_election = election_df.withColumn(
        "is_after_2000",
        when(col("date") >= "01/01/2000", 1).otherwise(0)
    )

    # Create a temporary view for Spark SQL
    transformed_election.createOrReplaceTempView("election_data")

    # Spark SQL Query: general elections political party counts
    query_result = spark.sql("""
        SELECT office_name, party, COUNT(*) AS count
        FROM election_data
        WHERE is_after_2000 = 1
        GROUP BY office_name, party
        ORDER BY office_name, party DESC
    """)

    # Show the query result
    query_result.show()
    return transformed_election

if __name__ == '__main__':
    from transform_load import trans_load
    
    spark = SparkSession.builder.appName("Election").getOrCreate()
    df = trans_load(spark)
    query(spark, df)
    spark.stop()
    
