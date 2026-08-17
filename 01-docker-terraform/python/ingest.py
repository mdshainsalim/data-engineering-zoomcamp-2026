import pandas as pd
from sqlalchemy import create_engine


# =========================================================
# Configuration
# =========================================================

CSV_FILE = "data/raw/NYC.csv"

DB_USER = "zoomcamp"
DB_PASSWORD = "zoomcamp"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "zoomcamp"

TABLE_NAME = "nyc_taxi_trips"

CHUNK_SIZE = 50_000


# =========================================================
# PostgreSQL connection
# =========================================================

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)


# =========================================================
# Start ingestion
# =========================================================

print("=" * 60)
print("NYC Taxi Data Ingestion Started")
print("=" * 60)

total_rows = 0
first_chunk = True


# =========================================================
# Read CSV in chunks
# =========================================================

for chunk_number, chunk in enumerate(
    pd.read_csv(
        CSV_FILE,
        chunksize=CHUNK_SIZE,
        parse_dates=[
            "pickup_datetime",
            "dropoff_datetime"
        ]
    ),
    start=1
):

    # Normalize column names
    chunk.columns = [
        column.lower().strip()
        for column in chunk.columns
    ]

    # Convert numeric columns
    numeric_columns = [
        "vendor_id",
        "passenger_count",
        "pickup_longitude",
        "pickup_latitude",
        "dropoff_longitude",
        "dropoff_latitude",
        "trip_duration"
    ]

    for column in numeric_columns:
        chunk[column] = pd.to_numeric(
            chunk[column],
            errors="coerce"
        )

    # =====================================================
    # Load into PostgreSQL
    # =====================================================

    if first_chunk:

        chunk.to_sql(
            TABLE_NAME,
            engine,
            if_exists="replace",
            index=False
        )

        first_chunk = False

    else:

        chunk.to_sql(
            TABLE_NAME,
            engine,
            if_exists="append",
            index=False
        )

    total_rows += len(chunk)

    print(
        f"Chunk {chunk_number:>3}: "
        f"{len(chunk):,} rows | "
        f"Total: {total_rows:,}"
    )


# =========================================================
# Finished
# =========================================================

print("=" * 60)
print("NYC Taxi Data Ingestion Completed")
print(f"Total rows loaded: {total_rows:,}")
print(f"PostgreSQL table: {TABLE_NAME}")
print("=" * 60)docker ps