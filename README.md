# Divera Hermine Bot

## Description
Application that queries all non-archived news from DIVERA247 and prints the details of news that will take place tomorrow into a specified Hermine channel.

## References
This software uses the Divera247 API described at https://api.divera247.com.
Only commands to authenticate and query news are implemented in this module: https://github.com/wolfi1k/Divera

This software uses the Stashcat API implementd by Anselm Eberhardt over at https://gitlab.com/aeberhardt/stashcat-api-client

## Usage

First create a `.env` file to substitute variables for your deployment.

### Divera Update Bot environment variables

They can either be declared as enivronment variables or inside the `.env` file

| Variable | Description |
| -------- | ---------- |
| `DIVERA_USER` | Username for Divera247 |
| `DIVERA_PASSWORD` | password for Divera247 |
| `HERMINE_USER` | Username for Hermine |
| `HERMINE_PASSWORD` | Password for Hermine |
| `HERMINE_ENCRYPTION_KEY` | Encryption password for Hermine |
| `HERMINE_CHANNEL_ID` | Channel id the details shall be pushed to |
