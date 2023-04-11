---
layout: post
title: Joint Torques
tags: [Joint Angle]
comments: true
---

The torque experienced in a joint of interest can also be found via inverse dynamics, using the following dynamic equilibrium formula:

{: .box-note}
(Moment of inertia) x (angular acceleration) = ΣM

Moment of inertia is a quantity defined by geometry and could have been calculated using the same variables used to find the mass of the foot. Angular acceleration is the double derivative of angular position (similar to linear acceleration and displacement), and could have been acquired in this analysis using marker position to solve for joint angle. 

However, in the same way that ankle force is largely defined by ground reaction force, ankle moment is largely defined by ground reaction *moment*, which is not a value that was recorded in the datasets used for this analysis. As such, joint torques could not have been defined here without substantial estimation.


### [→ Joint Angle](https://tudor-muresan.github.io/2023-03-31-joint-angle/)

### [← Ankle Force at Different Speeds](https://tudor-muresan.github.io/2023-04-02-ankle-force-at-different-speeds/)
