import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [cargo, setCargo] = useState([]);
  const [loading, setLoading] = useState(true);
  const [syncing, setSyncing] = useState(false);
  const [error, setError] = useState("");

  const fetchCargo = async () => {
    try {
      const response = await fetch("http://localhost:8000/api/cargo");

      if (!response.ok) {
        throw new Error("Failed to fetch cargo data.");
      }

      const data = await response.json();

      // Business Rule 4:
      // Sort by weight (highest → lowest)
      // Earth must always remain at the bottom.
      data.sort((a, b) => {
        if (a.destination === "Earth") return 1;
        if (b.destination === "Earth") return -1;

        return b.weight_in_kg - a.weight_in_kg;
      });

      setCargo(data);
      setError("");
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCargo();
  }, []);

  const handleSync = async () => {
    setSyncing(true);

    // UX Rule:
    // Disable button and show loading text for exactly 2.5 seconds
    await new Promise((resolve) => setTimeout(resolve, 2500));

    await fetchCargo();

    setSyncing(false);
  };

  return (
    <div className="container">
      <h1>Intergalactic Cargo Dashboard</h1>

      <p className="subtitle">
        Live cargo manifest sorted by weight (Earth always remains last)
      </p>

      <div className="button-container">
        <button onClick={handleSync} disabled={syncing}>
          {syncing ? "Aligning quantum drives..." : "Sync Data"}
        </button>
      </div>

      {loading && <p className="message">Loading cargo data...</p>}

      {error && <p className="error">{error}</p>}

      {!loading && !error && (
        <table>
          <thead>
            <tr>
              <th>Cargo ID</th>
              <th>Destination</th>
              <th>Weight</th>
              <th>Date</th>
            </tr>
          </thead>

          <tbody>
            {cargo.map((item) => (
              <tr
                key={item.cargo_id}
                className={item.destination === "Earth" ? "earth-row" : ""}
              >
                <td>{item.cargo_id}</td>

                <td>
                  {item.destination}
                  {item.destination === "Earth" && (
                    <span className="pinned-badge">Pinned</span>
                  )}
                </td>

                <td>
                  <span className="badge">
                    {item.weight_in_kg} kg
                  </span>
                </td>

                <td>{item.date}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default App;