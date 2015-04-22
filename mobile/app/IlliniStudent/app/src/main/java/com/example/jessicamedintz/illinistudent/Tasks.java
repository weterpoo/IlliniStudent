package com.example.jessicamedintz.illinistudent;

import android.app.Activity;
import android.content.Intent;
//import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TabHost;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;


/**
 * Created by Jessica on 3/3/2015.
 */
public class Tasks extends Activity {
    Button b4;
    EditText nameT, dateT, classT, desT;
    List<TaskClass> myTasks = new ArrayList<TaskClass>();
    ListView taskView;
    //String result;
    //ServerTasks st;
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.tasks);

        b4 = (Button) findViewById(R.id.button4);
        b4.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent i = new Intent(Tasks.this,MainActivity.class);
                startActivity(i);

            }
        });


        nameT = (EditText)findViewById(R.id.editText3);
        dateT = (EditText)findViewById(R.id.editText4);
        classT = (EditText)findViewById(R.id.editText5);
        desT = (EditText)findViewById(R.id.editText2);
        taskView = (ListView) findViewById(R.id.listView);
        final Button addBtn = (Button)findViewById(R.id.button);
        TabHost thost = (TabHost)findViewById(R.id.tabHost);

        thost.setup();

        TabHost.TabSpec tSpec = thost.newTabSpec("create");
        tSpec.setContent(R.id.tabCreate);
        tSpec.setIndicator("Add");
        thost.addTab(tSpec);

        tSpec = thost.newTabSpec("com.example.keith.taskmanager.Task List");
        tSpec.setContent(R.id.tabTasks);
        tSpec.setIndicator("Tasks");
        thost.addTab(tSpec);

        addTasks("Phys 211 Midterm Review","4/21/2015","Phys 211","can't fail this midterm");
        populate();

        /*result = st.getTasksAlreadyCreated();
        String a = result.substring(result.indexOf(","), (result.indexOf(",") + 1));
        result = result.substring(a.length() +1);
        String d = result.substring(result.indexOf(","), (result.indexOf(",") + 1));
        result = result.substring(d.length() +1);
        String c = result;

        addTasks(a.toString(),d.toString(),c.toString(),"need to pass");
        populate();*/

        addBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                addTasks(nameT.getText().toString(), dateT.getText().toString(), classT.getText().toString(), desT.getText().toString());
                populate();



                Toast.makeText(getApplicationContext(), "Task has been added!", Toast.LENGTH_SHORT).show();

            }
        });


        nameT.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                addBtn.setEnabled(!nameT.getText().toString().trim().isEmpty());
            }

            @Override
            public void afterTextChanged(Editable s) {

            }
        });

    }



    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    private void populate(){
        ArrayAdapter<TaskClass> adapter = new TaskListAdapter();
        taskView.setAdapter(adapter);


    }

    private void addTasks(String name, String date, String subject, String description){
        myTasks.add(new TaskClass(name, date, subject, description));




    }

    private class TaskListAdapter extends ArrayAdapter<TaskClass>{
        public TaskListAdapter(){

            super (Tasks.this, R.layout.listview_item, myTasks);
        }

        @Override
        public View getView(int position, View view, ViewGroup parent){
            if (view == null) {
                view = getLayoutInflater().inflate(R.layout.listview_item, parent, false);
            }
            TaskClass currentTask = myTasks.get(position);
            TextView name = (TextView)view.findViewById(R.id.taskName);
            name.setText(currentTask.getName());
            TextView date = (TextView)view.findViewById(R.id.taskDate);
            date.setText(currentTask.getDate());
            TextView subject = (TextView)view.findViewById(R.id.taskClass);
            subject.setText(currentTask.getTaskSubject());
            TextView des = (TextView)view.findViewById(R.id.taskDescription);
            des.setText(currentTask.getTaskDescription());


            return view;


        }


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
