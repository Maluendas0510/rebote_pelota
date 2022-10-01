# reobote de pelota

print("---------------------------")
print("-----rebote de pelota------")
print("---------------------------")

#input
h=int(input("dijite la altura desde donde cae la pelota:"))
i=(h/5)
r=0

#processing
while(h>i):
    h=h-(0.10*h)
    r=r+1
    
#fin
print("el resultado es:" + str(r))