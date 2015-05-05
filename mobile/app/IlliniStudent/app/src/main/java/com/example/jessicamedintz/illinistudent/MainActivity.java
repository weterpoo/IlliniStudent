package com.example.jessicamedintz.illinistudent;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.os.StrictMode;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.ImageButton;
import android.widget.TextView;
import java.text.SimpleDateFormat;


public class MainActivity extends Activity {
    TextView date;
    ImageButton tasksB;
    ImageButton calB;
    ImageButton webB;
    ImageButton professorsB;
    ImageButton schedB;
    ImageButton settingsB;
    ImageButton profile;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();

        StrictMode.setThreadPolicy(policy);

        date = (TextView) findViewById(R.id.dateView);

        long d = System.currentTimeMillis();

        SimpleDateFormat sdf = new SimpleDateFormat("EEE MMM dd, yyyy");
        String dateString = sdf.format(d);
        date.setText(dateString);//sets the current date onto the app

        tasksB = (ImageButton) findViewById(R.id.ImageButton1);
        tasksB.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(MainActivity.this,Tasks.class);//once clicked will change to the task layout.Allows the pages to be chnaged
                startActivity(i);

            }
        });

        calB = (ImageButton) findViewById(R.id.ImageButton2);
        calB.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(MainActivity.this,Cal.class);//once clicked will change to the cal layout.Allows the pages to be chnaged
                startActivity(i);

            }
        });

        webB = (ImageButton) findViewById(R.id.ImageButton4);
        webB.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(MainActivity.this,Web.class);//once clicked will change to the web layout.Allows the pages to be chnaged
                startActivity(i);

            }
        });

        professorsB = (ImageButton) findViewById(R.id.ImageButton5);
        professorsB.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(MainActivity.this,Professors.class);//once clicked will change to the professors layout.Allows the pages to be chnaged
                startActivity(i);

            }
        });

        schedB = (ImageButton) findViewById(R.id.ImageButton3);
        schedB.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(MainActivity.this,Schedule.class);//once clicked will change to the schedule layout.Allows the pages to be chnaged
                startActivity(i);

            }
        });

        settingsB = (ImageButton) findViewById(R.id.ImageButton6);
        settingsB.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(MainActivity.this,Settings.class);//once clicked will change to the settings layout.Allows the pages to be chnaged
                startActivity(i);

            }
        });

        profile = (ImageButton) findViewById(R.id.ImageButton7);
        profile.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(MainActivity.this,Profile.class);//once clicked will change to the profile layout.Allows the pages to be chnaged
                startActivity(i);

            }
        });
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
