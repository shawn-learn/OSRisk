# OSRisk
An open source risk analysis software.  Use cases range from FMEA, Cause Effect Diagram, RAM, Root Cause, PHA, Fish Bone Diagram, Risk Resister, etc. 


# OSRisk - Analysis Engine - Project Overview

## Project Description

This Python-based risk analysis engine evaluates complex risk scenarios using a branching cause-effect structure. It supports both analytical and Monte Carlo methods to simulate how initiating events, barriers, and consequences interact over time. This engine is designed for integration with external UIs (via API) and future extensibility toward tools like DNV’s SPS.

## Key Features

- Network based event modeling that allows for branching as well as complex networks where spliting rejoining and looping is allowed
- Barrier modeling (preventive and mitigative)
- Monte Carlo simulation for probabilistic risk
- Analytical shortcuts for simple configurations
- JSON-based scenario input/output
- REST API for integration
- Modular design ready for future enhancements
- Tracks system throughput and monetary consequences

## Initial Use Cases

- Root Cause Analysis (RCA)
- Process Hazard Analysis (PHA)
- Reliability, Availability, Maintainability (RAM)
- Bow Tie Risk Analysis
- Risk-Cost Assessment

## Architecture

- **Backend**: Python-based, stateless service
- **Interface**: REST API (Flask or FastAPI)
- **Data Format**: JSON input/output
- **Simulation**: Monte Carlo with NumPy; optional symbolic evaluation
- **Output**: Distribution of outcomes, expected loss, percentiles

