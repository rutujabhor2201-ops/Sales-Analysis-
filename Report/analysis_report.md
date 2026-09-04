# Sales Analysis Report

## 1. Project Overview

This project analyzes sales transaction data using **Python and Pandas** to identify important sales trends and business insights.

The objective of the project is to analyze the provided sales dataset and understand:

* Overall sales performance
* Product-wise sales performance
* Regional sales performance
* Quantity of products sold
* Highest and lowest sales transactions
* Key business insights from the sales data

The dataset contains **100 sales transactions** with information about the date, product, quantity, price, customer ID, region, and total sales.

---

## 2. Project Objectives

The main objectives of this project are:

1. Load and examine the provided sales dataset.
2. Check the dataset structure and data quality.
3. Identify missing values and understand the available data.
4. Calculate important sales metrics.
5. Analyze sales performance by product.
6. Analyze sales performance by region.
7. Identify the highest and lowest individual transactions.
8. Calculate the total quantity of products sold.
9. Extract meaningful business insights from the sales data.

---

## 3. Dataset Description

The project uses the provided `sales_data.csv` dataset.

The dataset contains the following columns:

| Column      | Description                            |
| ----------- | -------------------------------------- |
| Date        | Date of the sales transaction          |
| Product     | Product sold                           |
| Quantity    | Number of units sold                   |
| Price       | Price of the product                   |
| Customer_ID | Unique customer identifier             |
| Region      | Region where the sale occurred         |
| Total_Sales | Total sales amount for the transaction |

The dataset contains **100 transactions** covering multiple products and regions.

---

## 4. Tools and Technologies

The following technologies were used:

* **Python** – Programming language used for the analysis
* **Pandas** – Used for loading, processing, and analyzing the dataset
* **Matplotlib** – Used to create sales visualizations
* **CSV** – Data storage format used for the provided sales dataset
* **GitHub** – Used to store and submit the project files

---

## 5. Project Structure

The project contains the following files and folders:

```text
Sales-Analysis/
│
├── README.md
├── main.py
├── requirements.txt
├── sales_data.csv
│
├── Data/
│   └── sales_data.csv
│
├── Visualization/
│   ├── sales_by_product.png
│   └── sales_by_region.png
│
└── Report/
    └── analysis_report.md
```

### File and Folder Descriptions

| File / Folder      | Purpose                                                                               |
| ------------------ | ------------------------------------------------------------------------------------- |
| `main.py`          | Contains the Python code used to load, process, analyze, and visualize the sales data |
| `sales_data.csv`   | Provided sales transaction dataset                                                    |
| `Data/`            | Contains the dataset used by the analysis                                             |
| `Visualization/`   | Contains the generated sales charts                                                   |
| `Report/`          | Contains the detailed analysis report                                                 |
| `requirements.txt` | Contains the Python libraries required to run the project                             |
| `README.md`        | Provides an overview and documentation of the project                                 |

---

## 6. Setup and Installation

### Prerequisites

Make sure Python is installed on your computer.

### Step 1: Clone or Download the Repository

Download or clone the project from GitHub and open the project folder in a terminal or VS Code.

### Step 2: Install Required Dependencies

Run:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Analysis

Run the Python script using:

```bash
python main.py
```

The program reads the provided sales dataset and performs the required sales analysis.

---

## 7. Analysis Steps

The following steps were performed during the analysis.

### Step 1: Load the Dataset

The provided CSV file was loaded into Python using Pandas.

### Step 2: Inspect the Dataset

The first few records and the structure of the dataset were examined to understand the available data.

### Step 3: Check Data Quality

The dataset was checked for:

* Missing values
* Number of records
* Column names
* Data types
* Basic statistical information

### Step 4: Calculate Overall Sales Metrics

The following metrics were calculated:

* Total sales
* Average sales per transaction
* Highest individual sale
* Lowest individual sale
* Total quantity sold
* Number of transactions

### Step 5: Analyze Product Performance

Sales and quantity were grouped by product to determine which products contributed the most to overall sales.

### Step 6: Analyze Regional Performance

Sales and quantity were grouped by region to identify the strongest and weakest performing regions.

### Step 7: Create Visualizations

Bar charts were created to visualize:

* Total sales by product
* Total sales by region

The generated charts are stored in the `Visualization/` folder.

### Step 8: Extract Business Insights

