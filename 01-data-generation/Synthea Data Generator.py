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

# DBTITLE 1,import python modules
import subprocess

# COMMAND ----------

result = subprocess.run(["java", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# COMMAND ----------

java_version = result.stdout + result.stderr
print(java_version)

# COMMAND ----------

# MAGIC %md 
# MAGIC Typical output using default cluster JDK: 
# MAGIC > openjdk version "1.8.0_392"  
# MAGIC > OpenJDK Runtime Environment (Zulu 8.74.0.17-CA-linux64) (build 1.8.0_392-b08)  
# MAGIC > OpenJDK 64-Bit Server VM (Zulu 8.74.0.17-CA-linux64) (build 25.392-b08, mixed mode)  
# MAGIC
# MAGIC Output when the cluster JDK is set to version 17:  
# MAGIC >  
# MAGIC >  

# COMMAND ----------

# DBTITLE 1,Verify Version 17
if java_version.split(" ")[1].startswith("17"):
  print("Java Version is set correctly with version 17+")
else: 
  raise Exception("Error: Please ensure that java version 17 is set as the cluster default.  Please see https://docs.databricks.com/en/dev-tools/sdk-java.html#create-a-cluster-that-uses-jdk-17 for more information.")

# COMMAND ----------


