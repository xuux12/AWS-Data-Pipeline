# AWS-Data-Pipeline
This project demonstrates a complete AWS-based data pipeline for processing and analyzing traffic data from Copenhagen. 
It uses fully managed AWS services to build a serverless, scalable, and automated data analytics workflow.


# 🚦 Copenhagen Traffic Jam Analysis.

    
![Architecture Diagram](https://github.com/xuux12/AWS-Data-Pipeline/blob/d2217bb98ab56c991bc5b46ee8036c4ed50361b8/copenhagenTraffic.jpg)

This project analyzes 7 days of traffic data in Copenhagen using an end-to-end AWS data engineering pipeline.

## 🧱 Architecture 
![Architecture Diagram](https://github.com/xuux12/AWS-Data-Pipeline/blob/d85796be923a4e246dd1683b0d24405f6be2059c/AWS%20Data%20Engineering%20pipeline.png)



## ⚙️ Tech Stack

- **Amazon S3** – stores raw & processed data
- **AWS Glue** – ETL job to clean and transform data
- **AWS Lambda** – triggers Glue and sends email alerts
- **Amazon Athena** – SQL queries over traffic data
- **Amazon SNS** – email notification when Glue job finishes
- **Amazon EventBridge** – detects Glue job status

## 🚀 How It Works

1. Upload CSV to S3 bucket → triggers Lambda
2. Lambda starts Glue ETL job
3. Glue processes and stores clean data in S3 (Parquet)
4. Athena queries analyze traffic trends
5. When Glue finishes, SNS sends email alert



