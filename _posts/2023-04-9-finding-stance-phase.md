---
layout: post
title: Finding Stance Phase
tags: [Stance Phase, Introduction]
---

The datasets used in this analysis recorded subjects moving on a treadmill at a specified speed and include many individually recorded steps, as shown below. In this analysis, only the first complete step (stance phase) is of interest, and so it needed to be isolated from the rest of the dataset.

![WholeForce](/assets/img/WholeForce.PNG)

Stance phase is traditionally defined by force plate data. Specifically, it is located using sharp peaks and falls in detected ground reaction force. As such, the first data point of stance phase (‘A’) was found by locating the first point in the set which defined a force above 2N in the vertical direction, but followed five consecutive points which were all below 1N of force. The second index (‘B’) used a similar technique, where the point of interest was above 1N of force but the five following points below 1N. The output graph of ground reaction force between indices A and B is shown below: 

![StanceForce](/assets/img/StanceForce.PNG)

As such, since force plate and motion capture data now share a length after interpolation, the stance phase of each dataset could be defined as between the indices A and B. Below is an example of COM position once indices have been applied. 

![StanceCOM](/assets/img/MovingCOM.PNG)
