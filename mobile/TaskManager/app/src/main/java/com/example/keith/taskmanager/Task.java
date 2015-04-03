package com.example.keith.taskmanager;

/**
 * Created by Keith on 4/2/2015.
 */
public class Task {

    private String taskName, taskDate, taskSubject, taskDescription;

    public Task(String name, String date, String subject, String description){
        taskName = name;
        taskDate = date;
        taskSubject = subject;
        taskDescription = description;
    }

    public String getName(){

        return taskName;
    }

    public String getDate(){

        return taskDate;
    }

    public String getTaskSubject(){

        return taskSubject;
    }

    public String getTaskDescription(){

        return taskDescription;
    }
}
