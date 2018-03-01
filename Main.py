

def read_file(infile):
    with open(infile,"+r") as file:
        line=file.readline()
        R,C,F,N,B,T=[int(i)for i in line.split()]
        print(R,C,F,N,B,T)
        routes=[[] for i in range(N)]
        for i in range(N):
            line=file.readline()
            for j in line.split():
                if j!='\n':
                    n=int(j)
                    routes[i].append(n)
        return R,C,F,N,B,T,routes

class Route:
    def __init__(self,a,b,x,y):
        self.a=a
        self.b=b
        self.x=x
        self.y=y
        self.avaiable=True

def compute(r,c,f,n,b,t,routes):
    pass


def run():
    infile="a_example.in"
    r,c,f,n,b,t,raw_routes=read_file(infile)
    routes=[]
    for i in raw_routes:
        r=Route(i[0],i[1],i[2],i[3])
        routes.append(r)
    compute(r,c,f,n,b,t,routes)

run()