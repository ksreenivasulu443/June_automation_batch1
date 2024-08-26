# Databricks notebook source
from pyspark.sql.functions import lpad,rpad, lead, lag

emp = [(1, "Smith", -1, "2018", "10", "M", 3000), \
       (2, "Rose", 1, "2010", "20", "M", 4000), \
       (3, "Williams", 1, "2010", "30", "M", 1000), \
       (4, "Jones", 10, "2005", "10", "F", 2000), \
       (5, "Brown", 2, "2010", "40", "", 1000), \
       (6, "Brown", 2, "2010", "50", "", 500) \
       ]
empColumns = ["eno", "ename", "mgr_id", "year_joined", \
              "dept_id", "gender", "salary"]

emp = spark.createDataFrame(data=emp, schema=empColumns)
emp.printSchema()
emp.show(truncate=False)

dept = [("Finance", 10,'NY'), \
        ("Marketing", 20,"CA"), \
        ("Sales", 30,'NJ'), \
        ("IT", 40,'CA'),
        ("HR", 60,'NJ') \
        ]
deptColumns = ["dept_name", "dept_id","loc"]
dept = spark.createDataFrame(data=dept, schema=deptColumns)
dept.printSchema()
dept.show(truncate=False)



# COMMAND ----------

emp.createOrReplaceTempView('emp')
dept.createOrReplaceTempView('dept')
print("using spark sql code")
spark.sql(""" select emp.*, dept.* from emp inner join dept on emp.dept_id=dept.dept_id """).show()
print("using dataframe join")
emp.join(dept, on= emp.dept_id==dept.dept_id, how='inner').show()

# COMMAND ----------

# MAGIC %scala
# MAGIC // Assuming you have a SparkSession named 'spark'
# MAGIC
# MAGIC // Register DataFrames as temporary views
# MAGIC emp.createOrReplaceTempView("emp")
# MAGIC dept.createOrReplaceTempView("dept")
# MAGIC
# MAGIC // Using Spark SQL
# MAGIC println("using spark sql code")
# MAGIC spark.sql("SELECT emp.*, dept.* FROM emp INNER JOIN dept ON emp.dept_id = dept.dept_id").show()
# MAGIC
# MAGIC // Using DataFrame join
# MAGIC println("using dataframe join")
# MAGIC emp.join(dept, emp("dept_id") === dept("dept_id"), "inner").show()

# COMMAND ----------

print("left join using spark sql code")
spark.sql(""" select emp.*, dept.* from emp left join dept on emp.dept_id=dept.dept_id """).show()
print(" left join using dataframe join API/function/method")
emp.join(dept, on= emp.dept_id==dept.dept_id, how='left').show()

# COMMAND ----------

print("right join using spark sql code")
spark.sql(""" select emp.*, dept.* from emp right join dept on emp.dept_id=dept.dept_id """).show()
print(" right join using dataframe join API/function/method")
emp.join(dept, on= emp.dept_id==dept.dept_id, how='right').show()

# COMMAND ----------

print("full join using spark sql code")
spark.sql(""" select emp.*, dept.* from emp full join dept on emp.dept_id=dept.dept_id """).show()
print(" full join using dataframe join API/function/method")
emp.join(dept, on= emp.dept_id==dept.dept_id, how='full').show()

# COMMAND ----------

print("cross join using spark sql code")
spark.sql(""" select emp.*, dept.* from emp cross join dept """).show()
print(" cross join using dataframe join API/function/method")
emp.join(dept, how='cross').display()

# COMMAND ----------

spark.sql(""" select emp.* from emp inner  join dept on emp.dept_id=dept.dept_id """).show()
print("left semi join using spark sql code")
spark.sql(""" select * from emp left semi join dept on emp.dept_id=dept.dept_id """).show()
print(" left join using dataframe join API/function/method")
emp.join(dept, on= emp.dept_id==dept.dept_id, how='left_semi').show()

# COMMAND ----------

