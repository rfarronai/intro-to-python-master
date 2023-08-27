"""
Start at 10 seconds and count down until 1 and then print "Happy New Year! 🎉"
"""
import time

for counter in range(10, 0, -1):
    print(f"Happy New Year! 🎉 {counter}")
    time.sleep(1)