# Olist E-commerce Causal Analysis

## Project Overview
This project investigates the causal effect of delayed delivery on customer satisfaction ratings in e-commerce, using data provided by Olist, the largest department store in Brazilian marketplaces.



## Research Question
Our two research questions are:

1. **What is the causal effect of delayed delivery on customer ratings?**

2. **What is the causal effect of delayed delivery on revenue?**

## Methodology

Our analysis employed two complementary causal inference approaches:

![Causal DAG](results/figures/pictures/dag.jpg)

### 1. Propensity Score Matching
Based on the DAG insights, we implemented matching to estimate the causal effect:

- **Approach**: Paired late deliveries with similar on-time deliveries, effectively estimating the *average treatment effect on the treated*

- **Matching Variables**:
   - Distance (km)
   - Season
   - Product category
   - Freight value
   - Product size

- **Balance**: Achieved comparable covariate distributions between groups

- **Estimand**: Average Treatment Effect on the Treated (ATT)

- **Results**: -1.8 stars. On Average a late delivery causes customer ratings to drop by 1.8 stars.

- **Notebook**: 📊 [Propensity Score Matching](notebooks/model-development.ipynb)

### 1. Graphical Causal Modeling

We first modeled the data generating process using:

- **Directed Acyclic Graph (DAG)**: Visualized the causal relationships between variables

- **Key Variables**:
   - Distance (km)
   - Season
   - Product category
   - Freight value
   - Product size

- **Notebook**: 📊 [Graphical Causal Model](notebooks/gcm-development.ipynb)





### Causal Identification Strategy

Our formal estimand is:
```latex
E[Rating|do(is_delivery_late)] = ∫ E[Rating|is_delivery_late, X] P(X) dX


## Directed Acyclic Graph

![Causal DAG](results/figures/pictures/dag.jpg)


## Causal Estimand Identification

### Estimand Specification
- **Method**: Backdoor Adjustment
- **Treatment Variable**: `is_delivery_late`
- **Outcome Variable**: `Rating`

### Mathematical Expression
The causal effect is identified through the following estimand:

```latex
P(Rating|is_delivery_late,distance_km,season,Product_category_encoded,freight_value,Product_size)
```

realized estimand
```
Rating~is_delivery_late+distance_km+season+Product_category_encoded+freight_value+Product_size
```


## Expected Outcomes

This project aims to provide valuable insights into:
- The quantitative impact of delivery delays on customer satisfaction
- Key factors contributing to delivery delays in e-commerce
- Potential strategies for improving customer satisfaction in online retail

By leveraging causal inference techniques, we hope to move beyond mere correlation and uncover actionable insights for e-commerce businesses.

## Tools and Technologies

Python, DoWhy

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git

### Cloning the Repository

1. Open a terminal or command prompt.

2. Clone the repository using the following command:
   ```
   git clone https://github.com/yourusername/causal-attribution-analysis.git
   ```
   Replace `yourusername` with the actual username or organization name where the repository is hosted.

3. Navigate to the project directory:
   ```
   cd causal-attribution-analysis
   ```

### Setting up the Virtual Environment

1. Create a virtual environment:
   - On Windows:
     ```
     py -3.9 -m venv venv
     ```
   - On macOS and Linux:
     ```
     python3 -m venv venv
     ```

2. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

### Installing Dependencies

1. Ensure your virtual environment is activated (you should see `(venv)` at the beginning of your command prompt).

2. Install the required packages using the `requirements.txt` file:
   ```
   pip install -r requirements.txt
   ```

This will install all necessary dependencies for the project.

### Deactivating the Virtual Environment

When you're done working on the project, you can deactivate the virtual environment by running:
```
deactivate
```

## Contributors

## Contributors

- **[Juan Herrera](https://www.linkedin.com/in/juanherreras/)** 
- **[Denisse Wohlstein](https://www.linkedin.com/in/denissewohlstein/)** 
- **[Matteo Mennini](https://www.linkedin.com/in/matteomennini/)** 
- **[Anna Natasha](https://www.linkedin.com/in/anna-natasha/)**
- **[Avantika Gargya](https://www.linkedin.com/in/avantika-gargya/)**
