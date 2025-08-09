AnalogDots ML Engineer / Data Scientist Competency Assessment

Python Version
Libraries
Status
Introduction & Project Goal

This repository contains a comprehensive solution for the AnalogDots competency assessment. The goal is to design and implement a data-driven system that provides tangible business value by:

    Building a personalized shoe recommendation engine.

    Implementing business logic for customer-centric personalized services.

    Creating an interactive web interface for demonstration.

    Designing a scalable and efficient PostgreSQL database schema.

Key Features
Hybrid Recommendation Engine

    Combines Collaborative Filtering (CF) and Content-Based Filtering (CBF) for diverse, relevant, and accurate shoe recommendations.

Interactive Web UI

    Built with Streamlit for real-time visualization of recommendations and personalized services.

Proactive Personalized Services

    Smart Care Notifications: Remind users how to care for their shoes to boost longevity and loyalty.

    Automated Replacement Suggestions: Detects when shoes near end-of-life and recommends similar replacements to drive repeat sales.

Scalable Database Design

    A normalized PostgreSQL schema optimized for performance and future feature expansion.

Technical Deep Dive
1. Recommendation Algorithm: Hybrid Approach

Collaborative Filtering (CF)

    Uses Singular Value Decomposition (SVD) to analyze user-item interactions and discover latent features.

    Great for serendipitous and novel recommendations.

Content-Based Filtering (CBF)

    Utilizes TF-IDF Vectorizer to convert shoe attributes into vectors and Cosine Similarity to find similar items.

    Solves the cold-start problem and provides explainable recommendations.

Hybrid Model

    Combines CF and CBF results with a weighted average for better accuracy, diversity, and robustness.

2. Personalized Service Logic

    Care Notifications: Triggered based on purchase history and sends shoe-specific care tips after a set period (e.g., 30 days).

    Replacement Suggestions: Calculates shoe lifespan and recommends replacements using the content-based model as the end-of-life approaches.

3. Database Schema Design (schema.sql)

    Designed for production use with PostgreSQL.

    Fully normalized tables (users, shoes, interactions) reduce redundancy.

    Indexed columns for efficient real-time lookups.

    Supports future features with additional tables and columns (e.g., user_shoe_care, environmental_data, lifespan_days).

Technology Stack

    Language: Python 3.11+

    Core Libraries: Pandas, NumPy, Scikit-learn

    Web Framework: Streamlit

    Database: PostgreSQL

    Version Control: Git & GitHub
Setup and Execution
Step 1: Clone the Repository

git clone https://github.com/YourUsername/your-repo-name.git
cd your-repo-name

(Replace with your actual repository details)
Step 2: Create and Activate a Virtual Environment
Create virtual environment

python -m venv venv

Activate it

    On Windows:

venv\Scripts\activate

    On macOS/Linux:

source venv/bin/activate

Step 3: Install Required Libraries

pip install -r requirements.txt

Step 4: Run the Streamlit Web Application

streamlit run app.py

The app will open in your default browser. You can now select different users and explore personalized recommendations and services.

