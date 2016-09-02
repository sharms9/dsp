import pandas as pd

df = pd.read_csv('faculty.csv')

df.emails = df[df.columns[3]]

df.emails.to_csv('emails.csv', index = False)
