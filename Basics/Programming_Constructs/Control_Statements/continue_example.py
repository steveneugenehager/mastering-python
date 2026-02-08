# continue_example.py
"""Simple demonstration of the continue in a loop"""


for n in range(-3,8+1):
    # This if/break has to come before the continue since 7 is odd.
    print(f"{n=} ; " , end="")
    if n == 7:
        print("INFO: break to be encountered")
        break
    if n % 2 == 1:
        print("INFO: continue to be encountered")
        continue
    print(f"{n} is even.")
# In this example, the else will never be reached.
else:
    print("INFO: The for loop ended.")


        
        