---
layout: default
title: RIFT Frontend
---

<style>
    .server-status {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 50px;
    }

    .server {
        width: 150px;
        height: 150px;
        background-color: grey;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        color: white;
        font-family: Arial, sans-serif;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        position: relative; /* For absolute positioning of status icon */
    }

    .server-name {
        font-size: 20px;
        margin-bottom: 10px;
    }

    .status-icon {
        height: 20px;
        width: 20px;
        border-radius: 50%;
        display: inline-block;
        position: absolute;
        top: 10px;
        right: 10px;
    }

    .online {
        background-color: #28a745;
    }

    .offline {
        background-color: #dc3545;
    }

    .maintenance {
        background-color: #ffc107;
    }

    .details-container {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        flex-wrap: wrap;
        margin-top: 30px;
    }

    .server-card {
        background-color: #f2f2f2;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        padding: 20px;
        margin: 10px;
        width: 800px;
        font-family: monospace;
    }

    .server-title {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 15px;
    }

    .server-stats {
        white-space: pre-wrap;
        word-break: break-word;
    }
</style>

<body>

<div class="server-status">
    <div class="server">
        <span class="status-icon online"></span>
        <div class="server-name">RIFT P1</div>
        <div class="server-status-text">Online</div>
    </div>
    <div class="server">
        <span class="status-icon online"></span>
        <div class="server-name">RIFT P3</div>
        <div class="server-status-text">Online</div>
    </div>
    <div class="server">
        <span class="status-icon online"></span>
        <div class="server-name">RIFT Demo</div>
        <div class="server-status-text">Online</div>
    </div>
</div>

<div class="details-container">
    <div class="server-card">
        <div class="server-title">RIFT P1</div>
        <div class="server-stats">
System information as of Thu Jan 25 08:07:41 UTC 2024

Usage of /:                       10.9% of 28.89GB
Memory usage:                     17%
Swap usage:                       0%
Processes:                        118

AWS public IP:                    18.221.167.77
        </div>
    </div>
    <div class="server-card">
        <div class="server-title">RIFT P3 / Rift_CSA</div>
        <div class="server-stats">
System information as of Thu Jan 25 08:07:00 UTC 2024

Usage of /:                       12.0% of 28.89GB
Memory usage:                     25%
Swap usage:                       0%
Processes:                        118

AWS public IP:                    3.142.225.188
        </div>
    </div>
    <div class="server-card">
        <div class="server-title">RIFT Demo</div>
        <div class="server-stats">
System information as of Thu Jan 25 08:00:00 UTC 2024

Usage of /:                       54.2% of 7.57GB
Memory usage:                     56%
Swap usage:                       0%
Processes:                        105

AWS public IP:                    3.145.170.103
        </div>
    </div>
    <!-- Repeat for other servers as needed -->
</div>

</body>
