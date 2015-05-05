package com.example.jessicamedintz.illinistudent;


import android.os.StrictMode;
import android.widget.Button;
import android.app.Activity;

import com.google.gson.Gson;

import org.apache.commons.io.IOUtils;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.JSONValue;
import org.json.simple.parser.ParseException;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.List;

/**
 * Created by Jessica on 4/7/2015.
 */
public class ServerTasks extends Activity {
    String name = whatIsUsername();
    static String result = "";

        // Buffer to readUrl. I think you can also use this to create users, since that also returns a json array
    private static String readUrl(String urlString) throws Exception {
        BufferedReader reader = null;
        try {
            URL url = new URL(urlString);
            reader = new BufferedReader(new InputStreamReader(url.openStream()));
            StringBuffer buffer = new StringBuffer();
            int read;
            char[] chars = new char[1024];
            while ((read = reader.read(chars)) != -1)
                buffer.append(chars, 0, read);

            return buffer.toString();
        } finally {
            if (reader != null)
                reader.close();
        }
    }

    // the static classes here are to be able to acces the individual elements in the json
    // Item acceses the user's tasks
    // jsonTime is an object made to be able to read the time (probably should have had better management there
    // Page is the class used to put them all together.


    static class Item {
        // I think these have to be in the order that the json array is presented.
        String due_date;
        String description;
        String tags;
        String class_name;
        String assign_name;
        String due_time;

    }

    static class jsonTime {
        String UPDATED;
    }

    static class Page {
                /* Example:
            String title;
            String link;
            String description;
            String language;
            List<Item> items;
            */

        // change admin to the actual user name/ <username>_schedule for their schedule.
        List<Item> admin;
        String authid;
        jsonTime TIME;

    }

    public String getTasksAlreadyCreated() {//pulls tasks that are already on the server
        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();//overrides the apps strict mode. Which will allow the app to access network
        StrictMode.setThreadPolicy(policy);//implements the change in the policy

        try {
            String json = readUrl("http://illinistudent.cu.cc:5000/jqtask?id=$6$rounds=105845$xdT9IytYZTn7nURD$N/XLRlXD6.QPVA6mu2cdbZTMudIHKHV1UbvKyPBhpQH1ZIix7IC1qyFa4KOZa4Xg8FOKUAelUZtNYK0F3ph.6/");

            Gson gson = new Gson();
            Page page = gson.fromJson(json, Page.class);

            for (Item tasks : page.admin) {
                result = result + tasks.assign_name + " " + tasks.due_date + tasks.class_name + ", ";
            }

            // Getting the time, which is a json Object
        } catch (com.google.gson.JsonSyntaxException e) {
            System.out.println("No tasks are loaded.");
        } catch (Exception e) {
            e.printStackTrace();
        }
        return result;
    }

    public String whatIsUsername()
    {
        String userName = "";

        Button login,signUp;
        Login l = new Login();

        login = (Button) findViewById(R.id.button9);
        signUp = (Button) findViewById(R.id.button6);

        if(login.isPressed() == true) userName = l.getUser();
        if(signUp.isPressed() == true) userName = NewUser.getUserName();
        return userName;
    }


}
