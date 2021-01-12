import codecademylib3_seaborn
import pandas as pd
import numpy as np
from articles import articles
from preprocessing import preprocess_text

# import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer,TfidfVectorizer

# view article
print(articles[1])

# preprocess articles
processed_articles = preprocess_text(articles[1])
print(processed_articles)



# initialize and fit CountVectorizer
vectorizer = CountVectorizer()


# convert counts to tf-idf
counts = vectorizer.fit_transform(articles)


# initialize and fit TfidfVectorizer
transformer = TfidfTransformer(norm=None)


# check if tf-idf scores are equal
tfidf_scores_transformed = transformer.fit_transform(counts)
vectorizer = TfidfVectorizer(norm=None)
tfidf_scores = vectorizer.fit_transform(articles)

if np.allclose(tfidf_scores_transformed.todense(), tfidf_scores.todense()):
  print(pd.DataFrame({'Are the tf-idf scores the same?':['YES']}))
else:
  print(pd.DataFrame({'Are the tf-idf scores the same?':['No, something is wrong :(']}))
# get vocabulary of terms
try:
  feature_names = vectorizer.get_feature_names()
except:
  pass

# get article index
try:
  article_index = [f"Article {i+1}" for i in range(len(articles))]
except:
  pass

# create pandas DataFrame with word counts
try:
  df_word_counts = pd.DataFrame(counts.T.todense(), index=feature_names, columns=article_index)
  print(df_word_counts)
except:
  pass

# create pandas DataFrame(s) with tf-idf scores
try:
  df_tf_idf = pd.DataFrame(tfidf_scores_transformed.T.todense(), index=feature_names, columns=article_index)
  print(df_tf_idf)
except:
  pass

try:
  df_tf_idf = pd.DataFrame(tfidf_scores.T.todense(), index=feature_names, columns=article_index)
  print(df_tf_idf)
except:
  pass

# get highest scoring tf-idf term for each article
for i in range(1,10):
    print(tfidf_scores_transformed[i],tfidf_scores[i])
    print(df_tf_idf[[f'Article {i}']].idxmax())