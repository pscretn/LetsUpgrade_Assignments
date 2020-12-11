#Question 1
# Try 5 Different functions of the String in Python.

distro  =   "arch linux"
a = distro.split() # split fn
name = "lin,jim,lin"
b= name.count("lin") # count fn
print(a)
print(b)
c="CoDe"
print(c.upper()) # upper fn
print(c.lower()) # lower fn
d = distro.replace("arch","kali") # replace fn
print(d)
fs = 'repository'
print(fs.find('y')) # find fn

#Question 2
# Try 5 Different functions of the List object in Python

lst = ["roy","ram",5,6,6.7]
e = lst.pop(4) # pop fn
f =lst.index("ram") # index fn
print(e)
print(f)
ide =["geany","vscode"]
ide.append("xcode") # append fn
print(ide)
num = [1,3,5,6]
num.insert(1,2) # insert fn
print(num)
cou=num.count(5) # count fn
print(cou)

#Question 3
# Experiment with at least 5 default functions of Dictionary
dev1 = { "brand":"logitech","connectivity":"wireless"}
print(dev1)
dev1.clear() # clear fn
print(dev1)
dev2 = { "brand":"HP","connectivity":"wired"}
g=dev2.copy() # copy fn
print(dev2)
print(g)
h = dev2.get("brand") # get fn
print(h) 
dev2.pop("brand") # pop fn
print(dev2)
dev3 = { "brand":"dell","connectivity":"wireless"}
dev3.update({"color":"black"}) # update fn
print(dev3)