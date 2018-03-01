"""hash code 2018

git gud production ;)
"""

def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes:
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distance[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path

def save_file(*args):
    pass  # TODO


def open_file(*args):
    pass  # TODO

class Auto:
    def __init__(self, x = 0, y = 0, isDriving = 0):
        self.x = x
        self.y = y
        self.isDriving = isDriving



def main():
    print('hello # code')


if __name__ == '__main__':
    main()
