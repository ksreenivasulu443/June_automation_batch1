# Import SparkSession
from pyspark.sql import SparkSession #( Library )

# Create SparkSession
spark = SparkSession.builder \
      .getOrCreate()

#master - number of parallel thread
#App name - Application for your module file/script file
#getOrCreate - gets existing spark session if not present  creates new session
dataList = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]
df=spark.createDataFrame(dataList, schema=['Language','fee'])

df.show()

df.printSchema()
# df.display()


