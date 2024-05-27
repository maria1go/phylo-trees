from ete3 import Tree

first_tree  = input("1st tree: ")
second_tree  = input("2nd tree: ")


tree1 = Tree(first_tree)
tree2 = Tree(second_tree)

rf_distance, rf_max, common_labels, parts_t1, parts_t2, discard_t1, discard_t2 = tree1.robinson_foulds(tree2)

print(f"Robinson-Foulds distance: {rf_distance}")
print(f"Max possible RF distance: {rf_max}")
print(f"Normalized RF distance: {rf_distance / rf_max:.2f}")
print(f"Common labels: {common_labels}")
#print(f"Splits in Tree1 not in Tree2: {parts_t1}")
#print(f"Splits in Tree2 not in Tree1: {parts_t2}")
print(f"Labels discarded from Tree1: {discard_t1}")
print(f"Labels discarded from Tree2: {discard_t2}")
