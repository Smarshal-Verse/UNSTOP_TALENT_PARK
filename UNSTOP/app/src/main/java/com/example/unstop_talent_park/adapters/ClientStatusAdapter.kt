package com.example.unstop_talent_park.adapters

import android.content.Context
import android.content.Intent
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.core.content.ContextCompat
import androidx.recyclerview.widget.RecyclerView
import com.example.unstop_talent_park.R
import com.example.unstop_talent_park.activities.ClientUpdateStatusActivity
import com.example.unstop_talent_park.databinding.ClientStatusUserItemLayoutBinding
import com.example.unstop_talent_park.models.JobDataModel

class ClientStatusAdapter(var context: Context, var list:ArrayList<JobDataModel>) : RecyclerView.Adapter<ClientStatusAdapter.StatusViewHolder>() {

    inner class StatusViewHolder(view: View) : RecyclerView.ViewHolder(view){
        var binding : ClientStatusUserItemLayoutBinding = ClientStatusUserItemLayoutBinding.bind(view)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): StatusViewHolder {
        return StatusViewHolder(
            LayoutInflater.from(parent.context)
                .inflate(R.layout.client_status_user_item_layout,parent,false))
    }

    override fun getItemCount(): Int {
        return list.size
    }

    override fun onBindViewHolder(holder: StatusViewHolder, position: Int) {
        val data = list[position]
        //set the profile
        //Glide.with(context).load(user.imageUrl).into(holder.binding.userImage)
        holder.binding.userName.text = data.name
        holder.binding.userId.text = data.uid
        holder.binding.userEmail.text = data.email
//        holder.binding.tvStatus.setBackgroundColor(ContextCompat.getColor(context, R.color.your_background_color))
        if(data.mlOutput == "Declined"){
            holder.binding.tvStatus.text = "Declined"
            holder.binding.tvStatus.setBackgroundColor(ContextCompat.getColor(context, R.color.myRed))
        }
        else if(data.mlOutput == "Accepted"){
            holder.binding.tvStatus.text = "Accepted"
            holder.binding.tvStatus.setBackgroundColor(ContextCompat.getColor(context, R.color.myGreen))
        }
        else{
            holder.binding.tvStatus.text = "Pending"
            holder.binding.tvStatus.setBackgroundColor(ContextCompat.getColor(context, R.color.myGrey))
        }

        //on click
        holder.itemView.setOnClickListener {
            val intent = Intent(context, ClientUpdateStatusActivity::class.java)
            intent.putExtra("uid",data.uid)
            context.startActivity(intent)
        }

    }
}