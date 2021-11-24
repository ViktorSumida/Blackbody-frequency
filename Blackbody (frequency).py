#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:16:34 2021

@author: Viktor Sumida
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig = plt.figure()
visivel = fig.add_subplot(111)
rect1 = patches.Rectangle((400e12, 0), 350e12, 1e15, alpha=0.8, color='xkcd:cyan')
visivel.add_patch(rect1)

h = 6.62607015e-34
c = 3.0e+8
k = 1.38064852e-23

def planck(freq, T):
    freq1 = freq * 1e12
    num = 2*h*(freq1**3)
    exponencial = (h*freq1)/(k*T)
    denom = (c**2) * (np.exp(exponencial) - 1.0)
    intensity = num/denom
    return intensity

frequencia = np.arange(1e-1, 2e4, 30)

intensity_O = planck(frequencia, 40000.0)
intensity_B = planck(frequencia, 20000.0)
intensity_A = planck(frequencia, 9000.0)
intensity_F = planck(frequencia, 7000.0)
intensity_G = planck(frequencia, 5500.0)
intensity_K = planck(frequencia, 4500.0)
intensity_M = planck(frequencia, 3000.0)

plt.loglog(frequencia * 1e12, intensity_O, 'r-')
plt.loglog(frequencia * 1e12, intensity_B, 'g-')
plt.loglog(frequencia * 1e12, intensity_A, 'b-')
plt.loglog(frequencia * 1e12, intensity_F, 'c-')
plt.loglog(frequencia * 1e12, intensity_G, 'm-')
plt.loglog(frequencia * 1e12, intensity_K, 'y-')
plt.loglog(frequencia * 1e12, intensity_M, 'xkcd:sky blue')

plt.title('Espectro de corpo negro', fontsize=20)

plt.legend(['O (40000K)', 'B (20000K)', 'A (9000K)', 'F (7000K)', 'G (5500K)', 'K (4500K)',
            'M (3000K)', 'Visível'], loc=0)

plt.xlabel('Frequência [Hz]', fontsize=15)
plt.ylabel('Intensidade [W/(m$^2$ Hz sr)]', fontsize=15)

plt.grid(True, which="both")
plt.xlim(7e12, 2e16)
plt.ylim(1e-10, 2e-5)

plt.show()