---
layout: post
title: Joint Angle
tags: [Torques]
comments: true
---

As stated prior, joint angle can be found using marker position data, such as that used in this analysis. However, joint angle may also be derived from manual video analysis. Angles can be calculated by estimating the two body segments that make up the angle as straight lines. The angle between these two lines is then taken as the angular position of the distal segment (in this case, the foot). 

Such an analysis was conducted using Dartfish 10.0, though there were problems with extracting the edited video. As such, the same video was manually edited to superimpose segment lines and ankle joint angle values during one running stance phase. 

[![Joint Angle Video Analysis](/assets/img/JointAngle.PNG)](https://youtu.be/v2kiBL9FuOI)
*Please click on the image to be taken to the full video analysis*

The change in these angle values was also plotted below. In a full inverse dynamics analysis, this curve can be differentiated into angular velocity and acceleration, then used in a dynamic equilibrium equation to solve for joint moment.

![Joint Angle During Stance Phase](/assets/img/StanceAngle.png)
