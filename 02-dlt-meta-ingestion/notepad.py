# Databricks notebook source
filenames = spark.sql(f"select * from mgiglia.synthea.temp_landed_bronze_files").collect()

# COMMAND ----------

distinct_values = df.select("column_name").distinct().collect()
distinct_list = [row.column_name for row in distinct_values]

# COMMAND ----------

filenames_list = [row.inputFileName for row in filenames]
filenames_list

# COMMAND ----------

for row in filenames.iterrows():
  filename = row.inputFileName
  print(filename)

# COMMAND ----------

type(filenames)

# COMMAND ----------

filenames

# COMMAND ----------

# MAGIC %sql
# MAGIC use catalog mgiglia;
# MAGIC use schema synthea;

# COMMAND ----------

allergies_df = spark.table("allergies_csv_bronze")
display(allergies_df)

# COMMAND ----------

import pyspark.sql.functions as F
from pyspark.sql.types import StringType

# COMMAND ----------

help(F.from_csv)

# COMMAND ----------

# MAGIC %sql
# MAGIC with example as (
# MAGIC   select
# MAGIC     value
# MAGIC   from 
# MAGIC     allergies_csv_bronze limit 1
# MAGIC )
# MAGIC SELECT schema_of_csv(value) from example

# COMMAND ----------

csv_data = allergies_df.select(col("value")).head(1)
csv_data_list = [row.value for row in csv_data][0]
csv_data_list

# COMMAND ----------

schema = spark.sql(f"""describe select schema_of_csv({csv_data_list})""")

# COMMAND ----------

allergies_sdf = (
  allergies_df
  .withColumn("value_string", col("value").cast(StringType()))
  .withColumn("data", from_csv(col("value_string"), schema=schema_of_csv(allergies_df.select(col("value"))), options = {"inferSchema":"true", "header":"true"}))
)

# COMMAND ----------

import dlt
