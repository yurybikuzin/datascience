import numpy as np
import pandas as pd
import sys

# ============================================================================

def _norm(df, compound_col, sep='|', result_col=None):
  if result_col == None:
    result_col = compound_col
  df[result_col] = df[compound_col].str.split(sep)
  # https://stackoverflow.com/questions/27263805/pandas-column-of-lists-create-a-row-for-each-list-element
  df_orig = df
  return pd.DataFrame({
      col:np.repeat(df[col].values, df[result_col].str.len())
      for col in df.columns.drop(result_col)}
  ).assign(**{result_col:np.concatenate(df[result_col].values)})[df.columns]

# ============================================================================

from pathlib import Path
import time

def current_milli_time():
  return int(round(time.time() * 1000))

def load_tsv(tsv_file_name):
  start_time = current_milli_time()
  print('Loading ' + tsv_file_name + ' . . .')
  result = pd.read_csv(tsv_file_name, sep='\t')
  print('OK: ' + tsv_file_name + ' loaded', 'took {} msec'.format(current_milli_time() - start_time))
  return result

def save_pickle(pickle_file_name, df):
  start_time = current_milli_time()
  print('Saving ' + pickle_file_name + ' . . .')
  df.to_pickle(pickle_file_name)
  print('OK: ' + pickle_file_name + ' saved', 'took {} msec'.format(current_milli_time() - start_time))

data_pickle = 'data.pickle'
needed_file = Path(data_pickle)
if not needed_file.is_file():
  df = pd.read_csv('data.csv', parse_dates={'release_dt' : ['release_date']})
  df['income'] = df.revenue - df.budget
  df['release_month'] = df['release_dt'].map(lambda x: x.month)
  save_pickle(data_pickle, df)

title_crew_pickle = 'title.crew.pickle'
needed_file = Path(title_crew_pickle)
if not needed_file.is_file():
  # https://datasets.imdbws.com/title.crew.tsv.gz
  df_crew = load_tsv('title.crew.tsv')
  df_crew.columns = ['imdb_id', 'director', 'writer']

  print('Merging . . .')
  start_time = current_milli_time()
  df_merged = pd.DataFrame(
    pd.read_pickle(data_pickle).merge(
      df_crew,
      on = 'imdb_id',
      how = 'left'
    )[['imdb_id', 'director']]
  )
  print('OK: Merge', 'took {} msec'.format(current_milli_time() - start_time))

  save_pickle(title_crew_pickle, _norm(df_merged, 'director', sep=','))

name_basics_pickle = 'name.basics.pickle'
needed_file = Path(name_basics_pickle)
if not needed_file.is_file():
  # https://datasets.imdbws.com/name.basics.tsv.gz
  df_name = pd.DataFrame(load_tsv('name.basics.tsv')[['nconst', 'primaryName']])
  df_name.columns = ['director', 'directorName']

  print('Merging . . .')
  start_time = current_milli_time()
  df_merged = pd.DataFrame(
    pd.read_pickle(title_crew_pickle).merge(
      df_name,
      on = 'director',
      how = 'left'
    )[['director', 'directorName']]
  ).drop_duplicates(subset=None, keep='first', inplace=False)
  print('OK: Merge', 'took {} msec'.format(current_milli_time() - start_time))

  save_pickle(name_basics_pickle, df_merged)

# ============================================================================

