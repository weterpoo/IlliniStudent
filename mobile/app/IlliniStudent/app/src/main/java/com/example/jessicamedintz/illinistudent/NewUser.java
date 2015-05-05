package com.example.jessicamedintz.illinistudent;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.os.StrictMode;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.google.gson.Gson;

import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.List;

import static java.lang.System.out;

/**
 * Created by Jessica on 4/7/2015.
 */
public class NewUser extends Activity{
    Button reg;
    static String u;
    String p,em,n;

    EditText e1,e2,e3,e4;
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.new_user);

        reg = (Button) findViewById(R.id.button10);
        reg.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                try {
                    sendJSON();
                } catch (Exception e5) {
                    e5.printStackTrace();
                }

                Intent i = new Intent(NewUser.this, MainActivity.class);//once clicked will change to the main layout. Allows the pages to be changed
                startActivity(i);

            }
        });

        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();//overrides the apps strict mode. Which will allow the app to access network
        StrictMode.setThreadPolicy(policy);//implements the change in the policy
    }
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

    public void sendJSON() throws Exception
    {
        e1 = (EditText) findViewById(R.id.editText);//username
        e2 = (EditText) findViewById(R.id.editText6);//password
        e3 = (EditText) findViewById(R.id.editText7);//email
        e4 = (EditText) findViewById(R.id.editText10);//netid

         u = e1.getText().toString();
         p = e2.getText().toString();
         em = e3.getText().toString();
         n = e4.getText().toString();

        try {
            String json = readUrl("http://illinistudent.cu.cc:5000/" +
                    "jqcreatelogin?user=" + u.toString() + "&email=" + em.toString() + "&pass=" + p.toString() + "&netid=" + n.toString());

            Gson gson = new Gson();
            Page page = gson.fromJson(json, Page.class);

            HttpGet a = new HttpGet(json);

            HttpClient client = new DefaultHttpClient();
            client.execute(a);

        } catch (com.google.gson.JsonSyntaxException e) {
            out.println("User has been created.");
        }

    }

    public static String getUserName()
    {
        return u;
    }
}

