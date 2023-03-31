#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from os.path import join
import numpy as np
import pickle

#load object
def load_object(name, folder='.'):
    return pickle.load(open(join(folder, name + '.pickle'), 'rb'))


#Country / Year / Source to electrical capacity
cym2eleccapa = load_object('energy/cym2eleccapa_export')
c,y,m = 'France', 2015, 'Nuclear'
print(f'{m} capacity in {c} in {y}: {cym2eleccapa[c][y][m]:.2f} GW')

#Country / Year / Source to electrical production
cym2elecprod = load_object('energy/cym2elecprod_export')
c,y,m = 'Spain', 2018, 'Wind'
print(f'{m} production in {c} in {y}: {cym2elecprod[c][y][m]:.2f} TWh')

#Country / Year / Fossil to fossil consumption
cyf2fossilcons = load_object('energy/cyf2fossilcons_export')
c,y,f = 'Germany', 2013, 'Coal'
print(f'{f} consumption in {c} in {y}: {cyf2fossilcons[c][y][f]:.2f} TWh')

#Average global temperature to local temperature
ll2linregparam1, ll2linregparam2, pre_industrial_temperature = load_object('climate/ll2linregparams_export')
def temp_to_latlon2temp_cmip6_loclin(temp):
    dtemp = temp - pre_industrial_temperature
    ll2temp = ll2linregparam2 + ll2linregparam1 * dtemp
    return ll2temp
warming = 2.5 #°C
new_temp = pre_industrial_temperature + warming
print(f'Map of warming distribution on Earth for +{warming}°C')
plt.figure(figsize=(8,4))
after = temp_to_latlon2temp_cmip6_loclin(new_temp)
before = temp_to_latlon2temp_cmip6_loclin(pre_industrial_temperature)
plt.imshow((after-before), vmin=-6, vmax=6, cmap='jet')
plt.colorbar()
plt.show()

#Hydroelectricity potential per .1°
latlon_to_dam_maxpotentialtwh1800x3600 = np.load('energy/latlon_to_dam_maxpotentialtwh1800x3600_fp16.npy')
print(f'Max potential for hydroelectricity: {latlon_to_dam_maxpotentialtwh1800x3600.sum()/1e3:.2f} PWh')

#Proportion of land per .1°
latlon_to_landprop1800x3600 = np.load('demography/latlon_to_landprop1800x3600.npy')
print('Map of land proportion on Earth per .1° lat/lon')
plt.figure(figsize=(12,6))
plt.imshow(latlon_to_landprop1800x3600)
plt.show()

#Reserves (t / {'Coal':'mt', 'Gas':'bm3', 'Oil':'mmbbl'})
cyr2reserve = load_object('energy/cyr2reserve_exp')
c,y,r = 'Russia', 2022, 'Cobalt'
print(f'Reserves of {r} in {c} in {y}: {cyr2reserve[c][y][r]} t')

#Environmental risks for nuclear reactors
ll2nukegoodloc = np.load('energy/ll2nukegoodloc.npy')
print('Map of environmental risks for nuclear reactors')
plt.figure(figsize=(12,6))
plt.axis('off')
plt.imshow(ll2nukegoodloc[200:1400,550:3300], cmap='Oranges')
plt.show()

#Nuclear accidents
accidentsourcecause_to_deaths = load_object('energy/accidentsourcecause_to_deaths')
a,s,c='chernobyl', 'unscear_2000V2J', 'short_term_deaths'
print(f'Deaths ({c}) in {a} according to {s}: {accidentsourcecause_to_deaths[a][s][c]}')

#km/y/c
c2kmpy_sourced = load_object('energy/c2kmpy_sourced')

#Nuclear reactors data
nuclear_reactors = load_object('energy/nuclear_reactors')
nuc_construction_delays = []
for r in nuclear_reactors:
    if 'construction_delay' in r and r['capa_mw'] > 500:
        nuc_construction_delays += [r['construction_delay'] ]
plt.hist(nuc_construction_delays, 40)
plt.title('Construction delay for nuclear reactors')
plt.ylabel('Number of reactors')
plt.xlabel('Years')
plt.show()

#reactor2closurereason
nuclearreactor_to_state = load_object('energy/nuclearreactor_to_state')
n = 'Fukushima Daiichi 1'
print(f'Nuclear reactor: {n} | Closure reason: {nuclearreactor_to_state[n]}')








































