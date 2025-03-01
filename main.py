def one_hot_encode(sequence):
    blosum62 = substitution_matrices.load("BLOSUM62")
    encoded_vector = []

    for dataset in benchmark_list:
        dataset['length'] = dataset['seq'].apply(len)
        length = dataset['length'].max()
        print(length)
    return encoded


def threemers_encode(sequence):
    k = 3
    kmers = [sequence[i:i+k] for i in range(len(sequence) - k + 1)]

    kmer_to_index = {kmer: idx for idx, kmer in enumerate([''.join(p) for p in product(amino_acids, repeat=k)])}
    encoded = [kmer_to_index[kmer] for kmer in kmers]
    return encoded


def blosum62_encode(sequence):
    blosum62 = substitution_matrices.load("BLOSUM62")
    encoded_vector = []
    for i in range(len(sequence) - 1):
        pair = (sequence[i], sequence[i+1])
        kmers = [sequence[i:i+k] for i in range(len(sequence) - k + 1)]

            kmer_to_index = {kmer: idx for idx, kmer in enumerate([''.join(p) for p in product(amino_acids, repeat=k)])}
                encoded = [kmer_to_index[kmer] for kmer in kmers]
                    return encoded
            encoded_vector.append(blosum62[pair])
        elif (pair[1], pair[0]) in blosum62:
            encoded_vector.append(blosum62[(pair[1], pair[0])])
        else:
            encoded_vector.append(0)
    return encoded_vector

def process_dataset(df, encoding_func, encoding_name, pad_value):
    k = 3
    kmers = [sequence[i:i + k] for i in range(len(sequence) - k + 1)]
    for dataset in benchmark_list:
        for i in range(len(sequence) - 1):
                    pair = (sequence[i], sequence[i+1])
                            if pair in blosum62:
                                            encoded_vector.append(blosum62[pair])
                                                    elif (pair[1], pair[0]) in blosum62:
                                                                    encoded_vector.append(blosum62[(pair[1], pair[0])])
                                                                            else:
                                                                                            encoded_vector.append(0)print(length)
    kmer_to_index = {kmer: idx for idx, kmer in enumerate([''.join(p) for p in product(amino_acids, repeat=k)])}
    encoded = [kmer_to_index[kmer] for kmer in kmers]


    return result_df
