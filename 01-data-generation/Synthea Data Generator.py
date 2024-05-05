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

# DBTITLE 1,Verify Java Version
# MAGIC %sh 
# MAGIC java -version

# COMMAND ----------


