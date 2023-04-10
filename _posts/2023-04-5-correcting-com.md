---
layout: post
title: Correcting COM
tags: [Correction]
comments: true
---

Once a normalised velocity curve has been acquired, integration – the opposing process to derivation – may be used to find the normalised (corrected) position of the COM in the anterior axis. Numerical integration can be used to approximate the area under the curve at any given point of a function f(x), which should determine COM displacement. 

Similarly to numerical differentiation, numerical integration can be undertaken using multiple methods. For this analysis, the trapezoid rule, which estimates the area under a curve of any given point using a trapezoid, was used. The formula is as follows:

{: .box-note}
I(x) = (a – b) x 0.5 x [f(x) + f(x+1)]

Where A and B are indices on the x-axis. 

When this technique is applied to the normalised velocity, the following normalised COM position graph is created:

![Normalised COM](/assets/img/StaticCOM.PNG)

This graph is entirely as expected. The position of the COM increases as the foot moves forward slightly at the start of stance phase, is constant when planted, and increases again when the foot is lifted. 
