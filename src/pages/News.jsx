import React, { useEffect, useState } from 'react';
import axios from 'axios';

const News = () => {
  const [newsData, setNewsData] = useState([]);

  useEffect(() => {
    fetchNewsData();
  }, []);

  const fetchNewsData = async () => {
    try {
      const response = await axios.get('http://localhost:5000/news');
      setNewsData(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div>
      <h1>News</h1>
      <ul>
        {newsData.map((news) => (
          <li key={news.data[1]}>
            <h3>{news.data[2]}</h3>
            <p>{news.data[3]}</p>
            <p>{news.data[4]}</p>
            <p>{news.data[5]}</p>
            <p>{news.data[6]}</p>
            <p>{news.data[7]}</p>
            <p>{news.data[8]}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default News;

