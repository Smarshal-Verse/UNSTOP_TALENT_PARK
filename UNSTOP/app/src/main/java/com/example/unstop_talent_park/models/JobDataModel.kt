package com.example.unstop_talent_park.models

data class JobDataModel(
    val name:String? = null,
    val uid:String? = null,
    val email:String? = null,
    val jobType:String? = null,
    val noOfDependents:String? = null,
    val education:String? = null,
    val sritscore:String?=null,
    val etCgpa:String? = null,
    val etField:String? = null,
    val etExperience:String? = null,
    val etpreviousctc:String? = null,
    val etcurrentctc:String? = null,
    val etskills:String? = null,
    val etworkinghours:String? = null,
    val etadditionalinfo:String? = null,
    val mlOutput:String? = null,
)
