def one_hot_encode(sequence):
    encoder = OneHotEncoder(categories=[list(amino_acids)], dtype=int, sparse_output=False)
    sequence_array = np.array(list(sequence)).reshape(-1, 1)
    encoded = encoder.fit_transform(sequence_array).flatten()
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
        if pair in blosum62:
            encoded_vector.append(blosum62[pair])
        elif (pair[1], pair[0]) in blosum62:
            encoded_vector.append(blosum62[(pair[1], pair[0])])
        else:
            encoded_vector.append(0)
    return encoded_vector


def process_dataset(df, encoding_func, encoding_name, pad_value):
    encoded_data = df['seq'].apply(encoding_func)
    max_len = max(encoded_data.apply(len))

    encoded_data = encoded_data.apply(lambda x: np.pad(x, (0, max_len - len(x)), 'constant', constant_values=pad_value))

    encoded_df = pd.DataFrame(encoded_data.tolist(), index=df.index)

    result_df = pd.concat([df, encoded_df], axis=1)

    return result_df