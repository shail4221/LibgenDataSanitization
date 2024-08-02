import csv

fiction_md5_list = []
description_md5_list = []

errors = 0
count = 0


with open("processed_fiction_csv.csv", "r") as fiction_records:
    reader = csv.reader(fiction_records)
    for row in reader:
        count += 1

        if (count % 100000) == 0:
            print("Still running: ", count)

        try:
            fiction_md5_list.append(row[0])
        except:
            errors += 1
            continue
    

count = 0
with open("fiction_description_csv.csv", "r", encoding="utf-8") as fiction_descriptions:
    reader = csv.reader(fiction_descriptions)
    for row in reader:
        count += 1

        if (count % 100000) == 0:
            print("Pt 2 Still running: ", count)
        try:
            description_md5_list.append(row[0])
        except:
            errors += 1
            continue

print("len fiction: ", len(fiction_md5_list))
print("len descriptions: ", len(description_md5_list))
print("errors: ", errors)
print(len(set(description_md5_list) & set(fiction_md5_list)))

