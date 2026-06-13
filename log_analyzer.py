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

with open("log_report.txt", "w") as file:
    file.write(report)

print("Report saved to log_report.txt")

with open("log_report.txt", "w") as file:
    file.write(report)