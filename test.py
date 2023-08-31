import pandas as pd
import os

df = pd.read_csv(os.environ.get('INPUTPATH'))

df.to_csv('output.csv', index=False)
