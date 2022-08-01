


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
	- Pynapse automatically records inputs or outputs by enabling Epoc Store ID in Channel Assignments
- **Script Overview:**
	- Some scripts have the tag `legacy`in the script name. This denotes that the method and fashion of coding is more verbose, but rather ineffecient and no longer used.

## How To Run the Scripts

 1. Open a script ending in `.py` in GitHub
 2. Click the "Raw" button which is on the top right of the code display box
3. Copy and Paste the code into Pynapse
4. Click Commit, make sure no error messages are displayed and the file has been loaded successfully

## Dependencies

 - Many mathematical modules such as random, numpy, time, and so forth are dependencies. However, these come pre-installed with Pynapse.
 - One dependency that requires manual installation is PyOp. File, usage, and installation guide can be found in the [PyOp Repository](https://github.com/accelerate0/PyOp-Conditioning).

## Channel Assignments

Information Regarding Channel Assignment:
- Variable names must be exact and case sensitive as well as (3-20 Characters):
- Unused channels that are assigned are allowed
- Variable name nomenclature:
	- *o/i_L/Variable Name*
		- *o/i* for output/input,
		- *L/R* for Left/Right
	- Spaces are denoted by underscores

Assigning channels for Pynapse:

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
- Up to 4 runtime timers can be assigned in Pynapse
	- These are filled as followed on the bottom table
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
| Global Timer | Global_T | GloT | Timer that controls most experimental function and when finished, ends the experiment. This is controlled by the `const_ExperimentTime ` constant. |
| VI Timer | VI_T | VIT | Timer that is modified during runtime of the script and should not be modified by the user. Responsible for VI scheduling and randomly generated in avoidance training. |
| Trial Timer | Trial_T | TT | Timer that is modified during runtime of the script when it is not VI or ITI related. |
| ITI Timer | ITI_T | ITIT | Timer that is modified during runtime of the script and responsible for ITI Timing. |

## Variable Assignment
At the top of each scripts denotes 2 types of global variables used in the experiment
- **Global Static Variables:** These are variables that can be changed by the user as a preset and includes experimental timer settings and so forth.
- **Global Dynamic Variables:** These are variables that are changed during the course of the experiment and hsould not be changed by the user.

## Draw.io Diagrams for Script Visualization

Webbed diagrams are available on how the scripts work using draw.io. To use draw.io (editing and viewing), you must download the addon which is available here:
- https://chrome.google.com/webstore/detail/drawio-for-notion/plhaalebpkihaccllnkdaokdoeaokmle

## Trouble Shooting
- *ipy kernel related issues* or *python error code related issues*
	- Restart the synapse software via closing out the program. This may require multiple restarts or even a system reboot.
- *Inputs and Outputs are turning on/off randomly, constant FPS drop on camera*
	- Switch the iCon controller off then on
