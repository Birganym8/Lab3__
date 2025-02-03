def grams_to_ounces(grams):
    """Convert grams to ounces."""
    ounces = grams / 28.3495231
    return ounces


grams = float(input("Enter weight in grams: "))
ounces = grams_to_ounces(grams)
print(f"{grams} grams is equal to {ounces:.2f} ounces.")
