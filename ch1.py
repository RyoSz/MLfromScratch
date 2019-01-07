from csv import reader

# CSV loading function
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

# Load pima-indians-diabetes dataset
filenameDiabetes = 'datasets\pima-indians-diabetes.csv'
datasetDiabetes = load_csv(filenameDiabetes)
print('Loaded data file {0} with {1} rows and {2} columns'.format(filenameDiabetes, len(datasetDiabetes), len(datasetDiabetes[0])))
print(datasetDiabetes[0])


# Convert string column to float function
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

# Use it
for i in range(len(datasetDiabetes[0])):
    str_column_to_float(datasetDiabetes, i)
print(datasetDiabetes[0])


# Load Iris dataset
filenameIris = 'datasets\iris.csv'
datasetIris = load_csv(filenameIris)
print('Loaded data file {0} with {1} rows and {2} columns'.format(filenameIris, len(datasetIris), len(datasetIris[0])))
print(datasetIris[0])

# 最終列に文字列で何の種かという情報が入っている。
# 全3種類。これを整数値に置き換える。
# Convert string column to integer
def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup

# Convert string columns to float
for i in range(4):
    str_column_to_float(datasetIris, i)
# Convert class column to int
lookup = str_column_to_int(datasetIris, 4)
print(datasetIris[0])
print(lookup)













