# Project Data

This directory stores data used by and generated for **{{ cookiecutter.project_name }}**.

## Directory Structure

- **`raw/`**: Contains the original, immutable data as received from the source. This data should be treated as read-only.
  *(If raw data is too large to be versioned, this directory might contain scripts to download it, or instructions on where to obtain it.)*

- **`interim/`**: Stores intermediate data created during data processing and transformation steps. Files here can typically be regenerated from the raw data by running processing scripts.

- **`processed/`**: Contains the final, processed datasets that are ready for analysis, model training, or application use. These are the outputs of your data pipelines.

- **`external/`**: Holds data obtained from third-party sources, such as downloaded public datasets or data fetched from external APIs.

## Data Management Notes

* **Versioning Large Data:** If your project involves large data files, consider using tools like [Git LFS (Large File Storage)](https://git-lfs.github.com/) or storing the data in a dedicated data storage solution (e.g., cloud storage like S3, GCS, Azure Blob Storage) and referencing it or downloading it via scripts. Do not commit large binary data files directly to the Git repository if they exceed typical size limits (e.g., >50-100MB).
* **Sensitive Data:** Ensure that no sensitive or personally identifiable information (PII) is committed to the repository, especially in public repositories. Use the `.gitignore` file to exclude such data if it resides locally.
* **Data Provenance:** It's good practice to document where your data comes from and how it was processed. This can be done within this README, in notebooks, or through dedicated data documentation.

*(TODO: Add specific details about the data for this project, including sources, update frequency, and any relevant schemas or dictionaries, potentially in `references/` or `docs/`.)*