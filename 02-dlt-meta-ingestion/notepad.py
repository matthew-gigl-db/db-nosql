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
