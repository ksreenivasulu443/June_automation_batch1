# Databricks notebook source
df = spark.read.json("dbfs:/FileStore/June_batch/sample1.json", multiLine=True) # multiline = False

df.display()

# COMMAND ----------

df2 = spark.read.json("dbfs:/FileStore/June_batch/singleline.json")

df2.display()

# COMMAND ----------

#df1 = spark.read.format("json").load("dbfs:/FileStore/June_batch/singleline-1.json")

df1 = spark.read.json("dbfs:/FileStore/June_batch/singleline-1.json") # multiline=False

df1.display()

# COMMAND ----------

df2 = spark.read.json("dbfs:/FileStore/June_batch/Complex.json", multiLine=True)

df2.display()

df2.printSchema()

# COMMAND ----------

df5 = df2.select("address.city", "address.state", "address.streetAddress","age","firstname",'gender',"lastname")

# df5.display()

# df5.printSchema()

# COMMAND ----------

# explode is pyspark function convert array type data to multiple row , explode_outer will consider to null/blank and convert as new row
# [1,2,,4]-->  1
#             2
#             null/blank
#             3
from pyspark.sql.functions import explode, explode_outer
df2 = spark.read.json("dbfs:/FileStore/June_batch/Complex.json", multiLine=True)
df7 = df2.select("*",explode("phoneNumbers").alias("phone_number")).drop('phoneNumbers')

df7.display()

df7.printSchema()

df7.select("address.city", "address.state", "address.streetAddress","age","firstname",
           'gender',"lastname","phone_number.number","phone_number.type").display()

# COMMAND ----------



from pyspark.sql.functions import explode, explode_outer, upper,lower, instr, lead,lag, substring, length,col
df2 = spark.read.json("dbfs:/FileStore/June_batch/Complex.json", multiLine=True)
from pyspark.sql.types import *
def flatten(df):
    # compute Complex Fields (Lists and Structs) in Schema
    complex_fields = dict([(field.name, field.dataType)
                           for field in df.schema.fields
                           if type(field.dataType) == ArrayType or type(field.dataType) == StructType])
    while len(complex_fields) != 0:
        col_name = list(complex_fields.keys())[0]
        print("Processing :" + col_name + " Type : " + str(type(complex_fields[col_name])))

        # if StructType then convert all sub element to columns.
        # i.e. flatten structs
        if type(complex_fields[col_name]) == StructType:
            expanded = [col(col_name + '.' + k).alias(col_name + '_' + k) for k in
                        [n.name for n in complex_fields[col_name]]]
            df = df.select("*", *expanded).drop(col_name)

        # if ArrayType then add the Array Elements as Rows using the explode function
        # i.e. explode Arrays
        elif type(complex_fields[col_name]) == ArrayType:
            df = df.withColumn(col_name, explode_outer(col_name))

        # recompute remaining Complex Fields in Schema
        complex_fields = dict([(field.name, field.dataType)
                               for field in df.schema.fields
                               if type(field.dataType) == ArrayType or type(field.dataType) == StructType])
    return df


# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

df4 = spark.read.json("dbfs:/FileStore/June_batch/Complex2.json", multiLine=True)

df4.display()

df4.printSchema()

# COMMAND ----------


