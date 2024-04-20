# Databricks notebook source
# MAGIC %md
# MAGIC # Unity Catalog Set-Up 
# MAGIC
# MAGIC This notebook creates a catalog and schema that will use to create tables, plus a managed volume that will use to land the raw synthetic files that we'll generate from using Synthetic Health's Synthea package.  
# MAGIC
# MAGIC It's recommended to use a catalog name that you have read and write access to, or to create a new catalog (assuming that you have that permissoin in UC) to you'll be able to use to run the demo.  A brand new catalog is not required.  Please note that there is not a default setting for catalog, therefore you will need to supply a value in the Databricks widget.  You're welcome to create your own schema name in your catalog of choice.  The default schema name is "synthea" since we'll be generating synthetic files using the Synthea package.  You may need to change the schema name if more than one person in your organization is running this demo at the same time.  
# MAGIC
# MAGIC Since Unity Catalog uses a three level name space, the volume name "synthetic_files_raw" is techincally unique if either the catalog name or the schema name is unique.  For simplicity we'll be using a managed volume, though external volumes are also an option.  Our volume will have the path:  "/Volumes/<catalog_name>/<schema_name>/synthetic_files_raw/" 

# COMMAND ----------

# MAGIC %md 
# MAGIC Create a catalog and a schema to house the synthethic patient data.  

# COMMAND ----------

dbutils.widgets.text(name = "catalog_name", defaultValue="", label="Catalog Name")
dbutils.widgets.text(name = "schema_name", defaultValue="synthea", label="Schema Name")

# COMMAND ----------

catalog_name = dbutils.widgets.get(name = "catalog_name")
catalog_name

# COMMAND ----------

# MAGIC %sql
# MAGIC create catalog if not exists ${catalog_name};

# COMMAND ----------

# MAGIC %sql
# MAGIC use catalog ${catalog_name};
# MAGIC select current_catalog();

# COMMAND ----------

schema_name = dbutils.widgets.get("schema_name")
schema_name

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists ${schema_name};

# COMMAND ----------

# MAGIC %sql
# MAGIC use schema ${schema_name};
# MAGIC select current_schema();

# COMMAND ----------

# MAGIC %sql
# MAGIC create volume if not exists synthetic_files_raw;

# COMMAND ----------

# MAGIC %md
# MAGIC Volumes may be accessed using standard shell commands, just like they were local drives to our cluster, despite really being on a distributed file system in a cloud data lake storage account.  This makes working with files on Databricks very easy.  The following cell shows the (typically empty) contents of the volume we just created.  

# COMMAND ----------

command = f"ls -R /Volumes/{catalog_name}/{schema_name}/synthetic_files_raw/"
!{command}
