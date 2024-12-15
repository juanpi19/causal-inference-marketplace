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
# Pseudocode for how the treatment (T) is defined
if actual_delivery > expected_delivery
    is_late_delivery = 1
else
    is_late_delivery = 0
```

Another key variable is customer ratings, which serves as our outcome variable. This variable measures customer satisfaction following a purchase. It is ordinal, ranging from 1 to 5, where 5 represents an excellent experience and 1 signifies a poor experience.

With this being clear, we now define our research question:

**What is the impact of a late delivery on customer satisfaction?**

Our primary goal is to uncover the causal effect of late delivery on customer satisfaction. While we could explore associations using methods like regression, this project focuses on leveraging causal inference techniques to estimate the causal relationship more accurately.

```plaintext
# Causal Link
is_late_delivery -> customer_rating
```

## 2. Olist Marketplace data Overview

### 2.1 Source and Time Period
The Olist dataset, sourced from Kaggle, provides an in-depth view of the Brazilian e-commerce ecosystem. As the largest department store within Brazilian marketplaces, Olist offers data encompassing 100,000 orders from 2016 to 2018. This dataset includes various aspects such as order status, pricing, payment details, freight performance, customer location, product attributes, and customer reviews. The addition of a geolocation dataset that maps Brazilian zip codes to their latitude and longitude enhances the analysis, especially for variables such as distance_km.

For context, this is how the user interface looks for a customer trying to purchase a product or service through Olist: 
 *image of use interface*

An order may include multiple items, and different items might be fulfilled by distinct sellers.

### 2.2 Data Overview
The Kaggle-provided data comprises 11 datasets, of which nine are relevant for this project. These datasets encompass customer orders, customer and seller geolocations, order reviews, product descriptions (including measurements, weight, and photos), etc.

### 2.3 Data Processing
Data processing is crucial as it defines and implements assumptions that affect variable statistics and the overall analysis.

#### 2.3.1 Key Variables of the raw data 
The original 48 variables were filtered to 25 key variables essential for the analysis, some of these are:

-	Variables utilized as indexes for different tests in our analysis: customer_id, order_id, seller_id & product_id.

-	Variables that will allow us to calculate if a delivery is late or on time: order_delivered_customer_date & order_estimated_delivery_date.

-	Variables that might impact our treatment variable (late or on time delivery) referring specifically to the product delivered:  product_weight_g, product_length_cm, product_height_cm, product_width_cm.

-	Variables that might impact our treatment variable (late or on time delivery) referring specifically to the trajectory of the product delivered:  customer_zip_code_prefix, customer_city, customer_state, geolocation_lat_x, geolocation_lng_x, seller_zip_code_prefix, seller_city, seller_state, geolocation_lat_y, geolocation_lng_y.

#### 2.3.2 Missing Value Handling
-	Dropping Values: Missing values in seller_id, order_delivered_customer_date, review_score, and freight_value were dropped due to the absence of a logical method for imputation. Removing these values maintained data reliability.

-	Geolocation Imputation: The geolocation_lat_x, geolocation_lng_x, geolocation_lat_y, and geolocation_lng_y columns were imputed using a K-Nearest Neighbors (KNN) approach. This method utilized neighboring data points to estimate missing values, ensuring spatial consistency.

-	Imputation of product_category_name: A Random Forest model imputed missing product_category_name values. This column's imputation was important due to its categorical nature and relevance. The model was trained on product dimensions (product_weight_g, product_length_cm, product_height_cm, product_width_cm), encoded seller identifiers, and order month. The Random Forest method was chosen for its robust performance and ability to capture complex relationships.

-	 Dropping Irrelevant Columns: Columns with redundancy, excessive missing values, or irrelevance were dropped. These included geolocation_zip_code_prefix_x, geolocation_zip_code_prefix_y, geolocation_city_x, geolocation_state_x, geolocation_city_y, geolocation_state_y, product_name_lenght, shipping_limit_date, payment_sequential, product_description_lenght, review_comment_title, order_delivered_carrier_date, payment_type, payment_installments, review_id, and review_comment_message.

#### 2.3.3 Final Variables and Dataset Creation
To ensure the final dataset is well-prepared for analyzing the impact of late or on-time deliveries on customer ratings, a preprocessing strategy was employed. This process involves data type conversions, feature engineering, and data transformations. 

##### Conversions: 
-   Datetime Conversion: order_delivered_customer_date and order_estimated_delivery_date were converted to datetime format. This step enabled time-based calculations, such as identifying delivery delays.

##### Feature Engineering:
-   Rainfall Data Mapping: The rainfall feature was created by mapping the customer_state column to corresponding rainfall values provided in the state_to_region dictionary (a dictionary containing the corresponding region to each state). This variable was intended to assess any correlation between weather conditions and delivery performance.

-   Product Weight and Size: Converted product_weight_g to product_weight_kg, and calculated product size using volume (product_length_cm * product_height_cm * product_width_cm).

-   Number of Photos and Product Price: Standardized the columns no_photos and product_price to maintain consistency.

- Late Delivery Indicator: Created late_delivery_in_days by subtracting order_estimated_delivery_date from order_delivered_customer_date, and a binary feature is_delivery_late to classify deliveries.

-	Distance Calculation: Applied a custom haversine function to calculate the great-circle distance between customer and seller locations. This distance_km metric is essential for understanding delivery performance's impact on customer ratings. 

Rows with missing distance values were dropped to ensure analysis accuracy.

##### Rolling Mean Calculations:
-   Customer Experience: The customer_experience feature was calculated using a rolling mean of review_score, capped at 5, to track customer satisfaction over time.

-   Seller Average Rating: Computed using a rolling mean of review_score for sellers to gain insights into their performance consistency. Missing values were filled using review_score.

#### 2.3.4  Final Data frame Creation
The final dataset included key columns: order_id, customer_id, seller_id, timestamps (order_purchase_timestamp, order_approved_at, review_answer_timestamp), and features such as rainfall, product_weight_kg, product_size, no_photos, is_delivery_late, customer_experience, seller_avg_rating, freight_value, distance_km, product_category_name, and product_category_name_encoded. This selection ensured that the dataset was streamlined for efficient analysis and modeling.

#### 2.3.5 Implications and Limitations

##### Data Limitations:
-   Anonymization: The use of fictional names (e.g., from Game of Thrones) limits deeper analysis into actual seller or brand performance.

-   Time Period: The dataset only covers 2016-2018, potentially missing recent consumer behavior shifts or technological changes.

##### Handling Missing Data:
-   Imputation Reliability: Methods such as KNN for geolocation and Random Forest for product_category_name are assumption-dependent and could introduce biases, impacting analysis accuracy.

-   Dropped Data: Removing rows with missing critical information (e.g., seller_id, review_score) may reduce dataset size and introduce bias.

##### Limited Scope of Variables:
-  The dataset does not include potentially impactful variables such as real-time traffic data, weather conditions at delivery, or specific logistics details (e.g., third-party vs. in-house delivery), which could affect delivery performance and customer ratings.

##### Dependency on Assumptions:
-   The analysis relies on assumptions embedded in the Directed Acyclic Graph (DAG). These guide how variables interact, impacting decisions on data imputation, feature selection, and model-building. This dependency makes the analysis sensitive to changes in assumptions, emphasizing the need for careful validation and iterative testing.

### 2.4 Data exploration
#### 2.4.1 EDA process and insights  - Avantika
#### 2.4.2 Definitions of key variables for analysis (Confounders, Treatment, etc) - Avantika 


## 3. Methodology
### 3.1 Causal Framework
- Potential outcomes framework
- Key assumptions
- Identification strategy

### 3.2 Propensity Score Matching (Late Delivery --> Ratings)

### 3.2.1 Matching Methodology
The matching methodology employed in this project is grounded in the Potential Outcomes Framework, a key concept in causal inference. This framework defines causal effects by comparing the outcomes of treated and control groups as if they were both exposed and unexposed to the treatment. However, the Fundamental Problem of Causal Inference is that we can never observe both outcomes for the same unit simultaneously. This in this case is addressed by creating comparable groups through Propensity Score Matching (PSM), to approximate a randomized experimental design.
PSM is a widely used technique to address the problem of confounding by balancing covariates between treated and control groups. The method works in three main steps:

Propensity Score Calculation: A logistic regression model was used to estimate the propensity score, which is the probability of receiving the treatment (e.g., late deliveries) given the observed covariates. These scores summarize the multidimensional covariate space into a single scalar value, simplifying the matching process.

Matching: Using a 1-to-1 nearest neighbor matching algorithm, treated units were matched with control units that had similar propensity scores. Matching ensures that the treated and control groups are comparable in terms of the covariates, minimizing selection bias. Importantly, matching was performed without replacement to maintain the integrity of the control group.

Average Treatment Effect (ATE) Calculation: After matching, the treatment effect was estimated by comparing the average outcomes (e.g., ratings or revenue metrics) between the treated and control groups. The ATE represents the causal impact of the treatment on the outcome, assuming that unobserved confounding is minimal.

By leveraging PSM, we effectively created balanced treatment and control groups that allowed for more robust causal inference. This approach ensures that differences in outcomes can be more reliably attributed to the treatment rather than to pre-existing differences between the groups.

### 3.2.2 Covariate selection
The selection of covariates for propensity score matching was guided by their potential influence on both the treatment (late deliveries) and the outcome variables (ratings). Key covariates included product-specific characteristics (product category, product size), transaction attributes ( freight value, distance), and temporal factors (month). These covariates were chosen based on domain knowledge to capture relevant factors that could simultaneously affect the likelihood of late delivery and its subsequent impact on customer ratings. By including these covariates in the propensity score model, the matching process ensured balance across these factors, thereby minimizing confounding and improving the validity of the causal estimates.

### 3.3.3 Balance diagnostics
To evaluate the success of propensity score matching, we visually compared the distributions of propensity scores for the treated and control groups before and after matching. Before matching, the propensity score distributions showed divergence, indicating an imbalance in the covariates between the two groups.

 After matching, the distributions aligned closely, demonstrating that the matching process successfully balanced the covariates. 
This overlap ensures that treated and control units are comparable, reducing confounding and allowing for a more reliable estimation of the treatment effect.

### 3.3.4 Results
The results of the analysis indicate a negative impact of delayed deliveries on ratings. The ATE (Average Treatment Effect) of -1.91 suggests that, on average, late deliveries lead to a reduction of approximately 1.91 units in the outcome ratings. The ATT (Average Treatment Effect on the Treated) of -1.98 implies that for those orders that were actually delivered late, the impact is slightly stronger, with an average reduction of 1.98 units in ratings. Similarly, the ATC (Average Treatment Effect on the Controls) of -1.90 indicates that if orders that were not delayed had been delayed, the expected reduction in ratings would have been approximately 1.90 units. The close alignment between ATE, ATT, and ATC values indicates consistency in the treatment effect across the population, suggesting that the negative impact of late deliveries is broadly uniform. This highlights the importance of addressing delays to mitigate their negative effects on key performance metrics.

### 3.5.5 Robustness Checks
To ensure the robustness of the estimated treatment effect, we conducted two key robustness checks. First, we used a bootstrap confidence interval to validate the stability of the Average Treatment Effect (ATE) estimated through Propensity Score Matching (PSM). The ATE was calculated as -1.91, with a narrow 95% confidence interval ranging from -1.97 to -1.86 and a standard error of 0.0339. These results suggest high precision in the estimated treatment effect and provide evidence that the negative impact of delayed deliveries is statistically significant.
Second, we performed a sensitivity analysis by introducing an unobserved confounder to test how the treatment effect changes in its presence. After adding the hypothetical confounder, the estimated treatment effect remained consistent, with the new effect ranging from -1.94 to -1.85. This minimal deviation demonstrates that the causal estimate is robust to potential unmeasured confounding and further validates the reliability of the analysis. Together, these checks reinforce confidence in the validity and robustness of the findings.

### 3.6.6 Interpretation of Results
The results of the analysis reveal a consistent and significant negative impact of delayed deliveries on key metrics. The ATE of -1.91 suggests that late deliveries lead to a notable reduction in ratings, while the ATT (-1.98) and ATC (-1.90) indicate that this effect is uniformly felt across both treated and control groups. Robustness checks, including bootstrap confidence intervals and sensitivity analysis, confirm the reliability of these estimates, with minimal deviation even after accounting for potential unobserved confounders. These findings highlight the importance of timely deliveries in maintaining customer satisfaction and suggest that addressing delays could yield measurable benefits in outcomes.
However, the analysis has some limitations. While Propensity Score Matching successfully balanced observed covariates, the potential for unobserved confounders, though tested for robustness, cannot be entirely ruled out. Additionally, the treatment effect measured here captures the short-term impact on ratings or payment value but may not fully account for long-term effects or indirect pathways, such as the influence of ratings on future revenues. Finally, the results are conditional on the quality and completeness of the data, particularly regarding the accuracy of the treatment and outcome variables. Despite these limitations, the analysis provides actionable insights for mitigating the adverse effects of delivery delays.git 

### 3.3 Graphical Causal Models
- DAG specification
- Model assumptions
- Identification strategy
- Results
- Robustness Checks
- Interpretation of Results


### 3.4 Propensity Score Matching (Late Delivery --> Revenue)
- Matching methodology
- Logic behind lags
- Covariate selection
- Balance diagnostics
- Results
- Robustness Checks
- Interpretation of Results


### 3.5 Practical Implications
- Recommendations for e-commerce operations
- Potential interventions
- Cost-benefit considerations



### References

let's include some literature




