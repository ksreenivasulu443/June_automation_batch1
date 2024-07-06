with open('output.txt', 'w') as file:
    print("Writing to a file.", file=file)

import time

print("Starting...", end="", flush=False)
time.sleep(2)
print(" Done!")