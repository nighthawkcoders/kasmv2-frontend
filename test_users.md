---
layout: default
title: CSA Quiz Users and ID
---


# Display CSV Data on GitHub Pages

<div id="csv-root">Loading data...</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js"></script>

<script>
window.onload = function() {
    // Function to fetch and display CSV data
    function fetchAndDisplayCSV(csvUrl) {
        Papa.parse(csvUrl, {
            download: true,
            header: true, // Assuming your CSV has headers
            complete: function(results) {
                const data = results.data;
                displayData(data);
            }
        });
    }

    // Function to display the data on the page
    function displayData(data) {
        const container = document.getElementById('csv-root');
        container.innerHTML = ''; // Clear loading message or previous data

        // Example: Create and append a table to display the CSV data
        const table = document.createElement('table');
        const thead = document.createElement('thead');
        const tbody = document.createElement('tbody');
        const headers = ['Active Classes', 'Archived Classes', 'First Name 001', 'First Name 002', 'First Name 003', 'First Name 004', 'ID', 'Kasm Server', 'Last Name', 'Name', 'Server Needed', 'UID'];

        // Create table header
        let row = thead.insertRow();
        for(let header of headers) {
            let th = document.createElement('th');
            th.textContent = header;
            row.appendChild(th);
        }
        table.appendChild(thead);

        // Populate the table body with data
        data.forEach(item => {
            let row = tbody.insertRow();
            for(let header of headers.map(h => h.toLowerCase().replace(/ /g, '_'))) { // Map headers to field names
                let cell = row.insertCell();
                cell.textContent = item[header];
            }
        });
        table.appendChild(tbody);
        container.appendChild(table);
    }

    // Replace with the path to your CSV file in the repository
    const csvUrl = 'https://raw.githubusercontent.com/yourusername/yourrepository/branch/path/to/your/csvfile.csv';
    fetchAndDisplayCSV(csvUrl);
};
</script>

<style>
/* Optional: Add some basic styling for the table */
table {
    border-collapse: collapse;
    width: 100%;
}
th, td {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}
th {
    background-color: #f2f2f2;
}
</style>
