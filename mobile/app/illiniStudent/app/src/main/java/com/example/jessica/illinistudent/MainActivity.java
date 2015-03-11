package com.example.jessica.illinistudent;

import android.app.ActionBar;
import android.content.Intent;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.ImageButton;
import android.widget.TextView;
import java.text.SimpleDateFormat;


public class MainActivity extends ActionBarActivity {
    TextView date;
    ImageButton tasksB;
    ImageButton calB;
    ImageButton webB;
    ImageButton professorsB;
    ImageButton schedB;
    ImageButton settingsB;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        date = (TextView) findViewById(R.id.dateView);

        long d = System.currentTimeMillis();

        SimpleDateFormat sdf = new SimpleDateFormat("EEE MMM dd, yyyy");
        String dateString = sdf.format(d);
        date.setText(dateString);

        tasksB = (ImageButton) findViewById(R.id.ImageButton1);
        tasksB.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(MainActivity.this,Tasks.class);
                startActivity(i);

            }
        });

        calB = (ImageButton) findViewById(R.id.ImageButton2);
        calB.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(MainActivity.this,Calendar.class);
                startActivity(i);

            }
        });

        webB = (ImageButton) findViewById(R.id.ImageButton4);
        webB.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(MainActivity.this,Web.class);
                startActivity(i);

            }
        });

        professorsB = (ImageButton) findViewById(R.id.ImageButton5);
        professorsB.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(MainActivity.this,Professors.class);
                startActivity(i);

            }
        });

        schedB = (ImageButton) findViewById(R.id.ImageButton3);
        schedB.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(MainActivity.this,Schedule.class);
                startActivity(i);

            }
        });

        settingsB = (ImageButton) findViewById(R.id.ImageButton6);
        settingsB.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(MainActivity.this,Settings.class);
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
