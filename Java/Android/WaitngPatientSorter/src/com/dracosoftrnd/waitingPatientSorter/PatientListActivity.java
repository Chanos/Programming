package com.dracosoftrnd.waitingPatientSorter;

import java.util.Collections;
import android.os.Bundle;
import android.app.ListActivity;
import android.content.Intent;
import android.view.ContextMenu;
import android.view.ContextMenu.ContextMenuInfo;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.ListView;

public class PatientListActivity extends ListActivity {

	@Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.patient_list);
        setAdapter();
    }

    @Override
    public void onResume(){
    	super.onResume();
         setAdapter();
    }
    
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.patient_list, menu);
        return true;
    }
    public boolean onOptionsItemSelected(MenuItem item)
    {
 
        switch (item.getItemId())
        {
        case R.id.add_patient:
            Intent addPatient = new Intent(getApplicationContext(), AddPatientActivity.class);
            startActivity(addPatient);
            return true;
        case R.id.load_testData:
        	PatientList.loadTestData();
            setAdapter();
            return true;
        case R.id.mainMenu:
        	Intent mainMenu = new Intent(getApplicationContext(), MainMenuActivity.class);
            startActivity(mainMenu);
            return true;
        }
		return false;
    }

    @Override
    public void onCreateContextMenu(ContextMenu menu, View v,
        ContextMenuInfo menuInfo) {
      if (v.getId()==android.R.id.list) {
        AdapterView.AdapterContextMenuInfo info = (AdapterView.AdapterContextMenuInfo)menuInfo;
        menu.setHeaderTitle("Options");
        menu.add(Menu.NONE, 1, 1, "Remove Patient");
        menu.add(Menu.NONE, 2, 2, "Patient Info");
      }
    }
    
    @Override
    public boolean onContextItemSelected(MenuItem item) {
      AdapterView.AdapterContextMenuInfo info = (AdapterView.AdapterContextMenuInfo)item.getMenuInfo();
      int menuItemIndex = item.getItemId();
      if(menuItemIndex == 1)
      {
    	  PatientList.GlobalPatients.remove(info.position);
    	  setAdapter();
      }
      if(menuItemIndex == 2)
      {
    	  Intent displayInfo = new Intent(getApplicationContext(), ItemInfoActivity.class);
    	  displayInfo.putExtra("arrayIndex", info.position);
          startActivity(displayInfo);
      }
        return true;
    }
    
	private void setAdapter() {
		ListView patientList = (ListView) findViewById(android.R.id.list);
		patientList.setOnItemClickListener(new OnItemClickListener() {
		    public void onItemClick(AdapterView<?> parent, View view,
		            int position, long id) { 
		    	Intent displayInfo = new Intent(getApplicationContext(), ItemInfoActivity.class);
		    	  displayInfo.putExtra("arrayIndex", position);
		          startActivity(displayInfo);
		    }});
        Collections.sort(PatientList.GlobalPatients);
        PatientAdapter adapter = new PatientAdapter(this,
        		  PatientList.GlobalPatients);
        
        patientList.setAdapter(adapter);
        registerForContextMenu(patientList);
	}
	
}
