

import React, { useState, useEffect } from 'react';

function buttonClick(ticket_id, action_type, callback, callback_value) {

  const updateTicketState = async (ticket_id, action_type) => {
    try {
      const response = await fetch(`http://localhost:8080/reports/${ticket_id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          ticketState: action_type
        })
      });

      if (!response.ok) {
        throw new Error('Failed to update ticket state');
      }

    } catch (error) {
      console.log(error.message);
    }
  };

  updateTicketState(ticket_id, action_type);

  callback(!callback_value)
}

const DataTable = ({ data, callback, callback_value }) => {
  return (

    <table style={{ border: '1px solid black', borderCollapse: 'collapse' }}>
      <thead>
        <tr>
          <th style={{ border: '1px solid black', padding: '8px' }}>ID</th>
          <th style={{ border: '1px solid black', padding: '8px' }}>State</th>
          <th style={{ border: '1px solid black', padding: '8px' }}>Type</th>
          <th style={{ border: '1px solid black', padding: '8px' }}>Message</th>
          <th style={{ border: '1px solid black', padding: '8px' }}>Action</th>
        </tr>
      </thead>
      <tbody>
        {data.map((item) => (
          <tr key={item.id}>
            <td style={{ border: '1px solid black', padding: '8px' }}>{item.id}</td>
            <td style={{ border: '1px solid black', padding: '8px' }}>{item.state}</td>
            <td style={{ border: '1px solid black', padding: '8px' }}>{item.payload.reportType}</td>
            <td style={{ border: '1px solid black', padding: '8px' }}>{item.payload.message}</td>
            <td style={{ border: '1px solid black', padding: '8px' }}> <button onClick={() => buttonClick(item.id, "BLOCKED", callback, callback_value)} type="button">Block</button> <button onClick={() => buttonClick(item.id, "RESOLVED", callback, callback_value)} type="button">Resolve</button>  </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};


function App() {
  const [reports, setReports] = useState([]);
  const [refresh, setRefresh] = useState(false);


  useEffect(() => {
    fetch('http://localhost:8080/reports?q={"state":"OPEN"}')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(jsonData => {
        setReports(jsonData.results ?? []);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, [refresh]);


  return (
    <>
      <div style={{ display: 'flex', justifyContent: 'center', marginTop: "50px" }}>
        <DataTable data={reports} callback={setRefresh} callback_value={refresh} />
      </div>
    </>
  );
}

export default App;
