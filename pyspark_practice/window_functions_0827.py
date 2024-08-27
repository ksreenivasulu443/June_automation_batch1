# Databricks notebook source
from pyspark.sql.window import Window
from pyspark.sql.functions import *
simpleData = (("James", "Sales", 3000), \
              ("Michael", "Sales", 4600), \
              ("Robert", "Sales", 4100), \
              ("Maria", "Finance", 3000), \
              ("James", "Sales", 3000), \
              ("Scott", "Finance", 3300), \
              ("Jen", "Finance", 3900), \
              ("Jeff", "Marketing", 3000), \
              ("Kumar", "Marketing", 2000), \
              ("Saif", "Sales", 4100) \
              )

columns = ["employee_name", "department", "salary"]
df = spark.createDataFrame(data=simpleData, schema=columns)
df.printSchema()
df.show(truncate=False)

# COMMAND ----------

df.createOrReplaceTempView('source')

spark.sql(""" select * from source order by department asc, salary desc""").show()

# COMMAND ----------

df.orderBy( col('department').asc(), col('salary').desc()).show()

df.sort(col('department').asc(), col('salary').desc()).show()


# COMMAND ----------

spark.sql(""" select a.*, dense_rank() over (order by salary desc) dr from source a""").show()
spark.sql(""" select a.*, rank() over (order by salary desc) r from source a """).show()
spark.sql(""" select a.*, row_number() over (order by salary desc) rn from source a""").show()

# COMMAND ----------

a = Window.orderBy(col('salary').desc())

df.withColumn('dr', dense_rank().over(a)).show()
df.withColumn('r', rank().over(a)).show()
df.withColumn('rn', row_number().over(a)).show()

# COMMAND ----------

spark.sql(""" select a.*, dense_rank() over (partition by department order by salary desc) dr from source a""").show()
spark.sql(""" select a.*, rank() over (partition by department order by salary desc) r from source a """).show()
spark.sql(""" select a.*, row_number() over (partition by department order by salary desc) rn from source a""").show()

# COMMAND ----------

a = Window.partitionBy(col('department')).orderBy(col('salary').desc())
df.withColumn('dr', dense_rank().over(a)).show()
df.withColumn('r', rank().over(a)).show()
df.withColumn('rn', row_number().over(a)).show()

# COMMAND ----------

df.withColumn('r', expr("rank() over (order by salary desc)")).show()

df.withColumn('case_op', expr("""case when department='Sales' then 'S' when department='Finance' then 'F' else department end """)).show()

# COMMAND ----------

data = [
    ("2024-08-01", 100),
    ("2024-08-01", 50),
    ("2024-08-02", 200),
    ("2024-08-02", 100),
    ("2024-08-03", 150),
    ("2024-08-04", 300),
    ("2024-08-05", 250),
    ("2024-08-05", 100)
]

# Create DataFrame
columns = ["txn_date", "sales"]
df = spark.createDataFrame(data, columns)

df.show()

# COMMAND ----------

df.groupBy('txn_date').sum('sales').alias('sales').withColumn('cumm_sum', sum(col('sum(sales)')).over(Window.orderBy(col('txn_date')))).show()

# COMMAND ----------



# COMMAND ----------

df.withColumn('cumm_sum', sum(col('sales')).over(Window.partitionBy(col('txn_date')).orderBy(col('txn_date')))).show()

# COMMAND ----------



# COMMAND ----------

df.withColumn('rank', rank().over(window)).show()
df.withColumn('rank', dense_rank().over(window)).show()
df.withColumn('rank', row_number().over(window)).show()

# COMMAND ----------

window2 = Window.partitionBy(col('department')).orderBy(col('salary').desc())

df.withColumn('rank', rank().over(window2)).show()

# COMMAND ----------


