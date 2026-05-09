import dlt
from pyspark.sql import functions as F


@dlt.table(
    name="tpch_lakefoundry_test",
    comment="Customer sales aggregation from samples.tpch.orders",
)
def tpch_lakefoundry_test():
    orders_df = spark.table("samples.tpch.orders").select(
        F.col("o_custkey"),
        F.col("o_totalprice").cast("decimal(18,2)").alias("o_totalprice"),
    )

    return orders_df.groupBy("o_custkey").agg(
        F.sum("o_totalprice").cast("decimal(18,2)").alias("total_sales_amount")
    )
