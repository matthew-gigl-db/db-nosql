# Databricks notebook source
# MAGIC %md 
# MAGIC Create a catalog to house the synthethic patient data.  

# COMMAND ----------

dbutils.widgets.text(name = "catalog_name", defaultValue="", label="Catalog Name")

# COMMAND ----------

catalog_name = dbutils.widgets.get(name = "catalog_name")

# COMMAND ----------

spark.sql(f"create catalog if not exists {catalog_name}")
