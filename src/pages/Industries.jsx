import React, { useEffect, useState } from 'react';

function Industries() {
  const [industries, setIndustries] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/industries')
      .then(response => response.json())
      .then(data => setIndustries(data.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1 className="text-4xl font-bold mb-4">Industries</h1>
      <ul>
        {industries.map(industry => (
          <li key={industry.industry}>
            <h2>{industry.industry}</h2>
            <p>Stock: {industry.stock}</p>
            <p>Ticker: {industry.ticker}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Industries;
