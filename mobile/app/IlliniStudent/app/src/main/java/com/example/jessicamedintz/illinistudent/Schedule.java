package com.example.jessicamedintz.illinistudent;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;


import android.widget.Button;

/**
 * Created by Jessica on 3/9/2015.
 */
public class Schedule extends Activity {
    Button b;
    public void onCreate(Bundle savedInstanceState) {
        try
        {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.sched);

            TextView myListView = (TextView)findViewById(R.id.netResult);

            try {
                HttpClient httpclient = new DefaultHttpClient();
                HttpPost httppost = new HttpPost("https://ui2web1.apps.uillinois.edu/BANPROD1/bwskfshd.P_CrseSchd");
                HttpResponse response = httpclient.execute(httppost);
                HttpEntity entity = response.getEntity();
                InputStream webs = entity.getContent();

                try {
                    BufferedReader reader = new BufferedReader(new InputStreamReader(webs, "iso-8859-1"), 8);
                    myListView.setText(reader.readLine());
                    webs.close();


                } catch (Exception e) {
                    Log.e("log_tag", "Error converting result " + e.toString());

                }
            }catch (Exception e){
                Log.e("log_tag", "error in http connection " + e.toString() );
            }
        }
        catch (Exception e) {
            Log.e("ERROR", "ERROR IN CODE: " + e.toString());
            e.printStackTrace();
        }

        b = (Button) findViewById(R.id.button2);
        b.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(Schedule.this,MainActivity.class);
                startActivity(i);

            }
        });
    }

}

