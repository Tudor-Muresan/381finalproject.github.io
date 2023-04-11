---
layout: post
title: Numerical Differentiation
subtitle: From Position to Velocity
tags: [Calculus]
comments: true
---

A derivative of a function is the rate of change of that function relative to a shared X-axis. As such, the rate of change of displacement relative to time is velocity. Similarly, the rate of change of velocity relative to time is linear acceleration, which is a variable required for this analysis. 

Numerical differentiation is a derivation technique which, instead of defining the equation of a derivative’s line relative to the equation of a function’s line, calculates the average slope between that function’s points. While this method is not perfect (as it averages slopes between points), it is sufficient for this analysis. 

There are various numerical differentiation methods, some of which are more accurate to the ‘true’ derivative of a function. In this analysis, the central difference method was used. This method estimates the slope of a point by using both the successive and preceding points of the function, as opposed to only the following or previous point. Its formula is as follows:

{: .box-note}
D(x) = (f(x+1) – f(x-1))/2T

Where D(x) is the derivative of the function f(x), and T corresponds to the period of the function, the difference between successive points on the x-axis (i.e., the difference in time between when data points were recorded). 


### [→ Finding Velocity](https://tudor-muresan.github.io/2023-04-07-finding-velocity/)

### [← Finding Stance Phase](https://tudor-muresan.github.io/2023-04-09-finding-stance-phase/)
