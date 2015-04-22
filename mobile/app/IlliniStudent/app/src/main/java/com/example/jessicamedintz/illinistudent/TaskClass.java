package com.example.jessicamedintz.illinistudent;

/**
 * Created by Jessica on 4/6/2015.
 */
public class TaskClass {
    private String taskName, taskDate, taskSubject, taskDescription;

    public TaskClass(String name, String date, String subject, String description){
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
