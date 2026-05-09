import dlt
from pyspark.sql import functions as F


@dlt.table(
    name="tpch_lakefoundry_test",
    comment="Customer sales aggregation from samples.tpch.orders",
)
def tpch_lakefoundry_test():
    orders = spark.read.table("samples.tpch.orders")

    return (
        orders.groupBy("o_custkey")
        .agg(F.sum("o_totalprice").cast("decimal(38, 2)").alias("total_sales_amount"))
        .select("o_custkey", "total_sales_amount")
    )
