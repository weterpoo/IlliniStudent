package com.example.jessicamedintz.illinistudent;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.View;
import android.widget.Button;

/**
 * Created by Jessica on 3/29/2015.
 */
public class Login extends Activity {
    Button logBut;
    Button signUp;
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.login);

        logBut = (Button) findViewById(R.id.button9);
        logBut.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(Login.this, MainActivity.class);
                startActivity(i);
            }
        });

        signUp = (Button)findViewById(R.id.button6);
        signUp.setOnClickListener(new View.OnClickListener() {
                public void onClick(View v)
                {
                    Intent i = new Intent(Login.this, NewUser.class);
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

