import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [cargo, setCargo] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch("http://localhost:8000/api/cargo")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch cargo data.");
        }
        return response.json();
      })
      .then((data) => {
        setCargo(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  return (
    <div className="container">
      <h1>Intergalactic Cargo Dashboard</h1>

      {loading && <p>Loading cargo data...</p>}

      {error && <p>{error}</p>}

      {!loading && !error && (
        <table>
          <thead>
            <tr>
              <th>Date</th>
              <th>Cargo ID</th>
              <th>Weight (kg)</th>
              <th>Destination</th>
            </tr>
          </thead>

          <tbody>
            {cargo.map((item) => (
              <tr key={item.cargo_id}>
                <td>{item.date}</td>
                <td>{item.cargo_id}</td>
                <td>{item.weight_in_kg}</td>
                <td>{item.destination}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default App;