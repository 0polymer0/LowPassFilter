# LowPassFilter

This was a simple script I put together using Anaconda. Its intent is to show I have basic competency in programming and physics.

The program filters high frequencies. The basic idea is that higher frequencies don't travel well through heavier materials. Simulating sound shaking a spring is easy.

The basic equation is 

Sound(t) - v l - k Output(t) = ma

Given an initial output and velocity we can calculate an acceleration, which gives us the next output and velocity. The program simply integrates the above differential equation, using an input sound as a driving force.