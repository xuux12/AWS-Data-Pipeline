# AWS-Data-Pipeline
This project demonstrates a complete AWS-based data pipeline for processing and analyzing traffic data from Copenhagen. 
It uses fully managed AWS services to build a serverless, scalable, and automated data analytics workflow.


# 🚦 Copenhagen Traffic Jam Analysis.

This project analyzes 7 days of traffic data in Copenhagen using an end-to-end AWS data engineering pipeline.

## 🧱 Architecture



## ⚙️ Tech Stack

- **Amazon S3** – stores raw & processed data
- **AWS Glue** – ETL job to clean and transform data
- **AWS Lambda** – triggers Glue and sends email alerts
- **Amazon Athena** – SQL queries over traffic data
- **Amazon SNS** – email notification when Glue job finishes
- **Amazon EventBridge** – detects Glue job status




