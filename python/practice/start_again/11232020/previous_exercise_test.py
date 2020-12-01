#Write a function that computes the volume of a sphere given its radius.
def sphere(x):
    sphr = (4/3) * 3.14 * x**3
    print ("Sphere is {}".format(sphr))
sphere(input("Enter the radius  " ))