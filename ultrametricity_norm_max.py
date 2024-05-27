from ete3 import Tree
import numpy as np

newick = input("Tree to calculate: ")
tree = Tree(newick)

def calculate_ultrametricity(tree):
    root = tree.get_tree_root()
    leaves = tree.get_leaves()
    
    distances = np.array([root.get_distance(leaf) for leaf in leaves])
    max_dist = np.max(distances)
    norm_dist = distances / max_dist
    mean_norm_dist = np.mean(norm_dist)
    variance_norm_dist = np.var(norm_dist)
    return mean_norm_dist, variance_norm_dist

mean_norm_dist, variance_norm_dist = calculate_ultrametricity(tree)
print(f"Normalized Mean Distance ± Variance: {mean_norm_dist:.4f} ± {variance_norm_dist:.4f}")

