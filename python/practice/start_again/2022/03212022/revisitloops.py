def upper_triangle_for(n):
   for i in range(n,0,-1):
       stars=""
       for j in range(i):
           stars+="* "
       print (stars)
upper_triangle_for(int(input("Enter the number of stars: ")))