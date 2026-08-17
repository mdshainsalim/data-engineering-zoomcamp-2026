{{ config(materialized='view') }}

select
    id,
    vendor_id,
    pickup_datetime,
    dropoff_datetime,
    passenger_count,
    pickup_longitude,
    pickup_latitude,
    dropoff_longitude,
    dropoff_latitude,
    store_and_fwd_flag,
    trip_duration,

    cast(pickup_datetime as date) as pickup_date,

    extract(hour from pickup_datetime)::integer as pickup_hour,

    extract(dow from pickup_datetime)::integer as pickup_weekday,

    trip_duration / 60.0 as trip_duration_minutes

from {{ source('raw', 'nyc_taxi_trips') }}

where trip_duration > 0
  and trip_duration <= 10800
