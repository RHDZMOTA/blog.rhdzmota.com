---
# Course title, summary, and position.
linktitle: Applied machine-learning and big-data for credit scoring 
summary: Learn how to use big-data techniques and machine learning to create credit scoring models.
weight: 1

# Page metadata.
title: Overview
date: "2019-08-01T00:00:00Z"
lastmod: "2019-08-01T00:00:00Z"
draft: false  # Is this a draft? true/false
toc: true  # Show table of contents? true/false
type: docs  # Do not modify.

# Add menu entry to sidebar.
# - name: Declare this menu item as a parent with ID `name`.
# - weight: Position of link in menu.
menu:
  credit-scoring:
    name: Overview
    weight: 1
---

## _Applied Machine-Learning and Big-Data for Credit Scoring_

## About this course

This course aims to provide a comprehensive toolkit to create scalable credit-scoring systems. To achieve this goal, students must master state-of-the-art technologies in the field of data-engineering and machine learning. 

We embrace the open-source philosophy, and so this course contents and the software/datasets used are open to the public under a permissive license. 

## Requirements

Prospectus students must:

* Have their own hardware.
    * At least **4GB of RAM**. Recommended: 8GB or more.
    * Access to the internet.
* Have basic knowledge about the following topics.
    * Finance (e.g. interest rates, cash-flow analysis, profiling)
    * Mathematics (e.g. linear-algebra, calculus, probability & statistics)
    * Computer Science (e.g. programming languages, data structures, algorithms). 


## What you will learn

Successful completion of this course should enable students to: 

* Understand the financial theory behind credit scoring.
* Identify the relevance of behavioral data.
* Leverage different data-systems involved in the credit-scoring process. 
* Use the big-data techniques for data processing.
* Create credit-scoring models using machine learning. 

### Syllabus 

This course covers three main topics: 

1. Financial concepts & tools behind credit scoring (M1-M3).
2. Data processing and management in financial applications (M4-M8).
3. Predictive modeling (M9-M13). 

#### **Module 1**: Introduction and Context

This module provides fundamental concepts for understanding credit modeling.

* Relevant socio-economic factors for credit institutions. 
* Personal & behavioral information as predictors. 
* Conventional credit scoring.

---

#### **Module 2**: Interest rates and cash-flow analysis

In this module, we'll review the concepts regarding interest rates and cash flow analysis. 

* Net present value (NPV).
* Internal return rate (IRR).
* Monte Carlo simulations.

---

#### **Module 3**: Advanced Python programming

This module will teach students the principles behind the object-oriented paradigm, and some advanced programming techniques in python.

* Data structures & algorithms
* Iterators, generators, and decorators
* Data classes and the typing module
* Object-oriented programming

---

#### **Module 4**: Data systems and reporting tools

This module will explore the most common data systems used in finance. We will cover SQL and NO-SQL databases and explain the tradeoffs between both approaches. 

* The relational model and database normalization
* The structured query language (SQL)
* Object-relational mapping (ORM)
* NO-SQL databases (e.g., Cassandra, Elasticsearch)
* Elasticsearch query DSL

---

#### **Module 5**: Functional programming with Scala

Functional programming has become the basis for building big-data systems. Combined with a strongly-type language, the FP constructs guarantee reliability, type safety, and performance. In this module, students are introduced to the FP paradigm via the Scala programming language. 

* The java virtual machine (JVM).
* Introduction to Scala programming. 
* Dynamic polimorphism and algebraic data types. 
* Generics: invariance, covariance, contravariance.
* FP construct (e.g., fold, map, flatMap)
* Idiomatic scala (e.g. for-comprehension. pattern matching, type-classes)

---

#### **Module 6**: Batch processing with Apache Spark 

Apache Spark is one of the most popular frameworks for big-data processing and distributed machine learning. This module introduces the batch-oriented API.

* Monoids, semigroups, and functors.
* Spark Basics: architecture, map reduce.
* `Dataset[T]`: Typed API & operations.
* Understanding partitions & shuffling.
* Aggregations, joins, and SQL DSL.

---

#### **Module 7**: Data quality and record linkage

Data quality is a common problem in the financial industry. In this module, we will review the techniques for identifying, analyzing, and taking action on data quality assurance. 

---

#### **Module 8**: Entity Resolution with LSH

LSH is a highly scalable algorithm to solve the entity-resolution problem. This module introduces both the theory and implementation of LSH with an application on financial data. 

---

#### **Module 9**: GLMs

