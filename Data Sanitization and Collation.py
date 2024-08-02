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
shared_md5 = set(description_md5_list) & set(fiction_md5_list)
print("set size: ", len(shared_md5))
md5_dict = {}

count = 0
errors = 0

with open("fiction_description_csv.csv", "r", encoding="utf-8") as fiction_descriptions:
    reader = csv.reader(fiction_descriptions)
    for row in reader:
        count += 1
        if (count % 100000) == 0:
            print("Pt 3 Still running: ", count)
        try:
            if (row[0] in shared_md5):
                md5_dict[row[0]] = row[1]
        except:
            errors += 1
            continue

print("errors: ", errors)
count = 0
errors = 0

found_descriptions = 0
blank_description = 0
one_key = ""
with open("processed_fiction_csv.csv", "r") as original:
    reader = csv.reader(original)

    with open('sanitized_fiction_csv.csv', "w", newline = '') as result:
        writer = csv.writer(result)

        for row in reader:
            count += 1

            if (count % 100000) == 0:
                print("Pt 4 Still running: ", count)
            try:
                if (row[0] in md5_dict.keys()):
                    found_descriptions += 1
                    one_key = row[0]
                    writer.writerow((row[0], row[1], row[2], md5_dict[row[0]],row[4], row[6], row[7], row[8], row[9], row[10], row[11]))
                else:
                    blank_description += 1
                    writer.writerow((row[0], row[1], row[2], "", row[4], row[6], row[7], row[8], row[9], row[10], row[11]))
            except Exception as e:
                if errors == 0:
                    print(e)
                errors += 1
                continue
print("errors: ", errors)
print("found desc", found_descriptions)
print("blank desc", blank_description)
print("total records: ", count)
print(one_key)