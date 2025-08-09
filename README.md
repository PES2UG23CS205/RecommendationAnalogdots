AnalogDots Machine Learning Engineer Competency Assessment
Introduction

This repository contains a comprehensive solution for the AnalogDots Machine Learning Engineer/Data Scientist competency assessment. The project implements a robust, end-to-end system designed to enhance the customer experience through intelligent shoe recommendations and personalized, data-driven services. It features a hybrid recommendation engine, the logic for proactive user services, a scalable database schema, and an interactive web application for demonstration, showcasing a full spectrum of data science and engineering skills.
🎥 Video Demonstration

A complete walkthrough and demonstration of the project, including the recommendation output and an explanation of the personalized services, can be found at the link below.

▶️ Click here to watch the project demonstration on YouTube
🛠️ Tech Stack & Requirements

This project leverages a modern Python data science and web development stack to deliver a functional and efficient solution.

    Programming Language: Python 3.x

    Core Libraries:

        Pandas & NumPy: For data manipulation and numerical operations.

        Scikit-learn: For content-based filtering (TF-IDF, Cosine Similarity) and data preprocessing (MinMaxScaler).

        SciPy: For Singular Value Decomposition (SVD) in the collaborative filtering model.

    Web Framework:

        Streamlit: To create and serve the interactive web application demo.

    Database Schema:

        PostgreSQL: The schema is designed for this robust, open-source relational database.

🚀 How to Run the Project

Follow these instructions to set up the environment and run the interactive web application on your local machine.
1. Prerequisites

    Git installed on your system.

    Python 3.9+ installed on your system.

2. Environment Setup

Clone the repository and set up a virtual environment.
code Bash
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END

      
# Clone the repository to your local machine
git clone https://github.com/your-username/your-repository-name.git

# Navigate into the project directory
cd your-repository-name

# Create a Python virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

    

3. Install Dependencies

Install all the required libraries using the requirements.txt file.
code Bash
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END

      
pip install -r requirements.txt

    

4. Running the Application

Launch the Streamlit web application. This is the primary method for viewing the project's output.
code Bash
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END

      
streamlit run app.py

    

A new tab will automatically open in your default web browser, pointing to the running application.
🧠 Recommendation Algorithm: A Hybrid Approach
Chosen Algorithm: Hybrid (Collaborative Filtering + Content-Based Filtering)

The core of this project is a Hybrid Recommender System. This model intelligently combines the outputs of two powerful recommendation techniques:

    Collaborative Filtering (CF): Implemented using Singular Value Decomposition (SVD), a matrix factorization technique. It analyzes the user-interaction matrix (views, purchases) to uncover latent "taste" factors for users and "attribute" factors for shoes. It excels at finding novel, serendipitous items by identifying users with similar behavior patterns.

    Content-Based Filtering (CBF): Implemented using TF-IDF (Term Frequency-Inverse Document Frequency) and Cosine Similarity. It vectorizes the textual attributes of shoes (brand, type, material, color) and recommends items that are fundamentally similar to what a user has liked in the past. This is excellent for providing explainable and safe recommendations.

Rationale and Problem-Solving

A single-algorithm approach has inherent weaknesses. A hybrid model was chosen because it mitigates these weaknesses and provides a superior, more resilient solution.

    Solves the Cold-Start Problem: When a new shoe is added to the catalog, it has no interactions, making it invisible to a pure CF model. Our hybrid model can still recommend it effectively using its content features (CBF).

    Improves Accuracy and Relevance: By blending signals from user behavior (CF) and item attributes (CBF), the final recommendations are more robust, accurate, and less prone to bias from a single data source.

    Enhances Serendipity and Diversity: The CF component can suggest unexpected items that a user might love, while the CBF component ensures the recommendations remain relevant and grounded in the user's known preferences, creating a balanced and satisfying discovery experience.

The final recommendation score for a shoe is a weighted average of its normalized CF and CBF scores, allowing for fine-tuning of the recommendation logic.
💡 Personalized Service Logic

To drive user engagement and lifetime value, I designed the logic for two data-driven personalized services.
1. Proactive Care Notifications

    Objective: To build customer trust and loyalty by helping them maintain their purchases, demonstrating that our service extends beyond the point of sale.

    Logic:

        The system identifies shoes a user has purchased.

        After a predefined interval (e.g., 30 days) from the purchase date, a trigger is activated.

        A notification is generated that includes the specific care_instructions for that shoe model, pulled directly from the shoe catalog.

    Business Value: This simple, helpful nudge fosters a positive brand relationship and encourages responsible product ownership, which can lead to higher customer satisfaction and repeat business.

2. Shoe Replacement Suggestions

    Objective: To create timely, relevant, and highly personalized up-sell opportunities by predicting when a customer's shoes are wearing out.

    Logic:

        For each shoe a user has purchased, the system retrieves its estimated lifespan_days from the product data.

        It calculates an estimated_end_of_life_date by adding the lifespan to the original purchase date.

        If the current date is near or past this estimated date, the service is triggered.

        Crucially, it then leverages the content-based similarity model to recommend shoes that are very similar in style, type, and brand to the one being replaced.

    Business Value: This transforms a potential customer loss (when a shoe wears out) into a high-conversion sales opportunity. The suggestions are contextually perfect, reducing friction for the customer to make their next purchase.

🗄️ Database Schema Design

The database schema, defined in schema.sql, is designed for PostgreSQL with scalability, performance, and data integrity as its core principles.

    Logical Normalization: The schema is normalized to prevent data redundancy. User, shoe, and interaction data are stored in separate tables (users, shoes, interactions) and linked via foreign keys. This ensures that an update to a shoe's brand, for example, only needs to happen in one place.

    Performance and Scalability:

        Strategic Indexing: Indexes are created on user_id and shoe_id in the interactions table. As this table will grow to millions or billions of rows, these indexes are critical for ensuring that recommendation generation (which queries by user) remains fast and efficient.

        Appropriate Data Types: The schema uses efficient and appropriate data types (e.g., TIMESTAMPTZ for timezone-aware timestamps, SERIAL for auto-incrementing keys, VARCHAR with reasonable limits).

    Designed for Personalization: The schema was built to directly support the proposed services. The shoes table includes care_instructions and lifespan_days, and I have included a forward-thinking user_shoe_care table to potentially track care history for even smarter notifications in the future.

📊 Synthetic Dataset

The synthetic dataset, located in the /data directory, was created to realistically simulate the data context described in the assessment. It consists of three CSV files:

    users.csv: Contains user profiles, including ID, age, gender, and primary_usage. This last feature helps simulate a basic user segment for potential future personalization.

    shoes.csv: Represents the product catalog. It includes standard attributes (brand, model, type) and the specific fields required for the personalized services: care_instructions and lifespan_days.

    interactions.csv: This is the core behavioral dataset. It logs user actions (view, add_to_wishlist, purchase) with timestamps, simulating a real-world event stream that fuels the collaborative filtering model. The interactions are weighted to give more importance to high-intent actions like purchases.

Conclusion

This project successfully delivers on all the objectives outlined in the assessment. It provides a functional, well-engineered hybrid recommendation system that is more robust than single-algorithm approaches. It goes beyond simple recommendations by defining practical and valuable personalized services that can directly impact business metrics like customer retention and sales. The entire system is supported by a thoughtful and scalable database design, demonstrating an understanding of production-level data management. The final interactive web application serves as a clear and effective demonstration of these capabilities.
