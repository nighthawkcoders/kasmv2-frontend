---
layout: default
title: RIFT Request Test
---



<h1>EC2 Instance Information</h1>

<input type="button" id="fetchData" value="Fetch EC2 Instance Data" />
<div id="ec2Data"></div>

<script>
    document.getElementById('fetchData').addEventListener('click', function() {
        fetch('https://riftflask.stu.nighthawkcodingsociety.com/get-ec2-instances')
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Network response was not ok.');
        })
        .then(data => {
            displayEC2Data(data);
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('ec2Data').textContent = 'Error: ' + error.message;
        });
    });

    function displayEC2Data(data) {
        const container = document.getElementById('ec2Data');
        container.innerHTML = '';
        const currentDate = new Date().toLocaleString();
        data.Reservations.forEach(reservation => {
            reservation.Instances.forEach(instance => {
                let instanceId = instance.InstanceId;
                let publicIp = instance.PublicIpAddress || 'No Public IP';
                let instanceName = instance.Tags && instance.Tags.find(tag => tag.Key === 'Name')?.Value || 'No Name';
                container.innerHTML += `Instance ID: ${instanceId}, Name: ${instanceName}, Public IP: ${publicIp}, Request Date: ${currentDate}\n`;
            });
        });
    }
</script>