The calculated results were reviewed to identify important patterns and potential areas of business improvement.

---

## 8. Key Findings

### Overall Sales Performance

| Metric                        |      Result |
| ----------------------------- | ----------: |
| Total Sales                   | ₹12,365,048 |
| Average Sales per Transaction | ₹123,650.48 |
| Highest Individual Sale       |    ₹373,932 |
| Lowest Individual Sale        |      ₹6,540 |
| Total Quantity Sold           |   478 units |
| Number of Transactions        |         100 |

The business generated **₹12,365,048 in total sales** across **100 transactions**, with **478 units** sold.

### Product Performance

| Product    | Total Sales | Quantity Sold |
| ---------- | ----------: | ------------: |
| Laptop     |  ₹3,889,210 |           136 |
| Tablet     |  ₹2,884,340 |           127 |
| Phone      |  ₹2,859,394 |           101 |
| Headphones |  ₹1,384,033 |            48 |
| Monitor    |  ₹1,348,071 |            66 |

**Finding:** Laptops were the strongest-performing product, generating **₹3,889,210** in sales and recording the highest quantity sold at **136 units**.

Tablets were the second-highest contributor with **₹2,884,340** in sales, followed closely by phones with **₹2,859,394**.

Headphones generated **₹1,384,033**, while monitors generated the lowest product sales at **₹1,348,071**.

### Regional Performance

| Region | Total Sales | Quantity Sold |
| ------ | ----------: | ------------: |
| North  |  ₹3,983,635 |           147 |
| South  |  ₹3,737,852 |           143 |
| East   |  ₹2,519,639 |            94 |
| West   |  ₹2,123,922 |            94 |

**Finding:** The **North region** generated the highest sales at **₹3,983,635** and also recorded the highest quantity sold at **147 units**.

The **South region** was the second-best performing region with **₹3,737,852** in sales and **143 units** sold.

The **West region** generated the lowest total sales at **₹2,123,922**, indicating an opportunity for further investigation.

---

## 9. Business Insights

Based on the analysis:

1. **Laptops are the strongest-performing product**, generating the highest total sales and quantity sold.
2. **The North region is the best-performing region**, contributing the highest sales and selling the most units.
3. **The South region is also performing strongly** and is relatively close to the North in both sales and quantity.
4. **The West region has the lowest sales performance**, indicating an opportunity to investigate customer demand, pricing, product availability, or other regional factors.
5. **Tablets and phones are significant contributors** to overall revenue and should continue to receive attention.
6. The difference between the highest and lowest individual transactions shows considerable variation in transaction values.

---

## 10. Visualizations

The project includes two visualizations generated using Matplotlib.

### Sales by Product

The `sales_by_product.png` visualization shows the total sales generated by each product.

### Sales by Region

The `sales_by_region.png` visualization shows the total sales generated by each region.

Both visualizations are available in the `Visualization/` folder.

---

## 11. Technical Requirements

The project meets the technical requirements through the following implementation:

| Requirement           | Implementation                                                            |
| --------------------- | ------------------------------------------------------------------------- |
| Python-based analysis | Python is used for processing and analyzing sales data                    |
| Data handling         | Pandas is used to load and process the CSV dataset                        |
| Dataset usage         | The analysis uses the provided `sales_data.csv` dataset                   |
| Data inspection       | Dataset structure, records, and basic data quality are examined           |
| Sales calculations    | Total, average, minimum, and maximum sales are calculated                 |
| Product analysis      | Sales and quantity are analyzed by product                                |
| Regional analysis     | Sales and quantity are analyzed by region                                 |
| Data visualization    | Matplotlib is used to create product and regional sales charts            |
| Documentation         | Project steps, findings, setup instructions, and structure are documented |
| Version control       | Project files are maintained in a GitHub repository                       |

---

## 12. Conclusion

The sales analysis shows that the business generated **₹12,365,048 in total sales from 100 transactions**, with **478 units sold**.

Laptops were the top-performing product, while the North region generated the highest regional sales and quantity sold.

The analysis provides useful insights into product and regional performance. These findings can help identify strong-performing products and markets while highlighting areas such as the West region that may require further investigation.

This project demonstrates how **Python, Pandas, and Matplotlib** can be used to transform raw sales data into meaningful business insights through data inspection, calculations, grouping, and visualization.

