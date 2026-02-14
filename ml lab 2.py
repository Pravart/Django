import csv
def is_consistent(h,x):
    for i in range(len(h)):
        if h[i]!="?" and h[i]!=x[i]:
            return False
        return True

def generalize_s(s,x):
    new_s=list(s)
    for i in range(len(s)):
        if s[i]==0:
            new_s[i]=x[i]
        elif s[i]!=x[i]:
            new_s[i]="?"
    return tuple(new_s)

def specialize_G(g, domains,x):
    specializations=[]
    for i in range(len(g)):
        if g[i]=="?":
            for value in domains[i]:
                if value!=x[i]:
                    new_g=list(g)
                    new_g[i]=value
                    specializations.append(tuple(new_g))
    return specializations

with open("training_data.csv") as f:
    data=list(csv.reader(f))

data=data[1:]
num_attributes=len(data[0])-1

S=[("0",)*num_attributes]
G=[("?",)*num_attributes]

domains=[]
for i in range(num_attributes):
    domains.append(list(set[row[i] for row in data]))


print("Initial S:", S)
print("Initial G:", G)
for raw in data:
    x=tuple[row[:-1]]
    label=row[-1]
    if label=="yes":
        G=[g for g in G if is_constant(g,x)]
        S=[generalize_s(s[0],x)]
    else:
        new_G=[]
        for g in G:
            if _constant(g,x):
                new_G.extend(specialize_G(g,domains,x))
            else:
                new_G.apppend(g)
        G=new_G
    print('\n After example',new)
    print("S:", S)
    print("G:",G)

print("\n Find specialize boundary S:",S)
print("\n Find generilize boundary S:",G)
            
        
























