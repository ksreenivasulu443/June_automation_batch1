from pyspark.sql import SparkSession
jar = r"C:\Users\A4952\PycharmProjects\June_automation_batch1\jars\postgresql-42.2.5.jar"
spark = SparkSession.builder.master("local[2]") \
    .appName("test") \
    .config("spark.jars", jar) \
    .config("spark.driver.extraClassPath", jar) \
    .config("spark.executor.extraClassPath", jar) \
    .getOrCreate()

df2 = spark.read.format("jdbc"). \
    option("url", "jdbc:postgresql://localhost:5432/postgres"). \
    option("user", "postgres"). \
    option("password", "Dharmavaram1@"). \
    option("query", "select * from contact_info_raw"). \
    option("driver", "org.postgresql.Driver").load()

df2.show()