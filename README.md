# DFP Discord Bot
DeFi Pulse Discord Bot

## Intro
This repository is to supply auxiliary functionality to the DeFi Pulse engineering team through the use of an automated Discord user (bot). 

## Features
The bot currently supports the following tasks:
* Site HTTP status code monitoring
  * Check DeFi Pulse every minute and alert @dev tag (on a 10 min interval) if site returns 400 or higher code
  * Check any site's HTTP status code
* SDK Key provider
  * The bot will provide an SDK key in whatever channel it is summoned

## How to Use / Commands
Call the bot in any DeFi Pulse channel by sending a message in the channel. Commands:
* `/dfp help`
  * Show all commands available in the channel

* `/dfp give sdk_key`
  * Posts an SDK key tied (arbitrarily) to your discord ID to the channel

* `/dfp give random sdk_key`
  * Posts a random SDK key from the SDK key list
  
* `/dfp monitor <site>`
  * Return HTTP status code of site (example: /dfp monitor https://defipulse.com)
  * Note: Monitoring and alerting @devs for defipulse.com is automatic upon bot startup. This command does not need to be run in order for site monitoring feature to be in effect.
* `/dfp sup`
  * Ask the DeFi Pulse Bot what is up
