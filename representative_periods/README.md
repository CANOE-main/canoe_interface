# CANOE Representative Periods Processor

A toolkit for processing CANOE databases to apply representative periods using clustering algorithms. This tool supports multiple versions of the Temoa schema (v2, v3, v3.1).

## Features

- **Time Series Clustering**: Generates representative periods from raw time series data (`clustering.py`).
  - Supports Principal Component Analysis (PCA) for dimensionality reduction (`pca.py`).
  - Allows custom feature selection strategies (`feature_selection.py`).
- **Database Processing**: Applies generated representative periods to SQLite databases for:
  - Temoa Legacy Schema (`database_processing.py`)
  - Temoa Schema v3 (`database_processing_v3.py`)
  - Temoa Schema v3.1 (`database_processing_v3_1.py` - uses `canoe_schema_v3_1.sql`)
- **Automated Workflow**: `process_all.py` orchestrates the entire flow.
- **Configurable**: Highly customizable via `config.yaml`.

## Installation

1.  **Clone the repository** (if you haven't already).

2.  **Set up the environment**:
    It is recommended to use Conda/Mamba.
    ```bash
    conda env create -f environment.yml
    conda activate canoe-backend
    ```
    Alternatively, you can install dependencies via pip:
    ```bash
    pip install -r requirements.txt
    ```

3.  **CRITICAL: Patch `tsam` library**:
    The `tsam` library requires a custom modification for this tool to work correctly.
    You must replace the `timeseriesaggregation.py` file in your Python environment's `tsam` package with the one provided in this repository.

    **Source file:** `./timeseriesaggregation.py` (in this root directory)

    **Destination:**
    Find where `tsam` is installed. You can find the exact path by running:
    ```bash
    python -c "import tsam, os; print(os.path.dirname(tsam.__file__))"
    ```
    It is typically located at:
    - **Windows**: `C:\Users\<user>\miniconda3\envs\canoe-backend\Lib\site-packages\tsam\`
    - **macOS / Linux**: `~/miniconda3/envs/canoe-backend/lib/python3.12/site-packages/tsam/` 
      *(Note: On Apple Silicon Macs, this might be under `miniforge3` instead of `miniconda3`)*

    *Replace the existing `timeseriesaggregation.py` file in that directory with the one from this repo.*

    **macOS / Linux Shortcut:**
    If you have your conda environment activated, you can run this command from the `representative_periods` directory to automatically patch the file:
    ```bash
    cp ./timeseriesaggregation.py $(python -c "import tsam, os; print(os.path.dirname(tsam.__file__))")/
    ```

## Usage

1.  **Prepare Input Data**:
    - Place your source SQLite databases (`.sqlite`) in the `input_sqlite/` directory.
    - Ensure your time series data is correctly structured in `timeseries/` as referenced in `config.yaml`.

2.  **Configuration**:
    - Edit `config.yaml` to adjust clustering parameters, select time series columns, and define output settings.

3.  **Run the Processor**:
    To run the full workflow (clustering + database updating):
    ```bash
    python process_all.py
    ```

    Or run individual steps:
    ```bash
    # Step 1: Generate representative periods
    python clustering.py

    # Step 2: Update databases (choose the script matching your schema version)
    python database_processing_v3_1.py
    ```

4.  **Outputs**:
    - **Processed Databases**: Found in `output_sqlite/`.
    - **Clustering Data**: Debugging and visualization data in `clustering_output_data/`.
    - **Periods File**: `periods.csv` (the raw representative periods).

## Project Structure

- `process_all.py`: Main entry point.
- `clustering.py`: Logic for time series clustering.
- `pca.py`: Utilities for performing PCA on time series groups before clustering.
- `feature_selection.py`: Contains custom strategies for selecting specific periods (e.g. max mean).
- `database_processing*.py`: Scripts to update SQLite databases with new periods.
- `canoe_schema_v3_1.sql`: SQL schema definition for Temoa v3.1 databases.
- `config.yaml`: Main configuration file.
- `timeseries/`: Directory containing raw input data for clustering.
- `input_sqlite/`: Drop your raw databases here.
- `output_sqlite/`: Pick up your processed databases from here.
