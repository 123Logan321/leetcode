import sys

original_number = int(sys.stdin.readline())
reversed_number = int(str(original_number)[::-1])

if original_number == reversed_number:
    print("true")
else:
    print("false")