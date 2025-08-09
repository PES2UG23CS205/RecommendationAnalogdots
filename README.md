# AnalogDots ML Engineer / Data Scientist Competency Assessment

---
### 🎥 Project Demonstration
**A complete video walkthrough of the project, code, and a live demo of the Streamlit application can be found at the link below.**

### **[>>> CLICK HERE FOR THE VIDEO DEMONSTRATION <<<](https://your-youtube-video-link-here.com)**
*(Please replace the link above with your actual unlisted YouTube video URL)*
---

## Project Overview

This repository contains my submission for the AnalogDots competency assessment. The project implements a hybrid shoe recommendation system, outlines logic for personalized user services, and includes a scalable database schema design. The entire system is demonstrated through an interactive web application.

This solution achieves its goal through a three-pronged approach:

1.  **A Hybrid Recommendation Algorithm:** Combines the strengths of collaborative and content-based filtering to provide relevant and diverse suggestions.
2.  **Personalized Service Logic:** Defines two key services—Proactive Care Notifications and Shoe Replacement Suggestions—to enhance user engagement and drive repeat purchases.
3.  **An Interactive Web Application:** A user-friendly Streamlit interface to demonstrate the system's capabilities in a tangible way.

## 1. Recommendation Algorithm Design

### Chosen Algorithm: Hybrid (Collaborative Filtering + Content-Based Filtering)

I chose a hybrid approach because it provides the most robust and practical solution, overcoming the limitations of using a single algorithm.

*   **Collaborative Filtering (CF) via SVD:** This technique is based on user-item interactions. It identifies users with similar tastes and recommends items that similar users have liked. I used **Singular Value Decomposition (SVD)**, a powerful matrix factorization method, to uncover latent factors in the user-item interaction matrix. This helps in predicting a user's preference for a shoe they haven't interacted with yet.
*   **Content-Based Filtering (CBF) via TF-IDF & Cosine Similarity:** This technique recommends items based on their attributes. It finds shoes that are similar to those a user has shown interest in before. I used **TF-IDF** to vectorize shoe attributes (brand, type, material) and **Cosine Similarity** to calculate the similarity between shoes. This method is excellent for solving the "cold start" problem for new shoes and providing explainable recommendations ("Because you liked Nike Running shoes...").

### Rationale & How It Addresses the Problem

The hybrid model combines the scores from both CF and CBF using a weighted average: `Final_Score = (w_cf * CF_Score) + (w_cbf * CBF_Score)`. This leads to more accurate, diverse, and resilient recommendations.

## 2. Personalized Service Logic

I have designed the logic for two personalized service features that directly leverage the available data to create business value.

### Service 1: Proactive Care Notifications

*   **Objective:** To increase customer lifetime value by helping users maintain their purchases.
*   **Logic:** The system identifies a user's purchased shoes and, after a set period, sends a notification containing the specific `care_instructions` for that model. This builds brand loyalty and user trust.

### Service 2: Shoe Replacement Suggestions

*   **Objective:** To drive repeat sales by proactively suggesting replacements for worn-out shoes.
*   **Logic:** The system calculates a shoe's estimated end-of-life based on its `lifespan_days`. As it nears this date, it uses the **content-based similarity model** to recommend stylistically similar shoes, creating a timely and highly relevant sales opportunity.

## 3. Interactive Web Application (Streamlit Demo)

To provide a tangible and user-friendly way to demonstrate the system's capabilities, this project includes an interactive web application built with Streamlit.

**Key Features of the App:**
*   **User Selection:** A dropdown menu allows for the selection of any user from the dataset.
*   **Dynamic Generation:** A "Generate My Feed" button triggers the recommendation and personalization logic for the selected user.
*   **Clear Layout:** The results are presented in a clean, multi-column layout, separating the main recommendations from the personalized service alerts.
*   **User Experience:** Loading spinners provide feedback to the user while the backend models are running, ensuring a smooth experience.

## 4. Database Schema Design

The database schema is defined in `schema.sql` and is designed for scalability and performance in a production PostgreSQL environment. It features normalized tables, primary/foreign key constraints for data integrity, and indexes on frequently queried columns to ensure fast lookups. The design includes tables not only for core functionality but also for future enhancements like `environmental_data`.

## 5. Conclusion and Future Work

This project successfully demonstrates an end-to-end prototype of a personalization engine, from data modeling and ML algorithm implementation to a user-facing interactive application. The chosen hybrid approach is robust, and the personalized services are practical and directly tied to business objectives.

### Potential Enhancements
Given more time, the system could be extended with several advanced features:
*   **Deep Learning Models:** Incorporate neural network-based models (e.g., using embeddings) to capture more complex user patterns.
*   **Real-Time Capabilities:** Integrate with a streaming platform like Apache Kafka to update recommendations in real-time as users interact with the site.
*   **Context-Aware Recommendations:** Fully implement the `environmental_data` table to suggest shoes based on the user's current weather (e.g., "It's raining, consider these waterproof options!").
*   **A/B Testing Framework:** Build a framework to rigorously test different recommendation models and strategies to continuously improve key metrics like click-through rate and conversion.
*   **Explainable AI (XAI):** Add features that explain *why* an item was recommended (e.g., "Because you purchased Nike Air Max 90").

## 6. Setup and How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/PES2UG23CS205/RecommendationAnalogdots.git
    cd RecommendationAnalogdots
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
