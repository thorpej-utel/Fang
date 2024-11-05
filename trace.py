#write me a program to simuluate an OTDR trace

import numpy as np
import matplotlib.pyplot as plt

# Generate the waveform data for the OTDR trace
frequencies = np.linspace(10e9, 20e9, 1000)
amplitudes = np.sin(2 * np.pi * frequencies / (2 * 10e9)) + 0.5

# Create a plot of the OTDR trace
plt.plot(frequencies, amplitudes)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('OTDR Trace')
plt.show()

# Save the plot to a file
plt.savefig('otdr_trace.png')

# Generate a CSV file with the frequency and amplitude data for the OTDR trace
with open('otdr_data.csv', 'w') as f:
    f.write('Frequency (Hz),Amplitude\n')
    for i in range(len(frequencies)):
        f.write(f'{frequencies[i]},{amplitudes[i]}\n')

# Generate a JSON file with the frequency and amplitude data for the OTDR trace
import json
with open('otdr_data.json', 'w') as f:
    json.dump({'frequencies': frequencies, 'amplitudes': amplitudes}, f)

# Generate a YAML file with the frequency and amplitude data for the OTDR trace
import yaml
with open('otdr_data.yaml', 'w') as f:
    yaml.dump({'frequencies': frequencies, 'amplitudes': amplitudes}, f)

# Generate a Excel file with the frequency and amplitude data for the OTDR trace
import pandas as pd
df = pd.DataFrame({'Frequency (Hz)': frequencies, 'Amplitude': amplitudes})
df.to_excel('otdr_data.xlsx')