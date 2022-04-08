package com.company;

import java.util.*;

import static com.company.Main.maxCost;
import static com.company.Main.format;

public class CriticalPath {
    public static Task[] criticalPath(Set<Task> tasks) {
        // tasks whose critical cost has been calculated
        HashSet<Task> completed = new HashSet<Task>();
        // tasks whose critical cost needs to be calculated
        HashSet<Task> remaining = new HashSet<Task>(tasks);

        // Backflow algorithm
        // while there are tasks whose critical cost isn't calculated.
        while (!remaining.isEmpty()) {
            boolean progress = false;

            // find a new task to calculate
            for (Iterator<Task> it = remaining.iterator(); it.hasNext();) {
                Task task = it.next();
                if (completed.containsAll(task.getDependencies())) {
                    // all dependencies calculated, critical cost is max
                    // dependency
                    // critical cost, plus our cost
                    int critical = 0;
                    for (Task t : task.getDependencies()) {
                        if (t.getCriticalCost() > critical) {
                            critical = t.getCriticalCost();
                        }
                    }
                    task.setCriticalCost(critical + task.getCost());
                    // set task as calculated an remove
                    completed.add(task);
                    it.remove();
                    // note we are making progress
                    progress = true;
                }
            }
            // If we haven't made any progress then a cycle must exist in
            // the graph and we wont be able to calculate the critical path
            if (!progress)
                throw new RuntimeException("Cyclic dependency, algorithm stopped!");
        }

        // get the cost
        maxCost(tasks);
        HashSet<Task> initialNodes = initials(tasks);
        calculateEarly(initialNodes);

        // get the tasks
        Task[] ret = completed.toArray(new Task[0]);
        // create a priority list
        Arrays.sort(ret, new Comparator<Task>() {

            @Override
            public int compare(Task o1, Task o2) {
                return o1.getName().compareTo(o2.getName());
            }
        });

        return ret;
    }

    public static void calculateEarly(HashSet<Task> initials) {
        for (Task initial : initials) {
            initial.setEarlyStart(0);
            initial.setEarlyFinish(initial.getCost());
            setEarly(initial);
        }
    }

    public static void setEarly(Task initial) {
        int completionTime = initial.getEarlyFinish();
        for (Task t : initial.getDependencies()) {
            if (completionTime >= t.getEarlyStart()) {
                t.setEarlyStart(completionTime);
                t.setEarlyFinish(completionTime + t.getCost());
            }
            setEarly(t);
        }
    }

    public static HashSet<Task> initials(Set<Task> tasks) {
        HashSet<Task> remaining = new HashSet<Task>(tasks);
        for (Task t : tasks) {
            for (Task td : t.getDependencies()) {
                remaining.remove(td);
            }
        }

        System.out.print("Initial nodes: ");
        for (Task t : remaining)
            System.out.print(t.getName() + " ");
        System.out.print("\n\n");
        return remaining;
    }

    public static void maxCost(Set<Task> tasks) {
        int max = -1;
        for (Task t : tasks) {
            if (t.getCriticalCost() > max)
                max = t.getCriticalCost();
        }
        maxCost = max;
        System.out.println("Critical path length (cost): " + maxCost);
        for (Task t : tasks) {
            t.setLatest();
        }
    }

    public static void print(Task[] tasks) {
        System.out.format(format, "Task", "ES", "EF", "LS", "LF", "Slack", "Critical");
        for (Task t : tasks)
            System.out.format(format, (Object[]) t.toStringArray());
    }
}
