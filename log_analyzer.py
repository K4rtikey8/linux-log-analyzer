# info_count = 0
# warning_count = 0
# error_count = 0

# with open("sample.log", "r") as file:
#     for line in file:

#         if line.startswith("INFO"):
#             info_count += 1

#         elif line.startswith("WARNING"):
#             warning_count += 1

#         elif line.startswith("ERROR"):
#             error_count += 1

# print("===== LOG ANALYSIS REPORT =====")
# print(f"INFO Count: {info_count}")
# print(f"WARNING Count: {warning_count}")
# print(f"ERROR Count: {error_count}")

import sys
from datetime import datetime
import os

info_count = 0
warning_count = 0
error_count = 0

with open("sample.log", "r") as file:
    for line in file:

        if line.startswith("INFO"):
            info_count += 1

        elif line.startswith("WARNING"):
            warning_count += 1

        elif line.startswith("ERROR"):
            error_count += 1

counts = {
    "INFO": info_count,
    "WARNING": warning_count,
    "ERROR": error_count
}

most_common = max(counts, key=counts.get)

os.makedirs("reports", exist_ok=True)
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"reports/report_{timestamp}.txt"

print("===== LOG ANALYSIS REPORT =====")
print(f"INFO Count: {info_count}")
print(f"WARNING Count: {warning_count}")
print(f"ERROR Count: {error_count}")
print(f"Most Common Log Level: {most_common}")
report = f"""
===== LOG ANALYSIS REPORT =====

INFO Count: {info_count}
WARNING Count: {warning_count}
ERROR Count: {error_count}

Most Common Log Level: {most_common}
"""
search_level = sys.argv[1]

print(f"\nShowing all {search_level} logs:\n")

with open("sample.log", "r") as file:
    for line in file:
        if search_level in line:
            print(line.strip())


with open(filename, "w") as file:
    file.write(report)

print(f"Report saved to {filename}")

with open(filename, "w") as file:
    file.write(report)