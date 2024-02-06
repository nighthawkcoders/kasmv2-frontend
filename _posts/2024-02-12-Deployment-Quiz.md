---
title: Deployment Quiz README
description: What to do day of the deployment quiz
toc: True
layout: post
---

# Foreword

Hello everyone! Today you will be graded on your capabilities in deploying a backend server from scratch on your own instance. You are permitted to use any outside resources, including this website, except for other people (don't try and bend the rules we will know). 

You will be setting up a Java Spring-Boot Server on your own Amazon EC2 Instance. You will be tasked with the following:
- Connecting to an EC2 Instance
- Setting up an EC2 Instance for Deployment
- Copying the quiz backend to your EC2 instance
- Changing the port on the quiz backend
- Changing the homepage of the quiz backend to reflect "your page"
- Deploying the Backend (the main part)

# Critical Information

Each person will have their own EC2 Instance that has its own ID based on the Github ID you have provided at the start of the year. You will be deploying on your OWN EC2 instance, NOT the RIFT servers. A table with all the people, their ID's, and the randomized ports is shown below. 

You will need to copy the quiz backend onto the AWS server. You will need to clone [this backend](https://github.com/RIFT24/quizbackend) and then modify it on EC2 using a text editor...

You will also have to change the port to a randomized port. We will be running a test to see if you are using the port. 

You must also change the homepage of the quiz backend to have your title be your [NAME]:[Github-ID]. This should be visible on the page (I would change the Java Homepage title). You then need to add the image url ``` ``` to the front page.

You must then create a route53 route on the test subdomain with your github ID as the prefix. It must be routed to your container.

You must finally have https. If you do not know how to do this, start looking around.

# Submission and Grading

Once all changes have been made as per the requirements, please come up to the front with your device. You will be asked to have an EC2 Terminal open for us to validate your port, and you must have an open runtime on your browser. 

After grading, you must make an issue with the following:
- Screenshot of curl command (must include the prompt where you entered in actual command) with score out of 1
- Screenshot of website working without interferance, add score out of 2
- Screenshot of website working on deployed server with website security panel, example below. Add score out of 1

In total, you must have **three** screenshots.

Example of website security panel:
![example](https://rackets-assets.vercel.app/assets/csa_quiz/example_submission.png)


