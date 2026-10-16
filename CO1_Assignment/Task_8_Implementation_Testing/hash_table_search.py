
def hash_table_search(records, key):
    if key in records:
        return records[key]
    return -1


n = int(input("Enter number of records: "))
records = {}

print("Enter registration numbers:")

for i in range(n):
    reg_no = int(input())
    records[reg_no] = "Student Record " + str(i + 1)

key = int(input("Enter registration number to search: "))

result = hash_table_search(records, key)

if result != -1:
    print("Record found:", result)
else:
    print("Record not found")

