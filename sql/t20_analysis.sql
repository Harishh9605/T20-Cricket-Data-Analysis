/* =========================================================
   PROJECT: T20 Cricket Batting Analysis
   TOOLS: MySQL
   PURPOSE:
   - Clean T20 batting data
   - Analyze player performance
   - Identify top performers using SQL
   ========================================================= */


/* ===============================
   1. USE DATABASE
   =============================== */

USE t20_analysis;


/* ===============================
   2. DATA CLEANING
   =============================== */

-- Remove '*' from Highest Score (HS)
-- '*' indicates not out and prevents numeric analysis
UPDATE t20
SET HS = REPLACE(HS, '*', '')
WHERE HS LIKE '%*%';

-- Add a numeric column for Highest Score
ALTER TABLE t20
ADD COLUMN HS_int INT;

-- Convert cleaned HS to integer
UPDATE t20
SET HS_int = CAST(HS AS UNSIGNED);


/* ===============================
   3. DATA VALIDATION
   =============================== */

-- Total number of records
SELECT COUNT(*) AS total_players
FROM t20;

-- Check for null values in HS_int
SELECT COUNT(*) AS null_highest_scores
FROM t20
WHERE HS_int IS NULL;


/* ===============================
   4. ANALYSIS QUERIES
   =============================== */

-- 4.1 Top 10 Run Scorers in T20 Cricket
SELECT Player, Runs
FROM t20
ORDER BY Runs DESC
LIMIT 10;


-- 4.2 Most Consistent Batsmen (Highest Average)
-- Considering only players with at least 50 matches
SELECT Player, Ave
FROM t20
WHERE Mat >= 50
ORDER BY Ave DESC
LIMIT 10;


-- 4.3 Fastest Scoring Batsmen (Highest Strike Rate)
-- Considering only players with at least 50 matches
SELECT Player, SR
FROM t20
WHERE Mat >= 50
ORDER BY SR DESC
LIMIT 10;


-- 4.4 Boundary Impact Analysis
-- Calculates total runs scored from boundaries
SELECT Player,
       (4s * 4 + 6s * 6) AS Boundary_Runs
FROM t20
ORDER BY Boundary_Runs DESC
LIMIT 10;


-- 4.5 Runs Per Match (Efficiency Metric)
-- Measures average contribution per match
SELECT Player,
       ROUND(Runs / Mat, 2) AS Runs_per_Match
FROM t20
WHERE Mat >= 50
ORDER BY Runs_per_Match DESC
LIMIT 10;


/* ===============================
   5. ADDITIONAL INSIGHTS
   =============================== */

-- Players with highest individual scores
SELECT Player, HS_int AS Highest_Score
FROM t20
ORDER BY HS_int DESC
LIMIT 10;


-- Players with most sixes
SELECT Player, 6s AS Sixes
FROM t20
ORDER BY 6s DESC
LIMIT 10;


/* ===============================
   END OF SCRIPT
   =============================== */
