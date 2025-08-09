AnalogDots ML Engineer / Data Scientist Competency Assessment

![alt text](https://img.shields.io/badge/Python-3.11+-blue.svg)

![alt text](https://img.shields.io/badge/Libraries-Pandas%20%7C%20Scikit--learn%20%7C%20Streamlit-orange.svg)

![alt text](https://img.shields.io/badge/Status-Completed-green.svg)

Project Demonstration

A video demonstration of this project, created with OBS Studio, can be found at the link below. The video walks through the interactive Streamlit application, showcasing the recommendation engine and personalized services in action.

[INSERT YOUR OBS STUDIO VIDEO LINK HERE]
Introduction & Project Goal

This repository contains a comprehensive solution for the AnalogDots competency assessment. The goal is to design and implement a data-driven system that provides tangible business value by:

    Building a personalized shoe recommendation engine.

    Implementing business logic for customer-centric personalized services.

    Creating an interactive web interface for demonstration.

    Designing a scalable and efficient PostgreSQL database schema.

Key Features

    Hybrid Recommendation Engine: Combines Collaborative Filtering (CF) and Content-Based Filtering (CBF) for diverse, relevant, and accurate shoe recommendations.

    Interactive Web UI: A user-friendly web application built with Streamlit to visualize recommendations and personalized services in real-time.

    Proactive Personalized Services:

        Smart Care Notifications: Reminds users how to care for their shoes to increase product longevity and customer loyalty.

        Automated Replacement Suggestions: Drives repeat sales by identifying when a user's shoes are nearing their end-of-life and recommending similar replacements.

    Scalable Database Design: A well-normalized PostgreSQL schema designed for performance and future feature expansion.

Technical Deep Dive
1. The Recommendation Algorithm: A Hybrid Approach

To provide the best possible recommendations, a Hybrid Model was chosen, fusing two powerful techniques.
Collaborative Filtering (CF)

How it Works: Analyzes the behavior of all users to find others with similar tastes. It then recommends shoes that these "similar users" have liked.
Implementation: Singular Value Decomposition (SVD), a matrix factorization technique, is used to uncover latent features in the user-item interaction data.
Strength: Excellent for discovering new and unexpected items (serendipity).
Content-Based Filtering (CBF)

How it Works: Recommends items based on their inherent attributes. If a user likes a "Nike running shoe," it will recommend other shoes with similar characteristics.
Implementation: A TF-IDF Vectorizer converts shoe attributes into numerical vectors, and Cosine Similarity measures the likeness between any two shoes.
Strength: Solves the "cold-start" problem for new shoes and provides highly relevant, explainable recommendations.
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

    Performance: Critical columns like user_id and shoe_id in the interactions table are indexed to ensure lightning-fast lookups.

    Future-Proofing: The schema includes tables and columns (user_shoe_care, environmental_data, lifespan_days) to support more advanced features.

Technology Stack

    Language: Python 3.11+

    Core Libraries: Pandas, NumPy, Scikit-learn

    Web Framework: Streamlit

    Database: PostgreSQL (schema design)

    Version Control: Git & GitHub

Setup and Execution
Prerequisites

    Git

    Python 3.10+

Step 1: Clone the Repository
code Bash
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END

      
git clone https://github.com/YourUsername/your-repo-name.git
cd your-repo-name

    

(Replace with your actual repository details)
Step 2: Set Up a Virtual Environment

It is highly recommended to use a virtual environment to manage dependencies.
Create the environment
code Bash
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END

      
python -m venv venv

    

Activate it

On Windows:
code Bash
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END

      
venv\Scripts\activate

    

On macOS/Linux:
code Bash
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END

      
source venv/bin/activate

    

Step 3: Install Required Libraries
code Bash
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END

      
pip install -r requirements.txt

    

Step 4: Run the Streamlit Web Application

This command will start the local web server and open the application in your browser.
code Bash
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END

      
streamlit run app.py

    

You can now interact with the application, select different users, and see their personalized results.
Project Structure
code Code
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END

      
.
├── app.py                   # The main Streamlit web application script
├── schema.sql               # The PostgreSQL database schema design
├── requirements.txt         # List of Python dependencies for pip
├── README.md                # This file
├── .gitignore               # Specifies files for Git to ignore
│
└───data/                    # Contains the synthetic CSV datasets
│   ├── interactions.csv
│   ├── shoes.csv
│   └── users.csv
│
└───recommendation_system/   # Core Python module for all backend logic
    ├── __init__.py          # Makes the folder a Python package
    ├── data_loader.py       # Function to load and preprocess data
    ├── recommender.py       # Contains the HybridRecommender class
    ├── personalized_services.py # Logic for care/replacement services
    └── main.py              # Original script for command-line execution

    

