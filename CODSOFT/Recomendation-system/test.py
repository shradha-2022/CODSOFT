import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset (you'll need to load your own dataset)
data = {
    'Title': ['Book A', 'Book B', 'Book C'],
    'Author': ['Author X', 'Author Y', 'Author Z'],
    'Genre': ['Fiction', 'Non-fiction', 'Fiction'],
    'Description': ['Description of Book A', 'Description of Book B', 'Description of Book C']
}

# Create a DataFrame from the sample data
books_df = pd.DataFrame(data)

# Data Preprocessing
# Combine relevant text features into a single feature
books_df['Combined_Features'] = books_df['Title'] + ' ' + books_df['Author'] + ' ' + books_df['Genre'] + ' ' + books_df['Description']

# Vectorize text data using TF-IDF
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(books_df['Combined_Features'])

# Content-Based Filtering
# Calculate cosine similarity between books based on their feature vectors
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendations
def recommend_books(book_index, num_recommendations=5):
    # Get similarity scores for the given book index
    similarity_scores = list(enumerate(cosine_sim[book_index]))

    # Sort books based on similarity scores
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Get top similar books (excluding the given book)
    top_books_indices = [x[0] for x in similarity_scores[1:num_recommendations+1]]

    return books_df.iloc[top_books_indices]

# Example: Recommend books similar to Book B (index 1)
similar_books = recommend_books(book_index=1)
print(similar_books)
