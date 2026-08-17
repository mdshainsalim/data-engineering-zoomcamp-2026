{{ config(materialized='table') }}

select
    id,
    vendor_id,
    pickup_datetime,
    dropoff_datetime,
    pickup_date,
    pickup_hour,
    pickup_weekday,
    passenger_count,
    pickup_longitude,
    pickup_latitude,
    dropoff_longitude,
    dropoff_latitude,
    store_and_fwd_flag,
    trip_duration,
    trip_duration_minutes

from {{ ref('stg_nyc_taxi_trips') }}
