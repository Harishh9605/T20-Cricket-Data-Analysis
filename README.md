# T20 Cricket Data Analysis

## Project Overview
This project performs an end-to-end data analysis of T20 cricket match data using **SQL, Python, and Excel**.  
The goal is to analyze team performance, player contributions, and match trends to extract meaningful insights.

This project demonstrates a complete **data analyst workflow**:
- Data querying using SQL
- Data analysis and automation using Python
- Business-friendly reporting using Excel
- Version control using Git and GitHub

---

## Dataset Description
The dataset contains T20 cricket match data with information such as:
- Match details
- Teams
- Players
- Runs scored
- Wickets taken
- Match outcomes

The dataset was stored in a **MySQL database** and queried using SQL for analysis.

---

## Tools & Technologies
- **MySQL** – Data storage and SQL querying  
- **Python** – Data analysis and automation  
  - pandas
  - matplotlib
- **Excel** – Final outputs and reports  
- **VS Code** – Development environment  
- **Git & GitHub** – Version control and project hosting  

---

## SQL Analysis
SQL was used to:
- Explore the dataset
- Aggregate runs and wickets
- Analyze team and player performance
- Prepare clean datasets for Python analysis

Example SQL tasks:
- Total runs scored by each team
- Top-performing players
- Match result analysis
- Win percentage calculations

All SQL queries are available in the `sql/` folder.

---

## Python Analysis
Python was used to:
- Connect to the MySQL database
- Fetch data using SQL queries
- Perform data cleaning and transformation
- Generate summary statistics
- Export results to Excel files

Key Python libraries used:
- pandas
- mysql-connector-python
- matplotlib

The Python script can be found in the `python/analysis.py` file.

---

## Excel Outputs
Excel files were generated as final outputs for easy analysis and sharing.

The Excel outputs include:
- Team performance summaries
- Player statistics
- Aggregated match insights

All Excel files are available in the `output/` folder.

---

## Key Insights
Some of the insights derived from the analysis include:
- Certain teams consistently score higher average runs in T20 matches
- A small group of players contribute a significant portion of total runs
- Teams batting first show a higher win percentage in many matches
- Player performance has a strong impact on match outcomes

These insights can help understand performance patterns in T20 cricket.

---

## How to Run This Project

### 1. Clone the Repository
```bash
git clone https://github.com/Harishh9605/T20-Cricket-Data-Analysis.git
