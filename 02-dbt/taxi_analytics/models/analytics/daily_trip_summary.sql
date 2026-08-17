{{ config(materialized='table') }}

select
    pickup_date,

    count(*) as total_trips,

    count(distinct vendor_id) as active_vendors,

    sum(passenger_count) as total_passengers,

    round(avg(passenger_count), 2) as avg_passenger_count,

    round(avg(trip_duration_minutes), 2) as avg_trip_duration_minutes,

    round(min(trip_duration_minutes), 2) as min_trip_duration_minutes,

    round(max(trip_duration_minutes), 2) as max_trip_duration_minutes

from {{ ref('fct_trips') }}

group by pickup_date

order by pickup_date
