import pandas as pd
import io

def read_kestrel(dataset):
    f = open(dataset, 'r')
    lines = f.readlines()

    output = io.StringIO()
    for l in lines[3:]:
        output.write(','.join(l.split(',')[:16]) + '\n')
    
    output.seek(0)
    data = pd.read_csv(output, na_values='--')
    data = data.drop(0)
    data['Time'] = pd.to_datetime(data['FORMATTED DATE_TIME'])
    data = data.set_index('Time')
    data = data.drop('FORMATTED DATE_TIME', axis=1)
    data = data.astype(float)
    return data