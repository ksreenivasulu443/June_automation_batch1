# Databricks notebook source
simpleData = [(1, "James", "Sales", "NY", 90000), \
              (2, "Michael", "Sales", "NY", 86000), \
              (3, "Robert", "Sales", "CA", 81000), \
              (4, "Maria", "Finance", "CA", 90000), \
              (1, "James", "Sales", "NY", 90000)
              ]

columns = ["emp_id", "employee_name", "department", "state", "salary"]
df1 = spark.createDataFrame(data=simpleData, schema=columns)
# df1.printSchema()
df1.show(truncate=False)


simpleData2 = [(1, "James", "Sales", "NY", 90000), \
                (1, "James", "Sales", "NY", 90000), \
               (2, "Michael", "Sales", "NY", 86000), \
                (2, "Michael", "Sales", "NY", 86000),\
               (5, "Sonja", "Sales", "OH", 45000), \
               (6, "Randy H", "Finance", "NJ", 40000)
               ]

columns = ["emp_id", "employee_name", "department", "state", "salary"]
df2 = spark.createDataFrame(data=simpleData2, schema=columns)
# df2.printSchema()
df2.show(truncate=False)

# COMMAND ----------

df1.createOrReplaceTempView('source')
df2.createOrReplaceTempView('target')

# COMMAND ----------

spark.sql(" select * from source union select * from target ").show() # same numver of coumns, same order, data type?

# COMMAND ----------

df1.union(df2).show() # in pyspark we dont have union operation if we perform union we get union all operation o/p
df1.union(df2).distinct().show()

# COMMAND ----------

spark.sql(" select * from source union all select * from target ").show() # same numver of coumns, same order, data type?
df1.unionAll(df2).show()

# COMMAND ----------

print("intersect o/p")
spark.sql("select * from source intersect  select * from target").show()

print("intersectAll o/p")
spark.sql("select * from source intersect all select * from target").show()

# COMMAND ----------

df1.intersect(df2).show()

df1.intersectAll(df2).show()

# COMMAND ----------

spark.sql("select * from source except select * from target").show() # minus, except
df1.subtract(df2).show()
df2.subtract(df1).show()

# COMMAND ----------

df1.exceptAll(df2).show()

df2.exceptAll(df1).show()

# COMMAND ----------

df1 = spark.createDataFrame([
    (1, "Alice", 2000),
    (2, "Bob", 1500)
], ["id", "name", "salary"])

df2 = spark.createDataFrame([
    (3, 1800, "Charlie"),
    (4, 2500, "David")
], ["id", "bonus", "name"])

df1.show()
df1.printSchema()



df2 = df2.drop('bonus')

df2.show()
df2.printSchema()

# COMMAND ----------

df1.union(df2).show()

# COMMAND ----------

df1.select('id','name').union(df2.select('id','name')).show()

# COMMAND ----------

df1.unionByName(df2,allowMissingColumns=True).show()

# COMMAND ----------

df1.unionByName(df2,allowMissingColumns=True).show()

# COMMAND ----------

df1.distinct().show()

# COMMAND ----------

df1.show()

# COMMAND ----------

df1 = df1.drop('name','id')

df1.show()

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

unionDF = df1.union(df2)
unionDF.show(truncate=False)

unionDF_sql = df1.union(df2).distinct()

unionDF_sql.show()

# COMMAND ----------


unionAllDF = df1.unionAll(df2)
unionAllDF.show(truncate=False)

# COMMAND ----------

df1.intersect(df2).show()

# COMMAND ----------

df1.intersectAll(df2).show()

# COMMAND ----------

simpleData = [(1, "James", "Sales", "NY", 90000), \
              (2, "Michael", "Sales", "NY", 86000), \
              (3, "Robert", "Sales", "CA", 81000), \
              (4, "Maria", "Finance", "CA", 90000), \
              (1, "James", "Sales", "NY", 90000)
              ]

columns = ["emp_id", "employee_name", "department", "state", "salary"]
df1 = spark.createDataFrame(data=simpleData, schema=columns)
df1.show(truncate=False)


simpleData2 = [(1, "James", "Sales", "NY", 90000), \
               (2, "Michael", "Sales", "NY", 86000), \
               (5, "Sonja", "Sales", "OH", 45000), \
               (6, "Randy H", "Finance", "NJ", 40000), \
                   (1, "James", "Sales", "NY", 90000)
               ]

