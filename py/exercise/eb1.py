import pandas as pd

# data = pd.Series(["Январь", "Февраль", "Март", "Апрель"],
#                  index = ['Первый', "Второй", "Третий", "Четвёртый"])
# print(data)
# print(data.loc["Первый"])
# print(data.loc[["Первый", "Третий"]])
# print(data["Первый"])
# print(data[["Первый", "Третий"]])
# print(data.iloc[0])
# print(data.iloc[[0, 2]])

# data = pd.Series(list(range(10, 1001)))
# print(data)
# print(data.loc[10] + data.loc[23] - data.loc[245] + data.iloc[122])

# df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
# print(df)

# df = pd.DataFrame([ [1,2,3], [2,3,4] ],
#                   columns = ['foo', 'bar', 'baz'],
#                   index = ['foobar', 'foobaz'])
# print(df)

# # pd.DataFrame('Тестовая колонка', index = [1,5])
# # pd.DataFrame([1,5], index = 'Тестовая колонка')
# df = pd.DataFrame({'Тестовая колонка':[1,5]})
# print(df)

football = pd.read_csv('data_sf.csv')
# print(football.head())
# print(football.tail(7))
# print(football.info())
# print(len(football.columns))
# print(football['Club'].count())
# print(football.info(verbose=False))
# import collections
# c = collections.Counter()
# print(football.describe(include = ['object']))
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print(football.describe())

# df = pd.DataFrame([[i,i+1.2,i+2, 'hi'] for i in range(10)],
#                   columns = ['foo', 'bar', 'baz', 'foobar'])
# print(df)
# print(df.mean())
# print(df['foo'])
# print(df.bar.mean())
# print(football.Age.mean())
# print(football.Composure.count())
# print(football.ShortPassing.std())
# print(football.Wage.sum())
# print(football.Value.min())

# print(football[football.Age > football.Age.mean()].Name.count())
# print(football[(football.Age < football.Age.mean())|
#         (football.Club == 'FC Barcelona')].Name.count())
# print(football[(football.Age < football.Age.mean())&
#         (football.Club == 'FC Barcelona')].Wage.mean())

print(football[football.Wage > football.Wage.mean()].SprintSpeed.mean())
print(football[football.Wage < football.Wage.mean()].SprintSpeed.mean())
print(football[football.Wage == football.Wage.max()].Position)
print(football[football.Nationality == 'Brazil'].Penalties.sum())
print(football[football.HeadingAccuracy > 50].Age.mean())
print(football[
  (football.Composure > 0.9*football.Composure.max()) &
  (football.Reactions > 0.9*football.Reactions.max())
].Age.min())

print(
  football[
    football.Age == football.Age.max()
  ].Reactions.mean() -
  football[
    football.Age == football.Age.min()
  ].Reactions.mean() -
  0
)
print(football[
    football.Value > football.Value.mean()
  ].Nationality.describe()
)

print(
  football[
    (football.Position == 'GK') & (football.GKReflexes == football.GKReflexes.max())
  ].Wage.mean() /
  football[
    (football.Position == 'GK') & (football.GKHandling == football.GKHandling.max())
  ].Wage.mean()
)

print(
  football[
    (football.Aggression == football.Aggression.max())
  ].ShotPower.mean() /
  football[
    (football.Aggression == football.Aggression.min())
  ].ShotPower.mean()
)


