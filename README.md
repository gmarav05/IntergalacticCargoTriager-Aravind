# Intergalactic Cargo Triager

This project was developed as part of the **Intergalactic Cargo Triager Assessment**.

It consists of:

- A Python backend that serves the processed cargo data through a REST API.
- A React (Vite) frontend that displays the cargo dashboard.

---

# Project Structure

```
IntergalacticCargoTriager-Aravind/
│
├── api/
│   └── server.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── parser/
│   ├── parser.py
│   ├── manifest.txt
│   └── Task 1 - Aravind - Parser.json
│
└── README.md
```
---

# Instructions to run locally

## Requirements

- Python 3
- Node.js
- npm

---

# Running the Backend

Open a terminal from the project root.

```bash
cd api
python3 server.py
```

The backend will start on:

```
http://localhost:8000
```

API endpoint:

```
GET http://localhost:8000/api/cargo
```

---

# Running the Frontend

Open another terminal.

```bash
cd frontend
npm install
npm run dev
```

Open your browser and visit:

```
http://localhost:5173
```

---

# Testing the HTTP 418 Response

Run the following command:

```bash
curl -i -H "X-System-Override: true" http://localhost:8000/api/cargo
```

Expected response:

```
HTTP/1.0 418 I'm a teapot

System override denied.
```

---

# Features

- REST API serving processed cargo data
- Cargo dashboard built with React
- Cargo sorted by weight (highest to lowest)
- Earth cargo always pinned to the bottom
- Sync Data button with required 2.5-second loading behaviour
- Clean and responsive user interface