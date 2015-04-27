package com.example.jessicamedintz.illinistudent;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.text.Layout;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RelativeLayout;

/**
 * Created by Jessica on 3/9/2015.
 */
public class Settings extends Activity
{
    Button b;
    Button apply;
    RelativeLayout thisLayout;
    public static final int lav = Color.rgb(150, 123, 182);
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.settings);

        b = (Button) findViewById(R.id.button8);
        b.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(Settings.this,MainActivity.class);
                startActivity(i);

            }
        });
        apply = (Button) findViewById(R.id.button11);
        apply.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                thisLayout = (RelativeLayout) findViewById(R.id.settings);
                //EditText edit = (EditText) findViewById(R.id.editText11);
                //mycolor = edit.getText().toString();
                thisLayout.setBackgroundColor(lav);
            }
        });
    }
}
