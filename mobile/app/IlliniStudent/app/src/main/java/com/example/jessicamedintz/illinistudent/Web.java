package com.example.jessicamedintz.illinistudent;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebView;
import android.widget.Button;
import android.widget.RadioButton;

/**
 * Created by Jessica on 3/9/2015.
 */
public class Web extends Activity {

    Button b;
    //WebView myWeb;
    RadioButton r1,r2,r3,r4,r5,r6,r7,r8;
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

        //myWeb = (WebView) findViewById(R.id.webView);
        //myWeb.loadUrl("https://compass2g.illinois.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1");
        r1 = (RadioButton) findViewById(R.id.radioButton);
        r2 = (RadioButton) findViewById(R.id.radioButton2);
        r3 = (RadioButton) findViewById(R.id.radioButton3);
        r4 = (RadioButton) findViewById(R.id.radioButton4);
        r5 = (RadioButton) findViewById(R.id.radioButton5);
        r6 = (RadioButton) findViewById(R.id.radioButton6);
        r7 = (RadioButton) findViewById(R.id.radioButton7);
        r8 = (RadioButton) findViewById(R.id.radioButton8);

        r1.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                String url = "https://www.piazza.com";
                Intent i = new Intent(Intent.ACTION_VIEW);
                i.setData(Uri.parse(url));
                startActivity(i);

            }
        });

        r2.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                String url = "https://compass2g.illinois.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1";
                Intent i = new Intent(Intent.ACTION_VIEW);
                i.setData(Uri.parse(url));
                startActivity(i);

            }
        });

        r3.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                String url = "https://eas.admin.uillinois.edu/eas/servlet/EasLogin?redirect=https://webprod.admin.uillinois.edu/ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1";
                Intent i = new Intent(Intent.ACTION_VIEW);
                i.setData(Uri.parse(url));
                startActivity(i);

            }
        });

        r4.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                String url = "https://learn.illinois.edu";
                Intent i = new Intent(Intent.ACTION_VIEW);
                i.setData(Uri.parse(url));
                startActivity(i);

            }
        });

        r5.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                String url = "lon-capa.illinois.edu";
                Intent i = new Intent(Intent.ACTION_VIEW);
                i.setData(Uri.parse(url));
                startActivity(i);

            }
        });

        r6.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                String url = "https://www.webassign.net/uiuc/login.html";
                Intent i = new Intent(Intent.ACTION_VIEW);
                i.setData(Uri.parse(url));
                startActivity(i);

            }
        });

        r7.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                String url = "http://www.aleks.com";
                Intent i = new Intent(Intent.ACTION_VIEW);
                i.setData(Uri.parse(url));
                startActivity(i);

            }
        });

        r8.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                String url = "www.gmail.com";
                Intent i = new Intent(Intent.ACTION_VIEW);
                i.setData(Uri.parse(url));
                startActivity(i);

            }
        });

    }
}
