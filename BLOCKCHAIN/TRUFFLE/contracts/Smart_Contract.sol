// SPDX-License-Identifier: MIT

pragma solidity ^0.8.19;

contract ApplicantDataContract {
    struct Applicant {
        uint256 id;
        string name;
        string jobDescription;
        uint256 result;
        uint256 cgpa; 
    }

    Applicant[] public applicants;
    uint256 public nextApplicantId;

    function addApplicant(
        string memory _name,
        string memory _jobDescription,
        uint256 _result,
        uint256 _cgpa
    ) public {
        applicants.push(Applicant(nextApplicantId, _name, _jobDescription, _result, _cgpa));
        nextApplicantId++;
    }

    function getApplicantsCount() public view returns (uint256) {
        return applicants.length;
    }

    function getApplicantById(uint256 _id) public view returns (Applicant memory) {
        require(_id < applicants.length, "Applicant ID does not exist");
        return applicants[_id];
    }

    function updateApplicant(
        uint256 _id,
        string memory _name,
        string memory _jobDescription,
        uint256 _result,
        uint256 _cgpa
    ) public {
        require(_id < applicants.length, "Applicant ID does not exist");
        applicants[_id].name = _name;
        applicants[_id].jobDescription = _jobDescription;
        applicants[_id].result = _result;
        applicants[_id].cgpa = _cgpa;
    }

    function deleteApplicant(uint256 _id) public {
        require(_id < applicants.length, "Applicant ID does not exist");
        applicants[_id] = applicants[applicants.length - 1];
        applicants.pop();
    }
}

contract StringArrayContract {
    string[] public stringArray;

    function setStringArray(string[] memory _array) public {
        stringArray = _array;
    }

    function getStringArray() public view returns (string[] memory) {
        return stringArray;
    }
}