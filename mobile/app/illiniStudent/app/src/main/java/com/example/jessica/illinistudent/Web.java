package com.example.jessica.illinistudent;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

/**
 * Created by Jessica on 3/9/2015.
 */
public class Web extends Activity {

    Button b;
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.web);

        b = (Button) findViewById(R.id.button7);
        b.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(Web.this,MainActivity.class);
                startActivity(i);

            }
        });
    }
}
