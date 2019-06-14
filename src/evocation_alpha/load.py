# %matplotlib inline

# import matplotlib.pyplot as plt
# import mne

def load_data(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    compactData = []
    for i in range(len(data)):
        if i >= 6:
            compactData.append(data[i])

    return compactData

def convert(data):
    temp = []
    line = data.split(',')

    for e in range(len(line)):
        if e <= 6:
            temp.append(float(line[e]))
        if e == 12:
            temp.append(line[e].split('\n')[0].strip())
    
    return temp

def separate_data(data):
    index = []
    temp = []
    count = 0

    for e in range(len(data)):
        idx = data[e].split(',')[0]
        if int(idx) == 255 and count == 255:
            index.extend(temp)
            temp = []
            count = 0
        elif int(idx) == 255 and count < 255:
            temp = []
            count = 0
        else:
            temp.append(convert(data[e]))
            count += 1
    
    return index
    
data = load_data('dataset_alpha/RAW_00.txt')
newData = separate_data(data)

# def sem_nome(data):
#     newData = np.asarray(data)
    
#     ch_names = ['PO3', 'PO4', 'P8', 'O1', 'O2', 'P7']
#     ch_types = ['eeg'] * 6

#     info = mne.create_info(ch_names=ch_names, sfreq=256, ch_types=ch_types)
#     raw = mne.io.RawArray(newData, info)

#     plt.plot(np.linspace(0, len(data), len(data)*256), raw.get_data()[0]) #eletrodo index 0
#     plt.xlabel('tempo (s)')
#     plt.ylabel('Dados EEG (mV/cm²)')

#     raw.plot_psd

# sem_nome(newData)