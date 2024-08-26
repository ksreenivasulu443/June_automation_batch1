from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.csv(r"C:\Users\A4952\PycharmProjects\June_automation_batch1\files\IPL Matches 2008-2020.csv", header=True, inferSchema=True)
df.createGlobalTempView('ipldata') # CreateTempView will not allow you create view with same name if already exist

#df.createOrReplaceTempView('ipldata') # CreateOr ReplaceTempView will replace view if already exist or if not exist create new view

#df2 = spark.sql(" select * from ipldata where city='Bangalore' ")

#df2.show()

df.createTempView("ipldata1")

spark.sql("select * from ipldata1").show()