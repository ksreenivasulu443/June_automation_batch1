from pyspark.sql import SparkSession
import pandas as pd
import json


jar = r"C:\Users\A4952\PycharmProjects\June_automation_batch1\jars\mssql-jdbc-12.4.2.jre11.jar"
spark = SparkSession.builder.master("local[2]") \
    .appName("test") \
    .config("spark.jars", jar) \
    .config("spark.driver.extraClassPath", jar) \
    .config("spark.executor.extraClassPath", jar) \
    .getOrCreate()


mssql_df = spark.read \
        .format("jdbc") \
        .option("url", "jdbc:sqlserver://demoserver443.database.windows.net:1433;database=sampledb;") \
        .option("query", "select * from table") \
        .option("user", 'sampleadmin') \
        .option("password", 'Dharmavaram1@' ) \
        .option("driver",'com.microsoft.sqlserver.jdbc.SQLServerDriver')\
        .load()