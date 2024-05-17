import React, { useState } from 'react';

function App() {

  const [transactions, setTransactions] = useState([]);
  const [lastBlock, setLastBlock] = useState(null)
  
  const getBlockInfo = () => {
    fetch('http://127.0.0.1:5000/return_block_info')
    .then(response => response.json())
    .then(data => {
      const lastBlock = Object.keys(data.message)[0];
      console.log(lastBlock);
      setTransactions(data.message[lastBlock]);
      setLastBlock(lastBlock);
    })
    .catch(error => {
      console.error('Error fetching block info:', error);
    });
  }

  return (
    <div className="App">
      <button onClick={getBlockInfo}>Get Last Block Info</button>
      <p>Block: {lastBlock} </p>
      <div>
        {transactions.map((transaction, index) => (
          <div key={index}>{transaction}</div>
        ))}
      </div>
    </div>
  );
}

export default App;
