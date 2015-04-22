package com.example.jessicamedintz.illinistudent;

import android.util.Log;

import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.json.JSONException;
import org.json.simple.JSONObject;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URISyntaxException;
import java.net.URL;

/**
 * Created by Jessica on 4/15/2015.
 */
public class ServerRequest {

    public static void sendJSON() {
        JSONObject jo = new JSONObject();
        jo.put("user", "test1");
        jo.put("email", "test1@illinois.edu");
        jo.put("pass", "illinirocks");
        jo.put("netid", "test1");
        jo.put("major", "Poly Sci");
        jo.put("grad", "2016-8-5");

        try {
        //URL url = new URL("http://illinistudent.cu.cc:5000");

        HttpClient httpClient = new DefaultHttpClient();
        HttpPost httpPost = new HttpPost("http://illinistudent.cu.cc:5000");

        // Prepare JSON to send by setting the entity
        httpPost.setEntity(new StringEntity(jo.toString(), "UTF-8"));

        // Set up the header types needed to properly transfer JSON
        httpPost.setHeader("Content-Type", "application/json");
        httpPost.setHeader("Accept-Encoding", "application/json");
        httpPost.setHeader("Accept-Language", "en-US");

        // Execute POST
        HttpResponse response = httpClient.execute(httpPost);

        } catch (UnsupportedEncodingException e) {
            Log.e("Server Application", "Error: " + e);
        } catch (ClientProtocolException e) {
            Log.e("Server Application", "Error: " + e);
        } catch (IOException e) {
            Log.e("Server Application", "Error: " + e);
        }
    }
}

