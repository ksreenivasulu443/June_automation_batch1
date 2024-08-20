from pyspark.sql import SparkSession
jar = r"C:\Users\A4952\PycharmProjects\June_automation_batch1\jars\ojdbc8-21.5.0.0.jar"
spark = SparkSession.builder.master("local[2]") \
    .appName("test") \
    .config("spark.jars", jar) \
    .config("spark.driver.extraClassPath", jar) \
    .config("spark.executor.extraClassPath", jar) \
    .getOrCreate()



df = spark.read \
        .format("jdbc") \
        .option("url", "jdbc:oracle:thin:@//localhost:1521/freepdb1") \
        .option("query", "select * from serial_num4") \
        .option("user", "scott") \
        .option("password", "tiger") \
        .option("driver",'oracle.jdbc.driver.OracleDriver')\
        .load()

df.show()
