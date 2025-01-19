# Redash Jupyter Kernel

A Jupyter kernel that allows you to execute Redash queries directly from Jupyter notebooks.

## Installation

```bash
pip install redash-kernel
python -m redash_kernel.install
```

## Configuration

Set the following environment variables:

```bash
export REDASH_URL="https://your-redash-instance.com"
export REDASH_API_KEY="your-api-key"
```

## Usage

After installation, select the "Redash" kernel when creating a new Jupyter notebook.

You can execute queries in two ways:
1. Write a SQL query directly in the notebook cell
2. Enter a query ID to execute an existing Redash query

Example:
```sql
SELECT * FROM users LIMIT 5
```

Or just enter a query ID:
```
123
```
