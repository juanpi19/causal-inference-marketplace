import pandas as pd
import numpy as np
import time

from sklearn.impute import KNNImputer
from src.data.make_dataset import load_data, merge_all_datasets

import warnings
warnings.filterwarnings("ignore")

class HandleMissingValues:
    '''This class exclusively handles missing values by dropping or 
    imputing through different functions tailored to each type of variable.'''

    def dropping_values(self, df):
        """Drop rows with missing values in key columns."""
        df.dropna(subset=['seller_id', 'order_delivered_customer_date', 'review_score'], inplace=True)
        return df

    def geolocation_imputation(self, df):
        """Impute missing geolocation values using KNN."""
        geolocation_columns_x = ['geolocation_lat_x', 'geolocation_lng_x']
        geolocation_columns_y = ['geolocation_lat_y', 'geolocation_lng_y']
        knn_imputer = KNNImputer(n_neighbors=5)
        df[geolocation_columns_x] = knn_imputer.fit_transform(df[geolocation_columns_x])
        df[geolocation_columns_y] = knn_imputer.fit_transform(df[geolocation_columns_y])
        return df
    
    # JUAN (put product_category and freight_value here)


    def dropping_columns(self, df):
        """Drop columns that are not needed for further analysis."""
        columns_to_drop = [
            'geolocation_zip_code_prefix_x', 'geolocation_zip_code_prefix_y', 
            'geolocation_city_x', 'geolocation_state_x', 'geolocation_city_y', 
            'geolocation_state_y', 'product_name_lenght', 'shipping_limit_date', 
            'payment_sequential', 'product_description_lenght', 'review_comment_title', 
            'order_delivered_carrier_date', 'payment_type', 'payment_installments', 
            'review_id', 'review_comment_message'
        ]
        df.drop(columns=columns_to_drop, inplace=True, errors='ignore')
        return df

class ProcessingHelpers:
    '''This class hosts all helper functions needed for further processing.'''

    def haversine(self, lat1, lon1, lat2, lon2):
        """Calculate the great-circle distance between two points."""
        lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
        r = 6371  # Radius of Earth in kilometers
        return r * c

    def rolling_mean_customer(self, group):
        """Calculate expanding mean for customer experience."""
        filtered_reviews = group[group <= 5]
        expanding_mean = filtered_reviews.expanding().mean()
        return expanding_mean.reindex(group.index).ffill().bfill()

    def rolling_mean_seller(self, group):
        """Calculate expanding mean for seller experience."""
        filtered_reviews = group[group <= 5]
        expanding_mean = filtered_reviews.expanding().mean()
        return expanding_mean.reindex(group.index).ffill().bfill()

class Preprocess:
    '''Class for preprocessing data, using previous helper and imputation methods.'''

    def preprocessing(self, df, state_to_region):
        df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'], errors='coerce')
        df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'], errors='coerce')
        df['rainfall'] = df['customer_state'].map(state_to_region)
        df['product_weight_kg'] = df['product_weight_g'] / 1000
        df['product_size'] = df['product_length_cm'] * df['product_height_cm'] * df['product_width_cm']
        df['no_photos'] = df['product_photos_qty']
        df['product_price'] = df['price']
        df['late_delivery_in_days'] = (df['order_delivered_customer_date'] - df['order_estimated_delivery_date']).dt.days
        df['is_delivery_late'] = np.where(df['late_delivery_in_days'] > 0, 1, 0)
        df['month'] = pd.to_datetime(df['order_purchase_timestamp']).dt.month
        df['distance_km'] = df.apply(lambda row: ProcessingHelpers().haversine(
            row['geolocation_lat_x'], row['geolocation_lng_x'], 
            row['geolocation_lat_y'], row['geolocation_lng_y']), axis=1)
        df.dropna(subset=['distance_km'], inplace=True)
        return df

    def rolling_mean_process(self, df):
        df = df.sort_values(by=['customer_id', 'review_answer_timestamp'])
        df['customer_experience'] = df.groupby('customer_id')['review_score'].apply(ProcessingHelpers().rolling_mean_customer).reset_index(level=0, drop=True)
        df['customer_experience'].fillna(df['review_score'], inplace=True)
        df = df.sort_values(by=['seller_id', 'review_answer_timestamp'])
        df['seller_avg_rating'] = df.groupby('seller_id')['review_score'].apply(ProcessingHelpers().rolling_mean_seller).reset_index(level=0, drop=True)
        df['seller_avg_rating'].fillna(df['review_score'], inplace=True)
        return df

    def df_final(self, df):
        columns_of_interest = [
            'order_id', 'customer_id', 'order_status', 'order_purchase_timestamp',
            'order_approved_at', 'review_answer_timestamp', 'order_item_id', 
            'product_id', 'seller_id', 'payment_value', 'review_score', 'month',
            'rainfall', 'product_weight_kg', 'product_size', 'no_photos', 
            'product_price', 'is_delivery_late', 'customer_experience', 
            'seller_avg_rating', 'freight_value', 'distance_km'
             #JUAN 'product_category_encoded', 'product_category'
        ]
        return df[columns_of_interest]
    



    '''

class FinalDataFrame:
    def __init__(self, state_to_region):
        self.state_to_region = state_to_region
        self.handle_missing_values = HandleMissingValues()
        self.processing_helpers = ProcessingHelpers()
        self.preprocess = Preprocess()

    def process_data(self, df):
        df = self.handle_missing_values.dropping_values(df)
        df = self.handle_missing_values.geolocation_imputation(df)
        df = self.handle_missing_values.dropping_columns(df)
        print("Step 1: Missing values handled.")
        df = self.preprocess.preprocessing(df, self.state_to_region)
        print("Step 2: Data preprocessed.")
        df = self.preprocess.rolling_mean_process(df)
        print("Step 3: Customer and seller experience calculated.")
        df_final = self.preprocess.df_final(df)
        print("Step 4: Final DataFrame created.")
        return df_final

# Main script
if __name__ == "__main__":
    state_to_region = {
        'AC': 'North', 'AP': 'North', 'AM': 'North', 'PA': 'North', 'RO': 'North', 
        'RR': 'North', 'TO': 'North', 'AL': 'Northeast', 'BA': 'Northeast', 'CE': 'Northeast', 
        'MA': 'Northeast', 'PB': 'Northeast', 'PE': 'Northeast', 'PI': 'Northeast', 
        'RN': 'Northeast', 'SE': 'Northeast', 'GO': 'Central-West', 'MT': 'Central-West', 
        'MS': 'Central-West', 'DF': 'Central-West', 'ES': 'Southeast', 'MG': 'Southeast', 
        'RJ': 'Southeast', 'SP': 'Southeast', 'PR': 'South', 'RS': 'South', 'SC': 'South'
    }

    final_data_frame_processor = FinalDataFrame(state_to_region)

    # Load your data
    data_dict = load_data()
    df = merge_all_datasets(
        data_dict['olist_customers_df'], data_dict['olist_geolocation_df'],
        data_dict['olist_order_items_df'], data_dict['olist_order_payments_df'], 
        data_dict['olist_order_reviews_df'], data_dict['olist_orders_df'],
        data_dict['olist_products_df'], data_dict['olist_sellers_df']
    )

    print("Data loaded")






    '''