import random
import string


rows = ""
for x in range(0, 1000):
    rows += ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) + "\n"

with open("data.txt", "w") as f:
    f.write(rows)
  

