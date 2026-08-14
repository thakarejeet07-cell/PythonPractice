from itertools import product

# Generate all possible outfit combinations
shirts = ["Red", "Blue", "White"]
pants = ["Jeans", "Chinos"]

outfits = list(product(shirts, pants))
for shirt, pant in outfits:
    print(f"{shirt} shirt with {pant}")