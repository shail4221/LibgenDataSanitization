#Pass 1: Remove any book not in English
#Pass 2: Remove any book missing essential information -> MD5, Title, Author, 
import csv
import unicodedata

total = -1
dropped = -1
written = 0
errors = 0

with open("fiction_csv.csv", "r", encoding="utf-8") as original:
    reader = csv.reader(original)

    with open('processed_fiction_csv.csv', "w", newline = '') as result:
        writer = csv.writer(result)

        for row in reader:
            total += 1
            if(row[6] == "English"):
                try:
                    if(row[1] and row[2] and row[3]):
                        writer.writerow((row[1], row[2], row[3], row[4], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]))
                        written += 1
                    else:
                        dropped += 1
                except:
                    errors += 1
                    continue
            else:
                dropped += 1

            if (total % 50000 == 0):
                print("Program Still Running")

print("Total records: ", total)
print("Number of records dropped: ", dropped)
print("Number of records written: ", written)
print("Number of records discarded due to errors: ", errors)