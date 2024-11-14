# Olist E-commerce Causal Analysis

## Project Overview
This project investigates the causal effect of delayed delivery on customer satisfaction ratings in e-commerce, using data provided by Olist, the largest department store in Brazilian marketplaces.



## Research Question
Our primary research question is:

**What is the causal effect of delayed delivery on customer ratings?**


## Directed Acyclic Graph

![Causal DAG](results/figures/pictures/dag.jpg)


## Methodology

Our analysis will follow these key steps:

1. **Model Formulation**: Develop a causal inference model based on carefully considered assumptions.
2. **Causal Estimand Identification**: Determine an expression for the causal effect under our model assumptions.
3. **Statistical Estimation**: Apply advanced statistical methods such as matching or instrumental variables to estimate the causal effect.
4. **Robustness Checks**: Verify the validity of our estimates through various robustness checks.

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
