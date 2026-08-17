SELECT *
FROM {{ ref('fct_trips') }}
WHERE trip_duration_minutes <= 0
   OR trip_duration_minutes > 180
