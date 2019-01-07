# Load a CSV file
def load_csv(filename):
    file = open(filename, "r")
    lines = reader(file)
    dataset = list(lines)
    return dataset

#「標準ライブラリ」にある「CSVモジュール」から「readerオブジェクト」を呼び出す。
from csv import reader
filename = 'pima-indians-diabetes.csv'
dataset = load_csv(filename)
print(dataset[0])
print('Loaded data file {0} with {1} rows and {2} columns' .format(filename, len(dataset), len(dataset[0])))
