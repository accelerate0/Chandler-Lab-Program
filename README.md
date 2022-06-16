# Pynapse Scripts for Dr. Chandler Lab Experiments

This repository contains collections of Python 3 scripts for utilization in the Pynapse runtime environment.

By Erick Won
## Overview
 -   Behavioral Experimental set ups involving the usage of iCon Controllers (by Med-Associates) mediating behavioral boxs via Pynapse (TDT, Tucker-Davis Technologies)
 - Any questions or concerns can be forwarded to:
	 - [MUSC Email](mailto:ecw207@musc.edu)
	 - [Personal Email](mailto:goerick2k@gmail.com)
- **Pynapse Overview:**
	- Naming matters as well as presetting certain things in Pynapse and Synapse
	- Everything in Pynapse is *case-sensitive*
	- Never use spaces or non-alphanumeric characters, always use underscore (_) to denote spaces
	- Whenever it mentions `Epoc` this is referring to time stamping functionalities in the Pynapse software and will show up in the recorded data respectively.

## How To Run the Scripts

 1. Open a script ending in `.py` in GitHub
 2. Click the "Raw" button which is on the top right of the code display box
3. Copy and Paste the code into Pynapse
4. Click Commit, make sure no error messages are displayed and the file has been loaded successfully

## Channel Assignments

Information Regarding Channel Assignment:
- Variable names must be exact and case sensitive as well as (3-20 Characters):
- Unused channels that are assigned are allowed
- Variable name nomenclature:
	- *o/i_L/Variable Name*
		- *o/i* for output/input,
		- *L/R* for Left/Right
	- Spaces are denoted by underscores

Assigning channels for in

 1. Go to the `iCon Controller Settings`
 2. Fill in the variable names
 3. Configure the settings to the following:
	- `Hal Input Port`: Not checked
	- `Triggered Pulse`: Not checked
	- `Sync`: Not checked
	- `Invert Output`: Not checked
	- `Epoc Store`: Enabled
	- Fill in the Epoch ID to the respected assignment

**iH10_1 Controller:**
| Channel | Variable Name | Epoc Store ID |
| ------ | ------ | ------ |
| Channel 1 | o_L_Lever_Extension | x |
| Channel 2 | i_L_Lever_Press | x |
| Channel 3 | o_L_Lever_Light | x |
| Channel 4 | o_Reward_R_Light | x |
| Channel 5 | o_House_Light | x |
| Channel 6 | o_Tone | x |
| Channel 7 | i_Reward_R_B_B | x |
| Channel 9 | o_Pellet_Dispenser | x |
| Channel 10 | o_Shock | x |

**iH10_2 Controller:**
| Channel | Variable Name | Epoc Store ID |
| ------ | ------ | ------ |
| Channel 1 | o_R_Lever_Extension | x |
| Channel 2 | i_R_Lever_Press | x |
| Channel 3 | o_R_Lever_Light | x |

## Timer Assignment

- Fill timers into timer slot in the Synapse software
- Up to 6 runtime timers can be assigned in Pynapse
- Unused timers that are assigned are allowed
- Naming matters as well as presetting certain things in Pynapse+Synapse.
	- Therefore the following attributes needs to be declared in the Synapse program itself


1. Go into the `Timer iCon Settings`
2.  Assign the Timer Variable Name
3. For the `General Options` configure the following:
	- `Name`: variable name
	- `Epoc Save`: checked
	- `ID`: Epoc store ID
4. For the `Shape` configure the following:
	- `Control`: Trigger
	- `Period`: Does not matter so set to 1.000 seconds
	- `Repeats`: Does not matter so set to 1
	- `Early Pulse`: Not checked
	- `Sync`: Not checked
5. Set the Timer Assignments

| Timer Name | Variable Name | Epoc Store ID | Description |
| ------ | ------ | ------ | ------ |
| Global Timer | Global_T | GloT | x |
| VI Timer | VI_T | VIT | x |
| Trial Timer | Trial_T | TT | x |



## Draw.io Diagrams for Script Visualization

Webbed diagrams are available on how the scripts work using draw.io. To use draw.io (editing and viewing), you must download the addon which is available here:
- https://chrome.google.com/webstore/detail/drawio-for-notion/plhaalebpkihaccllnkdaokdoeaokmle

| Script Name | Draw.io Link |
|--|--|
| Platform Avoidance Training | [Link](https://app.diagrams.net/#G1HNz9VDa9wyPsMvxQO9PCpvsV23HluM3-) |
| Reward Training | [https://app.diagrams.net/#Haccelerate0%2FChandler-Lab-Program%2Fmain%2FTodd%27s%20Experiment%2FReward%20Training%2FReward%20Training](Link) |
| Conflict Test | [https://app.diagrams.net/#Haccelerate0%2FChandler-Lab-Program%2Fmain%2FTodd%27s%20Experiment%2FConflict%20Test%2FConflict%20Test](Link) |
| Conflict Training | [https://app.diagrams.net/#Haccelerate0%2FChandler-Lab-Program%2Fmain%2FTodd%27s%20Experiment%2FConflict%20Training%2FConflict%20Training](Link) |
