import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className="text-4xl font-bold mb-4">Welcome to the App</h1>
      <div className="space-y-2">
        <Link
          to="/stocks-by-industry"
          className="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded-md"
        >
          Stocks by Industry
        </Link>
        <Link
          to="/news-by-ticker"
          className="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded-md"
        >
          News by Ticker
        </Link>
        <Link
          to="/news-by-industry"
          className="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded-md"
        >
          News by Industry
        </Link>
        <Link
          to="/news-by-source"
          className="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded-md"
        >
          News by Source
        </Link>
        <Link
          to="/industry"
          className="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded-md"
        >
          Industry
        </Link>
        <Link
          to="/news"
          className="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded-md"
        >
          News 
        </Link>
      </div>
    </div>
  );
};

export default Home;
