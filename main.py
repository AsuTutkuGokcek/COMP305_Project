
def greedy_function(weight_list):
    maximumm = -1
    secondmaximum = -2
    max_index = -1
    second_max_index = -2
    for i in range(0, len(weight_list)):
        if weight_list[i] >= maximumm:
            secondmaximum = maximumm
            maximumm = weight_list[i]
            second_max_index = max_index
            max_index = i
        elif (weight_list[i] < maximumm and weight_list[i] > secondmaximum):
            secondmaximum = weight_list[i]
            second_max_index = i

    print("max element in basic greedy ",maximumm)
    print("secondmax element in basic greedy",secondmaximum)
    print("max index in basic greedy",max_index)
    print("secondmax index in basic greedy",second_max_index)


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
    for i in range(0, v):
        for j in range(0, v):
                if(i==j):
                    distance[i][j]=0
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
    

def find_row_total(input_matrix, weight_list,v):
    total = 0
    length= len(input_matrix[1])

    matrix = [0] * v
    for i in range(0, v):
        for j in range(0, v):
             total += input_matrix[i][j] * weight_list[j]
        matrix[i]=total
        total = 0
  
    return matrix


def find_locations(input_matrix,index):
    minnimumm =999999
    row_total = input_matrix
    min_index = -1

    for i in range(0, len(row_total)):
        if row_total[i] < minnimumm:
            minnimumm = row_total[i]
            min_index = i
    
    if(index == -1):
        print("first min element ",minnimumm)
        print("minnode",min_index)
        return min_index
    else:
        if(index >minnimumm):
            print("second min element ",minnimumm)
            print("minnode",min_index)
            return min_index
        else:
            minnimumm = minnimumm-1
            print("second min element ",minnimumm)
            print("minnode",min_index)
            return min_index




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
    
def reduce_matrix(index,matrix,length,weigth):
    print("length is", length)
    new_matrix=[[99999 for x in range(length-1)] for y in range(length-1)] 
    array = []
    new_weight=[]
    for i in range(0,v):
        if(i != index):
            array.append(i)
            new_weight.append(weight[i])
    print(array)
    index_i = 0 
    index_j = 0 
    for i in array:
        for j in array:
            if(i <index) and (j <index):  
                new_matrix[i][j]=matrix[i][j]
            elif(i <index) and (j >=index):  
                index_j = j-1 
                new_matrix[i][index_j]=matrix[i][j]
            elif(i >index) and (j <index): 
                index_i = i-1 
                new_matrix[index_i][j]=matrix[i][j]
            elif(i >index) and (j >index):  
                index_j = j-1 
                index_i = i-1 
                new_matrix[index_i][index_j]=matrix[i][j]
    return new_matrix, new_weight

if __name__ == '__main__':
 
    
    distance,weight,v,e=input_format("test1_new.txt")
    greedy_function(weight)

    # Print the solution
    #print("distance is: ", distance)
    print(distance)
    dist = floydWarshall(distance,v)
    print("shortest path for all pair:", dist)
    dist= clean_matrix(dist,v,e)
    
    row_total = find_row_total(dist,weight,v)
    print("result matirx is: ",row_total)
    index = find_locations(row_total,-1)
    reduced,new_weight = reduce_matrix(index,dist,v,weight)
    print(reduced)
    print(new_weight)
    new_row_total = find_row_total(reduced,new_weight,v-1)
    new_index = find_locations(new_row_total,index)  

    



