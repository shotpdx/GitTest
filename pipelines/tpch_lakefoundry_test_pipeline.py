import dlt
from pyspark.sql import functions as F


SOURCE_TABLE = "samples.tpch.orders"
TARGET_TABLE = "tpch_lakefoundry_test"


@dlt.table(
    name=TARGET_TABLE,
    comment="Customer sales aggregation from samples.tpch.orders",
)
def tpch_lakefoundry_test():
    return (
        spark.table(SOURCE_TABLE)
        .groupBy("o_custkey")
        .agg(F.sum(F.col("o_totalprice")).cast("decimal(38, 2)").alias("total_sales_amount"))
        .select("o_custkey", "total_sales_amount")
    )
