shape =str (input("enter a shape :"))
if shape == "rectangle":
    length = float(input("enter length:"))
    width= float(input("enter width:"))
    print("the area of rectangle:",length*width)
elif shape =="circle" :
      rad= float(input("enter radious"))
      print ("the area of circle",3.14*rad*rad)
elif shape =="triangle" :
      base = float(input("enter base "))
      height = float (input("enter height"))
      print("area of triangle ", base *height/2)
elif  shape =="square":
      side= float(input("enter side :"))   
      print("area of square",side**2)
      