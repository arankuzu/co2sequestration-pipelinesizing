from numpy import arange
import time
from cmath import pi

DIFF = 0.01

def pipesizingg(m):

    CO2_Density = 7.34 #lb/ft3 @ 660 psi, 70 F

    Z = 0.83 #Gas Deviation Factor
    
    L = float(input("Enter a value for L, in ft:  "))

    Pb = 660 #Psi

    Tb = 530 #Rankine

    G = 1.521 #CO2 Gas Specific Gravity

    T = 530 #Rankine

    P_1 = 660 #Psi

    P_2 = 600 #Psi

    q = ( ( m * 2204.62262 ) / 90 ) * ( 1 / CO2_Density ) #from TONNE/d to lb/day ----------> ft3/day

    m1 = m / 90

    print('The INJECTION mass flow rate is {} TONNE/day. '.format(m1))
    
    arr = arange(0.000001, 50., 0.000001)

    start = time.time()

    for d in arr:

        q1 = 433.5 * ( Tb / Pb ) * ( ( ( ( (P_1) **2 ) - ( (P_2) **2 ) ) / ( G * T * L * Z ) ) ** ( 0.5 ) ) * ( d ** (2.667) )

        if abs(q1 - q) <= DIFF:
            
            end = time.time()
            
            print(str(end - start), "seconds elapsed")
            
            print('The diameter of the pipe is {} inches.'.format(d))
    
    end = time.time()
    
    print(str(end - start), "seconds elapsed")
    
    g = 32.17405 #Gravitational Acceleration in Field Units

    CO2_viscosity = 0.014853282 #At 70 F Operating Temperature, cp
    
    q2 = q1 / ( 24 * 3600 ) #Unit Conversion from ft3/day to ft3/sec

    Velocity = q2 / ( pi * ( ( ( d / 12 ) ** 2 ) / 4 ) )

    Re = 1488 * ( CO2_Density * Velocity * ( d / 12 ) ) / ( CO2_viscosity )

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
    
    pressure_loss = Ff * ( L / ( d / 12 ) ) * ( CO2_Density ) * ( ( Velocity**2 ) / ( 2 * g )  ) #Pressure Loss During Transportation

    print('The pressure loss during the CO2 INJECTION is {} psi.'.format(pressure_loss))

required_mass = [ 5058.359001,
2936.978954,
1533.409076,
8437.109931,
5373.848372,
9426.371585,
5954.243754,
1885.982236,
6280.483117,
4026.002312,
929.0637623,
5323.311982,
4810.49067
 ]

for mass in required_mass:

    print(pipesizingg(mass))