spark.sql(""" select emp.* from emp left join dept on emp.dept_id=dept.dept_id where dept.dept_id is null """).show()
spark.sql(""" select * from emp left anti join dept on emp.dept_id=dept.dept_id """).show()
emp.join(dept,on = 'dept_id', how='left_anti' ).join('df3', on=emp.dept_id==df3.dept_id, how='left').show()

# COMMAND ----------

from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("PySparkJoinExample").getOrCreate()

# Sample data for df1
data1 = [("1", "Alice"), ("2", "Bob"), ("3", "Charlie")]
columns1 = ["id", "name"]

# Sample data for df2
data2 = [("1", "NYC"), ("2", "LA"), ("4", "Chicago")]
columns2 = ["id", "city"]

# Sample data for df3
data3 = [("1", "23"), ("2", "30"), ("3", "28")]
columns3 = ["id", "age"]

# Create DataFrames
df1 = spark.createDataFrame(data1, columns1)
df2 = spark.createDataFrame(data2, columns2)
df3 = spark.createDataFrame(data3, columns3)

# Perform join
# First, join df1 and df2, then join the result with df3
joined_df = df1.join(df2, on="id", how="inner").join(df3, on="id", how="inner")

# Show the result
joined_df.show()


# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select eno, ename, mgr_id, year_joined, dept_id, gender, salary, dept_name from emp inner join dept on emp.dept_id = dept.dept_id

# COMMAND ----------

# join_df = emp.join(dept, emp.dept_id == dept.dept_id , how='inner').\
#         drop(dept.loc, dept.dept_id, emp.mgr_id)

# join_df.display()
emp1 = emp.select('ename','salary','dept_id')
dept1 = dept.select('dept_id', 'loc')
emp1.join(dept1, 'dept_id', 'inner').display()


emp.select('ename','salary','dept_id').join(dept.select('dept_id', 'loc'),'dept_id', 'inner').display()

# COMMAND ----------

emp.join(dept, ['dept_id'], 'inner').show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Left join

# COMMAND ----------

emp.join(dept, emp.dept_id == dept.dept_id, 'left').show()

emp.join(dept, 'dept_id', 'left').show()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## right join

# COMMAND ----------

# emp.join(dept, emp.dept_id == dept.dept_id, 'right').show()
from pyspark.sql.functions import col
emp.alias('emp').join(emp.alias('emp2'), col('emp.eno') == col('emp2.mgr_id'), how= 'inner').display()




# empDF.alias("emp1").join(empDF.alias("emp2"), \
#     col("emp1.superior_emp_id") == col("emp2.emp_id"),"inner") \
#     .select(col("emp1.emp_id"),col("emp1.name"), \
#       col("emp2.emp_id").alias("superior_emp_id"), \
#       col("emp2.name").alias("superior_emp_name")) \
#    .show(truncate=False)

# COMMAND ----------

emp.join(other = dept, on = emp.dept_id == dept.dept_id, how='fullouter').show()


# COMMAND ----------

emp.createOrReplaceTempView('emp')
dept.createOrReplaceTempView('dept')

# COMMAND ----------

spark.sql("select * from emp where dept_id in ( select dept_id from dept)").display()

# COMMAND ----------



emp.join(dept, emp.dept_id == dept.dept_id, 'inner').show() 

emp.join(dept, emp.dept_id == dept.dept_id, 'leftsemi').show() 



# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC

# COMMAND ----------

emp.show()
dept.show()

# COMMAND ----------

emp.join(dept, emp.dept_id == dept.dept_id, 'left_anti').show()

spark.sql("""select emp.* from emp  left join dept  on emp.dept_id=dept.dept_id where dept.dept_id is null""").show()

emp.join(dept, emp.dept_id == dept.dept_id, 'left').show() 

# COMMAND ----------

from pyspark.sql.functions import broadcast

emp.join(broadcast(dept), emp.dept_id == dept.dept_id, how='left').show()

# COMMAND ----------

emp.join(dept, emp.dept_id == dept.dept_id, how='left').show()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Set oprators

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## union

# COMMAND ----------


