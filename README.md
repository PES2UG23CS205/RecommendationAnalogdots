# AnalogDots ML Engineer / Data Scientist Competency Assessment

---
### 🎥 Project Demonstration
**A complete video walkthrough of the project, code, and live Streamlit demo can be found here:**

**[>>> YOUR PUBLIC/UNLISTED YOUTUBE VIDEO LINK HERE <<<]**
---

## Project Overview

This repository contains my submission for the AnalogDots competency assessment. The project implements a hybrid shoe recommendation system, outlines logic for personalized user services, and includes a scalable database schema design. The entire system is demonstrated through an interactive web application.

This solution achieves its goal through a three-pronged approach:

1.  **A Hybrid Recommendation Algorithm:** Combines the strengths of collaborative and content-based filtering to provide relevant and diverse suggestions.
2.  **Personalized Service Logic:** Defines two key services—Proactive Care Notifications and Shoe Replacement Suggestions—to enhance user engagement and drive repeat purchases.
3.  **A Scalable Data Infrastructure:** A well-designed PostgreSQL schema that efficiently stores the necessary data and is built for future growth.

## 1. Recommendation Algorithm Design

### Chosen Algorithm: Hybrid (Collaborative Filtering + Content-Based Filtering)

I chose a hybrid approach because it provides the most robust and practical solution, overcoming the limitations of using a single algorithm.

*   **Collaborative Filtering (CF) via SVD:** This technique is based on user-item interactions. It identifies users with similar tastes and recommends items that similar users have liked. I used **Singular Value Decomposition (SVD)**, a powerful matrix factorization method, to uncover latent factors in the user-item interaction matrix. This helps in predicting a user's preference for a shoe they haven't interacted with yet.
*   **Content-Based Filtering (CBF) via TF-IDF & Cosine Similarity:** This technique recommends items based on their attributes. It finds shoes that are similar to those a user has shown interest in before. I used **TF-IDF** to vectorize shoe attributes (brand, type, material) and **Cosine Similarity** to calculate the similarity between shoes. This method is excellent for solving the "cold start" problem for new shoes and providing explainable recommendations ("Because you liked Nike Running shoes...").

### Rationale & How It Addresses the Problem

The hybrid model combines the scores from both CF and CBF using a weighted average: `Final_Score = (w_cf * CF_Score) + (w_cbf * CBF_Score)`.

*   **Benefits:**
    *   **Reduces Cold-Start Problem:** If a user or item is new, CF struggles. The content-based component can still provide sensible recommendations.
    *   **Increases Diversity & Serendipity:** CF can find unexpected but relevant items (serendipity), while CBF ensures recommendations are grounded in the user's known preferences.
    *   **Improves Accuracy:** The combination of signals (user behavior + item attributes) leads to more accurate and satisfying recommendations than either model alone.

## 2. Personalized Service Logic

I have designed the logic for two personalized service features. The implementation is detailed in `recommendation_system/personalized_services.py`.

### Service 1: Proactive Care Notifications

*   **Objective:** To increase customer lifetime value and brand loyalty by helping users maintain their purchases.
*   **Logic:**
    1.  **Trigger:** A user has purchased a shoe.
    2.  **Action:** After a set period (e.g., 30 days post-purchase), the system sends a notification.
    3.  **Content:** The notification includes the specific `care_instructions` for that shoe model, pulled directly from our shoe data.
    4.  **Business Value:** This simple, helpful nudge shows that AnalogDots cares about the customer post-purchase, building trust and engagement.

### Service 2: Shoe Replacement Suggestions

*   **Objective:** To drive repeat sales by proactively suggesting replacements for worn-out shoes.
*   **Logic:**
    1.  **Trigger:** A purchased shoe is nearing its estimated end of life. This is calculated as `purchase_date + lifespan_days`.
    2.  **Action:** The system identifies that the shoe might need replacing.
    3.  **Content:** It then generates a list of recommended replacements. **Crucially, these recommendations are generated using the content-based similarity model**, suggesting shoes that are very similar in style, brand, and type to the one being replaced.
    4.  **Business Value:** This creates a timely and highly relevant sales opportunity, making it easy for the customer to buy a similar pair they are likely to love.

## 3. Interactive Web Application (Streamlit Demo)

To provide a tangible and user-friendly way to demonstrate the system's capabilities, this project includes an interactive web application built with Streamlit. This moves beyond simple console output and allows an evaluator to experience the personalization engine in real-time.

**Key Features of the App:**
*   **User Selection:** A dropdown menu in the sidebar allows for the selection of any user from the dataset.
*   **Dynamic Generation:** A "Generate My Feed" button triggers the recommendation and personalization logic for the selected user.
*   **Clear Layout:** The results are presented in a clean, multi-column layout:
    *   **Shoe Recommendations:** The output of the hybrid recommender is displayed in a clear table.
    *   **Personalized Services:** Notifications for proactive care and shoe replacements are shown with distinct styling to mimic a real user feed.
*   **User Experience:** Loading spinners provide feedback to the user while the backend models are running, ensuring a smooth experience.

This web interface serves as the primary method for demonstrating the functionality of the implemented algorithms and business logic.

## 4. Database Schema Design

The database schema is defined in `schema.sql`. It is designed for PostgreSQL.

### Design Rationale:

*   **Normalization:** The schema is normalized to reduce data redundancy and improve data integrity. For instance, user and shoe information are stored in separate tables (`users`, `shoes`) and linked in the `interactions` table using foreign keys.
*   **Scalability & Performance:**
    *   **Indexing:** I've added indices on frequently queried columns, such as `interactions(user_id)`. This is critical for fast lookups when generating recommendations.
    *   **Data Types:** Appropriate data types are used (e.g., `TIMESTAMPTZ` for time-aware data).
*   **Support for Personalization:**
    *   The `shoes` table includes `care_instructions` and `lifespan_days`, which directly feed the personalized services.
    *   I've included `user_shoe_care` and `environmental_data` tables to demonstrate forward-thinking design for future, more advanced features.

## 5. Synthetic Dataset

The synthetic dataset is located in the `/data` folder and simulates real-world data needed to power the system. It consists of `shoes.csv`, `users.csv`, and `interactions.csv`.

## 6. Setup and How to Run

1.  **Clone the repository:**
    ```bash
    git clone <your_repo_link>
    cd analogdots-recommender-assessment
    ```

2.  **Set up a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit Web Application:**
    This is the primary way to view the project's output. It will open a new tab in your web browser with the interactive demo.
    ```bash
    streamlit run app.py
    ```

5.  **(Optional) Run the original command-line script:**
    If you wish to see the original console output, you can still run the `main.py` script.
    ```bash
    python recommendation_system/main.py
    ```
