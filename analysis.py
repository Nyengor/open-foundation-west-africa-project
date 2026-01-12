import csv
import sqlite3
from datetime import datetime


# -----------------------------
# LOAD AND CLEAN CSV DATA
# -----------------------------
def load_data(filepath):
    data = []

    with open(filepath, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # Clean column headers
        reader.fieldnames = [name.strip() for name in reader.fieldnames if name]

        for row in reader:
            clean_row = {}

            # Clean each row
            for key, value in row.items():
                if key and value:
                    clean_row[key.strip()] = value.strip()

            # Convert number of sites to int
            sites = int(clean_row["Number_of_Galamsay_Sites"])

            # Skip invalid negative values
            if sites < 0:
                continue

            clean_row["Number_of_Galamsay_Sites"] = sites
            data.append(clean_row)

    return data


# -----------------------------
# ANALYSIS FUNCTIONS
# -----------------------------
def total_sites(data):
    total = 0
    for row in data:
        total += row["Number_of_Galamsay_Sites"]
    return total


def region_with_highest_sites(data):
    region_totals = {}

    for row in data:
        region = row["Region"]
        sites = row["Number_of_Galamsay_Sites"]

        if region not in region_totals:
            region_totals[region] = 0

        region_totals[region] += sites

    highest_region = max(region_totals, key=region_totals.get)
    return highest_region, region_totals[highest_region]


def cities_above_threshold(data, threshold):
    cities = []

    for row in data:
        if row["Number_of_Galamsay_Sites"] > threshold:
            cities.append(row["City"])

    return cities


def average_sites_per_region(data):
    region_totals = {}
    region_counts = {}

    for row in data:
        region = row["Region"]
        sites = row["Number_of_Galamsay_Sites"]

        if region not in region_totals:
            region_totals[region] = 0
            region_counts[region] = 0

        region_totals[region] += sites
        region_counts[region] += 1

    averages = {}
    for region in region_totals:
        averages[region] = region_totals[region] / region_counts[region]

    return averages


# -----------------------------
# DATABASE FUNCTIONS
# -----------------------------
def init_database():
    conn = sqlite3.connect("galamsey_analysis.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analysis_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            total_sites INTEGER,
            highest_region TEXT,
            highest_region_count INTEGER,
            threshold INTEGER,
            cities_above_threshold TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_analysis_result(
    total_sites,
    highest_region,
    highest_region_count,
    threshold,
    cities_above_threshold
):
    conn = sqlite3.connect("galamsey_analysis.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO analysis_results (
            total_sites,
            highest_region,
            highest_region_count,
            threshold,
            cities_above_threshold,
            created_at
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, (
        total_sites,
        highest_region,
        highest_region_count,
        threshold,
        ", ".join(cities_above_threshold),
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()


# -----------------------------
# MAIN EXECUTION
# -----------------------------
if __name__ == "__main__":
    init_database()

    data = load_data("galamsey_data.csv")

    total = total_sites(data)
    print("Total number of Galamsay sites:", total)

    region, count = region_with_highest_sites(data)
    print("Region with highest sites:", region, f"({count})")

    threshold = 20
    cities = cities_above_threshold(data, threshold)
    print(f"Cities with more than {threshold} sites:")
    for city in cities:
        print("-", city)

    averages = average_sites_per_region(data)
    print("Average number of sites per region:")
    for region, avg in averages.items():
        print(f"- {region}: {avg:.2f}")

    save_analysis_result(
        total,
        region,
        count,
        threshold,
        cities
    )

    print("Analysis saved to database successfully.")
