import React, { useEffect, useState } from 'react';

const NewsBySource = () => {
  const [news, setNews] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/news-by-source')
      .then(response => response.json())
      .then(data => {
        setNews(data.data);
      })
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>News by Source</h1>
      <ul>
        {news.map(article => (
          <li key={article.id}>
            <h3>{article.title}</h3>
            <p>{article.summary}</p>
            <p>Published: {article.published}</p>
            <p>Ticker: {article.ticker}</p>
            <p>Stock: {article.stock}</p>
            <p>Industry: {article.industry}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NewsBySource;
