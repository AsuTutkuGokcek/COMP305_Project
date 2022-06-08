
def find_row_total(input_matrix):
    total = 0
    length= len(input_matrix[1])

    matrix = [0] * length
    print(input_matrix[1])
    for i in range(0, length):
        for j in range(0, length):
             total += input_matrix[i][j] * (i+1)
        matrix[i]=total
        total = 0
    print(matrix)
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
    print("max index",max_index+1)
    print("secondmax index",second_max_index+1)



def floydWarshall(graph, vertex_num):
    # Code retrieved from:https://www.geeksforgeeks.org/python-initialize-empty-array-of-given-length/
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



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use a breakpoint in the code line below to debug your script.
    graph = [[0, 8, 4, 12,5],
             [8, 0, 9, 8, 3],
             [4, 9, 0, 13,6],
             [12,8,13,0,7],
             [5,3,6,7,0]
             ]
    # Print the solution
    dist = floydWarshall(graph,5)
    row_total = find_row_total(dist)
    find_locations(row_total)


