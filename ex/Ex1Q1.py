def distance():
    x1,y1,z1 = input("Enter the coordinates of Point 1: ").split(",")
    x2,y2,z2 = input("Enter the coordinates of Point 2: ").split(",")
    
    x1 = float(x1)
    y1 = float(y1)
    z1 = float(z1)
    
    x2 = float(x2)
    y2 = float(y2)
    z2 = float(z2)
    
    temp_dist1 = x2 - x1
    temp_dist2 = y2 - y1
    temp_dist3 = z2 - z1
    temp_dist4 = temp_dist1**2 + temp_dist2**2 + temp_dist3**2
    distance = temp_dist4**0.5
    
    print("The distance between the two points is", distance, "units")
distance()