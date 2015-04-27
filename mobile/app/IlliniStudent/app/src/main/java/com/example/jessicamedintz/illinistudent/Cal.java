package com.example.jessicamedintz.illinistudent;

import android.app.ActionBar;
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
//import android.support.v7.app.ActionBarActivity;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.CalendarView;
import android.widget.TabHost;

import java.util.Calendar;

import static android.app.ActionBar.NAVIGATION_MODE_TABS;

/**
 * Created by Jessica on 3/3/2015.
 */
public class Cal extends Activity {
    Button b5;
    CalendarView Cal_Week;
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.calendar);

        b5 = (Button) findViewById(R.id.button5);
        b5.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(Cal.this,MainActivity.class);
                startActivity(i);
            }
        });

        TabHost tabHost =(TabHost) findViewById(R.id.tabHost);

        tabHost.setup();

        TabHost.TabSpec tabSpec = tabHost.newTabSpec("Day");

        tabSpec.setContent(R.id.Day);
        tabSpec.setIndicator("Day");
        tabHost.addTab(tabSpec);

        TabHost.TabSpec tabSpecWeek = tabHost.newTabSpec("Week");

        tabSpecWeek.setContent(R.id.Week);
        tabSpecWeek.setIndicator("Week");
        tabHost.addTab(tabSpecWeek);

        TabHost.TabSpec tabSpecMonth = tabHost.newTabSpec("Month");

        tabSpecMonth.setContent(R.id.Month);
        tabSpecMonth.setIndicator("Month");
        tabHost.addTab(tabSpecMonth);

        Cal_Week=(CalendarView)findViewById(R.id.calendarView_Week);
        Cal_Week.setShownWeekCount(2);


    }


    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }
    }
