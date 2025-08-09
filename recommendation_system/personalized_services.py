import pandas as pd
from datetime import datetime, timedelta, timezone

def get_proactive_care_notifications(user_id, interactions_df, shoes_df):
    """
    Generates proactive care notifications for a user.

    Returns:
        list: A list of notification message strings.
    """
    notifications = []
    
    user_purchases = interactions_df[
        (interactions_df['user_id'] == user_id) & 
        (interactions_df['interaction_type'] == 'purchase')
    ]
    
    if user_purchases.empty:
        return []

    for _, purchase in user_purchases.iterrows():
        shoe_id = purchase['shoe_id']
        purchase_date = purchase['timestamp']
        
        if (datetime.now(timezone.utc) - purchase_date) > timedelta(days=30):
            shoe_details = shoes_df[shoes_df['shoe_id'] == shoe_id].iloc[0]
            shoe_name = f"{shoe_details['brand']} {shoe_details['model']}"
            care_tip = shoe_details['care_instructions']
            
            message = (f"Time for some TLC! Remember to care for your **{shoe_name}**. "
                       f"Pro Tip: '{care_tip}'.")
            notifications.append(message)
            
    return notifications


def get_shoe_replacement_suggestions(user_id, interactions_df, shoes_df, recommender):
    """
    Generates shoe replacement suggestions based on estimated wear.

    Returns:
        dict: A dictionary where keys are expiring shoe names and values are DataFrames
              of recommended replacements.
    """
    replacement_suggestions = {}

    user_purchases = interactions_df[
        (interactions_df['user_id'] == user_id) & 
        (interactions_df['interaction_type'] == 'purchase')
    ]
    
    if user_purchases.empty:
        return {}

    for _, purchase in user_purchases.iterrows():
        shoe_id = purchase['shoe_id']
        purchase_date = purchase['timestamp']
        
        shoe_details = shoes_df.set_index('shoe_id').loc[shoe_id]
        lifespan = shoe_details['lifespan_days']
        
        if pd.isna(lifespan):
            continue
        
        # === THIS IS THE CRUCIAL FIX ===
        # The numpy.int64 'lifespan' is explicitly converted to a standard Python 'int'.
        end_of_life_date = purchase_date + timedelta(days=int(lifespan))
        
        if datetime.now(timezone.utc) >= (end_of_life_date - timedelta(days=30)):
            shoe_name = f"{shoe_details['brand']} {shoe_details['model']}"
            
            # Get content-based similar items
            shoe_idx = recommender.shoes_df.index.get_loc(shoe_id)
            sim_scores = list(enumerate(recommender.cosine_sim[shoe_idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            
            top_similar_shoes_indices = [i[0] for i in sim_scores[1:4]]
            replacement_ids = recommender.shoes_df.index[top_similar_shoes_indices]
            
            recommendations_df = recommender.shoes_df.loc[replacement_ids]
            replacement_suggestions[shoe_name] = recommendations_df[['brand', 'model', 'type', 'material']]
            
    return replacement_suggestions