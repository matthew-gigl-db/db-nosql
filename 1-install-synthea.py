# Databricks notebook source
# MAGIC %md
# MAGIC # Install Synthea
# MAGIC
# MAGIC The purpose of this notebook is download and set up Synthethic Health's latest Synthea jar files from Github for use in creating our synthetic patient files that will use as our data source.  
# MAGIC
# MAGIC For more infomration on the Synthea Patient Generator, please visit: [https://github.com/synthetichealth/synthea](https://github.com/synthetichealth/synthea)

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

# COMMAND ----------

command = f"""cd {volume_path} 
git clone https://github.com/synthetichealth/synthea.git 
"""
command

# COMMAND ----------

# MAGIC %sh
# MAGIC cd /Volumes/mgiglia/synthea/synthetic_files_raw/
# MAGIC pwd
# MAGIC git clone https://github.com/synthetichealth/synthea.git 

# COMMAND ----------

# cd {volume_path}synthea 
# pwd
# ./gradlew build check test 

# COMMAND ----------

!{command}

# COMMAND ----------

from urllib.request import urlretrieve

# COMMAND ----------

url = "https://github.com/synthetichealth/synthea/releases/download/v3.2.0/synthea-with-dependencies.jar"
filename = f"{volume_path}synthea-with-dependencies.jar"
filename

# COMMAND ----------

urlretrieve(
  url=url
  ,filename=filename
)

# COMMAND ----------

command = f"""
cd {volume_path}
java -jar synthea-with-dependencies.jar
"""

# COMMAND ----------

!{command}

# COMMAND ----------

# MAGIC %sh
# MAGIC java -version

# COMMAND ----------

# MAGIC %sh
# MAGIC synthea -h

# COMMAND ----------


