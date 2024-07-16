---
layout: post
title: "Kasm Image Persistent Data Configuration Guide"
date: 2024-07-15
categories: [multi-server]
---

Persistent data or persistent profiles is a setup that allows users to retain their data even after their images close using the storage availible on the agent servers. While this is beneficial, we recommend important data be backed up in Git, or moved into Drive.

## Step 1: Setup

Go into the settings of the image that you are trying to modify.

Scroll down to Persistent Profile Path. Put: `/mnt/kasm_profiles/{image_id}/{user_id}` (location to store user data)

## OPTIONAL Restrict user storage (WORK IN PROGRESS)

To restrict storage size, put this in Docker Run Config Override:

```json
{
  "KASM_PROFILE_SIZE_LIMIT": "2000000"
}
```
