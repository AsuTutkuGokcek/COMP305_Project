from collections import defaultdict
INT_MAX = float('Inf')

# Function that returns the vertex 
# with minimum distance 
# from the source
def Min_Distance(dist, visit):

    (minimum, Minimum_Vertex) = (INT_MAX, 0)
    for vertex in range(len(dist)):
        if minimum > dist[vertex] and visit[vertex] == False:
            (minimum, minVertex) = (dist[vertex], vertex)

    return Minimum_Vertex


# Dijkstra Algorithm for Modified
# Graph (After removing the negative weights)
def Dijkstra_Algorithm(graph, Altered_Graph, source):

    # Number of vertices in the graph
    tot_vertices = len(graph)

    # Dictionary to check if given vertex is
    # already included in the shortest path tree
    sptSet = defaultdict(lambda : False)

    # Shortest distance of all vertices from the source
    dist = [INT_MAX] * tot_vertices

    dist[source] = 0

    for count in range(tot_vertices):

        # The current vertex which is at min Distance
        # from the source and not yet included in the
        # shortest path tree
        curVertex = Min_Distance(dist, sptSet)
        sptSet[curVertex] = True

        for vertex in range(tot_vertices):
            if ((sptSet[vertex] == False) and
                (dist[vertex] > (dist[curVertex] +
                Altered_Graph[curVertex][vertex])) and
                (graph[curVertex][vertex] != 0)):
                                 
                                                    dist[vertex] = (dist[curVertex] +Altered_Graph[curVertex][vertex])

    # Print the Shortest distance from the source
    print(dist)

# Function to calculate shortest distances from source
# to all other vertices using Bellman-Ford algorithm
def BellmanFord_Algorithm(edges, graph, tot_vertices):

    # Add a source s and calculate its min
    # distance from every other node
    dist = [INT_MAX] * (tot_vertices + 1)
    dist[tot_vertices] = 0

    for i in range(tot_vertices):
        edges.append([tot_vertices, i, 0])

    for i in range(tot_vertices):
        for (source, destn, weight) in edges:
            if((dist[source] != INT_MAX) and
                    (dist[source] + weight < dist[destn])):
                dist[destn] = dist[source] + weight

    # Don't send the value for the source added
    return dist[0:tot_vertices]

# Function to implement Johnson Algorithm
def JohnsonAlgorithm(graph):

    edges = []

    # Create a list of edges for Bellman-Ford Algorithm
    for i in range(len(graph)):
        for j in range(len(graph[i])):

            if graph[i][j] != 0:
                edges.append([i, j, graph[i][j]])

    # Weights used to modify the original weights
    Alter_weigts = BellmanFord_Algorithm(edges, graph, len(graph))

    Altered_Graph = [[0 for p in range(len(graph))] for q in
                    range(len(graph))]

    # Modify the weights to get rid of negative weights
    for i in range(len(graph)):
        for j in range(len(graph[i])):

            if graph[i][j] != 0:
                Altered_Graph[i][j] = (graph[i][j] +
                        Alter_weigts[i] - Alter_weigts[j]);

    print ('Modified Graph: ' + str(Altered_Graph))

    # Run Dijkstra for every vertex as source one by one
    for source in range(len(graph)):
        print ('\nShortest Distance with vertex ' +
                        str(source) + ' as the source:\n')
        Dijkstra_Algorithm(graph, Altered_Graph, source)


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

    print("max element in greedy ",maximumm)
    print("secondmax element in greedy",secondmaximum)
    print("max index in greedy",max_index)
    print("secondmax index in greedy",second_max_index)




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
 
    
    distance,weight,v,e=input_format("test1_new.txt")
    greedy_function(weight)

    # Print the solution
    #print("distance is: ", distance)
    print(distance)
    dist = floydWarshall(distance,v)
    print("shortest path for all pair:", dist)
    dist= clean_matrix(dist,v,e)
    row_total = find_row_total(dist,weight,v,e)
    print("result matirx is: ",row_total)
    find_locations(row_total)
    



