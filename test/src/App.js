import React, { useEffect, useState } from 'react';
import BasketballStatsTable from './BasketballStatsTable';
import './App.css';

function App() {
  const [boxScores, setBoxScores] = useState([]);

  useEffect(() => {
    // Fetch box score data from the Flask backend
    fetch('http://localhost:5000/box_scores')
      .then((response) => response.json())
      .then((data) => setBoxScores(data))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Super Cup 2024 - Womens</h1>
      </header>
      <div className="table-container">
        {boxScores.length > 0 ? (
          <BasketballStatsTable data={boxScores} />
        ) : (
          <p>Loading stats...</p>
        )}
      </div>
    </div>
  );
}

export default App;