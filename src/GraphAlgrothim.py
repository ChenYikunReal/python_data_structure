from pythonds.graphs import PriorityQueue, Graph, Vertex
import sys


def dijkstra(aGraph, start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in aGraph])
    while not pq.isEmpty():
        currentVertex = pq.delMin()
        for nextVertex in currentVertex.getCollections():
            newDistance = currentVertex.getDistance() + currentVertex.getWeight(nextVertex)
        if newDistance < nextVertex.getDistance():
            nextVertex.setDistance(newDistance)
            nextVertex.setPred(currentVertex)
            pq.decreaseKey(nextVertex, newDistance)


def prim(graph, start):
    pq = PriorityQueue()
    for v in graph:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in graph])
    while not pq.isEmpty():
        currentVertex = pq.delMin()
        for nextVertex in currentVertex.getCollections():
            newCost = currentVertex.getWeight(nextVertex) + currentVertex.getDistance()
        if v in pq and newCost < nextVertex.getDistance():
            nextVertex.setPred(currentVertex)
            nextVertex.setDistance(newCost)
            pq.decreaseKey(nextVertex, newCost)
