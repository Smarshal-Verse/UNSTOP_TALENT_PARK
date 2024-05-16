# Unstop: Enhancing User Experience through Advanced Technology Integration

## Overview

Unstop is an innovative platform aiming to revolutionize talent engagement and hiring through the integration of cutting-edge technologies such as Artificial Intelligence (AI), Machine Learning (ML), and Blockchain. By leveraging these advanced technologies, Unstop seeks to enhance user experience, improve efficiency, ensure data security, and scale seamlessly.

## Problem Statement

**Technical Problem Statement**: Enhancing User Experience through Advanced Technology Integration

In the highly competitive recruitment industry, user experience is a key differentiator. Unstop needs to leverage advanced technologies such as Artificial Intelligence (AI), Machine Learning (ML), and Data Analytics to enhance its platform and provide a superior user experience.

**Key Issues to Address**:
1. **Personalization**: Providing a personalized experience to each user based on their behavior and preferences.
2. **Efficiency**: Improving the platform's efficiency and responsiveness, including enhancing the job matching algorithm and automating routine tasks.
3. **Data Security**: Ensuring robust data security measures to protect user data.
4. **Scalability**: Scaling the platform to handle increased load without compromising performance or user experience.

This problem statement provides a comprehensive overview of the challenges faced by Unstop and sets the stage for a detailed analysis and solution proposal. It offers a great opportunity to delve deep into the workings of a fast-growing tech startup and come up with innovative solutions to real-world business problems.

## Proposed Solution

Unstop can become the go-to platform for early talent by leveraging AI, ML, and Blockchain for a supercharged user experience.  
So Here's my plan:
I propose to use a Hybrid recommendation system (HRS) which is a combination of Content-based filtering(CBRS) and collaborative filtering(CFRS) for best recommendations and personalized suggestions using an Ai chat bot to enhance the user experience. Automating the interview process for better efficiency and HRS will further optimize the job-matching algorithm. Finally, we will ensure that all user information is kept secure and confidential by storing it on a private blockchain network. This will provide an additional layer of security and peace of mind for our users.

#### Personalization - ML

- **Behavioral Analysis and HRS**: The system uses a combination of collaborative filtering (which makes recommendations based on similar users' behavior) and content-based filtering (which makes recommendations based on the content of the job postings and the user's preferences from browsing history and interactions etc).
- **AI Chat Bot**: AI-powered chatbot that can assist users in finding relevant jobs and answering their queries. The chatbot can also provide personalized recommendations based on user behavior and preferences.

#### Efficiency - ML and Blockchain

- **Improved Job Matching Algorithm (HRS)**: Enhancing the job matching algorithm using HRS to provide accurate matches based on user behavior, skills, preferences, job requirements, and company culture.
- **Automated Interview**: Automating routine tasks such as job postings and scheduling interviews. This will free up time for recruiters and hiring managers to focus on more strategic tasks.

#### Data Security - Blockchain

- **Decentralized Data Storage**: Utilizing a private blockchain network for secure and decentralized storage of user data, ensuring privacy and protection against unauthorized access.
- **Access Control | Zero-knowledge Proof | Consensus**: Implementing access control policies to restrict unauthorized access to sensitive data. Implementing a zero-knowledge proof system that can authenticate user data without revealing the underlying data. This can help ensure that user data is protected and prevent unauthorized access to sensitive data.

#### Scalability

- **Horizontal Scaling & Microservices Architecture**: Implementing horizontal scaling with a microservices architecture enables Unstop to distribute workload across servers efficiently. This approach offers flexibility, fault tolerance, and improved performance while allowing independent scaling and maintenance of individual services.

## Workflow

