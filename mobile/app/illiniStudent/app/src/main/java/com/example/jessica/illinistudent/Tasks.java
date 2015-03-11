package com.example.jessica.illinistudent;

import android.app.Activity;
import android.content.Intent;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.view.Menu;
import android.app.ActionBar;
import android.view.View;
import android.widget.Button;
import android.widget.SpinnerAdapter;

/**
 * Created by Jessica on 3/3/2015.
 */
public class Tasks extends Activity {
   Button b3;
    Button b4;
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.tasks);

        b3 = (Button) findViewById(R.id.button3);
        b3.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(Tasks.this,Calendar.class);
                startActivity(i);

            }
        });

        b4 = (Button) findViewById(R.id.button4);
        b4.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(Tasks.this,MainActivity.class);
                startActivity(i);

            }
        });
    }


    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }
}
