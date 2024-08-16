from pyspark.sql import SparkSession
import json
from pyspark.sql.types import StructType
spark = SparkSession.builder.getOrCreate()


with open(r"C:\Users\A4952\PycharmProjects\June_automation_batch1\schema_files\contact_info_schema.json", 'r') as schema_file:
    schema = StructType.fromJson(json.load(schema_file))

print(schema)


df = spark.read.csv(r"C:\Users\A4952\PycharmProjects\June_automation_batch1\files\Contact_info.csv", header=True, schema=schema)
df.show()
df.display()
df.printSchema()