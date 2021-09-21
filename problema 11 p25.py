n=int(input('Dati numaru de elemente din vector='))
a=[]
print('Introduceti',n,'elemente pentru vectorul creat')
for i in range(0,n):
    x=int(input('Dati elementul='))
    a.extend([x])
print(a)
print('a)	 afişează pe ecran componentele tabloului la un interval de 5 poziţii;')
print('b)	 afişează pe ecran numerele în ordinea inversă a introducerii în calculator;')

print('c)	 sortează componentele tabloului în ordine descrescătoare;')
c=sorted(a)
c.sort(reverse=True)
print(c)
print('d)	 afişează pe ecran doar componentele pare;')
d=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        d.extend([y])
print(d)

print('e)	 afişează pe ecran media aritmetică a componentelor pare;')
e=sum(d)/len(d)
print(e)
print('f)	 afişează pe ecran doar componentele impare;')
f=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        x=a[i]
        f.extend([x])
print(f)
print('g)	 afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
x=int(input('x='))
y=int(input('y='))
g=[]
for i in range(0,len(a)):
    if(a[i]>x) and (a[i]%y != 0):
        g.append(a[i])
print(g)
           
print('h)	 afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')
h=[]
for i in range(0,len(a)):
    if(a[i]>x) and (a[i]<y):
        h.append(a[i])
print(h)
print('i)	 afişează pe ecran poziţiile (indicii) componentelor impare negative;')
m=[]
for i in range(0,len(a)):
    if(a[i]%2 !=0) and (a[i]<0):
        m.extend(a[i])
print(m)

print('j)	 afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
print('k)	 înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
k=a[:]
k[0]=min(k)
print(k)
print('l)	 înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;')
print('m)	creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
print('n)	 creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
n=[]
for i in range (0,len(a)):
    if a[i] %3==0:
        n.append(a[i])
print(n)
print('o)	 creează un tablou nou, format doar din acele componente ale tabloului introdus de la tastatură care au cel mult patru divizori.')