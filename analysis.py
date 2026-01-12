import csv

with open("galamsey_data.csv", newline='', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = []

    for row in reader:
        rows.append(row)


for i, row in enumerate(rows[:5]):
    print(f"Row {i+1}:", row)

# Total number of galamsey sites
def load_data(filepath):
    data = []
    with open(filepath, newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # convert sites from string to integer
            row["Number_of_Galamsay_Sites"] = int(row["Number_of_Galamsay_Sites"])
            data.append(row)
    return data


def total_sites(data):
    total = 0
    for row in data:
        total += row["Number_of_Galamsay_Sites"]
    return total



# Region with the higest number of galamsey sites
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




# Cities that exceed a given threshold with the threshold of 20
def cities_above_threshold(data, threshold):
    cities = []

    for row in data:
        if row["Number_of_Galamsay_Sites"] > threshold:
            cities.append(row["City"])

    return cities

# Average galamsey per region
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


# Conditional statement for the questions
if __name__ == "__main__":
    data = load_data("galamsey_data.csv")
    total = total_sites(data)
    print("Total number of Galamsay sites:", total)


    region, count = region_with_highest_sites(data)
    print("Region with highest sites:", region, "(", count, ")")
    

    threshold = 10
    cities = cities_above_threshold(data, threshold)
    print(f"Cities with more than {threshold} sites:")
    for city in cities:
        print("-", city)


    averages = average_sites_per_region(data)
    print("Average number of sites per region:")
    for region, avg in averages.items():
      print(f"- {region}: {avg:.2f}")