- **User Side Workflow**: Detailed workflow for users interacting with the platform.
![UNSTOP TALENT PARK-3](https://github.com/Smarshal21/UNSTOP_TALENT_PARK/assets/99678760/8410ab83-cadc-4a49-8459-81adbba54ef9)


- **Recruiter Side Workflow**: Detailed workflow for recruiters and hiring managers utilizing the platform.
![Blank diagram](https://github.com/Smarshal21/UNSTOP_TALENT_PARK/assets/99678760/91464afb-bcd8-498e-9b86-6349cbfdd3b4)


## USER END APPLICATION OVERVIEW

<img width="300" alt="Screenshot 1" src="https://github.com/Smarshal21/UNSTOP_TALENT_PARK/assets/99678760/69d1eecc-e705-40ee-a37e-83b625b810d9">
<img width="300" alt="Screenshot 2" src="https://github.com/Smarshal21/UNSTOP_TALENT_PARK/assets/99678760/b8acaa50-8d8a-4141-b538-9e8928c70586">
<img width="300" alt="Screenshot 3" src="https://github.com/Smarshal21/UNSTOP_TALENT_PARK/assets/99678760/19949ef5-f565-4cf1-b762-7ae32c429940">
<img width="300" alt="Screenshot 4" src="https://github.com/Smarshal21/UNSTOP_TALENT_PARK/assets/99678760/8503102d-862b-4240-832e-339efcde5fd4">
<img width="300" alt="Screenshot 5" src="https://github.com/Smarshal21/UNSTOP_TALENT_PARK/assets/99678760/a036b0d1-9d73-429a-a8c0-83f082448eb2">
<img width="300" alt="Screenshot 6" src="https://github.com/Smarshal21/UNSTOP_TALENT_PARK/assets/99678760/2c4adfaa-fdf7-40c4-bdf7-e9fd0a4553d6">
<img width="300" alt="Screenshot 7" src="https://github.com/Smarshal21/UNSTOP_TALENT_PARK/assets/99678760/ed71a3c3-9e67-4758-994a-e83e7bb4b721">


## RECRUITER END APPLICATION OVERVIEW
<img width="300" alt="Screenshot 1" src="https://github.com/Smarshal21/UNSTOP_TALENT_PARK/assets/99678760/ca29efe2-d696-4b4f-b94d-fd0942a0e695">
<img width="300" alt="Screenshot 2" src="https://github.com/Smarshal21/UNSTOP_TALENT_PARK/assets/99678760/5a3a8545-3cb5-43eb-ba75-cc325a17cd88">
<img width="300" alt="Screenshot 3" src="https://github.com/Smarshal21/UNSTOP_TALENT_PARK/assets/99678760/31238f3e-2cdc-49fa-a37d-5af8f348c72c">
<img width="300" alt="Screenshot 4" src="https://github.com/Smarshal21/UNSTOP_TALENT_PARK/assets/99678760/1972162f-23a5-4a82-890c-203896313225">


## ML Workflow:
### Overview
This project contains a Hybrid Recommendation Machine Learning Model which would be used to recommend jobs to the user according to their preferences. The models would be trained and then saved using pickle, then would be integrated into a Flask API. The Flask API will be deployed on Railway, enabling users to send data from their mobile devices and recommendations in real-time.

![Blank diagram-4](https://github.com/Smarshal21/UNSTOP_TALENT_PARK/assets/99678760/0f3c6fc3-0b0f-4be1-a4e5-ca176dc47ac3)


### Hybrid Recommendation System
A Hybrid recommendation system is a type of recommendation system that combines the benefits of both content-based and collaborative filtering. It uses the strengths of both approaches to provide more accurate and relevant recommendations to users.

![Blank diagram-2](https://github.com/Smarshal21/UNSTOP_TALENT_PARK/assets/99678760/75769c24-d956-4c73-a446-a280ec8840d4)


One way to implement a hybrid recommendation system is to use a deep learning approach, where the system learns to recommend items by analyzing the features of the items and the behavior of the users. This approach can be more accurate than content-based or collaborative filtering alone, as it can capture complex patterns and relationships in the data.

**There are two main types of recommender systems that are used in hybrid systems:**

**Content-based filtering**: This type of filtering recommends items that are similar to items that the user has liked in the past. For example, if a user has applied to a lot of software roles, a content-based recommender system might recommend other software roles to them. Content-based filtering uses information about the items themselves, such as their field, comapany, or roles.

Collaborative filtering: This type of filtering recommends items that other users with similar tastes have liked. For example, if users with comparable skills and experience have applied for or been successful **in certain positions, t**he system might recommend those jobs to the current user as well.

**By combining these approaches, a hybrid system can offer**:

Increased Accuracy: Matching a user's profile to relevant job descriptions provides a strong foundation. Additionally, factoring in what similar users find appealing adds another layer of relevant suggestions.

Considering Hidden Gems: A candidate passionate about a specific field but lacking a perfectly aligned experience might miss out on great opportunities in a purely collaborative system. Here, content-based filtering can recommend jobs that align with their skills and interests even if not a typical fit.

Addressing Company Needs:  Companies can leverage the system to target ideal candidates by considering skills and experience required for a specific role, while also factoring in the types of positions similar candidates have pursued in the past. This can unearth potential talent who might not have directly applied but possess the right skills and fit for the company culture.

Overall, a hybrid recommendation system in the job market aims to create a win-win situation for both candidates and employers by providing more relevant matches and fostering a more efficient job search process.


## Blockchain Workflow :

### Overview

This project focuses on the deployment of a Polygon Edge Chain on Amazon Web Services (AWS). The Polygon Edge Chain provides high-performance, low-latency infrastructure for blockchain applications. By successfully running a Polygon Edge Chain, this project aims to facilitate the development of efficient and scalable decentralized applications
### Consortium blockchain architecture
#### Node
Each node stores a copy of the blockchain and participates in the consensus process to validate transactions and add new blocks to the chain. There are two nodes running on polygon blockchain
#### Ledger
The ledger is the decentralized database that stores all of the transactions that occur on the blockchain
#### Smart Contracts
Smart contracts are self-executing contracts.These are used blockchain consortium architecture to automate the process of executing transactions on the blockchain. Smart Contract Management component simplifies Ethereum transaction submission and application development by providing clean RESTful interfaces for interaction with your smart contract methods.
##### Smart Contract WorkFlow
<img width="1030" alt="Screenshot 2023-11-17 at 5 08 15 PM" src="https://github.com/Smarshal21/GREY_LIFE_IT/assets/99678760/50640901-9417-4fec-b6fa-b85b505d0400">

#### Governance
Consortium blockchain governance is member-defined and adaptable, comprising rules and decision-making mechanisms tailored to specific use cases and goals.
Access to a private blockchain network is restricted to authorized parties only, and the network is not open to the public.
Private blockchains are preferred in enterprise use cases, such as supply chain management, to maintain greater network control.

#### Transaction Details
<img width="776" alt="Screenshot 2024-04-01 at 2 14 48 AM" src="https://github.com/Smarshal21/UNSTOP_TALENT_PARK/assets/99678760/8133f6c3-1c82-460b-a925-c9d5f4ba3e01">
<img width="776" alt="Screenshot 2024-04-01 at 2 14 48 AM" src="https://github.com/Smarshal21/UNSTOP_TALENT_PARK/assets/99678760/34135321-3cbb-43af-94b0-79954ce469c7">


## Conclusion

Unstop can become the go-to platform for early talent by leveraging AI, ML, and Blockchain for a supercharged user experience. By addressing key challenges in personalization, efficiency, data security, and scalability, Unstop is poised to make a significant impact in the recruitment industry.

---
**Author**: KSN Samanwith  
**Institution**: Indian Institute of Information Technology, Lucknow  
**Date**: April 1, 2024
