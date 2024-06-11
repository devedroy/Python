package org.example.graph;


import java.util.ArrayList;

/**
 * Implementation of a graph using adjacency list
 * <p>
 * 0 -> 1,2
 * <p>
 * 1 -> 0,2,3
 * <p>
 * 2 -> 0,1
 * <p>
 * 3 -> 1
 */
public class AdjacencyList {

    private static void addEdge(ArrayList<ArrayList<Integer>> adj, int u, int v) {
        adj.get(u).add(v);
        adj.get(v).add(u);
    }

    private static void printGraph(ArrayList<ArrayList<Integer>> adj) {
        for (int i = 0; i < adj.size(); i++) {
            System.out.print(i + " -> ");
            for (int j : adj.get(i)) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int v = 4;
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>(v);
        for (int i = 0; i < v; i++) {
            adj.add(new ArrayList<>());
        }

        addEdge(adj, 0, 1);
        addEdge(adj, 0, 2);
        addEdge(adj, 1, 0);
        addEdge(adj, 1, 2);
        addEdge(adj, 1, 3);
        addEdge(adj, 2, 0);
        addEdge(adj, 2, 1);
        addEdge(adj, 3, 1);

        printGraph(adj);
    }

}
