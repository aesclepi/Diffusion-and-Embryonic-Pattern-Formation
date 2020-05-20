# -*- coding: utf-8 -*-
"""
Created on Tue May 19 21:38:21 2020
Modified on Tue May 19 21:38:21 2020 
Author: A. Waterston
"""

import numpy as np
import matplotlib.pyplot as plt

class Simulation(object):
    def __init__(self, L=400, nx=1000, dt=0.001, tau=1, D=0.00000001):
        """
        :param L: float, length of box
        :param nx: int, number of grid points
        :param dt: float, time step
        :param tau: float, tau
        :param D: float, diffusion coefficient
        all units are under IS.
        """
        self.L = L
        self.n = nx
        self.x = np.linspace(0, L, nx)
        #self.c = 1.*self.gaussian(self.x, 0.0, 10.)
        self.c = np.zeros(self.n) # c(t=0)
        self.c0 = self.c.copy()
        self.dt = dt
        self.dx = self.x[1] - self.x[0]
        self.tau = tau
        self.D = D
        self.lumin = np.array([])

    def gaussian(self, x, mu, sig):
        return 1./(np.sqrt(2.*np.pi)*sig)*np.exp(-np.square((x - mu)/sig)/2)

    def set_f(self):
        """
        set the source term
        """
        self.f = 1e-6*self.gaussian(self.x, 0.0, 10.) 
        #self.f = 1e-6*1/self.x

    def calc_diffusion(self):
        """
        calculate the diffuion term
        return D*\lapacian c
        """
        xdc = np.gradient(self.c, self.x, edge_order=2)
        xdc2 = np.gradient(xdc, self.x, edge_order=2)
        return self.D*xdc2

    def calc_lumin(self):
        """
        calculate the luminescence term
        return -1/tau*c
        """
        return -1./self.tau*self.c

    def update(self, step):
        """
        :param step: int, time step
        updating c for one time step,
        adding up 3 terms (diffusion, lumin, source)
        """
        print("step: {}".format(step))
        print("diffusion: {}".format(self.calc_diffusion()[:10]))
        print("lumin: {}".format(self.calc_lumin()[:10]))
        print("source: {}".format(self.f[:10]))
        print("c: {}".format(self.c[:10]))
        print("-"*60)
        c_lumin = self.calc_lumin()
        c_lumin_int = -np.trapz(self.calc_lumin(), self.x)
        self.c += self.dt*(self.calc_diffusion() + c_lumin + self.f)
        self.lumin = np.append(self.lumin, c_lumin_int)
        # self.c += self.dt*self.calc_diffusion()

    def run(self, nt=100):
        self.set_f()
        for step in range(nt):
            self.update(step)
        plt.plot(self.x, self.c) 
        #plt.plot(self.x, self.f)
        #plt.plot(self.x, self.c0) 
        #plt.plot(self.lumin)
        plt.show()
    
simul = Simulation()
simul.run()

y = np.linspace(-200,200,400)
X, Y = np.meshgrid(simul.c, y)
Z = np.square(X-25)# (X-25)^2
Z[:, :25] = -Z[:, :25]
plt.contourf(X[:, :50], Y[:, :50], Z[:, :50], 500, cmap = 'bwr')
plt.colorbar();
