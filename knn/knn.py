import math

# ------------------ LOAD DATA ------------------
def load_data(filename, has_header=False):
    data = []
    col_names = None
    try:
        with open(filename, 'r') as f:
            if has_header:
                col_names = f.readline().strip().split()
            for line in f:
                row = line.strip().split()
                if row:
                    data.append(row)
        return (col_names, data) if has_header else data
    except:
        print("\nFile not found")
        return None
# ------------------ PRINT DATA INFO ------------------
def print_data_info(col_names, data):
    num_features = len(data[0]) - 1
    print("\nColumn info:")
    for i in range(num_features):
        col = [float(row[i]) for row in data]
        min_val = min(col)
        max_val = max(col)
        col_name = col_names[i] if col_names else f"Feature_{i+1}"
        print(f"  {col_name}: Range = [{min_val:.3f}, {max_val:.3f}]")

    # Count labels (assuming last column is label)
    labels = [row[-1] for row in data]
    from collections import Counter
    label_counts = Counter(labels)
    print("\nLabel counts:")
    print(f"  cat: {label_counts.get('cat', 0)}")
    print(f"  dog: {label_counts.get('dog', 0)}")

# ------------------ NORMALIZATION HELPERS ------------------
def min_max_scale(col):
    min_val = min(col)
    max_val = max(col)
    scale = max_val - min_val
    if scale == 0:
        return [0.0] * len(col), min_val, scale
    return [(x - min_val) / scale for x in col], min_val, scale


def z_score_scale(col):
    mean = sum(col) / len(col)
    std = math.sqrt(sum((x - mean) ** 2 for x in col) / len(col))
    if std == 0:
        return [0.0] * len(col), mean, std
    return [(x - mean) / std for x in col], mean, std

# ------------------ NORMALIZATION ----------------
def normalize(dataset, test_data=None):
    num_features = len(dataset[0]) - 1
    to_normalize = []
    for i in range(num_features):
        col = [float(row[i]) for row in dataset]
        if max(col) - min(col) >1.0:
            to_normalize.append(i)

    if not to_normalize:
        print("\nAll features in same range. No normalization needed")
        return dataset, test_data

    print("\nChoose normalization method:")
    print("1. Min-Max Normalization")
    print("2. Z-Score Normalization")
    print("3. Skip normalization")
    ch = int(input("Enter your choice: "))

    for i in to_normalize:
        train_col = [float(row[i]) for row in dataset]

        if ch == 1:
            norm_train, min_val, scale = min_max_scale(train_col)
        elif ch == 2:
            norm_train, mean, std = z_score_scale(train_col)
        else:
            continue

        for j in range(len(dataset)):
            dataset[j][i] = norm_train[j]

        if test_data:
            test_col = [float(row[i]) for row in test_data]
            if ch == 1:
                norm_test = [(x - min_val) / scale if scale != 0 else 0.0 for x in test_col]
            elif ch == 2:
                norm_test = [(x - mean) / std if std != 0 else 0.0 for x in test_col]

            for j in range(len(test_data)):
                test_data[j][i] = norm_test[j]

    print("\nNormalized training data:")
    for row in dataset:
        print("  ".join(f"{float(x):.3f}" if i < len(row)-1 else str(x)
                        for i, x in enumerate(row)))
    if test_data:
        print("\nNormalized test data:")
        for row in test_data:
            print("  ".join(f"{float(x):.3f}" for x in row))

    return dataset, test_data


# ------------------ DISTANCE FUNCTIONS ------------------
def euclidean(p1, p2):
    return math.sqrt(sum((float(a) - float(b)) ** 2 for a, b in zip(p1, p2)))


def manhattan(p1, p2):
    return sum(abs(float(a) - float(b)) for a, b in zip(p1, p2))


# ------------------ KNN ALGORITHM ------------------
def KNN(train_data, test_data):
    print("\nChoose KNN votes:")
    print("1. Unweighted KNN")
    print("2. Weighted KNN")
    knn_type = int(input("Enter your choice: "))

    print("\nChoose distance calculation:")
    print("1. Euclidean Distance")
    print("2. Manhattan Distance")
    dist_choice = int(input("Enter your choice: "))

    distance_func = euclidean if dist_choice == 1 else manhattan

    train_data, test_data = normalize(train_data, test_data)

    train = [[float(x) for x in row[:-1]] + [row[-1]] for row in train_data]
    test = [[float(x) for x in row] for row in test_data]

    predictions = []

    for idx, test_point in enumerate(test):
        print(f"\nTest sample {idx+1}: {'  '.join(f'{x:.3f}' for x in test_point)}")

        distances = []
        for train_point in train:
            train_features = train_point[:-1]
            dist = distance_func(test_point, train_features)
            distances.append((dist, train_point[-1], train_point))

        sorted_distances = sorted(distances, key=lambda x: x[0])
        dist_to_rank = {id(tp): rank+1 for rank, (d, l, tp) in enumerate(sorted_distances)}

        print("\nAll training points (unsorted order):")
        print(f"{'Features':<25} {'Distance':<12} {'Rank':<6}")
        for d, l, tp in distances:
            features_str = " ".join(f"{v:.3f}" for v in tp[:-1])
            print(f"{features_str:<25} {d:<12.4f} {dist_to_rank[id(tp)]:<6}")
        #while n>3:
        k = int(input("\nEnter the [K] value: "))
        print(f"\nSorted {k} nearest neighbors:")
        print(f"{'Features':<25} {'Distance':<12} {'Label':<10}")
        for d, l, tp in sorted_distances[:k]:
            features_str = " ".join(f"{v:.3f}" for v in tp[:-1])
            print(f"{features_str:<25} {d:<12.4f} {l:<10}")
        if knn_type == 1:
            from collections import Counter
            k_labels = [label for _, label, _ in sorted_distances[:k]]
            print(f"\nUnweighted Votes: {k_labels}")
            pred = Counter(k_labels).most_common(1)[0][0]
        else:
            from collections import defaultdict
            weights = defaultdict(float)
            print("\nWeighted Votes:")
            for d, l, _ in sorted_distances[:k]:
                w = 1.0 if d == 0 else 1 / (d ** 2)
                weights[l] += w
                print(f"Label: {l:<10} Distance: {d:.4f} Weight: {w:.4f}")
                pred = max(weights, key=weights.get)
                print(f"Weighted votes: {dict(weights)}")
                print(f"\nPredicted label: {pred}")
        predictions.append(pred)
    return predictions


# ------------------ MAIN ------------------
if __name__ == '__main__':
    # Assume first line in file is header (column names)
    file_name = input("Enter data file name: ")
    data_result = load_data(file_name, has_header=True)
    if data_result is None:
        exit()
    col_names, data = data_result

    print("\nTraining data:")
    for row in data:
        print("  ".join(row))

    # Print column names, ranges, and label counts
    print_data_info(col_names, data)

    file_name2 = input("\nEnter the test data file name: ")
    test_data = load_data(file_name2)
    if test_data is None:
        exit()

    print("\nTest data:")
    for row in test_data:
        print("  ".join(row))

    predictions = KNN(data, test_data)

    print("\nFinal Predictions:")
    for i, pred in enumerate(predictions, 1):
        print(f"Test sample {i}: Predicted label = {pred}")
