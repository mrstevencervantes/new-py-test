import pandas as pd

df = pd.read_csv(${{ secrets.inputpath }})

df.to_csv('output.csv', index=False)
