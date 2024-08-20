from pyspark.sql import SparkSession
import pandas as pd
import json


jar = r"C:\Users\A4952\PycharmProjects\June_automation_batch1\jars\ojdbc8-21.5.0.0.jar"
spark = SparkSession.builder.master("local[2]") \
    .appName("test") \
    .config("spark.jars", jar) \
    .config("spark.driver.extraClassPath", jar) \
    .config("spark.executor.extraClassPath", jar) \
    .getOrCreate()

url = "jdbc:sqlserver://demoserver443.database.windows.net:1433;database=sampledb;"
database_name = "sampledb"
username ='sampleadmin'
password='Dharmavaram1@'
database="sampledb"
table_name = "dbo.Persons2"


mssql_df = spark.read \
        .format("jdbc") \
        .option("url", url) \
        .option("query", "select * from table") \
        .option("user", username) \
        .option("password", password ) \
        .option("driver",'com.microsoft.sqlserver.jdbc.SQLServerDriver')\
        .load()