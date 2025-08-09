AnalogDots ML Engineer / Data Scientist Competency Assessment

![alt text](https://img.shields.io/badge/Python-3.11+-blue.svg)

![alt text](https://img.shields.io/badge/Libraries-Pandas%20%7C%20Scikit--learn%20%7C%20Streamlit-orange.svg)

![alt text](https://img.shields.io/badge/Status-Completed-green.svg)

🎯 Introduction & Project Goal

This repository presents a comprehensive solution for the AnalogDots competency assessment. The primary goal is to design and implement a system that provides tangible business value through data. This is achieved via:

    A fully functional, personalized shoe recommendation engine.

    Business logic for data-driven customer services.

    An interactive web interface for demonstration.

    A scalable and efficient database schema.

✨ Key Features

    ✅ Hybrid Recommendation Engine: Combines Collaborative and Content-Based filtering for accurate, diverse, and relevant shoe recommendations.

    ✅ Interactive Web UI: A user-friendly web application built with Streamlit to visualize recommendations and personalized services in real-time.

    ✅ Proactive Personalized Services:

        Smart Care Notifications: Reminds users how to care for their shoes to increase product longevity and customer loyalty.

        Automated Replacement Suggestions: Drives repeat sales by identifying when a user's shoes are nearing their end-of-life and recommending similar replacements.

    ✅ Scalable Database Design: A well-normalized PostgreSQL schema designed for performance and future feature expansion.

🚀 Technical Deep Dive
1. The Recommendation Algorithm: A Hybrid Approach

To provide the best possible recommendations, a Hybrid Model was chosen, fusing two powerful techniques:
Collaborative Filtering (CF)

    How it Works: Analyzes the behavior of all users to find others with similar tastes. It then recommends shoes that these "similar users" have liked.

    Implementation: Singular Value Decomposition (SVD), a matrix factorization technique, is used to uncover latent features in the user-item interaction data.

    Strength: Excellent for discovering new and unexpected items (serendipity).

Content-Based Filtering (CBF)

    How it Works: Recommends items based on their inherent attributes. If a user likes a "Nike running shoe," it will recommend other shoes with similar characteristics.

    Implementation: A TF-IDF Vectorizer converts shoe attributes into numerical vectors, and Cosine Similarity measures the likeness between any two shoes.

    Strength: Solves the "cold-start" problem for new shoes and provides highly relevant, explainable recommendations.

Why a Hybrid Model?

By combining these two models with a weighted average, the system gets the best of both worlds. It mitigates the weaknesses of each individual model, leading to higher accuracy, better diversity, and a more robust solution overall.
2. Personalized Service Logic

Beyond just recommending what to buy, the system is designed to engage users throughout their product ownership lifecycle.
Service 1: Proactive Care Notifications

    Objective: Increase customer lifetime value and brand loyalty.

    Logic: The system checks a user's purchase history. After a set period (e.g., 30 days), it triggers a notification containing the specific care_instructions for their purchased shoe.

    Business Value: This simple, helpful nudge shows that the brand cares about the customer post-purchase, building trust and engagement.

Service 2: Shoe Replacement Suggestions

    Objective: Drive timely, relevant, and repeat sales.

    Logic: Each shoe has an estimated lifespan_days. The system calculates the shoe's "end-of-life" date based on the purchase date. As this date approaches, it leverages the Content-Based Filtering model to find and recommend shoes that are stylistically similar to the one wearing out.

    Business Value: This creates a highly targeted sales opportunity, making it frictionless for a customer to repurchase a product they already love or a close alternative.

3. Database Schema Design (schema.sql)

The database is designed for a production environment using PostgreSQL. The schema is normalized, scalable, and built to support the recommendation and personalization features.

    Normalization: Data is organized into distinct tables (users, shoes, interactions) to reduce redundancy and ensure data integrity.

    Performance: Critical columns like user_id and shoe_id in the interactions table are indexed to ensure lightning-fast lookups, which is essential for real-time recommendations.

    Future-Proofing: The schema includes tables and columns (user_shoe_care, environmental_data, lifespan_days) to support more advanced features in the future.

🛠️ Technology Stack

    Language: Python 3.11+

    Core Libraries: Pandas, NumPy, Scikit-learn

    Web Framework: Streamlit

    Database: PostgreSQL (schema design)

    Version Control: Git & GitHub

⚙️ Setup and Execution
Prerequisites

    Git

    Python 3.10+

Step 1: Clone the Repository

Open your terminal and run the following command:
