# iterating_through_a_string_example.py
"""Simple example of iterating through a string."""
# Used the repr() function to ensure trailing spaces were not present.

output='' 
for character in 'Programming':
    output += character + "  "

print( 'Massaged string =' , repr(output.strip()))

# a more Pythonic approach to this is to use join().
print('Different approach to same Massaged string =', repr("  ".join('Programming')))