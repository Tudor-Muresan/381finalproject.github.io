---
layout: post
title: Introduction to Inverse Dynamics
subtitle: One Segment at a Time
gh-repo: daattali/beautiful-jekyll
# gh-badge: [star, fork, follow]
tags: [Introduction]
comments: true
---

Inverse dynamics is a data analysis process used to determine forces and torques within joints such as at the ankle or knee. It utilises force plate and motion capture analysis to determine ground reaction force and body position during a number of movements. These data can then be used to sequentially determine forces and moments at the body's joints. Inverse dynamics can be used to determine the effects of different gaits (ex., walking, forefoot running, hindfoot running, etc.) or different accessories (ex., running shoes, football shoes, etc.) on intersegmental forces and torques.

## Dynamic Equilibrium

Inverse dynamics works by utilising the dynamic equilibrium formula, which is as follows:

{: .box-note}
(Centre of mass acceleration) x (Segment mass) = ΣF**

This formula uses Newton's second law of motion (F = M x A) to equate all forces acting on an object to the product of that object's mass and its linear acceleration. When considering a series of objects in contact with each other, such as body segments contacting at joints, the force within a joint acts on both segments at the same time, only in opposite directions. This fact allows us to slowly 'move up' the body's segments if the external force applied to the first segment is known.

In practise, this means that, so long as the ground reaction force is known, we are able to calculate the force within the ankle joint, which is then used to calculate the force in the knee joint, etc. This pattern is repeated until the segment of interest is reached. 

Segment position data is supplied by motion capture analysis, which records the position of various reflective markers set upon the segment during a movement. As acceleration is the second derivative of position relative to time, numerical differentiation can be used to determine linear acceleration -- the acceleration of the segment's centre of mass. 


### [→ Experimental Setup and Early Analysis](https://tudor-muresan.github.io/2023-04-10-setup/)

### [← Explanation](https://tudor-muresan.github.io/2023-04-11-explanation/)
