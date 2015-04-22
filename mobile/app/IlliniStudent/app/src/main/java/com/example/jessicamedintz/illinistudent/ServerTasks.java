package com.example.jessicamedintz.illinistudent;

import org.apache.commons.io.IOUtils;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.JSONValue;
import org.json.simple.parser.ParseException;

import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
/**
 * Created by Jessica on 4/7/2015.
 */
public class ServerTasks {
   String dueDate,assignName,className,result;

    public String getTasksAlreadyCreated() {


        String url = "http://illinistudent.cu.cc:5000/jqtask?id=$6$rounds=103672$g/IoI7nLFLxI0u4W$lYnTZeAwZLQOHTkAS.vqG9EfjEVbg21Nlwwc1I4fLOuH6G3ioza931EH9VhcH7P6DdIMYv3Kn81S11W.gNCkg.";

        try{
            String taskURL = IOUtils.toString(new URL(url));
            JSONObject obj= (JSONObject) JSONValue.parseWithException(taskURL);

            JSONArray array = (JSONArray) obj.get("IlliniTester");

            for(int i = 1; i < array.size(); i ++)
            {
                JSONObject task = (JSONObject) array.get(i);
                dueDate = task.get("due_date").toString();
                assignName = task.get("assign_name").toString();
                className = task.get("class_name").toString();
                System.out.println(assignName + dueDate + className);

            }
            result = assignName + "," + dueDate + "," + className;


        } catch (IOException | ParseException e) {
            e.printStackTrace();
        }

        return result;
    }


}
