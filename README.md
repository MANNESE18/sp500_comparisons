# S&P 500 Market Cap per Employee Analysis

This project analyzes the relationship between a company's market valuation and its workforce size. Using `Python` and `SQLite`, I processed S&P 500 data to identify which companies in each sector generate the highest "market value per employee."

## Project Goal

The objective was to identify which S&P 500 sectors operate with the highest "valuation efficiency." This analysis helps pinpoint sectors that leverage automation and intellectual property over large-scale manual labor.

## Technical Workflow

* **Database Schema & Management:** I used `sqlite3` to build a relational database from scratch. The script initializes a `stock_study` table, ensuring a clean slate by dropping existing tables upon each execution to prevent data duplication.

* **Robust Data Ingestion:** To handle potential data inconsistencies in the source `CSV` (like missing values or formatting errors), I implemented:
  * `csv.DictReader` for reliable column mapping.
  * `try-except` blocks to catch `ValueErrors` during type conversion (e.g., non-numeric strings in numeric columns), allowing the script to skip corrupt rows without crashing.
 
* **Dynamic Table Generation:** I used `SELECT DISTINCT` to identify all unique sectors within the dataset. For each sector found, the script dynamically creates a specific sub-table (e.g., `Information_Technology`, `Energy`), sanitizing sector names to ensure they are SQL-compliant.

* **Data Aggregation:** The script performs a per-sector analysis to find the "Top Performer"—the company with the highest value-to-worker ratio.

* **Formatted Output:** Finally, the results are aggregated into a list and printed in a clean, tabular format in the terminal for immediate comparison across different industries.

## Logice Summary

The core metric calculated is:
```
Plaintext
```
```
Value per Worker = (Market Cap) / (Full-time Employees)
```

This provides insight into which sectors are highly automated or capital-intensive versus those that are labor-intensive.
