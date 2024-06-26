from typing import Union
from fastapi import FastAPI, Request
import os
import json

app = FastAPI()



@app.get("/helloworld")
def get_helloworld():
    return {"STATUS":"HELLOWORLD"}

@app.get("/test")
def get_test():
    return "OK"


@app.get("/nums")
def get_nums():
    return [1,2,3,4,"asghar"]

@app.get("/greet/{name}")
def get_greet(name):
    return "Hello "+str(name)

@app.get("/tavan/{number}")
def get_tavan(number):
    return int(number)**2

@app.get("/rev/{string}")
def get_rev(string):
    return string[::-1]

@app.get("/sum")
def get_sum(A:int = 10, B: int = 0):
    return A + B

@app.get("/run")
def get_run(command):
    return os.popen(command).read()

# @app.get("/counters/{num}")
# def get_counters(num):
#     num = int(num)
#     l = []
#     for i in range(1,num+1):
#         if num%i == 0:
#             l.append(i)
#     return l

@app.get("/user/info")
def get_user_data(request: Request): 
    userAgent = request.headers.get('User-Agent')
    ip = request.client.host
    port = request.client.port
    return {
        "user": {
            "agent": userAgent,
            "ip": ip,
            "port": port
        }
    }

    

@app.get("/counters/{num}")
def get_counters(num):
    return list(filter(lambda x : int(num)%x == 0,list(range(1,int(num)+1))))

@app.get("/contains")
def get_contains(A,B):
    return {"status":A in B}

@app.get("/wordout",status_code=200)
def get_wordout(string):
    return string.split(' ')

# @app.get("/common")
# def get_common(A,B,C):
#     a = A.split(' ')
#     b = B.split(' ')
#     c = C.split(' ')
#     l = []
#     for i in a:
#         if i in b and i in c:
#             l.append(i)
#     return l

@app.get("/common")
def get_common(A,B,C):
    return list(filter(lambda x : x in B.split(' ') and x in C.split(' '),A.split(' ')))

@app.get("/read_file")
def get_read_file():
    with open ('./ali.txt') as f:
        return f.read()
    
@app.get('/write_file')
def get_write_file(Text):
    with open('./ali.txt' , '+a') as f:
        f.write(Text)
        return {"status":200}
    
