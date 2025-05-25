import os
import requests

# This works for a specific file. We should consider changing this later to
# accommodate dowloading multiple file types. This will make for easier
# automation later down the line

url = "https://www.aer.ca/documents/sts/ST60B_2024.xlsx"
headers = {"User-Agent": "Mozilla/5.0"}

# Set up the file download structure
filename = "../data/raw/ST60B_2024.xlsx"
os.makedirs(os.path.dirname(filename), exist_ok=True)

response = requests.get(url, headers=headers)

# Attempts the download
if response.status_code == 200:
    with open("../data/raw/ST60B_2024.xlsx", "wb") as f:
        f.write(response.content)
    print("Download Successful")
else:
    print(f"Failed to download: {response.status_code}")
