import json

try:
    with open("logs.json", "r") as file:
        data = json.load(file)
    info = 0
    warning = 0
    error = 0
    print("--- LOG RECORDS ---")
    for log in data:
        print("\nTimestamp:", log["timestamp"])
        print("Level:", log["level"])
        print("Message:", log["message"])
        if log["level"] == "INFO":
            info += 1
        elif log["level"] == "WARNING":
            warning += 1
        elif log["level"] == "ERROR":
            error += 1
    print("\n--- LOG SUMMARY ---")
    print("INFO messages:", info)
    print("WARNING messages:", warning)
    print("ERROR messages:", error)
except FileNotFoundError:
    print("JSON file not found!")
except json.JSONDecodeError:
    print("Invalid JSON data!")
