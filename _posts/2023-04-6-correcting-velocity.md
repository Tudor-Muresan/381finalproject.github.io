---
layout: post
title: Correcting Velocity
tags: [Correcting Data]
comments: true
---

Initially derived velocity experiences an offset in the anterior direction due to the constant velocity of the moving treadmill. This can be solved by simply subtracting the velocity of the treadmill from every point in the velocity dataset. Velocity in the vertical direction should not be affected, and so the following is only applied to the anterior velocity. 

This constant value can either be input manually or calculated from the offset velocity data. Since the foot experiences only the movement of the treadmill during plant phase, the velocity during this phase is that of the treadmill, as shown below. In this example, the treadmill is moving at a constant 1.0 m/s, which is shown during the horizontal phase of the velocity curve. 

![Velocity](/assets/img/Velocity.PNG)

Any value of the velocity curve from this phase may be used to find treadmill velocity, which can then be removed from this velocity curve to form a velocity graph relative to the treadmill (i.e., without the offset of the treadmill’s motion), as shown below. In this case, velocity during plant phase is 0, as it should be. 

![Normalised Velocity](/assets/img/NormalisedVelocity.PNG)


### [→ Correcting COM](https://tudor-muresan.github.io/2023-04-05-correcting-com/)

### [← Finding Velocity](https://tudor-muresan.github.io/2023-04-07-finding-velocity/)
