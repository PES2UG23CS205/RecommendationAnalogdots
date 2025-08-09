from recommendation_system.data_loader import load_data
from recommendation_system.recommender import HybridRecommender
from recommendation_system.personalized_services import proactive_care_notifications, shoe_replacement_suggestions

def main():
    """
    Main function to run the demonstration.
    """
    # Load the data
    users_df, shoes_df, interactions_df = load_data(data_path='./data')
    if users_df is None:
        return

    # Initialize and fit the recommender
    # We give more weight to collaborative filtering as it captures user taste nuances,
    # but content-based is important for similarity and cold starts.
    recommender = HybridRecommender(n_svd_factors=2, cf_weight=0.7, cb_weight=0.3)
    recommender.fit(shoes_df, interactions_df)

    # --- DEMONSTRATION ---

    # == Task 1: Shoe Recommendation Algorithm ==
    test_user_id = 1
    print(f"\n==============================================")
    print(f"GENERATING RECOMMENDATIONS FOR USER ID: {test_user_id}")
    print(f"==============================================")
    
    recommendations = recommender.recommend(user_id=test_user_id, top_n=3)
    
    if not recommendations.empty:
        print("Top 3 Hybrid Recommendations:")
        print(recommendations[['shoe_id', 'brand', 'model', 'type']])
    else:
        print("Could not generate recommendations for this user.")
        
    # == Task 2: Personalized Service Logic ==
    print(f"\n==============================================")
    print(f"DEMONSTRATING PERSONALIZED SERVICES FOR USER ID: {test_user_id}")
    print(f"==============================================")

    # Service 1: Proactive Care Notifications
    proactive_care_notifications(test_user_id, interactions_df, shoes_df)
    
    # Service 2: Shoe Replacement Suggestions
    # Note: The recommender object is passed to reuse its content-similarity model
    shoe_replacement_suggestions(test_user_id, interactions_df, shoes_df, recommender)


if __name__ == '__main__':
    main()