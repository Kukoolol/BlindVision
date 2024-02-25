import requests

url = "https://api.apilayer.com/image_to_text/upload"

# Specify the file path
file_path = "/Users/naren/project/testBillboard.jpeg"

# Open the file in binary mode and read its contents
with open(file_path, "rb") as file:
    file_data = file.read()

# Set the API key in the headers
headers= {
    "apikey": "lcKy6shoM8ooDwmiuRH6Wxs4Be9if18D"
}

# Use the `files` parameter to upload the file
files = {
    "file": file_data
}

# Make the POST request
response = requests.post(url, headers=headers, files=files)

# Check the response
status_code = response.status_code
result = response.text
print(result)
