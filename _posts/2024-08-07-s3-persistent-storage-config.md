---
layout: post
title: "S3 Persistent Data Configuration"
date: 2024-07-31
categories: [multi-server]
---

Guide on how to configure S3 for persistent storage configuration.

## Step 1: Create a bucket

Go to AWS S3 and create a bucket.

## Step 2: Define AWS access and secret keys

The administrator needs to define the AWS Access Key ID and Access Secret in the Server Settings of Kasm.

## Step 3: Configure the persistent profile path in the workspace image

See Persistent Profile guide, just change the path to something like this:

```
s3://kasm-profile.s3.amazonaws.com/ubuntu_22_04/{username}/
```

This will store the profile in the S3 bucket.

## Step 4: Make sure to change the bucket policy

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PolicyForAllowKasmS3UserReadWrite",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<some arn number>:user/jm1021"
            },
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject"
            ],
            "Resource": "arn:aws:s3:::kasm-profile/*"
        },
        {
            "Sid": "PolicyForAllowKasmS3UserListLocate",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<some arn number>:user/jm1021"
            },
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketLocation"
            ],
            "Resource": "arn:aws:s3:::kasm-profile"
        }
    ]
}
```