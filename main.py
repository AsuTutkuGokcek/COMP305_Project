
def input_format(filename):
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    count = 0
    v= int(lines[0])
    e= int(lines[1])
    count =0
    weight = [0]*v
    for line in lines:
        count += 1
        if(count >=2 and count< 2+v):
            num1 = (lines[count].split())[0]
            num2 = (lines[count].split())[1]
            weight[int(num1)] = int(num2)
        if(count == 2+v):
            break

    print("wieghts are: ", weight)
    print("count is : ", count)
    distance = [[99999 for x in range(v)] for y in range(v)] 
    count = 0
    length= len(lines)

    for line in lines:
        count = count+1
        if(count >=2+v and count<length):
            if(lines[count] != None):
                num1 = (lines[count].split())[0]
                num2 = (lines[count].split())[1]
                num3 = (lines[count].split())[2]
                distance[int(num1)][int(num2)] = int(num3)
                distance[int(num2)][int(num1)] = int(num3)
            else: break
    
    return distance,weight,v,e
    

def find_row_total(input_matrix, weight_list,v,e):
    total = 0
    length= len(input_matrix[1])

    matrix = [0] * v
    for i in range(0, v):
        for j in range(0, v):
             total += input_matrix[i][j] * weight_list[i]
        matrix[i]=total
        total = 0
  
    return matrix


def find_locations(input_matrix):
    maximumm = -1
    secondmaximum = -2
    row_total = input_matrix
    max_index = -1
    second_max_index = -2
    for i in range(0, len(row_total)):
        if row_total[i] > maximumm:
            secondmaximum = maximumm
            maximumm = row_total[i]
            second_max_index = max_index
            max_index = i
        elif (row_total[i] < maximumm and row_total[i] > secondmaximum):
            secondmaximum = row_total[i]
            second_max_index = i

    print("max element ",maximumm)
    print("secondmax element",secondmaximum)
    print("max index",max_index)
    print("secondmax index",second_max_index)



def floydWarshall(graph, vertex_num):
    # Code retrieved from:https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
    V = vertex_num

    INF = 99999
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(V):

        # pick all vertices as source one by one
        for i in range(V):

            # Pick all vertices as destination for the
            # above picked source
            for j in range(V):
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )
    return dist


def clean_matrix(matrix,v,e):
    print("e is and v is : ",e,v)
    for i in range(v):
        for j in range(v):
            if(matrix[i][j]==99999):
                matrix[i][j] = 0
                matrix[j][i] = 0

    return matrix
    

if __name__ == '__main__':
 
    
    distance,weight,v,e=input_format("test2_new.txt")
    """
    graph = [[0, 8, 4, 12,5],
             [8, 0, 9, 8, 3],
             [4, 9, 0, 13,6],
             [12,8,13,0,7],
             [5,3,6,7,0]
             ]
    """
    # Print the solution
    #print("distance is: ", distance)
    dist = floydWarshall(distance,v)
    #print("shortest path for all pair:", dist)
    dist= clean_matrix(dist,v,e)
    row_total = find_row_total(dist,weight,v,e)
    #print("result matirx is: ",row_total)
    find_locations(row_total)
    



