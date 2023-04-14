import random
    
def g(x):
    #return (-1/27)*(x+0.1)*(x-10.1)   #optimal 5 yes
    return (-1/60)*(x+0.1)*(x-14.1)   #optimal 8 yes

def beta(num_yes):
    if  random.random() < g(num_yes):
        return 0
    else: 
        return 1

def tsetlin_action(n,state): 
    if state<=n:
        return 0
    else: 
        return 1

def tsetlin_state(n,state,num_yes): 
    res=beta(num_yes)
    if res==0:
        if state!=1 and state!=n+1:
            state=state-1
    else:
        if state==n:
            state=2*n
        elif state==2*n:
            state=n
        else:
            state=state+1
    return state

def lri_action(pr):
    if random.random() < pr[0]:
        return 0
    else:
        return 1

def lri(pr,num_yes,action):
    res=beta(num_yes)
    if res==0 and action==0:
        pr[1]=kr*pr[1]
        pr[0]=1-pr[1]
    elif res==0 and action==1:
        pr[0]=kr*pr[0]
        pr[1]=1-pr[0]
    return pr

n=10
num_players=10
states=[]
actions=[]
pr=[]
kr=0.90
for i in range(num_players):
    states.append(n)
    actions.append(1)
    pr.append([0.5,0.5])

flag=True
while flag:
    for i in range(len(states)):
        actions[i]=tsetlin_action(n,states[i])
    num_yes=actions.count(0)
    for i in range(len(states)):
        states[i]=tsetlin_state(n,states[i],num_yes)
    if states.count(1)+states.count(n+1)==len(states):
        flag=False

print("Tsetlin Number of yes: ",actions.count(0))
print(actions)
print(states)

flag=True
while flag:
    for i in range(len(pr)):
        actions[i]=lri_action(pr[i])
    num_yes=actions.count(0)
    for i in range(len(pr)):
        pr[i]=lri(pr[i],num_yes,actions[i])
    count=0
    for i in range(len(pr)):
        if pr[i][0]>=0.99 or pr[i][1]>=0.99:
            count+=1
    if count==len(pr):
        flag=False

print("LRI Number of yes: ",actions.count(0))
print(actions)