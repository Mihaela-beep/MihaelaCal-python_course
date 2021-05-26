from shapes import circle, rectangle, square, triangle, paralelogram, trapezoid

def main():
  r = 3
  
  print("Circle with r = {}".format(r))

  print ("--------")

  c = circle.circumference(r)
  print("Circumference is {}".format(c))

  a = circle.area(r)
  print("Area is {}". format(a))
  
  print ("------")

  w = 3
  l = 4

  #print("Rectangle with w = {} and l = {}".format(w, l))
  print(f"Rectangle with w = {w}, l = {l}")

  p = rectangle.perimeter(w, l)
  print("Perimeter is {}".format(p))

  a = rectangle.area(w, l)
  print("Area is {}".format(a))

  print ("-----------")

  l = 6

  print(f"Square with l = {l}")

  p = square.perimeter(l)
  print("Perimeter is {}".format(p))

  a = square.area(l)
  print("Area is {}".format(a))

  print ("-----------")

  a = 6
  b = 10
  c = 8
  h = 12

  print(f"Triangle with a = {a}, b = {b}, c = {c}")

  p = triangle.perimeter(a, b, c)
  print("Perimeter is {}".format(p))

  a = triangle.area(a, h)
  print("Area is {}".format(a))

  print ("--------------")

  a = 10
  b = 12
  h = 8

  print(f"Paralelogram with a = {a}, b = {b}, h = {h}")

  p = paralelogram.perimeter(a, b)
  print("Perimeter is {}".format (p))

  a = paralelogram.area(b, h)
  print("Area is {}".format(a))

  print ("--------------")

  a = 6
  b = 8
  c = 5
  d = 7
  h = 4

  print(f"Trapezoid with a = {a}, b = {b}, c = {c}, d = {d}, h = {h}")

  p = trapezoid.perimeter(a, b, c, d)
  print("Perimeter is {}".format (p))

  a = trapezoid.area(a, b, h)
  print("Area is {}".format (a))

  print ("-----------")

if __name__ == "__main__":
  main()

  













