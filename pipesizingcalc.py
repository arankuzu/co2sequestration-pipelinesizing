from cmath import pi

#PIPELINE SIZING CALCULATIONS FOR CO2 INJECTION.

import math

def pipesizing(L):

    Pdischarge = 660 #Compressor Discharge Pressure (Psi)
    
    d = float(input("Enter a value for d, in inches:  "))
    
    k = ( d**5 / ( 1 + 3.6 / d + 0.03 * d) ** (1/2) )
    
    L1 = L * 3280.8399 #Unit Conversion from km to ft
    
    h = ( 7 + 11 ) / 2 #Average of general. Height of water column in inches.
    
    SG = 1.521 #Specific Gravity of CO2
    
    g = 32.17405 #Gravitational Acceleration in Field Units
    
    q = 3550 * k * ( ( h / ( L1 * SG )) ** (1/2) ) 

    print('The amount of fluid that can be transported is {} ft3/h.'.format(q))

    CO2_Density = 0.03433537831687984 #Gas Density of CO2, 70 F of operating temperature, 660 psi operating Pressure (lb/ft3)

    Pipe_Area  = pi * ( ( d / 2 ) **2 )

    q1 = q / 3600 #Unit conversion from ft3/h to ft3/s

    print('The amount of fluid that can be transported is {} ft3/s.'.format(q1))

    Velocity = q1 / Pipe_Area

    CO2_viscosity = 0.014853282 #At 70 F Operating Temperature, cp

    Re = 1488 * ( CO2_Density * Velocity * (d/12) ) / ( CO2_viscosity )

    print('The reynolds number for the given pipe is {}.'.format(Re))

    if Re <= 2000:

        print("The flow regime is Laminar.  ")

        Ff = 64 / Re #Friction Factor, for circular pipes.

    elif 4000 > Re > 2000:

        print("The flow regime is Transient.  ")

        Ff =  1.2063 / ( Re ** (0.416) )
    
    elif Re >= 4000:

        print("The flow regime is Turbulent.  ")

        Ff =  0.316 / ( Re** (0.25) )
    
    pressure_loss = Ff * ( L1 / ( d / 12 ) ) * ( CO2_Density ) * ( ( Velocity**2 ) / ( 2 * g )  ) #Pressure Loss During Transportation

    print('The pressure loss during the CO2 transportation is {} psi.'.format(pressure_loss))

    Pinlet = Pdischarge - pressure_loss

    print('The discharge pressure is {} psi.'.format(Pinlet))

    mass_transferred_per_day = q * (0.01144) / (2204.62262)  #Conversion from lb to TONNE (Mass Flow Rate)

    print('The mass of CO2 transported per day is {} TONNE'.format(mass_transferred_per_day))

    return mass_transferred_per_day

pipe_length = [ 1, 2, 3, 4, 5 ] #Distances of pools from compressor

for distances in pipe_length:
    
    print(pipesizing(distances))
