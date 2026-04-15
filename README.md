# High-Density Network Monitor (Ubiquiti UniFi)

## Overview
This repository contains an automated network monitoring tool built in Python, designed to manage high-density IT infrastructure during large-scale events. It interacts with simulated Ubiquiti UniFi Controller APIs to track Access Point (AP) health, client density, and hardware status in real-time.

## The Problem it Solves
During massive events, maintaining stable internet connectivity is critical. If a single AP becomes oversaturated with client connections, performance degrades. This script automates the telemetry analysis, alerting the IT engineering team *before* the saturation causes a network outage, allowing for proactive load balancing.

## Technical Details
* **Language:** Python 3
* **Concept:** Network Automation, Telemetry Analysis, Infrastructure as Code (NetDevOps).
* **Target Hardware:** Ubiquiti UniFi Access Points (UAP-AC-HD, UAP-AC-PRO).
* **Features:**
  * Automated threshold alerting for client saturation.
  * Hardware failure detection (Disconnected status).
  * System event logging for post-event analysis.

## Usage
Simply run the script to execute a telemetry sweep and generate the corresponding logs.
`python unifi_density_monitor.py`
