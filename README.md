# tpch-lakefoundry-test

This repository delivers a minimal Databricks Asset Bundle containing the `tpch_lakefoundry_test` Spark Declarative Pipeline (DLT) resource.

At a high level, the bundle deploys a serverless pipeline that materializes `sandbox_us_west_2.lakefoundry.tpch_lakefoundry_test` from `samples.tpch.orders`, aggregating sales by customer.

Typical workflow:
- `databricks bundle validate`
- `databricks bundle deploy`
- `databricks bundle run tpch_lakefoundry_test`

The deployed pipeline can be executed as a full refresh to rebuild the target table in the configured Unity Catalog catalog and schema.
