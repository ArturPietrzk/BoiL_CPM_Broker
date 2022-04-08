package com.company;

import java.util.HashSet;

public class Main {
    public static int maxCost;
    public static String format = "%1$-10s %2$-5s %3$-5s %4$-5s %5$-5s %6$-5s %7$-10s\n";

    public static void main(String[] args) {
        HashSet<Task> allTasks = new HashSet<Task>();
        Task end = new Task("End", 0);
        Task J = new Task("J", 2, end);
        Task I = new Task("I", 1, J);
        Task E = new Task("E", 1, I);
        Task D = new Task("D", 7, E);
        Task B = new Task("B", 4, D);
        Task F = new Task("F", 2, I);
        Task H = new Task("H", 4, I);
        Task G = new Task("G", 3, H);
        Task C = new Task("C", 6, G,F);
        Task A = new Task("A", 3, B, C);
        Task start = new Task("Start", 0, A);
        allTasks.add(end);
        allTasks.add(J);
        allTasks.add(I);
        allTasks.add(H);
        allTasks.add(G);
        allTasks.add(F);
        allTasks.add(E);
        allTasks.add(D);
        allTasks.add(C);
        allTasks.add(B);
        allTasks.add(A);
        allTasks.add(start);
        Task[] result = CriticalPath.criticalPath(allTasks);
        CriticalPath.print(result);
    }
}
