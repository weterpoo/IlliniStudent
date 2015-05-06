package com.example.jessicamedintz.illinistudent;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RelativeLayout;
import android.widget.TextView;

import org.w3c.dom.Text;

/**
 * Created by Jessica on 4/9/2015.
 */
public class Profile  extends Activity {
    Button b1;
    EditText e1, e2, e3, e4, e5, e6;
    TextView t1,t2,t3,t4,t5,t6;
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.profile);

        b1 = (Button) findViewById(R.id.button12);
        b1.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(Profile.this, MainActivity.class);
                startActivity(i);

            }
        });

        e1 = (EditText) findViewById(R.id.editText);//gets the new user username
        t1 = (TextView) findViewById(R.id.textView16);
        //t1.setText(e1.getText());//sets the text box for the username with what is passed in
        t1.setText("admin");

        /*e2 = (EditText) findViewById(R.id.editText9);//gets the new user grad year
        t2 = (TextView) findViewById(R.id.textView19);
        t2.setText(e2.getText());//sets the grad year

        e3 = (EditText) findViewById(R.id.editText8);//gets the new user netid
        t3 = (TextView) findViewById(R.id.textView22);
        t3.setText(e3.getText());//sets the netid

        e4 = (EditText) findViewById(R.id.editText7);//gets the new user email
        t4 = (TextView) findViewById(R.id.textView20);
        t4.setText(e4.getText());//sets the email

        e5 = (EditText) findViewById(R.id.editText10);//gets the new user major
        t5 = (TextView) findViewById(R.id.textView21);
        t5.setText(e5.getText());//sets the major*/

    }
}
