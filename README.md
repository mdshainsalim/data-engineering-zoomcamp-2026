# NYC Taxi Data Engineering Pipeline

An end-to-end data engineering project built using NYC taxi trip data.

## Project Overview

This project demonstrates a complete modern data engineering workflow:

- Data ingestion into PostgreSQL
- Data transformation using dbt
- Data quality testing
- Dimensional data modeling
- Analytics-ready tables
- Workflow orchestration using Apache Airflow
- Containerization using Docker
- Git/GitHub version control

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data processing |
| PostgreSQL | Data warehouse |
| dbt | Data transformation and testing |
| Apache Airflow | Workflow orchestration |
| Docker | Containerization |
| Git | Version control |
| GitHub | Source control and portfolio |

## Architecture

```text
NYC Taxi CSV
     |
     v
PostgreSQL
     |
     v
dbt Staging
     |
     v
dbt Core Models
     |
     v
dbt Analytics Models
     |
     v
Airflow Orchestration
     |
     v
Analytics / BI
```

## dbt Models

### Staging

**stg_nyc_taxi_trips** — cleaned and transformed NYC taxi trip data.

### Core

**fct_trips** — validated taxi trip fact table.

**dim_vendor** — taxi vendor dimension table.

### Analytics

**daily_trip_summary** — daily aggregated taxi trip metrics.

## Data Quality

The project contains dbt schema tests and custom SQL data-quality tests.

Validation includes:

- NOT NULL checks
- Uniqueness checks
- Accepted vendor values
- Source data validation
- Passenger-count validation
- Trip-duration validation

## Airflow Pipeline

The Airflow DAG is:

`dbt_taxi_pipeline`

It executes:

```text
dbt_debug
    |
    v
dbt_build
```

The end-to-end DAG has been successfully executed.

## Final Results

Final validated fact records:

**1,456,532 trips**

Invalid trip-duration records:

**0**

Two taxi vendors are represented in the dataset.

## Project Structure

```text
data-engineering-zoomcamp-2026/
|
├── 02-dbt/
│   └── taxi_analytics/
│       ├── models/
│       │   ├── staging/
│       │   ├── core/
│       │   └── analytics/
│       ├── tests/
│       └── dbt_project.yml
|
├── airflow/
│   └── dags/
│       └── dbt_taxi_pipeline.py
|
├── data/
│   └── raw/
|
├── docker-compose.yml
|
└── README.md
```

## Future Improvements

- GitHub Actions CI/CD
- Automated dbt testing
- Incremental models
- Data freshness monitoring
- Dashboard development
- Pipeline monitoring
- Performance optimization

## Author

**Md Shain Salim**

Data Engineering / Analytics Portfolio Project