answer_ls = []
i = 0

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle)
answer = 4
print(i, df[df.budget == df.budget.max()].original_title.iloc[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle)
answer = 2
print(i, df[df.runtime == df.runtime.max()].original_title.iloc[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle)
answer = 3
print(i, df[df.runtime == df.runtime.min()].original_title.iloc[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle)
answer = 2
print(i, round(df.runtime.mean()), '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle)
answer = 1
print(i, round(df.runtime.median()), '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle)
answer = 5
print(i, df[df.income == df.income.max()].original_title.iloc[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle)
answer = 2
print(i, df[df.income == df.income.min()].original_title.iloc[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle)
answer = 1
print(i, df[df.income > 0].imdb_id.count(), '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle)
answer = 4
print(i, df[df.release_year == 2008].sort_values(['income'],ascending=False).original_title.iloc[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle)
answer = 5
print(i, df[(df.release_year >= 2012) & (df.release_year <= 2014)].sort_values(['income'],ascending=True).original_title.iloc[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = _norm(pd.read_pickle(data_pickle), 'genres', result_col='genre')
answer = 3
print(i, df.groupby(['genre']).imdb_id.count().sort_values(ascending=False).index[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = _norm(pd.read_pickle(data_pickle), 'genres', result_col='genre')
answer = 1
print(i, df[df.income > 0].groupby(['genre']).imdb_id.count().sort_values(ascending=False).index[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle).merge(
  pd.read_pickle(title_crew_pickle),
  on = 'imdb_id',
  how = 'left'
).merge(
  pd.read_pickle(name_basics_pickle),
  on = 'director',
  how = 'left',
)
answer = 3
print(i, df.groupby('directorName').imdb_id.count().sort_values(ascending=False).index[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle).merge(
  pd.read_pickle(title_crew_pickle),
  on = 'imdb_id',
  how = 'left'
).merge(
  pd.read_pickle(name_basics_pickle),
  on = 'director',
  how = 'left',
)
answer = 4
print(i, df[df.income > 0].groupby('directorName').imdb_id.count().sort_values(ascending=False).index[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle).merge(
  pd.read_pickle(title_crew_pickle),
  on = 'imdb_id',
  how = 'left'
).merge(
  pd.read_pickle(name_basics_pickle),
  on = 'director',
  how = 'left',
)
answer = 5
print(i, df[df.income > 0].groupby('directorName').income.sum().sort_values(ascending=False).index[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = _norm(pd.read_pickle(data_pickle), 'cast', result_col='actor')
answer = 1
print(i, df.groupby('actor').income.sum().sort_values(ascending=False).index[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = _norm(pd.read_pickle(data_pickle), 'cast', result_col='actor')
answer = 3
print(i, df[df.release_year == 2012].groupby('actor').income.sum().sort_values(ascending=True).index[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle)
budget_mean = df.budget.mean()
df = _norm(df, 'cast', result_col='actor')
answer = 3
print(i, df[df.budget > budget_mean].groupby('actor').imdb_id.count().sort_values(ascending=False).index[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = _norm(
  _norm(
    pd.read_pickle(data_pickle), 'genres', result_col='genre'
  ),
  'cast', result_col='actor'
)
answer = 2
print(i, df[df.actor == 'Nicolas Cage'].groupby('genre').imdb_id.count().sort_values(ascending=False).index[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

studio_crutch = True

i += 1
if studio_crutch:
  df = pd.read_pickle(data_pickle)
  studio_lst = ['Universal', 'Paramount Pictures', 'Columbia Pictures', 'Warner Bros', 'Twentieth Century Fox Film Corporation']
  qt_lst = []
  for j in studio_lst:
    qt_lst.append(df[df.production_companies.str.contains(j)].imdb_id.count())
  df_synt = pd.DataFrame({
    'studio': studio_lst,
    'qt': qt_lst,
  })
  answer = 1
  # print(df_synt.sort_values('qt', ascending=False).head())
  print(i, df_synt.sort_values('qt', ascending=False).iloc[0].studio, '=>', answer)
else:
  df = _norm(
    pd.read_pickle(data_pickle), 'production_companies', result_col='studio'
  )
  answer = 4
  print(i, df.groupby('studio').imdb_id.count().sort_values(ascending=False).index[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
if studio_crutch:
  df = pd.read_pickle(data_pickle)
  studio_lst = ['Universal Pictures', 'Paramount Pictures', 'Columbia Pictures', 'Warner Bros', 'Twentieth Century Fox Film Corporation']
  qt_lst = []
  for j in studio_lst:
    qt_lst.append(df[(df.release_year == 2015) & (df.production_companies.str.contains(j))].imdb_id.count())
  df_synt = pd.DataFrame({
    'studio': studio_lst,
    'qt': qt_lst,
  })
  answer = 4
  # print(df_synt.sort_values('qt', ascending=False).head())
  print(i, df_synt.sort_values('qt', ascending=False).iloc[0].studio, '=>', answer)
else:
  df = _norm(
    pd.read_pickle(data_pickle), 'production_companies', result_col='studio'
  )
  answer = 4
  print(i, df[df.release_year == 2015].groupby('studio').imdb_id.count().sort_values(ascending=False).index[0], '=>', answer)
answer_ls.append(answer)


# ============================================================================

i += 1
if studio_crutch:
  df = _norm(pd.read_pickle(data_pickle), 'genres', result_col='genre')
  studio_lst = ['Universal', 'Paramount Pictures', 'Columbia Pictures', 'Warner Bros', 'Walt Disney']
  qt_lst = []
  for j in studio_lst:
    qt_lst.append(df[(df.genre == 'Comedy') & (df.production_companies.str.contains(j))].income.sum())
  df_synt = pd.DataFrame({
    'studio': studio_lst,
    'qt': qt_lst,
  })
  answer = 2
  # print(df_synt.sort_values('qt', ascending=False).head())
  print(i, df_synt.sort_values('qt', ascending=False).iloc[0].studio, '=>', answer)
else:
  df = _norm(
    _norm(
      pd.read_pickle(data_pickle), 'production_companies', result_col='studio'
    ),
    'genres', result_col='genre'
  )
  answer = 2
  print(i, df[df.genre == 'Comedy'].groupby('studio').income.sum().sort_values(ascending=False).index[0], '=>', answer)
answer_ls.append(answer)


# ============================================================================

i += 1
if studio_crutch:
  df = pd.read_pickle(data_pickle)
  studio_lst = ['Universal', 'Paramount Pictures', 'Bad Robot', 'Warner Bros', 'Lucasfilm']
  qt_lst = []
  for j in studio_lst:
    qt_lst.append(df[(df.release_year == 2014) & (df.production_companies.str.contains(j))].income.sum())
  df_synt = pd.DataFrame({
    'studio': studio_lst,
    'qt': qt_lst,
  })
  answer = 2
  print(i, df_synt.sort_values('qt', ascending=False).iloc[0].studio, '=>', answer)
else:
  df = _norm(pd.read_pickle(data_pickle), 'genres', result_col='genre')
  df = _norm(
    pd.read_pickle(data_pickle), 'production_companies', result_col='studio'
  )
  answer = 4
  print(i, df[df.release_year == 2014].groupby('studio').income.sum().sort_values(ascending=False).head(), '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle)
answer = 1
print(i, df[df.production_companies.str.contains('Paramount Pictures')].sort_values(['income'], ascending=True).iloc[0]['original_title'], '=>', answer)
answer_ls.append(answer)

# sys.exit()
# ============================================================================

i += 1
df = pd.read_pickle(data_pickle)
answer = 5
print(i, df.groupby('release_year').income.sum().sort_values(ascending=False).index[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
answer = 1
df = pd.read_pickle(data_pickle)
print(i, df[df.production_companies.str.contains('Warner Bros')].groupby('release_year').income.sum().sort_values(ascending=False).index[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle)
answer = 4
months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
print(i, months[df.groupby('release_month').imdb_id.count().sort_values(ascending=False).index[0] - 1], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle)
answer = 2
print(i, df[df.release_month.isin([6, 7, 8])].imdb_id.count(), '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle).merge(
  pd.read_pickle(title_crew_pickle),
  on = 'imdb_id',
  how = 'left'
).merge(
  pd.read_pickle(name_basics_pickle),
  on = 'director',
  how = 'left',
)
answer = 5
print(i, df[df.release_month.isin([12, 1, 2])].groupby('directorName').imdb_id.count().sort_values(ascending=False).index[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle)
pivot = df.pivot_table(
  values=['income'],
  index=['release_month'],
  columns=['release_year'],
  aggfunc='sum',
  margins=False,
  fill_value=0
)
years = []
best_months = []
for j in pivot.columns.levels[1].tolist():
  df0 = pd.DataFrame(pivot[('income', j)])
  years.append(j)
  best_months.append(
    df0[df0[('income', j)] == df0[('income', j)].max()].index[0]
  )
df_best = pd.DataFrame({'year':years, 'best_month':best_months}, columns=['year', 'best_month'])
answer = 2
print(i, months[df_best.groupby('best_month').year.count().sort_values(ascending=False).index[0] - 1], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = _norm(pd.read_pickle(data_pickle), 'production_companies', result_col='studio')
answer = 5
df['original_title_len'] = df['original_title'].map(lambda x: len(x))
print(i, df.groupby('studio').original_title_len.mean().sort_values(ascending=False).index[0], '=>', answer)
answer_ls.append(5)

# ============================================================================

i += 1
df = _norm(pd.read_pickle(data_pickle), 'production_companies', result_col='studio')
df['original_title_words'] = df['original_title'].map(lambda x: len(x.split()))
answer = 5
print(i, df.groupby('studio').original_title_words.mean().sort_values(ascending=False).index[0], '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
import collections
c = collections.Counter()
def count_uniq_words(words):
  for w in words:
    c[w.lower()] += 1
  return words
df['words'] = df['original_title'].map(lambda x: count_uniq_words(x.split()))
answer = 3
print(i, len(c.keys()), '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = pd.read_pickle(data_pickle)
answer = 1
print(i, df[df.vote_average > df.vote_average.quantile(.99)].original_title.tolist(), '=>', answer)
answer_ls.append(answer)

# ============================================================================

i += 1
df = _norm(pd.read_pickle(data_pickle), 'cast', result_col='actor')
df_right = pd.DataFrame(_norm(pd.read_pickle(data_pickle), 'cast', result_col='actor')[['imdb_id', 'actor']])
df_right.columns = ['imdb_id', 'actor_right']
df_merged = df.merge(df_right, on = 'imdb_id', how = 'left')
df_merged = df_merged[(df_merged.actor != df_merged.actor_right) & (df_merged.actor < df_merged.actor_right)]
df_merged['actor_pair'] = df_merged['actor'] + ' & ' + df_merged['actor_right']
answer = 5
print(i, df_merged.groupby('actor_pair').imdb_id.count().sort_values(ascending=False).index[0:3].tolist(), '=>', answer)
answer_ls.append(answer)

# ============================================================================

print('='*10)
submission = pd.DataFrame({'Id':range(1,len(answer_ls)+1), 'Answer':answer_ls}, columns=['Id', 'Answer'])
submission.to_csv('submission.csv', index=False)
print(len(answer_ls))
print('Save submit')
