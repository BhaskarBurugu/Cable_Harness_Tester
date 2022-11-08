import json

# Data to be written
dictionary = {
                "bhaskar": "aditya",
                "aditya": "Abhisumat",
            }

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("logincred.json", "w") as outfile:
    outfile.write(json_object)