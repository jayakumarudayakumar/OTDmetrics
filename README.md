# OTDmetrics
On-time Delivery (OTD) Predictive Modeling

## Summary
This project optimizes taxi fleet management using Big Data Management tools like Apache Spark. ​
Some of our project objectives are,​
1. Analyze historical and real-time taxi trip data from the City of Chicago​
2. Identify high-demand pickup areas, peak hours, and traffic congestion hotspots​
3. Propose fleet reallocation strategies

## Methodology
1. Utilized Databricks and Apache Spark to perform distributed data processing and analysis
2. The dataset was preprocessed, cleaned, and aggregated to analyze trip volumes, fare distribution, and pickup/drop-off locations across various timeframes and geographic regions

## Dataset
The City of Chicago taxi trip data set was used for this analysis. ​
It contains fare amounts, trip miles, trip durations, pickup and drop-off timestamps, and the geographical location (community area) of pickups and drop-offs.​
Data Pre-processing, Descriptive Statistics, Demand Analysis, Congestion Analysis, Fleet Reallocation Recommendations​

## System Design
1. API Call - Historic Data (Jan 2024 - Sep 2024) and Real-time Data (Oct 2024 - Future)
2. Data Cleaning and Transformation
3. Load Data to Parquet files on Cloud Storage
4. Create Data Warehouse tables on PySpark
5. Load Data from Parquet files to DW tables
6. Data Analysis and Visualization

## RDBS Schema
1. Trip (Fact Table)
2. Company (Dimension Table)
3. Transaction (Fact Table)


​

​

​

​

​

​

​
​

​
