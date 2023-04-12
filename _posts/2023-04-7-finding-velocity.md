---
layout: post
title: Finding Velocity 
tags: [Correcting Data]
comments: true
---

Using the central difference method, COM position can be differentiated into COM velocity, as shown below. 

![Velocity](/assets/img/TwoAxisVelocity.PNG)

However, since these data are originally from a treadmill experiment, the planted phase of stance (when the foot is not moving) is moving at the constant velocity of the treadmill (in this case, 1.0 m/s) in the anterior direction. This is the perfectly rectilinear path seen in the COM position graph. In reality, this line should be mostly horizontal during this period. 

![COM](/assets/img/MovingCOM.PNG)

Though this should not majorly affect the COM acceleration required for the final analysis, it can be corrected for.


### [→ Correcting Velocity](https://tudor-muresan.github.io/2023-04-06-correcting-velocity/)

### [← Numerical Differentiation](https://tudor-muresan.github.io/2023-04-08-numerical-differentiation/)
