-- Create stock_industry_mapping table
CREATE TABLE stock_industry_mapping (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(255),
    stock VARCHAR(255),
    industry VARCHAR(255)
);

Create news table
CREATE TABLE news (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    link VARCHAR(255),
    summary TEXT,
    published TIMESTAMP,
    source VARCHAR(255),
    org VARCHAR(255),
    mapped_stock_id INTEGER,
    ticker VARCHAR(255),
    stock VARCHAR(255),
    industry VARCHAR(255),
    FOREIGN KEY (mapped_stock_id) REFERENCES stock_industry_mapping (id)
);


-- Add a new column with UUID data type
ALTER TABLE news ADD COLUMN temp_id UUID;

-- Update the new column with UUID values
UPDATE news SET temp_id = uuid_generate_v4();

-- Drop the existing id column
ALTER TABLE news DROP COLUMN id;

-- Rename the temporary column to id
ALTER TABLE news RENAME COLUMN temp_id TO id;

-- Step 1: Create a new temporary column
ALTER TABLE news ADD COLUMN temp_mapped_stock_id UUID;

-- Step 2: Update the new column with UUID values
UPDATE news SET temp_mapped_stock_id = uuid_generate_v4();

-- Step 3: Drop the existing column
ALTER TABLE news DROP COLUMN mapped_stock_id;

-- Step 4: Rename the temporary column
ALTER TABLE news RENAME COLUMN temp_mapped_stock_id TO mapped_stock_id;

-- Add a new temporary column with UUID data type
ALTER TABLE stock_industry_mapping ADD COLUMN temp_id UUID;

-- Update the new column with UUID values
UPDATE stock_industry_mapping SET temp_id = uuid_generate_v4();

-- Alter the data type of the temp_id column to UUID
ALTER TABLE stock_industry_mapping ALTER COLUMN temp_id TYPE UUID USING temp_id::UUID;

-- Drop the default constraint from the id column
ALTER TABLE stock_industry_mapping ALTER COLUMN id DROP DEFAULT;

-- Alter the data type of the id column to UUID using the temp_id values
ALTER TABLE stock_industry_mapping ALTER COLUMN id TYPE UUID USING temp_id;

-- Drop the temporary column
ALTER TABLE stock_industry_mapping DROP COLUMN temp_id;
