SELECT *
FROM {{ ref('fct_trips') }}
WHERE passenger_count < 0
