# Day 22 - Website Uptime Monitor

import requests
import time

# Websites ki list
websites = [
    "https://google.com",
    "https://github.com",
    "https://python.org",
    "https://openai.com"
]

# Report file open ki
with open("website_report.txt", "w") as report:

    # Har website check karo
    for website in websites:

        print("\nChecking:", website)

        # Request ka start time
        start_time = time.perf_counter()

        try:

            # Website ko request bheji
            response = requests.get(
                website,
                timeout=10
            )

            # Response time calculate kiya
            end_time = time.perf_counter()

            response_time = end_time - start_time

            # Website status
            if response.status_code == 200:
                status = "ONLINE"
            else:
                status = "CHECK STATUS"

            # Result display
            result = (
                f"{website} | "
                f"{status} | "
                f"Code: {response.status_code} | "
                f"Time: {response_time:.2f}s"
            )

            print(result)

            # Result save
            report.write(result + "\n")

        except requests.RequestException as error:

            result = f"{website} | ERROR: {error}"

            print(result)

            report.write(result + "\n")

print("\nMonitoring completed!")
print("Report saved successfully.")
