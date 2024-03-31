package com.example.unstop_talent_park.models

data class UserModel(
    val uid : String? = "",
    val name:String? = "",
    val email:String? = "",
    val recruiter:String? = "",
    val links:Int? = 0,
    val partner:String? = ""
)
