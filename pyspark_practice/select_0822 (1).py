# Databricks notebook source
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

df.createOrReplaceTempView("source")
spark.sql("select  firstname, state_name from source").show()

# COMMAND ----------

df.select(df.firstname, df.state_name).show()


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
columns = ["first name","last name","country","state name"]
df2 = spark.createDataFrame(data = data, schema = columns)
df2.show()

# COMMAND ----------

df2.createOrReplaceTempView('source2')

#spark.sql("""select first name,last name from source2 """).show()
# df2.select(df2.first name, df2.last name).show()
print(" with square brackets")
df2.select(df2['first name'], df2['last name']).show()
print(" with col")
df2.select(col('first name'), col('last name')).show()
print(" in single quotes")
df2.select("first name", "last name").show()
print("all columns")
df2.select("*").show()

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

df.select(df.colRegex("`.*stn.*`")).show() # *= %, .=_ is sql like search (' back tick is mandatory)


# COMMAND ----------

spark.sql("select upper(firstname)  firstname from source").show()

# COMMAND ----------

df.select(upper('firstname').alias('firstname'), lower('lastname').alias('lastname'), 'state_name', length('country').alias('country_length'), concat_ws('-', 'firstname', 'lastname', 'state_name').alias("fullname"), substring('state_name',1,1).alias('state_name_with_1_char'), instr(upper('firstname'),'R').alias("instr_first")).show()

# kastsreen100@gmail.com, katsreen100, gmail, com

df.show()

# COMMAND ----------

df.show()

# COMMAND ----------

df5 = df.select('firstname', 'lastname').where(" firstname = 'Rahul' or lastname='Rose' ")

df.where(" firstname = 'Rahul' or lastname='Rose' ").select('firstname', 'lastname').show()

df.where(" firstname = 'Rahul' or lastname='Rose' ").show()

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

df3 = df.select(df.firstname, df.lastname)

df3.show()

type(df3)


# COMMAND ----------

df.select(col('firstname'), col('lastname')).show(2)


# COMMAND ----------

df.select(df['firstname'], df['lastname'], df['country'], df['state_name']).show(2)


# COMMAND ----------

df5 = df.select(upper('firstname').alias('fn'), lower('lastname').alias('ln'), 'state_name',length('state_name').alias("state_name_length"))
df5.show()

df5.createOrReplaceTempView("df5")

spark.sql("select * from df5")

# COMMAND ----------

df.createOrReplaceTempView('source')

# COMMAND ----------

spark.sql("select upper(firstname) fn, lower(lastname) ln , state_name, length(state_name) state_name_length from source").show()


df = spark.sql("select upper(firstname) fn, lower(lastname) ln , state_name, length(state_name) state_name_length, 'US' as country_code from source")
df.show()
# id(df)

139776549024240
139776549024240

# COMMAND ----------

df.show()

# COMMAND ----------

df.select(df.colRegex("`.*name*`")).show()


# COMMAND ----------

df.select('*', lit('USA').alias("country_code")).show(2)


# COMMAND ----------

# df.select('firstname','lastname').where(" firstname = 'Rahul'  ").show()

# df.select('firstname','lastname').filter(" firstname = 'Rahul' ").show()

df.show()


# COMMAND ----------

df.where("('first name' = 'Rahul' or lastname ='Rose') and state_name='NY'  ").show()

df.select("*").filter( ((df['first name'] == 'Rahul') | (df.lastname== 'Rose' )) & ( df.state_name=='NY')).show()

# COMMAND ----------


