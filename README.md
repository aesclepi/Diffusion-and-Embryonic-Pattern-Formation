# Diffusion-and-Embryonic-Pattern-Formation

This is a python script that can model the 1 dimensional diffusion-based chemcial gradient set up during early embryonic pattern formation.This project is inspired by a 2005 PNAS article entitled, "Diffusion and scaling during early embryonic pattern formation." 
The conclusion of the study is that the Bicoid chemical gradient is sufficient to explain the scaling in gene patterning observed across species of Drosophila with various sized eggs. 
At first approximation, this can be modeled as an initial value problem, wherein an initial concentration profile in x is assumed and numerical methods are used to find the first time derivative. 
This simple model would be insufficient to show the effects of diffusion coefficeints or chemical lifetimes on the concentration profiles of large and small eggs. 
In the script shared here, we have a working model where diffusion follows the governing equation: dc/dt = D*d^2c/dx^2 - c/tau + s . 
Where C is a variable to represent chemical concentration in the x and time dimensions, tau is the chemical lifetime in seconds, and s is a constant source term.
The starting parameters in the model are for the species Lucillia sericata. 
Also, numpy.gradient is used to estimate the first and second spacial derivatives in x.
The resulting concentration gradient can be projected unto a rectangularly shaped egg with length L to show that scaling is indeed possible across species by merely tuning the chemical lifetime, tau (luminescence term in script, lifetime of mol lum.).
A real advantage of this model is that it encorporates L, D, and tau as input parameters.
The model assumes a gaussian distripution of the source term. Considerign these assumptions, which can be modified, the time to steady state can be predicted by the model by applying a threshold concentration at a certain x known to be association with steady state conditions.
