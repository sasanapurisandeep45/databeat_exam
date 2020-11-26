import pandas as pd
import json

df = pd.read_csv('data.csv')
out = pd.read_csv('output.csv')
n = len(df)
c = 0

# df.rename({'_source': '_tmp'}, axis=1, inplace=True)

del df['_type'], df['_id'], df['_score']
# df = df.set_index(df[[0]])
# df.set_index([df.iloc[0], df.columns[0]])
# del df.iloc[0]
# df.drop(df.columns[[0]], axis=1, inplace=True)

for i in df.index:
	df.at[i, '_source'] = df.at[i, '_source'][:-1]
	df.at[i, '_source'] += ", 'rating': nan, 'hide': nan, 'watchlist': nan, 'watched': nan}"
	# print(df.at[i, '_tmp'])
	# s = json.loads(x)
	# ifor_val = something
	# if <condition>:
		# ifor_val = something_else
	# df.set_value(i,'ifor',ifor_val)

# for row in df['']:
	# print(row)

# print(df.head())
# print(n, c)
df.to_csv('output2.csv');