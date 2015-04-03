package com.example.keith.taskmanager;

import android.support.v7.app.ActionBarActivity;
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


public class MainActivity extends ActionBarActivity {

    EditText nameT, dateT, classT, desT;
    List<Task> myTasks = new ArrayList<Task>();
    ListView taskView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

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
        ArrayAdapter<Task> adapter = new TaskListAdapter();
        taskView.setAdapter(adapter);


    }

    private void addTasks(String name, String date, String subject, String description){
        myTasks.add(new Task(name, date, subject, description));


    }

    private class TaskListAdapter extends ArrayAdapter<Task>{
        public TaskListAdapter(){

            super (MainActivity.this, R.layout.listview_item, myTasks);
        }

        @Override
        public View getView(int position, View view, ViewGroup parent){
            if (view == null) {
                view = getLayoutInflater().inflate(R.layout.listview_item, parent, false);
            }
            Task currentTask = myTasks.get(position);
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
