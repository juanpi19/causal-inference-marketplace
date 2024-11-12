
This is the analysis for the handling of missing values for the data and its processing.

1. Handling missing values:

list of variables of variables with there respective missing values:

- order_id: 0
- customer_id: 0
- order_status: 0
- order_purchase_timestamp: 0
- order_approved_at: 177
- order_delivered_carrier_date: 2086
- order_delivered_customer_date: 3421
- order_estimated_delivery_date: 0
- order_item_id: 833
- product_id: 833
- seller_id: 833
- shipping_limit_date: 833
- price: 833
- freight_value: 833
- payment_sequential: 3
- payment_type: 3
- payment_installments: 3
- payment_value: 3
- review_id: 997
- review_score: 997
- review_comment_title: 105154
- review_comment_message: 68898
- review_creation_date: 997
- review_answer_timestamp: 997
- product_category_name: 2542
- product_name_lenght: 2542
- product_description_lenght: 2542
- product_photos_qty: 2542
- product_weight_g: 853
- product_length_cm: 853
- product_height_cm: 853
- product_width_cm: 853
- customer_unique_id: 0
- customer_zip_code_prefix: 0
- customer_city: 0
- customer_state: 0
- seller_zip_code_prefix: 833
- seller_city: 833
- seller_state: 833
- geolocation_zip_code_prefix_x: 322
- geolocation_lat_x: 322
- geolocation_lng_x: 322
- geolocation_city_x: 322
- geolocation_state_x: 322
- geolocation_zip_code_prefix_y: 1098
- geolocation_lat_y: 1098
- geolocation_lng_y: 1098
- geolocation_city_y: 1098
- geolocation_state_y: 1098

List of variables that will be used in this analysis with their respective missing values:

- order_id: 0
- customer_id: 0
- order_purchase_timestamp: 0
- order_approved_at: 177
- order_delivered_customer_date: 3421
- order_estimated_delivery_date: 0
- product_id: 833
- seller_id: 833
- price: 833
- freight_value: 833
- payment_value: 3
- review_score: 997
- review_creation_date: 997
- review_answer_timestamp: 997
- product_category_name: 2542
- product_photos_qty: 2542
- product_weight_g: 853
- product_length_cm: 853
- product_height_cm: 853
- product_width_cm: 853
- customer_unique_id: 0
- customer_zip_code_prefix: 0
- customer_city: 0
- customer_state: 0
- seller_zip_code_prefix: 833
- seller_city: 833
- seller_state: 833
- geolocation_lat_x: 322
- geolocation_lng_x: 322
- geolocation_lat_y: 1098
- geolocation_lng_y: 1098


a. Dropping rows where 'seller_id', 'order_delivered_customer_date', 'review_score' are Null or NaN:
    
    We are not able to replace, impute, predict these values, it would add bias to our analysis.

b. Imputing seller and costumer geolocation:

    We are imputing the missing values in these columns with the purpose of calculating/creating a new and complete variable
    called 'distance_km' which will be the distance between a seller and a customar --> this directly affects the time that a delivery takes to be delivered (Assumption) and if the delivery is late or not.

    In this case, the K-Nearest Neighbors (KNN) imputation method finds the 5 nearest neighbors (rows with complete data) for each row with missing values in the specified geolocation columns and fills the missing values by averaging the corresponding values from those neighbors.


2. Preprocess: 

Final list of variable to be used in our analysis:

- order_id : to identify an order (index)
- customer_id : to identify a customer (index)
- order_status : 
- order_purchase_timestamp :
- order_approved_at :
- review_answer_timestamp :
- order_item_id :
- product_id : to identify a product (index)
- seller_id : to identify a seller (index)
- payment_value :
- review_score : 
- month :
- rainfall :
- product_weight_kg :
- product_size :
- no_photos :
- product_price :
- is_delivery_late :
- customer_experience :
- seller_avg_rating :
- freight_value :
- distance_km : 
- product_category_encoded :
- product_category :







