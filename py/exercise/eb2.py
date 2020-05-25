import pandas as pd
df = pd.read_csv('data_sf.csv')
small_df = df[df.columns[0:7]].head(25)
print(small_df)
s = small_df['Nationality'].value_counts()
print(s)
print(len(df.Club.value_counts()))
s = df.Club.value_counts()
print(s.index[len(df.Club.value_counts())-1])
name = s.index[len(df.Club.value_counts())-1]
print(s[name])

s = df.Position.value_counts(normalize=True)
print(s)

s = df.Age.value_counts()
print(s)

s = df.Wage.value_counts(bins=4)
print(s)

print(df.loc[(df.Wage > s.index[3].left) & (small_df.Wage <= s.index[3].right)])
# s = df.Wage.value_counts(bins=4)
# print(s)

print(df.FKAccuracy.value_counts(bins=5))
print(df['Position'].nunique())
print(len(df['Position'].unique()))
print(len(df['Position'].value_counts()))

s = df['Nationality'].value_counts()
print(s)
s_df = s.reset_index()
s_df.columns = ['Nationality','Players Count']
print(s_df.head())

print(df.Wage.value_counts(bins=4))
q25 = df[df.Nationality == 'Spain'].Wage.value_counts(bins=4).index[0].right
qtQ = df[(df.Nationality == 'Spain') & (df.Wage <= q25)].Name.count()
qtP = df[(df.Nationality == 'Spain')].Name.count()
print(q25, qtQ, qtP, qtQ / qtP)

print(df[df.Club == 'Manchester United'].Nationality.nunique())
print(df[(df.Club == 'Juventus') & (df.Nationality == 'Brazil')].Name.unique())
s = df[df.Age >= 35].Club.value_counts()
s_df = s.reset_index()
s_df.columns = ['Club', 'Count']
print(s_df[s_df.Count == s_df.Count.max()])

print(df[df.Nationality == 'Argentina'].Age.value_counts(bins=4))
qB = df[df.Nationality == 'Spain'].Name.count()
qA = df[(df.Age == 21) & (df.Nationality == 'Spain')].Name.count()
print(qB, qA, qA / qB)

grouped_df = df.groupby(['Club']).Wage.sum().sort_values(ascending=False)
# print(grouped_df)
print(grouped_df.head(5))

grouped_df = df.groupby(['Position']).Wage.sum().sort_values(ascending=False)
print(grouped_df.head(10))

grouped_df = df.groupby(['Nationality'])[['Wage','Age','ShotPower']].mean().sort_values(['Wage'],ascending=False)
print(grouped_df.head(10))
print(df.loc[df['Nationality'] == 'Dominican Republic'][['Name','Club','Wage','Age','ShotPower']])

print(df.groupby(['Position'])[['Wage','Value']].mean().sort_values(['Value'],ascending=False).head(10))

print(df.groupby(['Nationality'])[['Club','Name']].nunique().sort_values(['Name'],ascending=False).head())

# print(df.groupby(['Club'])[['Wage']].mean().sort_values(['Wage'],ascending=False).head())
# print(df.groupby(['Club'])[['Wage']].median().sort_values(['Wage'],ascending=False).head())

s = df.groupby(['Club'])[['Wage']].agg(['median', 'mean'])#[median == 3500]
# print(s)
s_df = s.reset_index()
# print(s_df.Wage.median)
# print(type(s_df.Wage['median']))
# ss_def = pd.DataFrame({'Club': s_df.Wage, 'WageMed': s_df.Wage.median, 'WageMean': s_df.Wage.median})
# print(s_df.Wage.median)#[s_df.Club == ])
# print(ss_def)
# print(s_df.head())
# wage_df = s_df.Wage
# print(s_df.Wage.median)
print(s_df[s_df.Wage['median'] == s_df.Wage['mean']].Club.count())
print(s_df[s_df.Wage['median'] == s_df.Wage['mean']].sort_values([('Wage', 'mean')], ascending=False).head())
# print(wage_df[wage_df.median == wage_df.mean])
  # s_df.columns,

  # df.groupby(['Club'])
  #   [
  #     ['Wage']
  #   ].agg(['median', 'mean']).
  #   head()
    # .sort_values(['Wage'],ascending=False).head()
# )
print(df.groupby(['Club']).sum().Wage['Chelsea'])
print(df[(df.Nationality == 'Argentina')&(df.Age == 20)].Wage.max())
print(df[(df.Nationality == 'Argentina')&(df.Age == 30)].Wage.min())

print(df[(df.Nationality == 'Argentina')&(df.Club == 'FC Barcelona')].Strength.max())
print(df[(df.Nationality == 'Argentina')&(df.Club == 'FC Barcelona')].Balance.max())

pivot = df.loc[
  df['Club'].isin(
    ['FC Barcelona','Real Madrid','Juventus','Manchester United']
  )
].pivot_table(
  values=['Wage'],
  index=['Nationality'],
  columns=['Club'],
  aggfunc='sum',
  margins=True,
  fill_value=0
)
print(pivot)

pivot = df.loc[
  df['Club'].isin(
    ['FC Barcelona','Real Madrid','Juventus','Manchester United']
  )
].pivot_table(
  values=['Name'],
  index=['Nationality'],
  columns=['Club'],
  aggfunc='count',
  margins=True,
  fill_value=0
)
print(pivot)
print(pivot.loc['Argentina']['Name']['Manchester United'])


pivot = df.pivot_table(
  values=['Name'],
  index=['Position'],
  columns=['Club'],
  aggfunc='count',
  # margins=True,
  fill_value=0
)
print(pivot)
print(pivot.loc['GK']['Name'].mean())

pivot = df.pivot_table(
  values=['Name'],
  index=['Club'],
  columns=['Position'],
  aggfunc='count',
  # margins=True,
  fill_value=0
)

df_pivot = pivot.reset_index()
print(df_pivot.columns)
print('='*80)
print(df_pivot[df_pivot.Name.CM == 0].Club.count())
# print(df_pivot[('Position', 'CM')])
# print(df_pivot[df_pivot.CM == 0].Club.count())


print('='*80)
pivot = df.pivot_table(
  values=['Wage'],
  index=['Club'],
  columns=['Nationality'],
  aggfunc='sum',
  # margins=True,
  fill_value=0
)
print(pivot.loc['AS Monaco']['Wage']['Russia'])

# print('='*80)
# print(df.columns)
pivot = df.pivot_table(
  values=['SprintSpeed'],
  index=['Club'],
  columns=['Position'],
  aggfunc='mean',
  margins=True,
  fill_value=0
)
df_pivot = pivot.reset_index()
print('='*80)
print(df_pivot.columns)
print( df_pivot.sort_values([('SprintSpeed', 'ST')], ascending=False).head())
# print( df_pivot.sort_values(['ST'], ascending=False) )
# print(df_pivot.loc['All'])

# df.groupby()
# print('='*80)
# print(
#   df[df.Position.isin(['RB', 'LM', 'RM', 'CF', 'RWM', 'RS'])].groupby(['Position'])[['SprintSpeed']].
#     mean().
#     sort_values(['SprintSpeed'], ascending=False).
#     head(3)
# )



