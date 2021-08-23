# Experiment-based Lab Validation: Domain-based Scalability Analysis

This directory holds all artifacts used for a domain-based scalability analysis using the results of CTT executions testing the ToDoList API demo application.

The goal is to compare two different configurations of the SUT with respect to scalability using operational profile data:
# The standard configuration from the RADON particles
# the standard configuration from the RADON particles but with enabled auto-scaling for the DynamoDB database.

Experiment setup: 
- The load test is implemented as a parameterized JMeter test plan that targets the five endpoints of the TODOListAPI, denoted as ToDo-Create, ToDo-Get-Single, ToDo-Get-All, ToDo-Update, and ToDo-Delete. The test plan implements a closed, session-based workload with n concurrent users iterating through a sequence of the aforementioned endpoints with some probabilistic branches. The JMeter test plan is integrated into the actual test definition in the TODOListAPI’s TOSCA model. The experiment duration is configured to be 840 seconds (14 minutes) with a 2-minute linear ramp up period.
- For both system configurations, we configure CTT to execute a series of tests for eleven different workload intensities (i.e., number of users), namely 1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 users. Hence, we obtain results for 22 different experiments. We removed the first 4 minutes and the last 2 minutes from the raw data of each experiment to eliminate warmup and cooldown effects.
- The results of the test with 1 user serves to obtain the baseline criteria for the pass/fail criteria of the scalability assessment. 
- After CTT has executed successfully, the test results are imported into the PPTAM tool. As the operational profile, we use Wikipedia traces according to the original publication on our approach (AFJ+20).

Artifact description:
* *01_CTT_Execution*: The CTT configuration files and a script to run the experiment for one test execution (either with or without scaling enabled).
* *02_CTT_Execution_Results*: The results returned by CTT for all tests of both test executions.
* *03_PPTAM_Import*: A tool to convert the JMeter logs to the format used by PPTAM, the converted results, as well as the (slightly customized) PPTAM toolchain.
* *04_PPTAM_Results*: The Jupyter Notebook applying the PPTAM approach containing all steps for the retrieval of the results presented in the *Deliverable 6.5: Final Assessment Report*.

References:
* AFJ+20: Alberto Avritzer, Vincenzo Ferme, Andrea Janes, Barbara Russo, André van Hoorn, Henning Schulz, Daniel Menasché, Vilc Queupe Rufino: Scalability Assessment of Microservice Architecture Deployment Configurations: A Domain-based Approach Leveraging Operational Profiles and Load Tests. J. Syst. Softw. 165: 110564 (2020).
