
keywords = ['Fragment', 'fragment', 'Predicted', 'predicted', 'LOW QUALITY', 'putative', 'Putative', 'Uncharacterized', 'uncharacterized', 'viral',  'hypothetical', 'probable', 'Probable', 'partial', 'Partial']

with open('gtpase.fasta', 'r') as input_file:
    with open('gtpase_f.fasta', 'w') as output_file:
        entry_lines = []  
        inside_entry = False  
        for line in input_file:
            if line.startswith('>'):  
                if entry_lines:  
                    if all(keyword not in ''.join(entry_lines) for keyword in keywords):
                        for entry_line in entry_lines:
                            output_file.write(entry_line)  
                entry_lines = [line]  
            else:
                entry_lines.append(line)  

        if entry_lines:
            if all(keyword not in ''.join(entry_lines) for keyword in keywords):
                for entry_line in entry_lines:
                    output_file.write(entry_line)
