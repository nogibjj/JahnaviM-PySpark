# Jahnavi Maddhuri: PySpark
This project demonstrates the use of PySpark in combination with ETL and Spark Query strategies to gather insights about a dataset. Specifically, I use election data in the [races.csv]([https://github.com/fivethirtyeight/data/blob/master/bad-drivers/bad-drivers.csv](https://github.com/fivethirtyeight/election-results/blob/main/races.csv)) dataset. The main ETL python script will extract data from the url to a csv, then transform and load this csv into a spark dataframe and finally query the data to gather insights about the general state elections and political party distribution.

## CI/CD Badge
[![CICD](https://github.com/nogibjj/JahnaviM-PySpark/actions/workflows/cicd_python.yml/badge.svg)](https://github.com/nogibjj/JahnaviM-PySpark/actions/workflows/cicd_python.yml)

## Instructions for Use
To use this repository, start by cloning it. Make sure all the requirements in requirements.txt are fulfilled as these are necessary tools to run the python script. Finally, run the script, etl.py, and review the results from the query statements.

## Spark Transformation and Query
Spark Transformation: I created the column is_after_2000 based on where or not the general election date is after January 1st, 2000
Query:
```sql
SELECT office_name, party, COUNT(*) AS count
FROM election_data
WHERE is_after_2000 = 1
GROUP BY office_name, party
ORDER BY office_name, party DESC
```
I analyze the distribution of political parties in the various general elections after 2000.

## Example Script Result
<img width="694" alt="image" src="https://github.com/user-attachments/assets/e585e7e7-b076-42ef-b665-3ad91ba39391">

