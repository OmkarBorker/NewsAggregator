# NewsAggregator
Backend using FLASK and PostgreSQL
### Given Tasks as follows :
Given two csv files. Following data is present in the two files.
- The `stock_industry_mapping.csv` has a all stocks and industry that are present in india.
    1. id → Unique id for stock
    2. ticker → name of the stocks’s ticker *******************************ticker is a symbol for the stock*******************************
    3. stock → name of the stock
    4. industry → name of the industry.
- 2. the `news.csv` has multiple news where news are mapped to stocks, for news that is not related to any stock the value is filled with `nan`
    1. id → unique id for news
    2. title → heading of the news
    3. link → URL for the news
    4. summary → text summary describing the news
    5. published → when was the news created
    6. source → news source
    7. org → if the news is related to an organisation
    8. mapped_stock_id → stock id from the csv `stock_industry_mapping.csv`
    9. ticker → ticker of the mapped stock
    10. stock → name of the mapped stock
    11. industry → industry of the mapped stock

Given these two files perform the following objectives
1. Create Two different endpoints to push the data from the two csv in separate tables inside the database. You are free to use any database. Do justify the reason of choosing the database
2. A user should be able to perform the following tasks using API/Endpoints.
    1. Get all the list of industries, stock, ticker that are present in India.
    2. Given an industry get all the stocks along with the tickers. *(Used the get method here which passes parameters through the url to get desired data)* 
    3. Get all news at ones 
    4. Get news by news-id (News id is casted to its unique UUID format)
    5. Get all news related to a ticker  *(Used the get method here which passes multiple ticker parameters through the url to get desired data)*
    6. Get all news related to an industry *(Used the get method here which passes multiple industry names as parameters through the url to get desired data)* 
    7. Get all news related to a source *(Used the get method here which passes multiple source names as parameters through the url to get desired data)*

### The Deployed on Railway and tested using postman


 
