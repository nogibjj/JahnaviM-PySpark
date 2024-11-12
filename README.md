# Jahnavi Maddhuri: PySpark
This project demonstrates the use of PySpark in combination with ETL and Spark Query strategies to gather insights about a dataset. Specifically, I use election data in the [races.csv]([https://github.com/fivethirtyeight/data/blob/master/bad-drivers/bad-drivers.csv](https://github.com/fivethirtyeight/election-results/blob/main/races.csv)) dataset. The main ETL python script will extract data from the url to a csv, then transform and load this csv into a spark dataframe and finally query the data to gather insights about the general state elections and political party distribution.

## CI/CD Badge
[![CICD](https://github.com/nogibjj/JahnaviM-PySpark/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/JahnaviM-PySpark/actions/workflows/cicd.yml)

## Instructions for Use
To use this repository, start by cloning it. Make sure all the requirements in requirements.txt are fulfilled as these are necessary tools to run the python script. Finally, run the script, etl.py, and review the results from the CRUD statements.

## Example Script Result
<img width="585" alt="image" src="https://github.com/user-attachments/assets/7c9b8c67-f53a-401c-9af5-6b870290048b">
