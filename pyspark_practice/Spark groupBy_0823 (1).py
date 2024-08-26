# Databricks notebook source

from pyspark.sql.functions import sum, avg, min, max, count, round,ceil, floor

simpleData = [("James", "Sales", "NY", 90000, 34, 10000),
              ("James", "Sales", "NY", 86000, 56, 20000),
              ("Robert", "Sales", "CA", 81000, 30, 23000),
              ("Maria", "Finance", "CA", 90000, 24, 23000),
              ("Raman", "Finance", "CA", 99000, 40, 24000),
              ("Scott", "Finance", "NY", 83000, 36, 19000),
              ("Jen", "Finance", "NY", 79000, 53, 15000),
              ("Jeff", "Marketing", "CA", 80000, 25, 18000),
              ("sreenivasulu kattubadi Sreenivasulu", "Marketing", "NY", 91000, 50, 21000)
              ]

schema = ["employee_name", "department", "state", "salary", "age", "bonus"]
df = spark.createDataFrame(data=simpleData, schema=schema)
df.printSchema()
df.show(truncate=6)

# COMMAND ----------

df.show(n=3, truncate=True, vertical=True)

# COMMAND ----------

summary = df.summary()
summary.display()

# COMMAND ----------

df.select(sum('salary').alias('sum_sal'), avg('age'), min('salary'), max('salary'), count('employee_name')).show()

# COMMAND ----------

df.createOrReplaceTempView('source')
print("group by using spark sql")
spark.sql(""" select department,state , count(1) as count from source group by department,state having count(1)>1""").show()
print("group by using spark groupBy API")
df.groupBy('department', 'state').count().filter('count>1').show()
df.groupBy('department').sum('salary').show()
df.groupBy('department').min('salary').show()

# COMMAND ----------

df.createOrReplaceTempView('source')
print("group by using spark sql")
spark.sql(""" select department, count(1), avg(salary), sum(salary), sum(bonus)  from source group by department """).show()
print("group by using spark groupBy API")
df_agg_out = df.groupBy('department').agg(count('employee_name').alias('num_employee'),
                             sum('salary').alias('sum_salary'), 
                             round(avg('salary')).alias('avg_salary'), 
                             sum('bonus').alias('sum_bonus'), 
                             floor(avg('bonus')).alias('avg_bonus'))

# COMMAND ----------

df_agg_out.show()

# COMMAND ----------

df_agg_out.createOrReplaceTempView('source')

spark.sql(""" select a.*,'USA' as country from source a  """).show()

# COMMAND ----------

from pyspark.sql.functions import lit, concat
df_agg_out = df_agg_out.withColumn('concat_out', concat('department','num_employee'))

df_agg_out.show()

# COMMAND ----------

from pyspark.sql import SparkSession
 
from pyspark.sql.functions import col,upper, lower, length, concat, initcap, explode, substring, instr,concat_ws, expr,lit
 
