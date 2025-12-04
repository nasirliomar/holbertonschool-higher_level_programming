#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0
    # Loop through arguments starting from index 1 (skipping the script name)
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])
        
    print(total)
