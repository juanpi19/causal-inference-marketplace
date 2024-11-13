# Olist Marketplace Causal Analysis


Understanding the causal relationship between delivery delays and customer satisfaction is crucial for e-commerce platforms, as it directly impacts customer retention, brand reputation, and long-term profitability. While delivery performance metrics are routinely collected, establishing a true causal link between delays and customer satisfaction presents unique challenges.

Although randomized controlled trials (RCTs) represent the gold standard in causal inference, deliberately delaying customer deliveries for experimental purposes would be both unethical and potentially damaging to business operations. This necessitates the use of observational study methods to draw reliable causal conclusions from existing data.

This study leverages the rich dataset from Olist, Brazil's largest department store marketplace, to estimate the causal effect of delivery delays on customer satisfaction ratings. We employ two complementary approaches: propensity score matching to simulate experimental conditions using observational data, and graphical causal models to understand the underlying data-generating process. This dual methodology allows us to not only quantify the impact of delays but also to understand the complex mechanisms through which delivery performance affects customer satisfaction.


### 1.1 What is a Marketplace? Why the Need of Data Science?



The role of a marketplace is to effectively connect customers with suppliers, whether they offer products or services. An important aspect of being a marketplace is that it neither owns inventory nor provides services directly. Instead, its primary goal is to facilitate connections between those who do and the customers who need them. However, this is far more complex than it might seem. Key questions arise, such as: How can we match customers and suppliers effectively? And once a match is made, how do we ensure a positive experience for both sides of the marketplace? This is where data comes in and plays a crucial role in streamlining this process.

According to <a href="https://www.youtube.com/watch?v=BVzTfsUMaK8&t=492s" target="_blank">Ramesh Johari</a> , the fundamental idea of any marketplace is taking the friction of the transaction cost away. 

That friction is reduced by data science, who would tackle three important aspects in any marketplace (any vertical): 

- Finding the people to match with
- Making the matching
- Learning about the matching


### Finding the People to Match with

Depending on the nature of the marketplace—particularly in the case of a two-sided marketplace—we must connect two groups: suppliers, who are willing to sell products or offer services, and customers, who are looking to purchase those products or services.

### Making the Matching

If I’m a customer, my question is: Who should I hire? If I’m a supplier, my question is: Who do I want as a customer?

### Learning About Matching

Suppliers will continue to sell products or offer services in the marketplace only if they have a positive experience—and the same holds true for customers. So, how can we learn from these interactions to ensure both sides are satisfied?

This is where our analysis comes into play. A match has been made, and the product delivery is late. However, our focus isn’t on understanding why the delivery was late. Instead, we aim to examine how the delay impacts the customer’s experience. To quantify this, we analyze customer ratings as a measure of satisfaction.


### 1.2 Research Questions

Before formalizing our research questions, it’s important to define what constitutes a late delivery. Each order includes an *expected delivery date* and an *actual delivery date*. A delivery is classified as late if the actual delivery date occurs after the expected delivery date. For our analysis, we treat late delivery as a binary variable: it takes a value of 1 if the delivery is late, regardless of whether it is delayed by 1 day or 10 days; otherwise, it is set to 0.


```plaintext
# Define late delivery logic
if actual_delivery > expected_delivery
    is_late_delivery = 1
else
    is_late_delivery = 0
end if


- Definition of key terms (delayed delivery, customer satisfaction)
- Scope and limitations

## 2. Data Overview
### 2.1 Dataset Description
- Source and time period
- Key variables
- Summary statistics

### 2.2 Missing Data Analysis
- Pattern of missing data
- Treatment of missing values
- Potential impact on analysis

## 3. Methodology
### 3.1 Causal Framework
- Potential outcomes framework
- Key assumptions
- Identification strategy

### 3.2 Propensity Score Matching (Late Delivery --> Ratings)
- Matching methodology
- Covariate selection
- Balance diagnostics
- Results
- Robustness Checks
- Interpretation of Results

### 3.3 Graphical Causal Models
- DAG specification
- Model assumptions
- Identification strategy
- Results
- Robustness Checks
- Interpretation of Results


### 3.2 Propensity Score Matching (Late Delivery --> Revenue)
- Matching methodology
- Logic behind lags
- Covariate selection
- Balance diagnostics
- Results
- Robustness Checks
- Interpretation of Results


### 3.3 Practical Implications
- Recommendations for e-commerce operations
- Potential interventions
- Cost-benefit considerations



### References

let's include some literature



