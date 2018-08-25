import networkx as nx
from networkx.algorithms.flow import ford_fulkerson
file = 'Katia.txt'

def CountNodes(file):
    f = open(file)
    for line in f.readlines():
        rt = [int(item) for item in line.split()]
    f.close()
    return str(rt[1])
def initialization(G):
    f = open(file)
    for line in f.readlines():
        tmp = [item for item in line.split()]
        G.add_edge(tmp[0], tmp[1], capacity=float(tmp[2]))
    f.close()
    return G


def transfer_to_matrix(R):

    matrix = []
    for i in range(len(R.graph['flow_dict'])):
        matrix.append([0] * len(R.graph['flow_dict']))

    for key in R.graph['flow_dict']:
        dict = R.graph['flow_dict'][key]
        for item in dict:
            matrix[int(key) - 1][int(item) - 1] = int(dict[item])

    return matrix


def balance_point(matrix, maxf):
    for count in range(len(matrix)):
        out = 0
        inp = 0
        for item in range(len(matrix)):
            out += matrix[count][item]
            inp += matrix[item][count]
        if out != inp:
            print('Рiзниця кiлькостi заходячих i виходячих потокiв вершини ' + str(count + 1) + ": " + maxf)
        else:
            print('Рiзниця кiлькостi заходячих i виходячих потокiв вершини ' + str(count + 1) + ": 0")


def main():
    G = nx.DiGraph()
    G = initialization(G)
    R = ford_fulkerson(G, '1', CountNodes(file))
    print("Максимальний потік даного графа: " + str(int(R.graph['flow_value'])) + '\n')
    matrix = transfer_to_matrix(R)
    balance_point(matrix, str(int(R.graph['flow_value'])))


if __name__ == "__main__":
    main()
