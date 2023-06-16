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

   deployment website in description

### <a href="https://github.com/OmkarBorker/NewsAggregator/tree/main/tests">The Tests conducted are stored in test directory</a>

## The Hierarchy of the flask app are
    app.py
    ├── __init__.py
        ├── main.py
        └── data.py
- The app runs through app.py 
- The app is setup through __init__.py
- main.py contains all the user functions as mentioned in part 2
- data.py contains all the post operations through which data is posted onto the system 

## The Database and App functionality
- PostgresSQL as the database for the following reasons:
    - PostgreSQL is a powerful open-source RDBMS with strong ACID compliance, making it suitable for data integrity and reliability.
    - It supports complex queries, indexing, and advanced features like JSONB and UUID data type, which can be useful for handling diverse data.
    - It has good integration capabilities with Python and Flask especially with psycopg2 library.
    - As the Schema for the database is given to use it is much prefered to make a structured database using postgresSQL for data analysis and         manipulation, making it easy for isolation of specific data.
- The Fuctionality of the app includes 
    - > _/industries_  
    - Get all the list of industries, stock, ticker that are present in India
    - > _stocks-by-industry?industry=industry1&industry=industry2_
    -  Given an industry get all the stocks along with the tickers ( parameter passing         through url takes care of multiple inputs through GET request)    <p></p>
    - > _/news_ 
    - Get all news at ones
    - > _/news/<id<id>>_ 
    - Get news by news-id
    - > _/news-by-ticker?ticker=ticker1&ticker=ticker2_ 
    - Get all news related to a ticker (parameter passing through url takes care of multiple inputs GET request)
    - > _/news-by-industry?industry=industry1&industry=industry2_ 
    - Get all news related to an industry 
    - > _/news-by-source?source=source1&source=source2_ 
    - Get all news related to a source
    
    <p></p>
    
    -  - **POST request**
    - > _/push-stock-industry-mapping_ 
    - data of industries into table stock_industry_mappings
    - > _/push-news_
    - data of news into table news
    - both endpoints are different to push the data from the two csv in separate tables inside the database.

