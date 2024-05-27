def filter_fasta_by_length(input_file, output_file, max_length):
  
    def write_sequence(header, sequence, output_handle):
        output_handle.write(f"{header}\n")
        output_handle.write(f"{sequence}\n")

    with open(input_file, 'r') as input_handle, open(output_file, 'w') as output_handle:
        header = None
        sequence = []
        
        for line in input_handle:
            line = line.strip()
            if line.startswith(">"):
                if header and len("".join(sequence)) <= max_length:
                    write_sequence(header, "".join(sequence), output_handle)

                header = line
                sequence = []
            else:
                sequence.append(line)
        

        if header and len("".join(sequence)) <= max_length:
            write_sequence(header, "".join(sequence), output_handle)
        
    print(f"Sequences longer than {max_length} aa have been removed.")


input_fasta = input("Enter the input FASTA file path: ")
output_fasta = input("Enter the output FASTA file path: ")
max_length = int(input("Enter the maximum sequence length: "))

filter_fasta_by_length(input_fasta, output_fasta, max_length)
