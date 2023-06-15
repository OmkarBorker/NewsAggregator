import React, { useEffect, useState } from 'react';

const StocksByIndustry = () => {
  const [stocks, setStocks] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/stocks-by-industry')
      .then((response) => response.json())
      .then((data) => {
        setStocks(data.data);
      })
      .catch((error) => console.error(error));
  }, []);

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className="text-4xl font-bold mb-4">Stocks by Industry</h1>
      <div className="grid grid-cols-3 gap-4">
        {stocks.map((stock) => (
          <div key={stock.ticker} className="bg-gray-200 p-4 rounded-md">
            <h3 className="text-lg font-bold">{stock.industry}</h3>
            <p>Ticker: {stock.ticker}</p>
            <p>Stock: {stock.stock}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default StocksByIndustry;
