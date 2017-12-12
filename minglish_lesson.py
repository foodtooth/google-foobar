def answer(words):
    graph = create_graph(words)
    sorted_graph = sort_graph(graph)
    return ''.join(sorted_graph[::-1])


def create_graph(words):
    wordsLength = len(words)
    graph = {}
    for i in range(wordsLength):
        if words[i][0] not in graph:
            graph[words[i][0]] = []
        if i + 1 <= wordsLength - 1:
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    if words[i][j] not in graph:
                        graph[words[i][j]] = []
                    graph[words[i][j]].append(words[i + 1][j])
                    break
    return graph


def sort_graph(graph_dict):
    sorted_graph = []
    while graph_dict:
        acyclic = False
        for node, edges in graph_dict.items():
            for edge in edges:
                if edge in graph_dict:
                    break
            else:
                acyclic = True
                del graph_dict[node]
                sorted_graph.append(node)
        if not acyclic:
            raise RuntimeError("A cyclic dependency occurred")
    return sorted_graph

if __name__ == "__main__":
    answer(["ba", "cx", "fc", "fa", "ff"])
