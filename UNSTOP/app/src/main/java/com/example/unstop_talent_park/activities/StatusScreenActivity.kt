package com.example.unstop_talent_park.activities

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.appcompat.app.AlertDialog
import androidx.core.content.ContextCompat
import com.example.unstop_talent_park.R
import com.example.unstop_talent_park.databinding.ActivityStatusScreenBinding
import com.example.unstop_talent_park.models.JobDataModel
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.database.DataSnapshot
import com.google.firebase.database.DatabaseError
import com.google.firebase.database.FirebaseDatabase
import com.google.firebase.database.ValueEventListener

class StatusScreenActivity : AppCompatActivity() {

    private lateinit var binding: ActivityStatusScreenBinding
    private lateinit var uid: String
    private lateinit var status:String
    private lateinit var database: FirebaseDatabase
    private lateinit var dialog:AlertDialog

    val USERNAME = "u0yxvm2kkq"
    val PASSWORD = "t5OvSDtcASGoP6xRLBAfaYGZQ53XG4IpZHjorph3vtA"
    val BASE_URL =
        "https://u0lj156pi7-u0mlmn54wo-connect.us0-aws.kaleido.io/gateways/greylife/0xe18110e266f642686981ba41179709d241eb04cf/"
    val kldFromValue = "0xdbca2ba3f5843a82ad7c811174d001cb51cc329a"



    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityStatusScreenBinding.inflate(layoutInflater)
        setContentView(binding.root)

        enableBottomNavView()
        getStatusFromDatabase()



    }

    private fun enableBottomNavView(){
        val bottomNavigationView = binding.bottomNavigation
        bottomNavigationView.setSelectedItemId(R.id.statusScreen)
        bottomNavigationView.setOnNavigationItemSelectedListener { item ->
            when (item.itemId) {
                R.id.homeScreen -> {
                    startActivity(Intent(applicationContext, HomeScreenActivity::class.java))
                    finish()
                    overridePendingTransition(0, 0)
                    true
                }
                R.id.statusScreen -> true
                R.id.supportScreen -> {
                    startActivity(Intent(applicationContext, SupportScreenActivity::class.java))
                    finish()
                    overridePendingTransition(0, 0)
                    true
                }
                R.id.notificationsScreen -> {
                    startActivity(Intent(applicationContext, NotificationsScreenActivity::class.java))
                    finish()
                    overridePendingTransition(0, 0)
                    true
                }
                else -> false
            }
        }
    }

    private fun getStatusFromDatabase(){
        dialogBox("Fetching your job status","Please wait...")
        uid = FirebaseAuth.getInstance().uid!!
        database = FirebaseDatabase.getInstance()
        database.reference.child("jobs")
            .addValueEventListener(object : ValueEventListener {
                override fun onDataChange(snapshot: DataSnapshot) {
                    for(snapshot1 in snapshot.children){
                        val data = snapshot1.getValue(JobDataModel::class.java)
                        if(data!!.uid == uid){
                            status = data.mlOutput.toString()
                            binding.tvjobType.text = data!!.jobType
                            if(status == "Accepted"){
                                binding.tvStatus.text = "Accepted"
                                binding.tvStatus.setBackgroundColor(ContextCompat.getColor(this@StatusScreenActivity, R.color.myGreen))
                            }
                            else if(status == "Declined"){
                                binding.tvStatus.text = "Declined"
                                binding.tvStatus.setBackgroundColor(ContextCompat.getColor(this@StatusScreenActivity, R.color.myRed))
                            }
                            else{
                                binding.tvStatus.text = "Pending"
                                binding.tvStatus.setBackgroundColor(ContextCompat.getColor(this@StatusScreenActivity, R.color.myGrey))
                            }
                            dialog.dismiss()
                            break
                        }
                    }
                }
                override fun onCancelled(error: DatabaseError) {
                    dialog.dismiss()
                }
            })
        dialog.dismiss()
    }

    private fun dialogBox(title:String,message:String){
        val builder = AlertDialog.Builder(this)
        builder.setMessage(message)
        builder.setTitle(title)
        builder.setCancelable(false)
        dialog = builder.create()
        dialog.show()
    }

}