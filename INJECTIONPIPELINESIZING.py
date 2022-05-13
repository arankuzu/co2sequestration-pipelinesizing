from cmath import pi

import math
from numpy import absolute

def diameter(m):

    L = float(input("Enter the length of this pipe, in ft:  ")) #in ft

    L1 = L / 3280.8399 #from ft to km

    D = float(input("Enter a diameter, in inches:  "))

    CO2_Density = 117.57552116486639 #lb/ft3

    T = 70 #Fahrenheit

    e = 0.00015 #ft

    CO2_Viscosity = 0.0000148533 #Pa-s

    Pin = 4.550540997271744 #MPa

    Pout =  Pin - ( Pin * 0.1 )

    dP = Pin - Pout

    Pint = ( Pin + Pout ) / 2
    
    m1 = m / 90 #Unit conversion from TONNE to TONNE/day

    Re = ( 4 * 1000 / 24 / 3600 / 0.0254 ) * m1 / ( pi * CO2_Viscosity * D )

    print('The Reynolds Number is {} .'.format(Re))

    Ff = 1 / ( 4 * ( ( -1.8 ) * ( math.log10( ( 6.91 / Re ) + ( ( 12 * ( e / D ) / 3.7 ) ** (1.11) ) ) ) ) ** ( 2 ) )

    print('The Ff is {} .'.format(Ff))

    D1 = ( 1 / 0.0254 ) * ( ( ( 32 * Ff * (m1**2)  ) * ( ( 1000 / 24 / 3600) ** 2 ) /  ( (pi**2) * CO2_Density * (dP/L1) * (10**6) / 1000 ) ) ** (1/5) ) 

    print('The diameter is {} inches.'.format(D1))

    if absolute(D1-D) <= 0.1:

        print('The diameter of the pipe is {} inches'.format(D1))

        return D1

    elif absolute(D1-D) > 0.1:

        Re1 = ( 4 * 1000 / 24 / 3600 / 0.0254 ) * m1 / ( pi * CO2_Viscosity * D1 )

        print('The Reynolds Number is {} .'.format(Re1))

        FF1 = 1 / ( 4 * ( ( -1.8 ) * ( math.log10( ( 6.91 / Re1 ) + ( ( 12 * ( e / D1 ) / 3.7 ) ** (1.11) ) ) ) ) ** ( 2 ) )

        print('The Ff1 is {} .'.format(Ff))

        D2 = ( 1 / 0.0254 ) * ( ( ( 32 * FF1 * (m1**2)  ) * ( ( 1000 / 24 / 3600) ** 2 ) /  ( (pi**2) * CO2_Density * (dP/L1) * (10**6) / 1000 ) ) ** (1/5) ) 

        print('The diameter is {} inches.'.format(D2))

        if absolute(D2-D1) <= 0.1:

            print('The diameter of the pipe is {} inches'.format(D2))

            return D2

        elif absolute(D2-D1) > 0.1:

            Re2 = ( 4 * 1000 / 24 / 3600 / 0.0254 ) * m1 / ( pi * CO2_Viscosity * D2 )

            print('The Reynolds Number is {} .'.format(Re2))

            Ff2 = 1 / ( 4 * ( ( -1.8 ) * ( math.log10( ( 6.91 / Re2 ) + ( ( 12 * ( e / D2 ) / 3.7 ) ** (1.11) ) ) ) ) ** ( 2 ) )

            print('The Ff is {} .'.format(Ff))

            D3 = ( 1 / 0.0254 ) * ( ( ( 32 * Ff2 * (m1**2)  ) * ( ( 1000 / 24 / 3600) ** 2 ) /  ( (pi**2) * CO2_Density * (dP/L1) * (10**6) / 1000 ) ) ** (1/5) ) 

            print('The diameter is {} inches.'.format(D3))

            if absolute(D3-D2) <= 0.1:

                print('The diameter of the pipe is {} inches'.format(D3))

                return D3

            elif absolute(D3-D2) > 0.1:

                Re3 = ( 4 * 1000 / 24 / 3600 / 0.0254 ) * m1 / ( pi * CO2_Viscosity * D3 )

                print('The Reynolds Number is {} .'.format(Re3))

                Ff3 = 1 / ( 4 * ( ( -1.8 ) * ( math.log10( ( 6.91 / Re3 ) + ( ( 12 * ( e / D3 ) / 3.7 ) ** (1.11) ) ) ) ) ** ( 2 ) )

                print('The Ff is {} .'.format(Ff3))

                D4 = ( 1 / 0.0254 ) * ( ( ( 32 * Ff3 * (m1**2)  ) * ( ( 1000 / 24 / 3600) ** 2 ) /  ( (pi**2) * CO2_Density * (dP/L1) * (10**6) / 1000 ) ) ** (1/5) ) 

                print('The diameter is {} inches.'.format(D4))

                if absolute(D4-D3) <= 0.1:

                    print('The diameter of the pipe is {} inches'.format(D4))

                    return D4

                elif absolute(D4-D3) > 0.1:

                    Re4 = ( 4 * 1000 / 24 / 3600 / 0.0254 ) * m1 / ( pi * CO2_Viscosity * D4 )

                    print('The Reynolds Number is {} .'.format(Re4))

                    Ff4 = 1 / ( 4 * ( ( -1.8 ) * ( math.log10( ( 6.91 / Re4 ) + ( ( 12 * ( e / D4 ) / 3.7 ) ** (1.11) ) ) ) ) ** ( 2 ) )

                    print('The Ff is {} .'.format(Ff4))

                    D5 = ( 1 / 0.0254 ) * ( ( ( 32 * Ff4 * (m1**2)  ) * ( ( 1000 / 24 / 3600) ** 2 ) /  ( (pi**2) * CO2_Density * (dP/L1) * (10**6) / 1000 ) ) ** (1/5) ) 

                    print('The diameter is {} inches.'.format(D1))

                    if absolute(D5-D4) <= 0.1:

                        print('The diameter of the pipe is {} inches'.format(D5))

                        return D5

                    else:

                        print("ARE YOU KIDDING ME!!!!!!  ")

                        return -1

mass = [ 3098 ]

for masses in mass:

    print(diameter(masses))