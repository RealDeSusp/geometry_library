# 15.09.2023 Mikhail Porokhnya

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode

# creating SparkSession
spark = SparkSession.builder.appName("ProductCategory").getOrCreate()

# example DataFrame with data
data = [("Product1", ["Category1", "Category2"]),
        ("Product2", ["Category2", "Category3"]),
        ("Product3", [])]

schema = ["Product_name", "Categories"]

df = spark.createDataFrame(data, schema)

# split the list of categories into separate lines
df_exploded = df.select(col("Product_name"), explode(col("Categories")).alias("Categories_name"))

# create a DataFrame with products without categories
df_without_categories = df.select(col("Product_name")).filter(col("Categories").isEmpty())

# merging two DataFrames
result_df = df_exploded.union(df_without_categories)

# display the result
print(result_df)
# result_df.show()
