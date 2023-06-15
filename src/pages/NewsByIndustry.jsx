import React, { useEffect, useState } from 'react';

const NewsByIndustry = () => {
  const [news, setNews] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/news-by-industry')
      .then(response => response.json())
      .then(data => {
        setNews(data.data);
      })
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>News by Industry</h1>
      <ul>
        {news.map(article => (
          <li key={article.id}>
            <h3>{article.title}</h3>
            <p>{article.summary}</p>
            <p>Published: {article.published}</p>
            <p>Source: {article.source}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NewsByIndustry;
