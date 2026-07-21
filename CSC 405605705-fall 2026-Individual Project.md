---
title: Individual Project
nav_order: 4
last_modified_date: true
---

# Individual Data Science Project

### 1. Project Overview

There is no final exam in this course. Instead, each student will complete an **individual** AI-assisted data science project that demonstrates the complete data science workflow using the concepts and techniques learned throughout the semester. Students are expected to independently design, implement, and present a complete data analysis project using Streamlit as an interactive reporting platform.

**Each project should include the following stages:**

- Data acquisition
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Statistical analysis
- Machine learning modeling
- Model evaluation
- Data visualization
- AI-assisted interpretation and discussion
- Final interactive report

**Each student is responsible for:**

- Selecting one real-world dataset from a publicly available repository (e.g., Kaggle, UCI Machine Learning Repository, Data.gov, etc.).
- Defining at least one data-driven research question or business problem.
- Choosing appropriate analytical methods and machine learning models.
- Submit a project proposal during the semester.
- Developing a Streamlit application that presents the complete analysis.
- Maintaining an individual GitHub repository containing all source code.
- Submitting a PDF version of the final Streamlit report together with the GitHub repository link.

### 2. Important Project Dates

| Date        | Milestone                                        |
| ----------- | ------------------------------------------------ |
| October 30  | Project Proposal Due                             |
| November 9  | Instructor Feedback on Project Proposal Returned |
| November 30 | Final Project Report Submission Due              |
| November 30 | Student Project Presentations (Session I)        |
| December 2  | Student Project Presentations (Session II)       |

### 3.Project Grading Policy

| Task                 | 100 points total (worth 50% for undergraduate and 40% for graduate in final scores) |
| -------------------- | ------------------------------------------------------------ |
| Project Proposal     | 20 points                                                    |
| GitHub repository    | 30 points (Source code 20 points, Version control 10 points) |
| Final Project Report | 50 points                                                    |
| Presentation         | Bonus 0~10 points                                            |

**Project Presentation (Bonus Opportunity)**

During the final two class meetings (Nov 30 & Dec 2), 10 students will present their projects (about 5 presentations per class, 15–20 minutes each).

Presentation opportunities are intended as a bonus rather than a course requirement.

- Students may volunteer to present.
- If more than 10 students volunteer, presenters will be selected by random drawing.
- If fewer than 10 students volunteer, the remaining presentation slots will be filled by randomly selecting additional students from the class.
- Students who present may earn up to 10 bonus points, based on the quality of the presentation.

Please note that presentation participation does not affect the evaluation of the project itself. All projects will be graded using the same rubric. Presentations are offered as a bonus opportunity for students to share their project outcomes with the class and receive constructive feedback from both the instructor and their peers.

### 4. Detailed Project Grading Rubric

**(1) Project Proposal (20 Points)**

The project proposal is intended to help students receive early feedback and guidance before beginning the full project. The proposal should demonstrate that the project is feasible, well planned, and aligned with the course objectives.

Students should download and complete the [**Project Proposal Template**](Data Science Project Proposal_template.docx) provided and submit it by the posted deadline.

There is no page requirement; however, the proposal should address all sections of the template with sufficient detail.

**(2) Reproducible AI-Assisted Workflow (30 points)**

Your project must be fully reproducible.

**Required:**

- An individual GitHub repository (must be publicly accessible during grading)
- A clear project structure, for example:

```
data/          # dataset
src/app.py     # source code
figures/       # generated figures
report/        # exported PDF report
```

The README must include: Project title, Dataset source (URL), Project objective, Instructions for running the code

Version control (GitHub commit history) will be considered as part of the evaluation.

**(3) Streamlit Report Components (30 points)** 

The report must presents the complete data science workflow.

**Required:**

- **Dataset overview**

- **Exploratory analysis**

  You **must** demonstrate:

  - Identification and handling of missing values
  - Detection of outliers or anomalies
  - Use of:
    - Group-by / aggregation
    - Descriptive statistics

  Simply dropping data without justification is not acceptable.

