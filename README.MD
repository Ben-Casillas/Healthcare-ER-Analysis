Tech Stack:
Python
Jupyter



steps:
Sprint 2 — Data Validation & Quality Checks
- [x] Write a function that identifies missing required values in patient and encounter records.
- [x] Write a function that identifies duplicate patient and encounter IDs.
- [ ] Write a function that checks whether encounter start and end dates are valid.
- [ ] Write a function that identifies encounters referencing nonexistent patients or organizations.
- [ ] Write a function that checks whether condition records reference valid patients and encounters.
- [ ] Create a rejection report that records each invalid record and its rejection reason.
- [ ] Create a summary showing total records checked, valid records, rejected records, and failure percentages.
- [ ] Create deliberately corrupted sample records to test your validation functions.
- [ ] Use pytest to create automated tests for your validation functions.

Sprint 3 — Data Cleaning & Transformation
- [ ] Create a Python file named transform.py.
- [ ] Write functions to standardize date and timestamp formats.
- [ ] Standardize relevant categorical values (gender, encounter class, etc.) using documented mapping rules.
- [ ] Handle missing optional values without incorrectly replacing them with fabricated information.
- [ ] Remove or resolve duplicate records according to documented rules.
- [ ] Calculate encounter duration using start and end timestamps.
- [ ] Create a cleaned dataset for each source table.
- [ ] Ensure rejected records remain available for review.
- [ ] Compare raw and cleaned datasets to document how many records were changed, retained, or rejected.
- [ ] Write automated tests for your transformation functions.

Sprint 4 — SQL Database Integration
- [ ] Install and configure PostgreSQL.
- [ ] Create a database named hospital_analytics.
- [ ] Create SQL tables for patients, encounters, organizations, and conditions.
- [ ] Define primary keys, foreign keys, appropriate data types, and constraints.
- [ ] Create a Python file named load.py.
- [ ] Use SQLAlchemy to establish a Python-to-PostgreSQL connection.
- [ ] Load your cleaned datasets into their corresponding SQL tables.
- [ ] Ensure the loading process does not create duplicate records when executed repeatedly.
- [ ] Verify that foreign key relationships are enforced.
- [ ] Write SQL queries to verify row counts, relationships, and data integrity.
- [ ] Document your database schema.

Sprint 5 — Operational Analysis
- [ ] Create a Jupyter notebook named 02_operational_analysis.ipynb.
- [ ] Connect Python to PostgreSQL and retrieve analytical datasets.
- [ ] Calculate total encounters by month.
- [ ] Calculate encounters by facility and encounter class.
- [ ] Calculate average, median, minimum, and maximum encounter duration.
- [ ] Identify facilities with the highest and lowest encounter volumes.
- [ ] Analyze encounter trends over time.
- [ ] Analyze patient demographics across encounter types.
- [ ] Identify at least three meaningful findings from your analysis.
- [ ] Create at least five charts using matplotlib or seaborn.
- [ ] Document the methodology, findings, and limitations of your analysis.

Sprint 6 — Power BI Dashboard
- [ ] Connect Power BI Desktop to your PostgreSQL database.
- [ ] Create a data model with relationships between the four tables.
- [ ] Create measures for total encounters, unique patients, and average encounter duration.
- [ ] Create a visualization of encounter volumes over time.
- [ ] Create a comparison of encounter volumes across facilities.
- [ ] Create a breakdown of encounter classes.
- [ ] Create visualizations of encounter duration.
- [ ] Create demographic breakdowns where the data supports meaningful analysis.
- [ ] Add filters for facility, date range, and encounter class.
- [ ] Verify dashboard totals against SQL queries.
- [ ] Document your dashboard metrics and definitions.

Sprint 7 — Pipeline Automation & Finalization
- [ ] Create a Python file named pipeline.py.
- [ ] Connect ingestion, validation, transformation, and loading into one workflow.
- [ ] Make the pipeline executable through a single command.
- [ ] Add logging for each pipeline stage.
- [ ] Add error handling for missing files, invalid data, and database connection failures.
- [ ] Ensure failed processing stages are clearly reported.
- [ ] Add a final pipeline summary showing records processed, accepted, rejected, and loaded.
- [ ] Run the pipeline against the original dataset.
- [ ] Run the pipeline a second time and verify that duplicate records are not created.
- [ ] Run the pipeline against a new batch containing additional and intentionally corrupted records.
- [ ] Review and organize your GitHub repository.
- [ ] Write a README explaining the business problem, architecture, technologies, setup, execution, and findings.
- [ ] Include screenshots of your dashboard and examples of pipeline output.