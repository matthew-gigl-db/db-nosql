# Databricks notebook source
# MAGIC %md 
# MAGIC # Synthea Data Generator 
# MAGIC ***
# MAGIC
# MAGIC Setup: 
# MAGIC
# MAGIC * A catalog, schema, and volumne setup with write permissions for the principal executing this notebook. 
# MAGIC * A cluster with Java JDK version 17 set as the default.
# MAGIC * The **synthea-with-dependencies.jar** available for the cluster to use. 
# MAGIC * A preconfigured Synthea configuration file.  
# MAGIC
# MAGIC All of these requirements can be set up using the notebooks found in the 00-setup-notebooks folder of this repo, or from the original on Github:  [https://github.com/matthew-gigl-db/db-nosql](https://github.com/matthew-gigl-db/db-nosql)
# MAGIC
# MAGIC ***

# COMMAND ----------

# DBTITLE 1,Import Python Modules
import subprocess

# COMMAND ----------

# DBTITLE 1,Retrieve Java Version
result = subprocess.run(["java", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
java_version = result.stdout + result.stderr
print(java_version)

# COMMAND ----------

# MAGIC %md 
# MAGIC Typical output using default cluster JDK: 
# MAGIC > openjdk version "1.8.0_392"  
# MAGIC > OpenJDK Runtime Environment (Zulu 8.74.0.17-CA-linux64) (build 1.8.0_392-b08)  
# MAGIC > OpenJDK 64-Bit Server VM (Zulu 8.74.0.17-CA-linux64) (build 25.392-b08, mixed mode)  
# MAGIC >  
# MAGIC
# MAGIC Output when the cluster JDK is set to version 17:  
# MAGIC > openjdk version "17.0.9" 2023-10-17 LTS  
# MAGIC > OpenJDK Runtime Environment Zulu17.46+19-CA (build 17.0.9+8-LTS)  
# MAGIC > OpenJDK 64-Bit Server VM Zulu17.46+19-CA (build 17.0.9+8-LTS, mixed mode, sharing)  
# MAGIC >  

# COMMAND ----------

# DBTITLE 1,Verify Version 17
if java_version.split('openjdk version "')[1].startswith("17"):
  print("Java Version is set correctly with version 17+")
else: 
  raise Exception("Error: Please ensure that java version 17 is set as the cluster default.  Please see https://docs.databricks.com/en/dev-tools/sdk-java.html#create-a-cluster-that-uses-jdk-17 for more information.")

# COMMAND ----------

# MAGIC %md
# MAGIC ***
# MAGIC ### Set Catalog, Schema, and Volume Paths 

# COMMAND ----------

# DBTITLE 1,set catalog and schema widgets
dbutils.widgets.text(name = "catalog_name", defaultValue="", label="Catalog Name")
dbutils.widgets.text(name = "schema_name", defaultValue="synthea", label="Schema Name")

# COMMAND ----------

# DBTITLE 1,get widget values and set volume path
catalog_name = dbutils.widgets.get(name = "catalog_name")
schema_name = dbutils.widgets.get(name = "schema_name")
volume_path = f"/Volumes/{catalog_name}/{schema_name}/synthetic_files_raw/"
print(f"""
  catalog_name = {catalog_name}
  schema_name = {schema_name}
  volume_path = {volume_path}
""")

# COMMAND ----------

# MAGIC %md
# MAGIC ***
# MAGIC ### Set Min and Max Values for Random Number of Patient Records Generated 
# MAGIC
# MAGIC Each run of this notebook will generate a random number of Synthea Patient records between the minimum number and the maximum number set.  This helps us simulate the variability in how patient records might arrive in a real world environment.  

# COMMAND ----------

dbutils.widgets.text(name = "min_records", defaultValue="1", label = "Minimum Generated Record Count")
dbutils.widgets.text(name = "max_records", defaultValue="1000", label = "Maximum Generated Record Count")

# COMMAND ----------

# Check if "min_records" is an integer
try:
  min_records = int(dbutils.widgets.get("min_records"))
except ValueError:
  raise Exception("Please set the minimum generated record count to an integer value")
min_records

# COMMAND ----------

# Check if "max_records" is an integer
try:
  max_records = int(dbutils.widgets.get("max_records"))
except ValueError:
  raise Exception("Please set the maximum generated record count to an integer value")
max_records