Generalized linear models are one of the most common predictive algorithms in the financial industry. We'll use this algorithm as a gateway to more complex machine-learning models. 

---

#### **Module 10**: Feature engineering & model performance

This module reviews the most common model performance metrics and feature engineering techniques. 

---

#### **Module 11**: Non-Linear models

Distributed non-linear machine learning using Apache Spark. 

---

#### **Module 12**: Hyperparameter optimization


This module enables students to leverage distributed computing to improve model predictions via hyperparameter optimization techniques.

---

#### **Module 13**: Operationalizing machine-learning models

In this module, students will be able to create a REST API for serving a machine-learning model. We'll define the essential metrics for monitoring both performance and usage. 

---

## Grading

The grading system is fairly simple: 

| Activity | #  | %  |
|----------|----|----|
| Homework | 14 | 40 |
| Exams    | 3  | 30 |
| Projects | 2  | 30 |

### Homework (40%)

Consider the following homework types:

* **Data Entry** 
    
    Student answering surveys or uploading a particular set of data points. Read the privacy notice for more information.
* **Exercise**

    Math or programming exercises to demonstrate technical proficiency. 
* **Report**

    Technical document containing detailed analysis on a subject. Technical proficiency, analysis, and communication skills are evaluated. 
* **Essay**

    Opinion-based writing with in-depth analysis and insight on a particular subject.
* **Code** 

    Functional application following the coding best practices. Includes documentation and testing. 

#### Delivery dates

|      | Title                                    | Type       | Deadline | Points |
|------|------------------------------------------|------------|----------|--------|
| [1]  | Sociodemographic Data                    | Data Entry | W01/S01  | 05     |
| [2]  | Simple Data Analysis                     | Report     | W01/S02  | 10     |
| [3]  | Social Stability and Inflation Rates     | Essay      | W02/S04  | 15     |
| [4]  | Personal Credit Score                    | Data Entry | W03/S05  | 05     |
| [5]  | The Role of Tech in Financial Innovation | Essay      | W03/S06  | 15     |
| [6]  | Expected Interest Rate                   | Code       | W04/S08  | 20     |
| [7]  | L.A. Traffic Collision Analysis          | Report     | W06/S12  | 10     |
| [8]  | Data Modeling with Scala                 | Exercise   | W07/S13  | 10     |
| [9]  | Functional Programming with Scala        | Exercise   | W07/S14  | 20     |
| [10] | Dataset Transformations                  | Exercise   | W08/S16  | 10     |
| [11] | Record Matching Application              | Code       | W10/S19  | 25     |
| [12] | The Big Data Revolution                  | Essay      | W11/S21  | 15     |
| [13] | Privacy in the Fintech Era               | Essay      | W12/S24  | 15     |
| [14] | GLMs with Apache Spark                   | Code       | W13/S26  | 25     |

Total points: **200**

[1]: https://rhdzmota.com/lectures/credit-scoring/hw1/
[2]: https://rhdzmota.com/lectures/credit-scoring/hw2/
[3]: https://rhdzmota.com/lectures/credit-scoring/hw3/
[4]: https://rhdzmota.com/lectures/credit-scoring/hw4/
[5]: https://rhdzmota.com/lectures/credit-scoring/hw5/
[6]: https://rhdzmota.com/lectures/credit-scoring/hw6/
[7]: https://rhdzmota.com/lectures/credit-scoring/hw7/
[8]: https://rhdzmota.com/lectures/credit-scoring/hw8/
[9]: https://rhdzmota.com/lectures/credit-scoring/hw9/
[10]: https://rhdzmota.com/lectures/credit-scoring/hw10/
[11]: https://rhdzmota.com/lectures/credit-scoring/hw11/
[12]: https://rhdzmota.com/lectures/credit-scoring/hw12/
[13]: https://rhdzmota.com/lectures/credit-scoring/hw13/
[14]: https://rhdzmota.com/lectures/credit-scoring/hw14/

### Projects (30%)

To be defined. 

### Exams (30%)

To be defined. 

## Attendance monitoring

Student attendance will not be enforced by the professor. To gain the "attendance point of the day" the student must complete and upload a typing test within the first 10 minutes of the class.

The typing test can be found [here](https://www.goodtyping.com/test.php). The student should then download the certificate using his/her student id and upload it in [this google drive](https://drive.google.com/drive/u/0/folders/126RzMLdpHikFKzYtQuBxIYLReIUjgYXV). 

Certificates will be [validated](https://www.goodtyping.com/certificates/) at the end of each week.  
