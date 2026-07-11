#Some problems on Strings
x="Coding for All"
print(x)
print(len(x))
print(x.upper())
print(x.lower())
print(x.capitalize())
print(x.title())
print(x.swapcase())
print(x[7:])
print(x.find("Coding"))
print(x.replace("Coding","Python"))
y="Python for Everyone"
print(y.replace("Everyone","All"))
print(x.split())
z="Facebook,Google,Microsoft,Apple,IBM,Oracle,Amazon"
print(z.split(","))
print(z.index("M"))
print(z.rfind("M"))
print(z.rfind("Apple"))
k="You cannot end a sentence with because because because is a conjunction"
start=k.find("because")
end=k.rfind("because")
print(start)
print(end)
print(k[start:end])
x="     Coding For All      "
print(x.strip())
a=["Bag","Bottle","Notes",]
print("Pen".join(a))
#Calculating radius
r=int(input("Enter the radius: "))
a=3.14*r**2
print(f"The area of the circle with the radius {r} is {a} meters square")
a,b=8,7
print(f"{a}+{b} = {a+b}")
print(f"{a}-{b} = {a-b}")
print(f"{a}*{b} = {a*b}")
print(f"{a}/{b} = {a/b}")
print(f"{a}//{b} = {a//b}")
print(f"{a}%{b} = {a%b}")
print(f"{a}**{b} = {a**b}")