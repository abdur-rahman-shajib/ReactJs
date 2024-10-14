// backend/index.js
const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

// Dummy data for active projects
const activeProjects = [
    { id: 1, name: 'Project A', status: 'In Progress', startDate: '2024-01-01', endDate: '2024-12-31' },
    { id: 2, name: 'Project B', status: 'In Progress', startDate: '2024-02-01', endDate: '2024-11-30' },
    { id: 3, name: 'Project C', status: 'In Progress', startDate: '2024-03-01', endDate: '2024-10-31' },
];

// Dummy data for archived projects
const archivedProjects = [
    { id: 1, name: 'Project X', status: 'Completed', archiveDate: '2023-12-31' },
    { id: 2, name: 'Project Y', status: 'Completed', archiveDate: '2023-11-30' },
    { id: 3, name: 'Project Z', status: 'Completed', archiveDate: '2023-10-31' },
];

// Endpoint to get active projects
app.get('/active-projects', (req, res) => {
    res.json(activeProjects);
});

// Endpoint to get archived projects
app.get('/archived-projects', (req, res) => {
    res.json(archivedProjects);
});

app.get('/', (req, res) => {
    res.send('hi hello');
});

// Start the server
const PORT = 5000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
