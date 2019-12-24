import random
import time
# This is a simulated dice roll application using error excepts and rules. by newklear December 2019!
count = 1
low = 1
while True:
    try:
        hi = int(input("Enter max range: "))
        if hi <= 0:
    	    while hi <= 0:
                hi = int(input("Enter a number higher than 0: "))
        break
    except ValueError:
        print("Not a Valid Number, please try again!")
ranum = random.randint(low, hi)
while True:
    try:
        target = int(input("Enter number for computer to guess between 1 and max range: "))
        if target < low or target == 0:
    	    while target < low or target == 0:
                target = int(input("Enter a number higher than 0: "))
        if target > hi or target < low:
            while target > hi or target < low:
                target = int(input("Enter a number less than your max range: "))
        break
    except ValueError:
        print("Not a Valid Number, please try again!")
start = time.time()
while ranum != target:
	print(ranum)
	ranum = random.randint(low, hi)
	count += 1
else:
	print ("That took", f"{count:,d}", "dice rolls to roll the target number:", f"{target:,d}", "with a range of:", f"{low:,d}", "to", f"{hi:,d}", "and took", time.time() - start, "seconds to complete.")