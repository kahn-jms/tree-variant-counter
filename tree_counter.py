# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # First attempt

from functools import reduce
from operator import mul

# ## Try with a simple example

node_dict = {
    'a': [['b', 'c'], ['c', 'd']],
    'b': [['c', 'c'], ['d']],
    'c': ['d', 'e']
}

# Make copy for posterity

node_counts = dict(node_dict)

# Placeholder to populate possible trees for any non-leaf node

node_variants = {}

# ### Algorithm
#
# Idea is to populate the values in `node_counts` with the number of variants for the node corresponding to that child.

# First replace all leaf nodes with $1$ as they have only one variant (themselves).

for k, v in node_counts.items():
    node_counts[k] = [[1 if child not in node_counts.keys() else child for child in children] for children in v]

# Now loop through nodes until all their variants have been calculated

while len(node_variants) < len(node_dict):
    # Only go over nodes we haven't calculated the variants of yet
    for node in [x for x in node_counts.keys() if x not in node_variants.keys()]:
        # Populate child variant values where possible
        node_counts[node] = [
            [
                node_variants[child] if child in node_variants.keys() else child for child in children
            ] for children in node_counts[node]
        ]

        # If no unknown children remain for this node then add up the possible variants
        if not [child for children in node_counts[node] for child in children if not isinstance(child, int)]:
                node_variants[node] = sum([reduce(mul, children, 1) for children in node_counts[node]])

# ### Print results

node_variants, node_counts, max(node_variants.values())
