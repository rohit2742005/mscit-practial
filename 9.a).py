#Find ratios using fuzzy logic
# Install fuzzywuzzy if not already installed:
# pip install fuzzywuzzy[speedup]

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Two sample strings
s1 = "I love fuzzysforfuzzys"
s2 = "I am loving fuzzysforfuzzys"

# Different fuzzy matching ratios
print("FuzzyWuzzy Ratio:", fuzz.ratio(s1, s2))              # Basic ratio
print("FuzzyWuzzy Partial Ratio:", fuzz.partial_ratio(s1, s2))  # Partial matching
print("FuzzyWuzzy Token Sort Ratio:", fuzz.token_sort_ratio(s1, s2))  # Sort tokens before comparison
print("FuzzyWuzzy Token Set Ratio:", fuzz.token_set_ratio(s1, s2))    # Compare token sets
print("FuzzyWuzzy WRatio:", fuzz.WRatio(s1, s2), '\n')     # Weighted ratio

# Using process library to compare a query with multiple choices
query = "fuzzys for fuzzys"
choices = ["fuzzy for fuzzy", "fuzzy fuzzy", "g. for fuzzys"]

print("List of ratios:")
print(process.extract(query, choices), '\n')  # Returns a list of tuples (choice, score)

print("Best among the above list:")
print(process.extractOne(query, choices))     # Returns the best match
