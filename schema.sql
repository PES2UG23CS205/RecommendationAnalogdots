-- schema.sql for AnalogDots Recommendation System

-- Disables annoying notices and sets timezone
SET client_min_messages TO WARNING;
SET time zone 'UTC';

-- Drop tables if they exist to ensure a clean slate
DROP TABLE IF EXISTS user_shoe_care CASCADE;
DROP TABLE IF EXISTS environmental_data CASCADE;
DROP TABLE IF EXISTS interactions CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS shoes CASCADE;

-- Users table to store user profile information
-- primary_usage helps in personalizing recommendations beyond interaction history
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    age INT,
    gender VARCHAR(10),
    primary_usage VARCHAR(50), -- e.g., 'Athletic', 'Casual', 'Office'
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Shoes table to store product catalog attributes
-- care_instructions and lifespan_days are crucial for personalized services
CREATE TABLE shoes (
    shoe_id INT PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(100) NOT NULL,
    type VARCHAR(50), -- e.g., 'Running', 'Casual', 'Boot'
    material VARCHAR(50),
    color VARCHAR(30),
    care_instructions TEXT,
    lifespan_days INT, -- Estimated lifespan in days for wear-and-tear notifications
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE(brand, model, color)
);

-- Interactions table to log all user activities
-- This is the core table for collaborative filtering.
-- An ENUM type is used for interaction_type for data consistency.
CREATE TABLE interactions (
    interaction_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    shoe_id INT NOT NULL REFERENCES shoes(shoe_id) ON DELETE CASCADE,
    interaction_type VARCHAR(20) NOT NULL CHECK (interaction_type IN ('view', 'add_to_wishlist', 'purchase')),
    timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indexing for performance:
-- Frequently queried columns in the interactions table
CREATE INDEX idx_interactions_user_id ON interactions(user_id);
CREATE INDEX idx_interactions_shoe_id ON interactions(shoe_id);

-- User Shoe Care table to track personalized care history
-- This table enables the proactive care notification service
CREATE TABLE user_shoe_care (
    care_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    shoe_id INT NOT NULL REFERENCES shoes(shoe_id) ON DELETE CASCADE,
    last_care_date DATE NOT NULL,
    UNIQUE(user_id, shoe_id) -- A user has one care record per shoe
);

-- Environmental data table (as mentioned in the prompt)
-- This allows for context-aware recommendations (e.g., recommend boots on rainy days)
CREATE TABLE environmental_data (
    data_id SERIAL PRIMARY KEY,
    location_zip_code VARCHAR(10) NOT NULL,
    date DATE NOT NULL,
    weather_condition VARCHAR(50), -- e.g., 'Rainy', 'Sunny', 'Snowy'
    temperature_celsius DECIMAL(4, 1),
    UNIQUE(location_zip_code, date)
);

-- Insert sample data (optional, but good for testing)
-- This would be populated from your CSVs in a real ETL process
-- For brevity, this part is omitted here but would be part of a complete solution.