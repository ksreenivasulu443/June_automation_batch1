# Databricks notebook source
import datetime
import json
import os
import sys
import pandas as pd
from pyspark.sql.functions import explode_outer, concat, col, \
    trim,to_date, lpad, lit, count,max, min, explode, current_timestamp
from pyspark.sql import SparkSession
import getpass
file_path = 'dbfs:/FileStore/June_batch/Contact_info.csv'
system_user = getpass.getuser()

batch_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

file = spark.read.csv(file_path, header=True, inferSchema=True)
file = file.filter('Identifier is not null')

file= file.withColumn('batch_date', lit(batch_id))\
    .withColumn('create_date', current_timestamp())\
    .withColumn('update_date', current_timestamp())\
    .withColumn('create_user',lit(system_user))\
    .withColumn('update_user',lit(system_user))

file.display()

file.printSchema()

# COMMAND ----------

file.rdd.getNumPartitions()

# COMMAND ----------

file = file.repartition(5)

file.rdd.getNumPartitions()

# COMMAND ----------

# df1 = spark.read.format("csv").option("header", "true").load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/IPL_Matches_2008_2020-2.csv")

# df1.display()

from pyspark.sql.functions import spark_partition_id, asc, desc
file.withColumn("partitionId", spark_partition_id()) \
    .groupBy("partitionId")\
    .count()\
    .orderBy(asc("count"))\
    .show()
# file.withColumn("partitionId", spark_partition_id()).filter('partitionId=0').display()

# COMMAND ----------

file.write.json('dbfs:/FileStore/June_batch/08282024/contact_info/cf3', mode='overwrite')

# COMMAND ----------

spark.read.parquet("dbfs:/FileStore/June_batch/08282024/contact_info/cf3").display()

# COMMAND ----------



# COMMAND ----------

import datetime
import json
import os
import sys
import pandas as pd
from pyspark.sql.functions import explode_outer, concat, col, \
    trim,to_date, lpad, lit, count,max, min, explode, current_timestamp
from pyspark.sql import SparkSession
import getpass

# Fetch system user's login name
system_user = getpass.getuser()

batch_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")


# Load from File to DB raw table

file_path = 'dbfs:/FileStore/June_batch/Contact_info.csv'

file = spark.read.csv(file_path, header=True, inferSchema=True)

file = file.filter(file.Identifier.isNotNull())

file= file.withColumn('batch_date', lit(batch_id))\
    .withColumn('create_date', current_timestamp())\
    .withColumn('update_date', current_timestamp())\
    .withColumn('create_user',lit(system_user))\
    .withColumn('update_user',lit(system_user))

file.show()

url = 'jdbc:snowflake://epizybn-qo01792.snowflakecomputing.com/?user=KSREENIVASULU443&password=Dharmavaram1@&warehouse=COMPUTE_WH&db=SAMPLEDB&schema=CONTACT_INFO'

file.write.mode("overwrite") \
    .format("jdbc") \
    .option("driver", "net.snowflake.client.jdbc.SnowflakeDriver") \
    .option("url", url) \
    .option("dbtable", "SAMPLEDB.CONTACT_INFO.CONTACT_INFO_RAW") \
    .save()


file.createOrReplaceTempView("file")

contact_info_bronze = spark.sql(
    """ select
    cast(Identifier as decimal(10)) Identifier,
    upper(Surname) Surname,
    upper(given_name) given_name,
    middle_initial,
    suffix,
    Primary_street_number,
    primary_street_name,
    upper(city) city,
    state,
    zipcode,
    Primary_street_number_prev,
    primary_street_name_prev,
    city_prev,
    state_prev,
    zipcode_prev,
    Email
    from file
    """
 )

contact_info_bronze= contact_info_bronze.withColumn('batch_date', lit(batch_id))\
    .withColumn('create_date', current_timestamp())\
    .withColumn('update_date', current_timestamp())\
    .withColumn('create_user',lit(system_user))\
    .withColumn('update_user',lit(system_user))


contact_info_bronze.write.mode("overwrite") \
    .format("jdbc") \
    .option("driver", "net.snowflake.client.jdbc.SnowflakeDriver") \
    .option("url", url) \
    .option("dbtable", "SAMPLEDB.CONTACT_INFO.CONTACT_INFO_BRONZE") \
    .save()


# contact_info_bronze.createOrReplaceTempView("contact_info_bronze")

# contact_info_silver= spark.sql(
#         """
#         select
#         Identifier,
#         Surname,
#         given_name,
#         middle_initial,
#         Primary_street_number,
#         primary_street_name,
#         city,
#         state,
#         zipcode,
#         Email,
#         Phone,
#         birthmonth,
#         'Y' as Current_ind
#         from contact_info_bronze
#         union
#         select
#         Identifier,
#         Surname,
#         given_name,
#         middle_initial,
#         Primary_street_number_prev,
#         primary_street_name_prev,
#         city_prev,
#         state_prev,
#         zipcode_prev,
#         Email,
#         Phone,
#         birthmonth,
#         'N' as Current_ind
#         from contact_info_bronze
#         """)

# contact_info_silver=contact_info_silver.withColumn('batch_date', lit(batch_id))\
#     .withColumn('create_date', current_timestamp())\
#     .withColumn('update_date', current_timestamp())\
#     .withColumn('create_user',lit(system_user))\
#     .withColumn('update_user',lit(system_user))



# contact_info_silver.write.mode("overwrite") \
#     .format("jdbc") \
#     .option("driver", "net.snowflake.client.jdbc.SnowflakeDriver") \
#     .option("url", url) \
#     .option("dbtable", "SAMPLEDB.CONTACT_INFO.CONTACT_INFO_SILVER") \
#     .save()



# COMMAND ----------

import os
import sys
import pandas as pd
from pyspark.sql.functions import explode_outer, concat, col, \
    trim,to_date, lpad, lit, count,max, min, explode, current_timestamp
from pyspark.sql import SparkSession
import getpass

# Fetch system user's login name
system_user = getpass.getuser()

batch_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")


# Load from File to DB raw table

file_path = 'dbfs:/FileStore/June_batch/'

file = spark.read.csv(file_path, header=True, inferSchema=True)
file = file.filter(file.Identifier.isNotNull())

source= file.withColumn('batch_date', lit(batch_id))\
    .withColumn('create_date', current_timestamp())\
    .withColumn('update_date', current_timestamp())\
    .withColumn('create_user',lit(system_user))\
    .withColumn('update_user',lit(system_user))

source.display()

# COMMAND ----------

target = spark.read \
    .format("jdbc") \
    .option("driver", "net.snowflake.client.jdbc.SnowflakeDriver") \
    .option("url",url) \
    .option("query", 'select * from CONTACT_INFO_RAW')     \
    .load()

# COMMAND ----------

source.drop('create_date','update_date','create_user','update_user','batch_date').exceptAll(target.drop('create_date','update_date','create_user','update_user','batch_date')).display()

# COMMAND ----------

spark.read.csv("dbfs:/FileStore/June_batch/multiple_files/*.csv", header=True).display()

# COMMAND ----------

spark.read.json("dbfs:/FileStore/June_batch/multiple_files/*.json", multiLine=True).display()

# COMMAND ----------

csv - profile- vendor(10)
json - profile - vendor2(10)

df.select(8 cols).write().
