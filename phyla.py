from ete3 import NCBITaxa

textfile = input("List of organisms: ")
output_file = input("Write results to: ")


organisms = []
with open(textfile, 'r') as f:
    for line in f:
        organism = line.strip()
        organisms.append(organism)

ncbi = NCBITaxa()

def fetch_lineages(organisms, output_file):
    with open(output_file, 'w') as file:
        for organism in organisms:
            taxid = ncbi.get_name_translator([organism])[organism][0]
            lineage = ncbi.get_lineage(taxid)
            rank_info = ncbi.get_rank(lineage)
            names = ncbi.get_taxid_translator(lineage)
            phylum_name = next((names[taxid] for taxid, rank in rank_info.items() if rank == 'phylum'), "Phylum not found")
            file.write(f"{organism}: {phylum_name}\n")


fetch_lineages(organisms, output_file)
