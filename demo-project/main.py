# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC ## This notebook acts as the master playbook that imports and executes necessary modules 

# COMMAND ----------

# MAGIC %md
# MAGIC Execute Setup script

# COMMAND ----------

# MAGIC %run ./utils/setup

# COMMAND ----------

# MAGIC %md
# MAGIC Generate Bronze Layer

# COMMAND ----------

# MAGIC %run ./modules/bronze

# COMMAND ----------

# MAGIC %md
# MAGIC Generate Silver Layer

# COMMAND ----------

# MAGIC %run ./modules/silver

# COMMAND ----------

# MAGIC %md
# MAGIC Generate Gold Layer

# COMMAND ----------

# MAGIC %run ./modules/gold

# COMMAND ----------

# MAGIC %md
# MAGIC Execute Cleanup script

# COMMAND ----------

# MAGIC %run ./utils/cleanup