columns = ["emp_id", "employee_name", "department", "state", "salary"]
df2 = spark.createDataFrame(data=simpleData2, schema=columns)
df2.show(truncate=False)

# COMMAND ----------

df1.intersectAll(df2).show()

# COMMAND ----------

df1.intersect(df2).show()

# COMMAND ----------

df1.exceptAll(df2).show()

# COMMAND ----------

simpleData = [(1, "James", "Sales", "NY", 90000), \
              (2, "Michael", "Sales", "NY", 86000), \
              (3, "Robert", "Sales", "CA", 81000), \
              (4, "Maria", "Finance", "CA", 90000), \
              (1, "James", "Sales", "NY", 90000)
              ]

columns = ["emp_id", "employee_name", "department", "state", "salary"]
df1 = spark.createDataFrame(data=simpleData, schema=columns)
df1.show(truncate=False)


simpleData2 = [(1, "James", "Sales", "NY", 90000), \
               (2, "Michael", "Sales", "NY", 86000), \
               (5, "Sonja", "Sales", "OH", 45000), \
               (6, "Randy H", "Finance", "NJ", 40000)
               ]

columns = ["emp_id", "employee_name", "department", "state", "salary"]
df2 = spark.createDataFrame(data=simpleData2, schema=columns)
df2.show(truncate=False)

# COMMAND ----------

df1.exceptAll(df2).show()

# COMMAND ----------

df1.subtract(df2).show()

# COMMAND ----------

df1 = spark.createDataFrame([("a", 1), ("a", 1), ("a", 1), ("a", 2), ("b", 3), ("c", 4)], ["C1", "C2"])
df2 = spark.createDataFrame([("a", 1), ("b", 3), ("a", 1)], ["C1", "C2"])


# COMMAND ----------

df1.exceptAll(df2).show()

# COMMAND ----------

df1.subtract(df2).show()

# COMMAND ----------

df1 = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])

df1.show()

df2 = spark.createDataFrame([(1, "Alice"), (2, "Bob"),(1, "Alice")], ["id", "name"])

df2.show()

# COMMAND ----------

df1.union(df2).show()

# COMMAND ----------

df1.unionAll(df2).show()

# COMMAND ----------

df2.intersect(df1).show()

# COMMAND ----------

df2.intersectAll(df1).show()

# COMMAND ----------

df2.exceptAll(df1).show()

# COMMAND ----------

TN1 = spark.createDataFrame([(1,), (2,),(3,),(1,)], ["A"])

TN1.show()

TN2 = spark.createDataFrame([(1,), (2,),(3,),(2,),(1,)], ["A"])

TN2.show()

# COMMAND ----------

TN1.union(TN2).show()

# COMMAND ----------

TN1.union(TN2).distinct().show()

# COMMAND ----------

TN1.unionAll(TN2).show()

# COMMAND ----------

TN1.intersect(TN2).show()

# COMMAND ----------

TN1.intersectAll(TN2).show()

# COMMAND ----------

TN2.exceptAll(TN1).show()

TN2.subtract(TN1).show() # minus, except

# COMMAND ----------

TN1 = spark.createDataFrame([(1,), (2,),(3,),(1,),(5,),(5,)], ["A"])

TN1.show()

TN2 = spark.createDataFrame([(1,), (2,),(3,),(2,),(1,),(5,)], ["B"])

TN2.show()

# COMMAND ----------

TN1.exceptAll(TN2).show()

# COMMAND ----------

TN1.subtract(TN2).show()

# COMMAND ----------

df1 = spark.createDataFrame([
    (1, "Alice", 2000),
    (2, "Bob", 1500)
], ["id", "name", "salary"])

df2 = spark.createDataFrame([
    (3, 1800, "Charlie"),
    (4, 2500, "David")
], ["id", "sal", "name"])

# COMMAND ----------

df1.printSchema()

# COMMAND ----------

df1.select("id", "name", "salary").union(df2.select("id", "name", "salary")).show()

# COMMAND ----------



# COMMAND ----------

df1.unionByName(df2,allowMissingColumns=True).show()

# COMMAND ----------

df1.unionByName?

# COMMAND ----------

df1.union(df2).union(df3).union(df4)
