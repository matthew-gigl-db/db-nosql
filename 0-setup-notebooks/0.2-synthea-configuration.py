# Databricks notebook source
# MAGIC %md
# MAGIC # Synthea Configuration 
# MAGIC
# MAGIC The purpose of this notebook is to create a configuration file that will be used to set the parameters for each run of the Synthea Patient Generator.  
# MAGIC
# MAGIC Examples of some of the parameters that may be set: 
# MAGIC
# MAGIC * File formats including FHIR, C-CCA, simple text or CSV
# MAGIC * Append modes for CSV files
# MAGIC * Export folders
# MAGIC * Patient locations
# MAGIC * Population size
# MAGIC
# MAGIC For a full list of configuarion details please visit Synthethic Health's GitHub [page](https://github.com/synthetichealth/synthea).

# COMMAND ----------

# MAGIC %md
# MAGIC ***
# MAGIC ### Set Catalog, Schema, and Volume Paths 

# COMMAND ----------

dbutils.widgets.text(name = "catalog_name", defaultValue="", label="Catalog Name")
dbutils.widgets.text(name = "schema_name", defaultValue="synthea", label="Schema Name")

# COMMAND ----------

catalog_name = dbutils.widgets.get(name = "catalog_name")
schema_name = dbutils.widgets.get(name = "schema_name")
volume_path = f"/Volumes/{catalog_name}/{schema_name}/synthetic_files_raw/"
print(f"""
  catalog_name = {catalog_name}
  schema_name = {schema_name}
  volume_path = {volume_path}
""")
