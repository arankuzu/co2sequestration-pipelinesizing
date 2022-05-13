#ENGINEERING DESIGN ECONOMICAL EVALUATION

import math

from pyrsistent import v

import pandas as pd

def CO2_Needed(Volume):
    
    P  = 500 #psi (Average in Lloydminster)
    
    mA = 44.01 #lb (Average in Lloydminster)
    
    T  = 535 #R (Average in Lloydminster)
    
    R  = 10.732 #Universal Gas Constant 
    
    z  = 0.83 #from COX graph
    
    Vsand = Volume * 0.02 #Sand Volume
    
    Vtotal = Volume + Vsand #Total Volume ( Sand + Primary Fluid Production )

    n = ( P * Vtotal ) / ( R * T * z )

    m = n * mA
    
    m1 = m / 2204.62262 #Unit Conversion from lb to TONNE
    
    print('The amount of CO2 that is required to pressurize the reservoir {} TONNE.'.format(m1))
    
    CO2 = 50 #Price for CO2 Per TONNE
    
    daily_injection_rate = m1 / 90 #Daily rate for 3 months of Injection
    
    print('The amount of CO2 that should be injected DAILY for this well is {} TONNE.'.format(daily_injection_rate))
    
    money = m1 * CO2
    
    print('The amount of money required to buy required amount of CO2 is {} $.'.format(money))
    
    return money

voidage_list_for_pools = [ 453453 ]

for volumes in voidage_list_for_pools:

    zx = input("Enter a pool name:  ")
    
    print('The Calculations for {} is: '.format(zx))

    print(CO2_Needed(volumes))