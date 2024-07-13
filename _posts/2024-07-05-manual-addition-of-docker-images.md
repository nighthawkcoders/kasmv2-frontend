---
layout: post
title: "Manual Addition of Docker Images to Kasm"
date: 2024-07-05
categories: [multi-server]
---

When Kasm registry is not working, even with third party additions, there are ways to directly import a docker image from dockerhub.

## Step 1: Navigation

In the Kasm administrative panel, navigate to `Workspaces > Workspaces`, then click the blue `Add Workspace` button.

<img width="1495" alt="image" src="https://github.com/nighthawkcoders/kasmv2/assets/56803677/891129d1-cca3-4c26-ad6f-3f7d0bd73399">

On another tab, open the registry for the images: [https://nighthawkcoders.github.io/kasm_registry/1.0/](https://nighthawkcoders.github.io/kasm_registry/1.0/)

## Step 2: Filling everything out

Follow the below configuration, use information you can get from the registries, whatever is not here you can leave blank:

Workspace Type > Container
Registry Entry > _BLANK_
Friendly Name > _Name you want users to see_
Description > _Description_
Thumbnail URL > _From registry_
Enabled > Yes
Docker Image > _Get from image info in registry, ie `nighthawkcoders/pusd-student-ubuntu:1.14.0-rolling`_
Cores > _From registry: JSON config_
Memory (MB) > _From registry: JSON config_
GPU Count > _From registry: JSON config_
Uncompressed Image Size (MB) > _From registry: JSON config_
CPU Allocation Method > _From registry: JSON config_
Docker Registry > _From registry: JSON config_
Docker Registry Username > nighthawkcoders
Web Filter Policy > Inherit (autofilled)
All *(JSON)* fields should be left with: `{}`

### Persistent Setup Using Volume Storage
In Persistent Profile Path: `/mnt/kasm_profiles/{image_id}/{user_id}` (location to store user data)
To restrict storage size, put this in Docker Run Config Override:
```json
{
  "KASM_PROFILE_SIZE_LIMIT": "2000000"
}
```