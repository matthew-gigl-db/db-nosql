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

# DBTITLE 1,Retrieve Java Version
import os

# verify the java version is greater than 17.  
java_version = os.popen("java --version").read()
print(java_version)

# COMMAND ----------

# DBTITLE 1,Verify Version 17
if java_version.split(" ")[1].startswith("17"):
  print("Java Version is set correctly with version 17+")
else: 
  raise Exception("Error: Please ensure that java version 17 is set as the cluster default.  Please see https://docs.databricks.com/en/dev-tools/sdk-java.html#create-a-cluster-that-uses-jdk-17 for more information.")

# COMMAND ----------


