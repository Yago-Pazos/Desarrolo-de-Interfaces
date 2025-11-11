package com.example.mycatalog;

import android.os.Bundle;
import android.util.Log;

import androidx.appcompat.app.AppCompatActivity;

import com.google.android.material.bottomnavigation.BottomNavigationView;

import androidx.navigation.NavController;
import androidx.navigation.fragment.NavHostFragment;
import androidx.navigation.ui.NavigationUI;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        NavHostFragment navHostFragment = (NavHostFragment) getSupportFragmentManager().findFragmentById(R.id.nav_host_fragment);
        if (navHostFragment == null) {
            Log.e(TAG, "NavHostFragment not found (id: nav_host_fragment). Check activity_main.xml");
            return;
        }

        NavController navController = navHostFragment.getNavController();

        BottomNavigationView bottomNav = findViewById(R.id.bottom_nav);
        if (bottomNav == null) {
            Log.e(TAG, "BottomNavigationView not found (id: bottom_nav). Check activity_main.xml");
            return;
        }

        NavigationUI.setupWithNavController(bottomNav, navController);
    }
}