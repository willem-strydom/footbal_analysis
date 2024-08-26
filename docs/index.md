# Welcome to "Sports Group Project"


## ETL overview

Data is scraped from ProFootballReference.com via "pfr_scraping_methods.py", and loaded into bigquery for warehousing. 
Transformation is done by sql models, and testing is being performed with pytest. Bottlenecks included
performing tests with sql, getting big query extractor to work, and also getting mkdocs to work. Because big query was
not working, we had to directly import the model outputs as csvs into our project o perform pytests
