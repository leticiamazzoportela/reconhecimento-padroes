import pandas as pd
def load_data(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    compactData = []
    for i in range(len(data)):
        if i >= 6:
            compactData.append(data[i])

    return compactData

def separate_data(data):
    index = []
    info = {}

    for e in range(len(data)):
        idx = data[e].split(',')[0]
        if int(idx) >= 0 and int(idx) <= 255:
            info['linha'] = e
            info['index'] = idx
            index.append(info)
        info = {}

    print(len(index))
    print(index[300])

data = load_data('dataset_alpha/RAW_00.txt')
separate_data(data)