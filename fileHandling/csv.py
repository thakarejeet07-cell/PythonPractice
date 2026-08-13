import csv

# Writing
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Grade"])
    writer.writerow(["Aman", 20, "A"])
    writer.writerow(["gaurav", 22, "B"])


# Reading
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)



# Dictionaries
fieldnames = ["Name", "Age", "Grade"]

writer = csv.DictWriter(file, fieldnames=fieldnames)
writer.writeheader()

writer.writerow({
    "Name": "Aman",
    "Age": 20,
    "Grade": "A"
})









