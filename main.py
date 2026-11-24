"""One Line, One Minute: The Vending Machine Pickup Line Contest — entry for make.fun.

Writes one line to /output/entry.txt.
The line is a pickup line of at most 200 characters a vending machine would use on a passing human.
"""
import os

LINE = "Are you exact change? Because every time I see you, my coils get stuck and my lights start flashing."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
