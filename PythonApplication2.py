#We have a steam heating boiler whose bursting pressure is known, but we of course want to use it only at pressures well below this limit. Our engineers recommend a safety factor of 3; that is, we should never exceed a pressure that is one-third of the rated bursting pressure.
#Write a program that reads in the rated bursting pressure and the current pressure, and determines if the boiler is operating at a safe pressure.
#For example:
#Enter the rated bursting pressure of the boiler (psi): 625
#Enter the current pressure (psi): 137.8
#The maximum safe pressure is 208.3 psi.
#The current pressure is safe.
#or
#Enter the rated bursting pressure of the boiler (psi): 625
#Enter the current pressure (psi): 250
#The maximum safe pressure is 208.3 psi.
#WARNING!  The current pressure is not safe.

#input
print("Enter the rated bursting pressure of the boiler (psi):")
ratedPressure = float(input())

print("Enter the current pressure (psi):")
currentPressure = float(input())

#calculated 1/3 psi of rated bursting pressure 
maximumPressure = ratedPressure * (1/3)

#output
print("The maximum safe pressure is {:.1f} psi.".format(maximumPressure))

#check entered psi is more than 1/3 of rated bursting pressure 
if (maximumPressure >= currentPressure):
    print("The current pressure is safe.")
else:
    print("WARNING! The current pressure is not safe.")