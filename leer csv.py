if __name__ == "__main__":
    """import csv
    with open('Egg Grade Dataset.csv',newline='') as csvfile:
        read = csv.DictReader(csvfile, delimiter=',')
        for row in read:
            print(row["Diameter "])"""
    import csv

    with open("Egg Grade Dataset Final.csv", mode="r", encoding="utf-8") as file:
        data_table = list(csv.reader(file))

    for row in data_table:
        print(row)
