# Databricks notebook source
import dlt
# from pyspark.sql.functions import *

# COMMAND ----------

# MAGIC %run "./classes"

# COMMAND ----------

# used for active development, but not run during DLT execution, use DLT configurations instead
# dbutils.widgets.dropdown(name = "env_mode", defaultValue = "prd", choices = ["dev", "tst", "uat", "prd"], label = "Environment Mode")
# dbutils.widgets.text(name = "catalog_name", defaultValue="", label="Catalog Name")
# dbutils.widgets.text(name = "schema_name", defaultValue="synthea", label="Schema Name")
# dbutils.widgets.text(name = "volume_name", defaultValue="synthetic_files_raw", label="Volume Name")

# spark.conf.set("workflow_inputs.env_mode", dbutils.widgets.get(name = "env_mode"))
# spark.conf.set("workflow_inputs.catalog_name", dbutils.widgets.get(name = "catalog_name"))
# spark.conf.set("workflow_inputs.schema_name", dbutils.widgets.get(name = "schema_name"))
# spark.conf.set("workflow_inputs.volume_name", dbutils.widgets.get(name = "volume_name"))

# COMMAND ----------

# dbutils.widgets.removeAll()

# COMMAND ----------

env_mode = spark.conf.get("workflow_inputs.env_mode")
catalog_name = spark.conf.get("workflow_inputs.catalog_name")
schema_name = spark.conf.get("workflow_inputs.schema_name")
volume_name = spark.conf.get("workflow_inputs.volume_name")
volume_path = f"/Volumes/{catalog_name}/{schema_name}/{volume_name}/"
print(f"""
    env_mode = {env_mode}
    catalog_name = {catalog_name}
    schema_name = {schema_name}
    volume_name = {volume_name}
    volume_path = {volume_path}
""")

# COMMAND ----------

# from pyspark.sql import DataFrame
# from pyspark.sql.session import SparkSession
# from pyspark.sql.streaming import DataStreamReader, DataStreamWriter
# from typing import Callable

# COMMAND ----------

# def read_stream_raw(spark: SparkSession, path: str, maxFiles: int, maxBytes: str, wholeText: bool = True, options: dict = None) -> DataFrame:
#     stream_schema = "value STRING"
#     read_stream = (
#         spark
#         .readStream
#         .format("cloudFiles")
#         .option("cloudFiles.format", "text")
#         .option("wholetext", wholeText)
#         .option("cloudFiles.maxBytesPerTrigger", maxBytes)
#         .option("cloudFiles.maxFilesPerTrigger", maxFiles)
#     )

#     if options is not None:
#         read_stream = read_stream.options(**options)

#     read_stream = (
#         read_stream
#         .schema(stream_schema)
#         .load(path)
#     )

#     return read_stream

# COMMAND ----------

# class IngestionDLT:

#     def __init__(
#         self
#         ,spark: SparkSession = spark
#         ,env_mode: str = "dev"
#         ,catalog: str = "lakehouse"
#         ,schema: str = "landing"
#         ,volume: str = "dropbox"
#     ):
#         self.spark = spark
#         self.env_mode = env_mode
#         self.catalog = catalog
#         self.schema = schema
#         self.volume = volume

#         # use_catalog_schema(catalog = self.catalog, schema = self.schema, env_mode = self.env_mode, verbose = False)
#         if self.env_mode == "prd":
#             self.catalog_set = self.catalog
#         else:
#             self.catalog_set = f"{self.catalog}_{self.env_mode}"

#     def __repr__(self):
#         return f"""IngestionDLT(env_mode='{self.env_mode}', catalog='{self.catalog_set}', schema='{self.schema}', volume='{self.volume}')"""

#     def ingest_raw_to_bronze(self, table_name: str, table_comment: str, table_properties: dict, source_folder_path_from_volume: str = "", maxFiles: int = 1000, maxBytes: str = "10g", wholeText: bool = True, options: dict = None):
#         """
#         Ingests all files in a volume's path to a key value pair bronze table.
#         """
#         @dlt.table(
#             name = table_name
#             ,comment = table_comment
#             ,temporary = False
#             ,table_properties = table_properties

#         )
#         def bronze_ingestion(spark = self.spark, source_folder_path_from_volume = source_folder_path_from_volume, maxFiles = maxFiles, maxBytes = maxBytes, wholeText = wholeText, options = options, catalog = self.catalog_set, schema = self.schema, volume = self.volume):

#             if source_folder_path_from_volume == "":
#                 file_path = f"/Volumes/{catalog}/{schema}/{volume}/"
#             else:
#                 file_path = f"/Volumes/{catalog}/{schema}/{volume}/{source_folder_path_from_volume}/"

#             raw_df = read_stream_raw(spark = spark, path = file_path, maxFiles = maxFiles, maxBytes = maxBytes, wholeText = wholeText, options = options)

#             bronze_df = (raw_df
#                 .withColumn("inputFilename", col("_metadata.file_name"))
#                 .withColumn("fullFilePath", col("_metadata.file_path"))
#                 .withColumn("fileMetadata", col("_metadata"))
#                 .select(
#                     "fullFilePath"
#                     ,lit(file_path).alias("datasource")
#                     ,"inputFileName"
#                     ,current_timestamp().alias("ingestTime")
#                     ,current_timestamp().cast("date").alias("ingestDate")
#                     ,"value"
#                     ,"fileMetadata"
#                 )
#             )

#             return bronze_df
        
#     def ingest_raw_to_bronze_synchronous(self, table_names: list, table_comments: list, table_properties: dict, source_folder_path_from_volumes: str, maxFiles: int = 1000, maxBytes: str = "10g", wholeText: bool = True, options: dict = None):
#         """
#             Synchronously ingest from multiple subfolders of the same Volume into more than one bronze table.  Each bronze table created is managed as a streaming Delta Live Table in the same <catalog.schema> as the source volume.  
#         """
#         for i in range(0,len(table_names)):
#             ingest_raw_to_bronze(self = self, table_name = table_names[i], table_comment = table_comments[i], source_folder_path_from_volume = source_folder_path_from_volumes[i], table_properties = table_properties, maxFiles = maxFiles, maxBytes = maxBytes, wholeText = wholeText, options = options)


# COMMAND ----------

Pipeline = IngestionDLT(
    spark = spark
    ,env_mode = env_mode
    ,catalog = catalog_name
    ,schema = schema_name
    ,volume = volume_name
)

# COMMAND ----------

Pipeline

# COMMAND ----------

Pipeline.ingest_raw_to_bronze(
    table_name="synthea_csv_bronze"
    ,table_comment="A full text record of every file that has landed in our raw synthea landing folder."
    ,table_properties=None # {"quality":"bronze"}
    ,source_folder_path_from_volume="output/csv"
)
