import pandas as pd

if False:
  df_ratings = pd.read_csv('ratings.csv')
  df_movies = pd.read_csv('movies.csv')
  print(df_ratings.info())
  print(df_movies.info())
  # print(df_movies['genres'].unique())
  print(df_movies['title'].head().unique())
  print(df_ratings['rating'].max())
  # print(df_ratings['rating'].value_counts(bins=4))
  df_joined = df_ratings.merge(df_movies, on='movieId', how='left')
  print(df_joined.head())
  print(len(df_ratings) == len(df_joined), len(df_ratings), len(df_joined))

  df_ratings_example = pd.read_csv('ratings_example.txt', sep = '\t')
  df_movies_example = pd.read_csv('movies_example.txt', sep = '\t')
  df_movies_example.drop_duplicates(subset = 'movieId', keep = 'first', inplace = True)
  print(df_ratings_example.head())
  print(df_movies_example.head())
  print(df_ratings_example.merge(df_movies_example, on = 'movieId', how = 'left').head())

if False:
  items_dict = {

      'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 100132, 312394],

      'vendor': ['Samsung', 'LG', 'Apple', 'Apple', 'LG', 'Apple', 'Samsung', 'Samsung', 'LG', 'ZTE'],

      'stock_count': [54, 33, 122, 18, 102, 43, 77, 143, 60, 19]

  }
  purchase_log = {

      'purchase_id': [101, 101, 101, 112, 121, 145, 145, 145, 145, 221],

      'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 103845, 100132],

      'price': [13900, 5330, 38200, 49990, 9890, 33000, 67500, 34500, 89900, 11400]

  }
  df_items = pd.DataFrame(items_dict)
  df_purchase = pd.DataFrame(purchase_log)
  df_merged = df_items.merge(df_purchase, on='item_id', how='right')
  # print(df_merged.head(100))
  print(df_merged[df_merged.stock_count.isna()].head())

  df_merged = df_purchase.merge(df_items, on='item_id', how='right')
  print(df_merged[df_merged.purchase_id.isna()].head())

  df_merged = df_purchase.merge(df_items, on='item_id', how='inner')
  print(df_merged.item_id.count())
  df_merged['revenue'] = df_merged['stock_count'] * df_merged['price']
  print(df_merged.sort_values('revenue', ascending=False).head(100))
  print(df_merged.revenue.sum())


import os

if False:
  files = os.listdir('data')
  print(files)

if False:
  files = ['setup.py', 'ratings.txt', 'stock_stats.txt', 'movies.txt', 'run.sh', 'game_of_thrones.mov']
  data = list(filter(lambda x: 'txt' in x, files))
  print(data)

if False:
  for root, dirs, files in os.walk('.'):
    print(root, dirs, files)

if False:
  data = pd.DataFrame(columns = ['userId', 'movieId', 'rating', 'timestamp'])
  for root, dirs, files in os.walk('data'):
    for file in files:
      temp = pd.read_csv(os.path.join(root, file), names=['userId', 'movieId', 'rating', 'timestamp'])
      data = pd.concat([data, temp])
  print(data.info())

if False:
  df_ratings = pd.read_csv('ratings.csv')
  print(df_ratings.count())
  print(df_ratings[df_ratings.rating == df_ratings.rating.min()].count())

if False:
  df_ratings = pd.read_csv('ratings.csv')
  df_movies = pd.read_csv('movies.csv')
  df_merged = df_ratings.merge(df_movies, on="movieId", how="right")
  print(df_ratings.info(), df_movies.info(), df_merged.info())
    # print(root, dirs, files)
if True:
  df_movies = pd.read_csv('movies.csv')
  df_ratings = pd.read_csv('ratings.csv')
  print(df_movies[df_movies.movieId == 3456].head())
  print(df_ratings[df_ratings.movieId == 3456].head())

