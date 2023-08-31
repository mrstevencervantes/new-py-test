import pandas as pd

df = pd.read_csv(${{ secrets.INPUTPATH }})

df.to_csv('output.csv', index=False)
