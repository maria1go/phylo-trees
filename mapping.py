from ete3 import Tree, TreeStyle, TextFace, add_face_to_node

map_file=input("Mapping file (.txt): ")
output_file_svg = input("Annotated output .svg file name: ")


id_to_family = {}
with open(map_file, "r") as file:
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 2:
            protein_id = parts[0].strip()
            family = parts[1].strip()
            id_to_family[protein_id] = family

print("ID to Family Mapping:")
for protein_id, family in id_to_family.items():
    print(f"{protein_id}: {family}")


newick_file = input("Tree file (.nwk): ")
tree = Tree(newick_file)



annotated_count = 0
for leaf in tree:
    protein_id = leaf.name.strip()  
    print(f"Leaf name: {protein_id}")
    for id_from_mapping in id_to_family.keys():
        if protein_id == id_from_mapping:
            family = id_to_family[id_from_mapping]
            leaf.add_feature("family", family)
            annotated_count += 1
            print(f"Annotated leaf with ID: {protein_id}, Family: {family}")
            break


print(f"Number of nodes annotated: {annotated_count}")

for node in tree.traverse():
    node.dist = 0.01 


def add_annotation(node):
    if hasattr(node, "family"):
        text_face = TextFace(node.family, fsize=10)
        add_face_to_node(text_face, node, column=0, position="branch-right")


ts = TreeStyle()
ts.mode = "c"
ts.show_leaf_name = True 
ts.show_branch_length = False  
ts.layout_fn = add_annotation  


tree.render(output_file_svg, tree_style=ts)
print("Annotated tree saved as", output_file_svg)


