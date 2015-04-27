package com.example.jessicamedintz.illinistudent;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

/**
 * Created by Jessica on 4/7/2015.
 */
public class NewUser extends Activity{
    Button reg;
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.new_user);

        reg = (Button) findViewById(R.id.button10);
        reg.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(NewUser.this, MainActivity.class);
                startActivity(i);
            }
        });

    }


}
