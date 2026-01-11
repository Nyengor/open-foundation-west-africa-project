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



if __name__ == "__main__":
    data = load_data("galamsey_data.csv")
    total = total_sites(data)
    print("Total number of Galamsay sites:", total)


    region, count = region_with_highest_sites(data)
    print("Region with highest sites:", region, "(", count, ")")