- **Statistical Analysis & Hypothesis Testing**

  You must perform at least one formal statistical analysis (e.g., t-test, ANOVA, Chi-square test, correlation analysis)

  For each test: State the null hypothesis; Explain why the test is appropriate; report test statistic and p-value; interpret the result in context.

- **Machine learning results**

  You must implement:

  - One baseline machine learning model (e.g., Logistic Regression, Decision Tree, Linear Regression)
  - One more advanced model (e.g., Random Forest, XGBoost, LightGBM, Neural Networks)

- **Visualizations**

  You must present multiple informative figures:

  - Appropriate chart selection
  - Clear labels and captions
  - Interpretation of every figure

  Visualizations should support the project's conclusions rather than simply displaying data.

- **Final conclusions**

**(4) AI-Assisted Analysis (20 points)**

Students must demonstrate the effective use of an AI assistant to support the data analysis process.

**Required:**

- The Streamlit application must integrate an LLM through LangChain/LangGraph and an LLM API (e.g., OpenAI/Gemini API). **Using web-based AI tools (e.g., ChatGPT's web interface) does not satisfy this requirement.**
- Students should design effective prompts to obtain meaningful insights and assistance from the AI assistant.
- For each major data preparation or analysis decision, students should:
  - formulate an effective prompt,
  - critically evaluate the AI-generated response,
  - explain whether the recommendation was accepted, modified, or rejected, and justify the decision.
- AI may be used to assist with tasks such as code generation, visualization, statistical interpretation, and result explanation, but **all AI interactions must be performed through the integrated LangChain + API workflow**.
- Representative examples of AI interactions should be documented in the final report to demonstrate how AI contributed to the project's development.

Simply accepting AI-generated suggestions without critical evaluation or explanation will receive limited credit.

### Appendix

The datasets listed below were used by students in the last semester. You may use them as references when selecting a topic, but you must choose a different dataset for your own project. This policy promotes fairness and ensures that each student develops an original analysis rather than relying on materials or solutions from previous classes.

- Fast Food Consumption & Health Impact Dataset

  https://www.kaggle.com/datasets/prince7489/fast-food-consumption-and-health-impact-dataset

- Career Path Recommendations Dataset

  https://www.kaggle.com/datasets/ahsanneural/career-path-recommendations-dataset?resource=download

- Breast Cancer Dataset

  https://www.kaggle.com/datasets/neurocipher/breast-cancer-dataset

- EuroMillions Historical Data

  https://www.kaggle.com/datasets/duartepereiradacruz/euromillions-historical-data

- Delivery Logistics Dataset

  https://www.kaggle.com/datasets/muhammadahmaddaar/delivery-logistics-dataset-india-multi-partner

- Synthetic Diabetes Prediction Dataset

  https://www.kaggle.com/datasets/miadul/synthetic-diabetes-prediction-dataset

- Student Placement Dataset

  https://www.kaggle.com/datasets/sonalshinde123/student-placement-dataset

- Hospital Readmission Risk dataset

  https://www.kaggle.com/datasets/miadul/hospital-readmission-risk-dataset

- Dirty Iranian Transactions Dataset

  https://www.kaggle.com/datasets/hosseinbadrnezhad/dirty-iranian-transactions-dataset

- Customer Churn Dataset

  https://www.kaggle.com/datasets/sonalshinde123/customer-churn-prediction-dataset

- Crop Yield Prediction

  https://www.kaggle.com/datasets/miadul/smart-crop-recommendation-dataset

- COVID-19 Patient Symptoms & Diagnosis Dataset

  https://www.kaggle.com/datasets/miadul/covid-19-patient-symptoms-and-diagnosis-dataset

- Fertilizer Recommendation Dataset

  https://www.kaggle.com/datasets/miadul/fertilizer-recommendation-dataset

- Synthetic Credit Risk Dataset 

  https://www.kaggle.com/datasets/emirhanakku/synthetic-credit-risk-dataset-extreme-imbalance
