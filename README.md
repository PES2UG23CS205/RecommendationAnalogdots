👟 AnalogDots Shoe Recommendation Engine 👟
A Competency Assessment for the Machine Learning Engineer Role
</div>


This repository contains a comprehensive solution for the AnalogDots competency assessment. It features a hybrid recommendation engine, the logic for proactive user services, a scalable database schema, and an interactive web application for demonstration.

The core mission is to enhance the customer experience through intelligent, data-driven personalization.

<br>

🎥 Video Demonstration

A complete walkthrough and demonstration of the project, including the recommendation output and an explanation of the personalized services, can be found at the link below.

➡️ Watch the Project Demonstration Here
<br>

🛠️ Tech Stack

This project leverages a modern Python data science and web development stack to deliver a functional and efficient solution.

![alt text](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)


![alt text](https://img.shields.io/badge/Pandas-2.x-blue?style=for-the-badge&logo=pandas)


![alt text](https://img.shields.io/badge/NumPy-1.2x-blue?style=for-the-badge&logo=numpy)


![alt text](https://img.shields.io/badge/Scikit--learn-1.x-orange?style=for-the-badge&logo=scikit-learn)


![alt text](https://img.shields.io/badge/Streamlit-1.x-red?style=for-the-badge&logo=streamlit)


![alt text](https://img.shields.io/badge/PostgreSQL-Schema-blue?style=for-the-badge&logo=postgresql)

<br>

🚀 How to Run the Project

Follow these instructions to set up the environment and run the interactive web application on your local machine.

1. Prerequisites

Git installed.

Python 3.9+ installed.

2. Clone the Repository
code
Bash
download
content_copy
expand_less

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
3. Set Up Virtual Environment

It is highly recommended to use a virtual environment.

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# Create the environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
4. Install Dependencies

Install all required libraries from the requirements.txt file.

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
pip install -r requirements.txt
5. Launch the Application

Run the Streamlit app. Your browser will automatically open with the interactive demo.

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
streamlit run app.py
<br>

🧠 Recommendation Algorithm: A Hybrid Approach
Chosen Algorithm: Hybrid (Collaborative Filtering + Content-Based Filtering)

The core of this project is a Hybrid Recommender System that intelligently combines the outputs of two powerful recommendation techniques:

👥 Collaborative Filtering (CF): Implemented using Singular Value Decomposition (SVD). It analyzes the user-interaction matrix to uncover latent "taste" factors for users and "attribute" factors for shoes.

📝 Content-Based Filtering (CBF): Implemented using TF-IDF and Cosine Similarity. It recommends items based on their fundamental attributes (brand, type, material), finding shoes similar to what a user has previously liked.

Rationale & Problem-Solving

A hybrid model was chosen because it mitigates the weaknesses of any single algorithm, providing a superior and more resilient solution.

Solves the Cold-Start Problem: The content-based component can recommend new shoes that have no interaction history, a failure point for pure collaborative filtering.

Improves Accuracy & Relevance: By blending signals from user behavior (CF) and item attributes (CBF), the recommendations are more robust and accurate.

Enhances Serendipity: The model creates a balanced discovery experience by providing both safe, similar recommendations (from CBF) and novel, unexpected ones (from CF).

<br>

💡 Personalized Service Logic

To drive user engagement and lifetime value, I designed the logic for two data-driven personalized services.

Service 1: Proactive Care Notifications

Objective: To build customer trust and loyalty by helping them maintain their purchases.

Logic: After a set period (e.g., 30 days) from a shoe's purchase date, the system generates a notification that includes the specific care_instructions for that model.

Business Value: This fosters a positive brand relationship and encourages responsible product ownership, leading to higher customer satisfaction.

Service 2: Shoe Replacement Suggestions

Objective: To create timely and highly relevant up-sell opportunities by predicting when shoes are wearing out.

Logic: The system calculates an estimated_end_of_life_date for each purchased shoe using its lifespan_days. As this date approaches, it leverages the content-based model to recommend shoes that are very similar in style and brand to the one needing replacement.

Business Value: This transforms a potential customer loss into a high-conversion sales opportunity with perfectly timed, context-aware suggestions.

<br>

🗄️ Database Schema Design

The schema.sql is designed for PostgreSQL with scalability, performance, and data integrity as its core principles.

✅ Logical Normalization: Prevents data redundancy by separating user, shoe, and interaction data into distinct tables linked by foreign keys.

⚡ Performance and Scalability: Employs strategic indexing on frequently queried columns (like user_id and shoe_id) to ensure recommendation generation remains fast, even with millions of rows.

🎯 Designed for Personalization: The schema was built to directly support the proposed services, including specific columns like care_instructions and lifespan_days in the shoes table.

<br>

📊 Synthetic Dataset

The dataset in the /data directory was created to realistically simulate the required data context.

users.csv: Contains user profiles and a primary_usage feature for potential segmentation.

shoes.csv: Represents the product catalog, including the special fields care_instructions and lifespan_days needed for the personalized services.

interactions.csv: A log of weighted user actions (view, add_to_wishlist, purchase) that fuels the behavioral side of the recommendation engine.

<br>

✨ Conclusion

This project successfully delivers a functional, well-engineered hybrid recommendation system that is more robust than single-algorithm approaches. It goes beyond simple recommendations by defining practical and valuable personalized services that can directly impact key business metrics. The entire system is supported by a thoughtful and scalable database design, demonstrating a holistic understanding of building and deploying production-ready machine learning systems.
