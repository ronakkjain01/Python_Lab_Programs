try:
    file = open("log.txt", "r")
    error_count = 0
    print("--- LOG FILE CONTENTS ---")
    for line in file:
        print(line.strip())
        if "ERROR" in line:
            error_count += 1
    file.close()
    print("\nTotal ERROR messages:", error_count)
except FileNotFoundError:
    print("Log file does not exist!")
