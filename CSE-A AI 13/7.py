from collections import deque

def waterjug(jug1_capacity,jug2_capacity,target):
    queue=deque()
    visited=set()

    queue.append((0,0))
    visited.add((0,0))
    parent={}
#bfs
    while queue:
        jug1,jug2=queue.popleft()
        print(f"{jug1},{jug2}")

        if jug1==target or jug2==target or jug1+jug2==target:
            print("Target Reached")
            path=[]
            while(jug1,jug2) in parent:
                path.append((jug1,jug2))
                jug1,jug2=parent[(jug1,jug2)]
            path.append((0,0))
            path.reverse()
            print("Step to reach target:")
            for step in path:
                print(f"Jug1={step[0]},Jug2={step[1]}")
            return


        possible_states=[
            (jug1_capacity,jug2),
            (jug1,jug2_capacity),
            (0,jug2),
            (jug1,0),
            (min(jug1_capacity,jug1+jug2),jug2-(min(jug1_capacity,jug1+jug2)-jug1)),
            (jug1-(min(jug2_capacity,jug1+jug2)-jug2),min(jug2_capacity,jug1+jug2))
        ]
        for state in possible_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
                parent[state]=(jug1,jug2)
    print("Target can't be reached")
    return
jug1_capacity=4
jug2_capacity=3
target=2
waterjug(jug1_capacity,jug2_capacity,target)
