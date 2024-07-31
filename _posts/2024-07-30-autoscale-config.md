---
layout: post
title: "Kasm Autoscale Config Guide"
date: 2024-07-30
categories: [multi-server]
---

How to set up Kasm Autoscaling from scratch.

## Step 1: KASM Key

Make sure to place the KASM key in the required location. `Diagnostics > System Info > Licenses`

## Step 2: Update Deployment Zone

Go to `Infrastructure > Zones`, edit your zone. Use the parameters below:

| Field                 | Description                 |
|-----------------------|-----------------------------|
| Zone Name             | Name of Zone                |
| Allow Origin Domain   | Must be domain of Kasm site |
| Upstream Auth Address | Private IP of Web Server    |
| Others                | Leave same                  |

## Step 3: Create Pool

Go to `Infrastructure > Pools`. Create a new pool. Configure it to docker agents.

## Step 4: Create VM Provider Config

Go back to `Infrastructure > Pools`. Click on the button that says `All VM Provider Configs`. It will be there if the license is accepted.

Click add. Use the parameters below.

| Field                                 | Description                                                                                     | Recommended Value                                             |
|---------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| VM Provider Configs                   | If you want to create a new config or edit one                                                  | Create new (unless you are editing)                           |
| Provider                              | Which cloud provider you are using                                                              | AWS                                                           |
| Name                                  | Choose preferred name of hosting config                                                         | N/A                                                           |
| AWS Access Key ID                     | Get this by running the command `cat ~/.aws/credentials` or something similar                   | Output                                                        |
| AWS Secret Access Key                 | Get this by running the command `cat ~/.aws/credentials` or something similar                   | Output                                                        |
| AWS Region                            | Region where Kasm is running on AWS where it will build servers                                 | us-west-#                                                     |
| AWS: EC2 AMI Id                       | AMI ID for instances. Cannot use ubu24 as it is not supported yet.                              | ami-0075013580f6322a1 (ubu22)                                 |
| AWS: EC2 Instance Type                | Type of instance for AWS                                                                        | t3.medium / c6a.8xlarge                                       |
| AWS Max EC2 Nodes                     | Depends on instance...                                                                          | 15                                                            |
| AWS: EC2 Security Group IDs           | ID of the security group that Kasm runs on                                                      | ["sg-idhere"]                                                 |
| AWS: EC2 Subnet ID                    | ID of the subnet the web server is running on. Can be found in the description of the instance. | subnet-idhere                                                 |
| AWS: EC2 EBS Volume Size              | Size of EC2 instance volume                                                                     | 50                                                            |
| AWS: EC2 EBS Volume Type              | Type of EC2 volume                                                                              | gp2 / gp3                                                     |
| AWS: EC2 Custom Tags                  | Custom EC2 tags                                                                                 | {}                                                            |
| AWS: EC2 Startup Script               | Script to set up Kasm                                                                           | Get from below                                                |
| AWS Config Override                   | AWS configuration override parameters                                                           | {"instance_config": {}}                                       |
| Retrieve Windows VM Password from AWS | N/A since we don't use Windows                                                                  | Disabled                                                      |
| SSH Keys                              | SSH keys you want to use to access the VM                                                       | Use the deployer keys stated for the machine, but can use any |

## Step 5: Create Autoscale Config

Go back to `Infrastructure > Pools`. Click the button that says `All Autoscale Configs`. It will be there if the license is accepted.

Add an autoscale config. Use the Parameters Below:

### Section 1: Autoscale Details

| Field                 | Description                                                                                                               | Recommended Values |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------|--------------------|
| Name                  | Put in the autoscale config name                                                                                          | N/A                |
| Autoscale Type        | Set to "Docker Agent"                                                                                                     | N/A                |
| Pool                  | Set to created pool                                                                                                       | N/A                |
| Enabled               | Should be activated                                                                                                       | Enabled            |
| Aggressive Scaling    | Optional, but recommended                                                                                                 | Enabled            |
| Deployment Zone       | Set to created zone                                                                                                       | N/A                |
| Standby Cores*        | Cores available                                                                                                           | 2                  |
| Standby GPUs*         | GPUs available                                                                                                            | 2                  |
| Standby Memory*       | RAM available                                                                                                             | 5536               |
| Downscale Backoff     | Time for instances to shut off if not being used                                                                          | 900                |
| Agent Cores Override  | Forceful usage of agent server cores                                                                                      | 4                  |
| Agent GPUs Override   | Forceful usage of agent server GPUs                                                                                       | 0                  |
| Agent Memory Override | Forceful usage of agent memory (rec value tbr)                                                                            | 5536               |
| Nginx Cert            | Go to  `/opt/kasm/current/certs/`  on the web server, and pull the nginx cert, that begins with "Begin Nginx Certificate" | N/A                |
| Nginx Key             | Go to  `/opt/kasm/current/certs/`  on the web server, and pull the nginx cert, that begins with "Begin Nginx Certificate" | N/A                |
| Register DNS          | Google it                                                                                                                 | Disabled           |

### Section 2: VM Provider Configs

Choose the VM provider config you configured in step 4. You can modify it here, but you can proceed if step 4 was done properly.

## Step 6: Activation Step

Go to `Sessions > Staging`. Add a new staging config. Choose the workspace, zone, desired sessions, expiration, and the pool and autoscale config you just made. Allow all permissions except printing. A sample config is shown below.

| Field                | Sample Input                 |
|----------------------|------------------------------|
| Workspace            | Ubuntu 22.04 Student Edition |
| Zone                 | zone1                        |
| Desired Sessions     | 24                           |
| Expiration           | 1                            |
| Pool                 | autoscaler                   |
| AutoScale Config     | autoscaler-main              |
| Allow Audio - Webcam | Enabled                      |
| Allow Printing       | Disabled                     |
