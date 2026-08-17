{{ config(materialized='table') }}

select distinct
    vendor_id
from {{ ref('stg_nyc_taxi_trips') }}
where vendor_id is not null
