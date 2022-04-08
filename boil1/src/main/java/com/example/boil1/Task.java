package com.example.boil1;

import java.util.ArrayList;
import java.util.HashSet;

import static com.example.boil1.Main.maxCost;

public class Task {
    private int cost;
    private int criticalCost;
    private String name;
    private int earlyStart;
    private int earlyFinish;
    private int latestStart;
    private int latestFinish;
    private HashSet<Task> dependencies = new HashSet<>();
    private ArrayList<String> dep_names = new ArrayList<>();

    public Task(String name, int cost, Task... dependencies) {
        this.name = name;
        this.cost = cost;
        for (Task task : dependencies) {
            this.dependencies.add(task);
        }
        this.earlyFinish = -1;
        setDep_names();
    }

    public void setLatest() {
        latestStart = maxCost - criticalCost;
        latestFinish = latestStart + cost;
    }

    public String[] toStringArray() {
        String criticalCond = earlyStart == latestStart ? "Yes" : "No";
        String[] toString = {name, earlyStart + "", earlyFinish + "", latestStart + "", latestFinish +"", latestStart - earlyStart + "", criticalCond};
        return toString;
    }

    public boolean isDependent(Task task) {
        if (dependencies.contains(task)) {
            return true;
        }

        for (Task dep : dependencies) {
            if (dep.isDependent(task)) {
                return true;
            }
        }
        return false;
    }

    public HashSet<Task> getDependencies() {
        return dependencies;
    }

    public int getCriticalCost() {
        return criticalCost;
    }

    public int getCost() {
        return cost;
    }

    public String getName() {
        return name;
    }

    public int getEarlyFinish() {
        return earlyFinish;
    }

    public int getEarlyStart() {
        return earlyStart;
    }

    public void setCriticalCost(int newCriticalCost) {
        criticalCost = newCriticalCost;
    }

    public void setEarlyStart(int newEarlyStart) {
        earlyStart = newEarlyStart;
    }

    public void setEarlyFinish(int newEarlyFinish) {
        earlyFinish = newEarlyFinish;
    }


    public void setDep_names(){
        for(Task t : dependencies){
            dep_names.add(t.name);
        }
    }

    public ArrayList<String> getDep_names(){
        return dep_names;

    }
}
