import streamlit as st
import pandas as pd
from recommendation_system.data_loader import load_data
from recommendation_system.recommender import HybridRecommender
from recommendation_system.personalized_services import get_proactive_care_notifications, get_shoe_replacement_suggestions

# --- Page Configuration ---
st.set_page_config(
    page_title="AnalogDots Shoe Recommender",
    page_icon="👟",
    layout="wide"
)

# --- Caching ---
# Use st.cache_data for caching data and models
@st.cache_data
def load_and_prepare_data():
    """
    Loads data and fits the recommender model.
    The @st.cache_data decorator ensures this function only runs once.
    """
    users_df, shoes_df, interactions_df = load_data(data_path='./data')
    if users_df is None:
        st.error("Failed to load data. Check console for errors.")
        return None, None, None, None
        
    recommender = HybridRecommender(n_svd_factors=2, cf_weight=0.7, cb_weight=0.3)
    recommender.fit(shoes_df, interactions_df)
    
    return recommender, users_df, shoes_df, interactions_df

# --- Main Application ---
st.title("👟 AnalogDots Personalized Shoe Engine")
st.markdown("This app demonstrates a hybrid recommendation system and personalized services for shoe customers.")

# Load data and model with a spinner
with st.spinner('Warming up the recommendation engine... This may take a moment.'):
    recommender, users_df, shoes_df, interactions_df = load_and_prepare_data()

if recommender:
    # --- Sidebar for User Input ---
    st.sidebar.header("Select a User")
    user_list = users_df['user_id'].unique()
    selected_user_id = st.sidebar.selectbox(
        "Choose a user ID to see their personalized results:",
        user_list
    )

    if st.sidebar.button("Generate My Feed", type="primary"):
        st.success(f"### Personalizing feed for User {selected_user_id}")

        # --- 1. Display Recommendations ---
        st.header("Top Shoe Recommendations For You")
        
        with st.spinner('Generating hybrid recommendations...'):
            recommendations = recommender.recommend(user_id=selected_user_id, top_n=5)

        if not recommendations.empty:
            st.dataframe(
                recommendations[['shoe_id', 'brand', 'model', 'type', 'color', 'material']],
                use_container_width=True,
                hide_index=True
            )
        else:
            st.warning("Could not generate recommendations for this user. They may be new or have limited interactions.")

        st.divider()

        # --- 2. Display Personalized Services ---
        st.header("Your Personalized Services")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("💡 Proactive Care Notifications")
            with st.spinner('Checking your shoe collection...'):
                care_notifications = get_proactive_care_notifications(selected_user_id, interactions_df, shoes_df)
            
            if care_notifications:
                for msg in care_notifications:
                    st.info(msg)
            else:
                st.write("No care reminders for you at this time. Great job!")

        with col2:
            st.subheader("♻️ Shoe Replacement Suggestions")
            with st.spinner('Analyzing shoe wear-and-tear...'):
                replacement_suggestions = get_shoe_replacement_suggestions(selected_user_id, interactions_df, shoes_df, recommender)

            if replacement_suggestions:
                for shoe_name, replacements_df in replacement_suggestions.items():
                    st.markdown(f"Your **{shoe_name}** might be wearing out. Consider these alternatives:")
                    st.table(replacements_df)
            else:
                st.write("All your shoes seem to be in good shape!")

    else:
        st.info("Select a user from the sidebar and click 'Generate My Feed' to get started.")

else:
    st.error("Application could not start. Recommender model failed to load.")