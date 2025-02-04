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


def process_dataset(df, encoding_func, encoding_name, pad_value):
    k = 3
    kmers = [sequence[i:i + k] for i in range(len(sequence) - k + 1)]

    kmer_to_index = {kmer: idx for idx, kmer in enumerate([''.join(p) for p in product(amino_acids, repeat=k)])}
    encoded = [kmer_to_index[kmer] for kmer in kmers]

    return result_df
