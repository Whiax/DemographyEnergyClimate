# DEC : Demography Energy Climate 

This repository contains some data and models used to produce the DEC report.  
The DEC report is freely accessible: 
- ➡️➡️ [The DEC Report (pdf)](https://drive.google.com/file/d/1q0wuwa_jcpo6eeyIMtnUm5bYaVvF3j82/)  
- 🌊 [Hydropower potential](https://hyugen-ai.medium.com/how-i-evaluated-the-worlds-potential-for-hydroelectricity-f97ca7376e20) (1/8)
- ☀️ [Solar power potential](https://hyugen-ai.medium.com/how-i-evaluated-the-worlds-potential-for-solar-energy-8bf32225af1b) (2/8)
- 🌬️ [Wind power potential](https://hyugen-ai.medium.com/how-i-evaluated-the-worlds-potential-for-wind-energy-3200ab3b19b9) (3/8)
- 🏭 [Nuclear power potential](https://hyugen-ai.medium.com/how-i-assessed-the-global-potential-of-nuclear-energy-f26ec101b41b) (4/8)
- 🛢 [How much fossil fuel do we consume each year?](https://hyugen-ai.medium.com/how-much-fossil-fuel-do-we-consume-each-year-5afaa67f43a6) (5/8)
- 🔥 [Energy, EROI and limits to growth](https://hyugen-ai.medium.com/energy-eroi-and-limits-to-growth-6e8baeed7dc1) (6/8)
- ☢️ [How many people died because of the Chernobyl disaster?](https://hyugen-ai.medium.com/how-many-people-died-because-of-the-chernobyl-disaster-b01c392736b1) (7/8)
- ⚡ [Why do we close nuclear reactors?](https://hyugen-ai.medium.com/why-do-we-close-nuclear-reactors-cdfa7f1ea86c) (8/8)

*(Sources are detailed in the report)*

## Examples

**Installed nuclear capacity in France in 2015:**
```
cym2eleccapa = load_object('energy/cym2eleccapa_export')
c,y,m = 'France', 2015, 'Nuclear'
print(f'{m} capacity in {c} in {y}: {cym2eleccapa[c][y][m]:.2f} GW')
```
> Nuclear capacity in France in 2015: 63.13 GW

**Wind electricity production in Spain in 2018:**
```
cym2elecprod = load_object('energy/cym2elecprod_export')
c,y,m = 'Spain', 2018, 'Wind'
print(f'{m} production in {c} in {y}: {cym2elecprod[c][y][m]:.2f} TWh')
```
> Wind production in Spain in 2018: 49.65 TWh

**Coal consumption in Germany in 2013:**
```
cyf2fossilcons = load_object('energy/cyf2fossilcons_export')
c,y,f = 'Germany', 2013, 'Coal'
print(f'{f} consumption in {c} in {y}: {cyf2fossilcons[c][y][f]:.2f} TWh')
```
> Coal consumption in Germany in 2013: 979.27 TWh

**Map of warming distribution on Earth for +2.5°C**
```
warming = 2.5 #°C
new_temp = pre_industrial_temperature + warming
after = temp_to_latlon2temp_cmip6_loclin(new_temp)
before = temp_to_latlon2temp_cmip6_loclin(pre_industrial_temperature)
plt.imshow((after-before), vmin=-6, vmax=6, cmap='jet')
```
> ![te](https://user-images.githubusercontent.com/12411288/229200161-98209e2a-a3bc-45ea-9ee4-98275e7ee470.png)

**Hydroelectricity potential**
```
print(f'Max potential for hydroelectricity: {latlon_to_dam_maxpotentialtwh1800x3600.sum()/1e3:.2f} PWh')
```
> Max potential for hydroelectricity: 51.71 PWh

**Proportion of land**
```
plt.imshow(latlon_to_landprop1800x3600)
```
> ![landprop](https://user-images.githubusercontent.com/12411288/229200773-81edb5d8-413f-4fec-8ef2-58842e987c31.png)

**Reserves of Cobalt in Russia in 2022**
```
cyr2reserve = load_object('energy/cyr2reserve_exp')
c,y,r = 'Russia', 2022, 'Cobalt'
print(f'Reserves of {r} in {c} in {y}: {cyr2reserve[c][y][r]} t')
```
> Reserves of Cobalt in Russia in 2022: 250000.0 t

**Map of environmental constraints for nuclear reactors**
> ![nukeenv](https://user-images.githubusercontent.com/12411288/229201876-9332a688-f10b-4016-b1c7-742719183232.png)

**Data on civilian nuclear accidents:**
```
accidentsourcecause_to_deaths = load_object('energy/accidentsourcecause_to_deaths')
a,s,c='chernobyl', 'unscear_2000V2J', 'short_term_deaths'
print(f'Deaths ({c}) in {a} according to {s}: {accidentsourcecause_to_deaths[a][s][c]}')
```
> Deaths (short_term_deaths) in chernobyl according to unscear_2000V2J: 31

**Data on nuclear reactors**
```
nuclear_reactors = load_object('energy/nuclear_reactors')
nuc_construction_delays = []
for r in nuclear_reactors:
    if 'construction_delay' in r and r['capa_mw'] > 500:
        nuc_construction_delays += [r['construction_delay'] ]
plt.hist(nuc_construction_delays, 40)
```
> ![ezfze](https://user-images.githubusercontent.com/12411288/229202590-4ff439ac-9e39-439e-b2e6-92391742ac52.png)

**Nuclear reactor status / closure reasons**
```
nuclearreactor_to_state = load_object('energy/nuclearreactor_to_state')
n = 'Fukushima Daiichi 1'
print(f'Nuclear reactor: {n} | Closure reason: {nuclearreactor_to_state[n]}')
```
> Nuclear reactor: Fukushima Daiichi 1 | Closure reason: internal_accident