data = [("Rahul","Smith","USA","C"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL"),
    ("Robert","Williams","USA","K"),
    ("Maria","Jones","USA","FL")
  ]
columns = ["firstname","lastname","country","state_name"]
df = spark.createDataFrame(data = data, schema = columns)
df.show()

# COMMAND ----------

300  columns -- 5 cols have transformation remaining 295 straight load

spark.sql("""select c1, 
          c2, 
          c3, 
          upper(c95), 
          ..c300 as name from table""")

df.select('c1', 'c2','c3', upper(c95))


# COMMAND ----------

df.withColumn('c95', upper('c95')).withColumnRenamed('c300', 'name')

# COMMAND ----------

df_out = df.withColumn('full_name', concat_ws(' ', 'firstname', 'lastname')).\
    withColumn('country_new', substring('country',1,2)).\
    withColumn('zip_code',lit(10011))

df_out.show()

# COMMAND ----------

df_out.withColumnRenamed('country', 'country_code').show()

# COMMAND ----------

df_out = df.withColumn('full_name',concat_ws('','firstname','lastname')).\
   withColumn('country',substring('country',1,2)).\
   withColumn('zip_code',lit(10011))
 
df_out.show()

# COMMAND ----------



# COMMAND ----------

summary = df.summary()
summary.show()

# COMMAND ----------

df.select(sum('salary').alias("sum_sal"), avg('age')).show()

df.groupBy('department').sum('salary').show()

df.groupBy('department','state').sum('salary').show()

df.groupBy('department').agg(sum('salary').alias('sum_salary'),
                             avg('salary').alias('avg_salary'),
                             avg('age').alias("avg_age")).show()

# COMMAND ----------



# COMMAND ----------


from pyspark.sql.functions import sum, avg, min, max, count, round,ceil, floor,substring,instr,col

simpleData = [("James1@gmail.com", "Sales", "NY", 90000, 34, 10000),
              ("James@gmail.com", "Sales", "NY", 86000, 56, 20000),
              ("Robert@gmail.com", "Sales", "CA", 81000, 30, 23000),
              ("Maria@gmail.com", "Finance", "CA", 90000, 24, 23000),
              ("Raman@gmail.com", "Finance", "CA", 99000, 40, 24000),
              ("Scott@gmail.com", "Finance", "NY", 83000, 36, 19000),
              ("Jen@gmail.com", "Finance", "NY", 79000, 53, 15000),
              ("Jeff@gmail.com", "Marketing", "CA", 80000, 25, 18000),
              ("123@yahoo.in", "Marketing", "NY", 91000, 50, 21000)
              ]

schema = ["employee_name", "department", "state", "salary", "age", "bonus"]
df = spark.createDataFrame(data=simpleData, schema=schema)
df.printSchema()
df.show(truncate=False)

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

df.select(expr("substring(employee_name, 1, instr(employee_name, '@') - 1)").alias("username")).show()

# COMMAND ----------



# COMMAND ----------


summary2 = df.summary()
summary2.display()
summary2.select('summary', 'state', 'salary', 'bonus').where("summary in ('count','max','min') ").display()

# COMMAND ----------

df.createOrReplaceTempView("source")
spark.sql( """
select 'salary' column ,sum(salary) as sum_salry, min(salary) min_salary, max(salary) max_salary, count(1) cnt, round(avg(salary),2) avg_salary from source  """).display()


# COMMAND ----------

from pyspark.sql.functions import lit

# COMMAND ----------

df10= df.select(lit("salry").alias("column"),sum('salary').alias("sum_sal"), \
          count("*").alias("num_of_records"), \
          avg('salary').alias("average_sal"), \
          min('salary').alias("min_sal"), \
          max('salary').alias("max_sal"))


df10.display()


# COMMAND ----------


spark.sql("""select department, sum(salary), avg(salary), min(salary) from source group by department""").show()

# COMMAND ----------

df.groupBy('department','state').sum('salary').count().max()
# df.groupBy('department').min().show()
# df.groupBy('department').max().show()

# df.groupBy('department').avg().show()

df.groupBy('department').count().show()



# COMMAND ----------

spark.sql("""
select department, state, sum(salary) from source group by all""").display()

# COMMAND ----------

df.groupBy("department", "state").sum('bonus').show()

# COMMAND ----------

spark.sql("select employee_name , count(1) from source group by all having count(1)>1").show()

# COMMAND ----------

df.groupBy("employee_name").count().where('count>1').show()

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select department, sum(salary), round(avg(salary)), min(salary), sum(bonus), min(salary), count(1) from source group by department

# COMMAND ----------

from pyspark.sql.functions import ceil, floor

df.groupBy("department") \
    .agg(sum("salary").alias("sum_salary"),
         avg("salary").alias("avg_salary"), \
         round(avg("salary")).alias("avg_salary"), \
         sum("bonus").alias("sum_bonus"), \
         max("bonus").alias("max_bonus"), \
         min("salary").alias("min_sal"), \
         count('department').alias('num_emp')
         ) \
    .show(truncate=False)

df.groupBy('department','state').sum('salary').min('salary')
# # df.groupBy('department').min().show()
# # df.groupBy('department').max().show()

# # df.groupBy('department').avg().show()

# df.groupBy('department').count().show()

spark.sql( """ select department, sum(salary), max(salary),min(salary), avg(salary) sum(bonus), avg(bonus) from source group by all """).show()

# COMMAND ----------


