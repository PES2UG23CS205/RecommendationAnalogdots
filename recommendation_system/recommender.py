import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from scipy.sparse.linalg import svds
import numpy as np

class HybridRecommender:
    """
    A Hybrid Recommender System combining Content-Based Filtering and
    Collaborative Filtering (using SVD).
    """
    def __init__(self, n_svd_factors=2, cf_weight=0.7, cb_weight=0.3):
        self.n_svd_factors = n_svd_factors
        self.cf_weight = cf_weight
        self.cb_weight = cb_weight
        
        # Content-Based attributes
        self.tfidf_matrix = None
        self.cosine_sim = None
        
        # Collaborative Filtering attributes
        self.user_item_matrix = None
        self.preds_df = None
        
        # Data
        self.shoes_df = None
        self.interactions_df = None

    def _create_content_features(self):
        """Creates a TF-IDF matrix from shoe attributes."""
        # Combine relevant text features into a single string
        self.shoes_df['content'] = self.shoes_df.apply(
            lambda row: f"{row['brand']} {row['type']} {row['material']} {row['color']}", axis=1
        )
        tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = tfidf.fit_transform(self.shoes_df['content'])
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

    def _create_interaction_matrix(self):
        """Creates the user-item interaction matrix for collaborative filtering."""
        # Assign weights to interactions
        interaction_weights = {'view': 1.0, 'add_to_wishlist': 3.0, 'purchase': 5.0}
        self.interactions_df['interaction_strength'] = self.interactions_df['interaction_type'].map(interaction_weights)
        
        # Create a user-item matrix
        self.user_item_matrix = self.interactions_df.groupby(['user_id', 'shoe_id'])['interaction_strength'].max().unstack().fillna(0)

    def fit(self, shoes_df, interactions_df):
        """
        Fits the recommender models on the provided data.
        
        Args:
            shoes_df (pd.DataFrame): DataFrame of shoe attributes.
            interactions_df (pd.DataFrame): DataFrame of user-shoe interactions.
        """
        print("Fitting the hybrid recommender...")
        self.shoes_df = shoes_df.copy().set_index('shoe_id')
        self.interactions_df = interactions_df.copy()
        
        # 1. Fit Content-Based Model
        self._create_content_features()
        
        # 2. Fit Collaborative Filtering Model (SVD)
        self._create_interaction_matrix()
        
        # De-mean the data (normalize by each user's mean)
        R = self.user_item_matrix.values
        user_ratings_mean = np.mean(R, axis=1)
        R_demeaned = R - user_ratings_mean.reshape(-1, 1)
        
        # Perform Singular Value Decomposition
        U, sigma, Vt = svds(R_demeaned, k=self.n_svd_factors)
        sigma = np.diag(sigma)
        
        # Reconstruct the matrix with predicted ratings
        all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)
        
        self.preds_df = pd.DataFrame(
            all_user_predicted_ratings,
            columns=self.user_item_matrix.columns,
            index=self.user_item_matrix.index
        )
        print("Fit complete.")

    def recommend(self, user_id, top_n=5):
        """
        Generates top N recommendations for a given user.
        
        Args:
            user_id (int): The ID of the user to recommend for.
            top_n (int): The number of recommendations to return.
            
        Returns:
            pd.DataFrame: A DataFrame of recommended shoes.
        """
        if self.preds_df is None or self.cosine_sim is None:
            raise RuntimeError("The recommender has not been fitted yet. Call fit() first.")
        if user_id not in self.preds_df.index:
            print(f"User {user_id} not found. Returning top popular items (not implemented).")
            # Fallback strategy (e.g., return most popular shoes) could be implemented here
            return pd.DataFrame()

        # --- 1. Get Collaborative Filtering Scores ---
        cf_scores = self.preds_df.loc[user_id].sort_values(ascending=False)
        
        # --- 2. Get Content-Based Scores ---
        # Find user's top-rated/interacted shoe to find similar items
        user_interactions = self.interactions_df[self.interactions_df['user_id'] == user_id]
        if user_interactions.empty:
             # Cold start user: rely on popularity or random items
            return pd.DataFrame()
        
        # Find the shoe the user interacted with most strongly
        top_shoe_id = user_interactions.sort_values('interaction_strength', ascending=False).iloc[0]['shoe_id']
        top_shoe_idx = self.shoes_df.index.get_loc(top_shoe_id)
        
        # Get pairwise similarity scores for the user's favorite shoe
        cb_scores_raw = self.cosine_sim[top_shoe_idx]
        cb_scores = pd.Series(cb_scores_raw, index=self.shoes_df.index)
        
        # --- 3. Hybrid Combination ---
        # Normalize scores to be on the same scale (0-1)
        scaler = MinMaxScaler()
        cf_scores_norm = pd.Series(scaler.fit_transform(cf_scores.values.reshape(-1, 1)).flatten(), index=cf_scores.index)
        cb_scores_norm = pd.Series(scaler.fit_transform(cb_scores.values.reshape(-1, 1)).flatten(), index=cb_scores.index)

        # Combine scores with weights
        hybrid_scores = (self.cf_weight * cf_scores_norm) + (self.cb_weight * cb_scores_norm)
        
        # Filter out shoes the user has already purchased
        purchased_shoes = self.interactions_df[
            (self.interactions_df['user_id'] == user_id) & 
            (self.interactions_df['interaction_type'] == 'purchase')
        ]['shoe_id']
        
        recommendations = hybrid_scores.drop(purchased_shoes, errors='ignore').sort_values(ascending=False)
        
        # Get top N recommendations
        top_recs_ids = recommendations.head(top_n).index
        return self.shoes_df.loc[top_recs_ids].reset_index()