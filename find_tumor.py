#!/usr/bin/python3
import sys

def find_tumor(filename):
    sys.setrecursionlimit(5000)
    f = open(filename,"r")
    data = f.read()
    matrix = in_to_matrix(data)
    if rectangle_test(matrix) == False:
        return "Error,NA,NA\n"
    graph = build_graph(matrix)
    connected_components = get_connected_components(graph, matrix)
    return str(tumor_test(connected_components)) +','+ str(len(matrix)) + ',' + str(len(matrix[0]))+'\n'

def in_to_matrix(data):
    data = data.lower()
    data = data.splitlines()
    for index, segment in enumerate(data):
        data[index] = ''.join(filter(str.isalpha,segment))
        data[index]= list(data[index])
    return data

def rectangle_test(matrix):
    for row in matrix:
        if len(row) == len(matrix[0]):
            pass
        else:
            return False
    return True

def build_graph(matrix):
    graph = {}
    for i,row in enumerate(matrix):
        for j,cell in enumerate(row):
            v = str(i) +',' + str(j) 
            if v not in graph: graph[v] = set()
            for n in get_neighbors(matrix,i,j):
                if n not in graph: graph[n] = set()
                graph[v].add(n)
                graph[n].add(v)
    return graph


def get_neighbors(matrix,i,j):
    n = []
    letter = matrix[i][j]
    if (i - 1 > 0 and matrix[i-1][j] == letter): n.append(str(i-1) + ',' + str(j))
    if (j - 1 > 0 and matrix[i][j-1] == letter): n.append(str(i) + ',' + str(j-1))
    if (i + 1 < len(matrix) and matrix[i+1][j] == letter): n.append(str(i+1) + ',' + str(j))
    if (j + 1 < len(matrix[0]) and matrix[i][j+1] == letter): n.append(str(i) + ',' + str(j+1))
    #top left
    if (i - 1 > 0 and j - 1 > 0 and matrix[i-1][j-1] == letter): n.append(str(i-1)+','+str(j-1))
    #top right
    if (i - 1 > 0 and j + 1 < len(matrix[0]) and matrix[i-1][j+1] == letter): n.append(str(i-1)+','+str(j+1))
    #bottom right
    if (i + 1 < len(matrix) and j + 1 < len(matrix[0]) and matrix[i+1][j+1] == letter): n.append(str(i+1)+','+str(j+1))
    #bottom left
    if (i + 1 < len(matrix) and j - 1 > 0 and matrix[i+1][j-1] == letter): n.append(str(i+1)+','+str(j-1))
    return n


def get_connected_components(graph,matrix):
    componet_id = 0
    vertex_componets = {}  
    marked = set()
    def dfs(vertex):
        marked.add(vertex)
        i,j = vertex.split(',')
        vertex_componets[vertex] = [componet_id, matrix[int(i)][int(j)]]
        for u in graph[vertex]:
            if u not in marked: dfs(u)
    for v in graph:
        if v not in marked and len(graph[v])>0:
            dfs(v)
            componet_id = componet_id + 1 
    return vertex_componets

def tumor_test(connected_components):
    group_list = {}
    group_values = connected_components.values()
    for value in group_values:
        if value[1] not in group_list: group_list[value[1]] = set()
        group_list[value[1]].add(value[0])
    for x in group_list:
        if len(group_list[x]) > 1 : 
            return True
    return False



