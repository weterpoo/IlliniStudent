package com.example.jessicamedintz.illinistudent;

import android.app.Activity;
import android.os.StrictMode;
import android.widget.EditText;

import com.google.gson.Gson;

import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.List;

import static java.lang.System.out;

/**
 * Created by jessicamedintz on 5/5/15.
 */
public class UploadTaks extends Activity
{
    EditText e1, e2, e3, e4;
    static String a,d,c,des;

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

    public void sendTasks() throws Exception
    {
        e1 = (EditText) findViewById(R.id.editText3);//assign_name
        e2 = (EditText) findViewById(R.id.editText5);//due_date
        e3 = (EditText) findViewById(R.id.editText4);//class_name
        e4 = (EditText) findViewById(R.id.editText2);//description

        a = e1.getText().toString();
        d = e2.getText().toString();
        c = e3.getText().toString();
        des = e4.getText().toString();

        try {
            String json = readUrl("http://illinistudent.cu.cc:5000/" +
                    "jqaddtask?assign_name=" + a.toString() + "&due_date=" + d.toString() + "&class_name=" + c.toString() + "&description=" + des.toString());

            Gson gson = new Gson();
            Page page = gson.fromJson(json, Page.class);

            HttpGet a = new HttpGet(json);

            HttpClient client = new DefaultHttpClient();
            client.execute(a);

        } catch (com.google.gson.JsonSyntaxException e) {
            out.println("Task has been created.");
        }

    }

}
