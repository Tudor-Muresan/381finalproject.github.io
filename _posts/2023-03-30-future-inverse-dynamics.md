---
layout: post
title: Further Inverse Dynamics
comments: true
---

Inverse dynamics can be used sequentially to find the force and torque of any segment of interest, so long as the ground reaction force is known. In this analysis, ankle force was found. Though the datasets used here only include foot marker position data, if the position of the calf and thigh were also known, the ankle force could be used to find the knee or hip joint forces. For instance, the ankle force would replace the ground reaction force in this analysis while solving for the knee force, which would then be similarly used to solve for hip force. 

As an example, below are the force and torque outputs for a running analysis that included the necessary ground reaction moment information.

![Ankle joint force and torque during running](/assets/img/AnkleForceAndMoment.PNG)

![Knee joint force and torque during running](/assets/img/KneeForceAndMoment.PNG)


### [This is the last page of the analsys, click here to get back to the main page](https://tudor-muresan.github.io/)

### [← Joint Angle](https://tudor-muresan.github.io/2023-03-31-joint-angle/)
