from ete3 import Tree, TreeStyle, TextFace, add_face_to_node

map_file = input("Mapping file (.txt): ")
newick_file = input("Tree file (.nwk): ")
output_file = input("Annotated output .nwk file name: ")


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

tree = Tree(newick_file)

annotated_count = 0
for leaf in tree:
    protein_id = leaf.name.strip()
    if protein_id in id_to_family:
        family = id_to_family[protein_id]
        leaf.name = f"{protein_id} {family}"  
        annotated_count += 1

print(f"Number of nodes annotated: {annotated_count}")

tree.write(outfile=output_file, format=1)
print("Annotated tree saved to", output_file)

