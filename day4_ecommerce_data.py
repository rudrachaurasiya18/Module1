# =========================================================
# 🛒 E-COMMERCE ORDER INTELLIGENCE USING PANDAS
# =========================================================

import pandas as pd
# =========================================================
# STEP 1 — LOAD DATASETS
# =========================================================

orders = pd.read_csv(
    r"olist_orders_dataset.csv"
)

customers = pd.read_csv(
    r"olist_customers_dataset.csv"
)

order_items = pd.read_csv(
    r"olist_order_items_dataset.csv"
)

products = pd.read_csv(
    r"olist_products_dataset.csv"
)

payments = pd.read_csv(
    r"olist_order_payments_dataset.csv"
)


# =========================================================
# STEP 2 — DISPLAY FIRST ROWS
# =========================================================

print("=================================================")
print("📌 ORDERS DATA")
print("=================================================")

print(orders.head())

print("\n=================================================")
print("📌 CUSTOMERS DATA")
print("=================================================")

print(customers.head())


# =========================================================
# STEP 3 — MERGE ORDERS + CUSTOMERS
# =========================================================

orders_customers = pd.merge(

    orders,
    customers,

    on='customer_id',

    how='inner'

)


# =========================================================
# STEP 4 — MERGE ORDER ITEMS
# =========================================================

master_df = pd.merge(

    orders_customers,
    order_items,

    on='order_id',

    how='inner'

)


# =========================================================
# STEP 5 — MERGE PRODUCTS
# =========================================================

master_df = pd.merge(

    master_df,
    products,

    on='product_id',

    how='left'

)


# =========================================================
# STEP 6 — MERGE PAYMENTS
# =========================================================

master_df = pd.merge(

    master_df,
    payments,

    on='order_id',

    how='left'

)


# =========================================================
# STEP 7 — FINAL DATA INFORMATION
# =========================================================

print("\n=================================================")
print("📊 MASTER DATAFRAME INFO")
print("=================================================")

print(master_df.info())


# =========================================================
# STEP 8 — TOTAL REVENUE PER CUSTOMER
# =========================================================

print("\n=================================================")
print("💰 TOTAL REVENUE PER CUSTOMER")
print("=================================================")

customer_revenue = master_df.groupby(
    'customer_unique_id'
)['price'].sum().sort_values(
    ascending=False
)

print(customer_revenue.head())


# =========================================================
# STEP 9 — CUSTOMERS WITH ONLY ONE ORDER
# =========================================================

print("\n=================================================")
print("🛍️ CUSTOMERS WITH ONLY ONE ORDER")
print("=================================================")

order_count = master_df.groupby(
    'customer_unique_id'
)['order_id'].nunique()

single_order_customers = order_count[
    order_count == 1
]

print(single_order_customers.head())


# =========================================================
# STEP 10 — CONVERT DATE COLUMN
# =========================================================

master_df['order_purchase_timestamp'] = pd.to_datetime(

    master_df['order_purchase_timestamp']

)


# =========================================================
# STEP 11 — EXTRACT YEAR & MONTH
# =========================================================

master_df['Year'] = master_df[
    'order_purchase_timestamp'
].dt.year

master_df['Month'] = master_df[
    'order_purchase_timestamp'
].dt.month_name()


print("\n=================================================")
print("📅 YEAR & MONTH EXTRACTION")
print("=================================================")

print(

    master_df[
        ['order_purchase_timestamp', 'Year', 'Month']
    ].head()

)


# =========================================================
# STEP 12 — STRING OPERATIONS
# =========================================================

master_df['product_category_name'] = master_df[
    'product_category_name'
].fillna('UNKNOWN')

master_df['product_category_name'] = master_df[
    'product_category_name'
].str.upper()


print("\n=================================================")
print("🔤 STRING OPERATIONS")
print("=================================================")

print(

    master_df[
        ['product_category_name']
    ].head()

)


# =========================================================
# STEP 13 — PIVOT TABLE
# =========================================================

print("\n=================================================")
print("📊 PIVOT TABLE")
print("=================================================")

pivot = pd.pivot_table(

    master_df,

    values='price',

    index='Year',

    columns='customer_state',

    aggfunc='mean'

)

print(pivot)


# =========================================================
# STEP 14 — MELT FUNCTION
# =========================================================

print("\n=================================================")
print("🔄 MELT FUNCTION")
print("=================================================")

sales_wide = pd.DataFrame({

    'Product': ['A', 'B'],

    'Jan': [100, 200],
    'Feb': [150, 250],
    'Mar': [300, 400]

})

print("\n📌 WIDE FORMAT:")
print(sales_wide)

melted = pd.melt(

    sales_wide,

    id_vars='Product',

    var_name='Month',

    value_name='Sales'

)

print("\n📌 LONG FORMAT:")
print(melted)


# =========================================================
# STEP 15 — MULTI INDEX DATAFRAME
# =========================================================

print("\n=================================================")
print("📚 MULTI-INDEX DATAFRAME")
print("=================================================")

multi_index = master_df.groupby(

    ['Year', 'Month']

)['price'].sum()

print(multi_index.head(10))


# =========================================================
# STEP 16 — BONUS CHALLENGE
# =========================================================
# Average Delivery Time
# =========================================================

master_df['order_delivered_customer_date'] = pd.to_datetime(

    master_df['order_delivered_customer_date']

)


master_df['Delivery Days'] = (

    master_df['order_delivered_customer_date']

    -

    master_df['order_purchase_timestamp']

).dt.days


# =========================================================
# STEP 17 — AVERAGE DELIVERY DAYS
# =========================================================

print("\n=================================================")
print("🚚 AVERAGE DELIVERY TIME")
print("=================================================")

average_delivery = master_df[
    'Delivery Days'
].mean()

print(f"Average Delivery Days : {average_delivery:.2f}")


# =========================================================
# STEP 18 — SLOWEST DELIVERY CITIES
# =========================================================

print("\n=================================================")
print("🐢 SLOWEST DELIVERY CITIES")
print("=================================================")

slowest_cities = master_df.groupby(
    'customer_city'
)['Delivery Days'].mean().sort_values(
    ascending=False
)

print(slowest_cities.head())


# =========================================================
# STEP 19 — TOP STATES BY REVENUE
# =========================================================

print("\n=================================================")
print("🏆 TOP STATES BY REVENUE")
print("=================================================")

top_states = master_df.groupby(
    'customer_state'
)['price'].sum().sort_values(
    ascending=False
)

print(top_states.head())


# =========================================================
# STEP 20 — PAYMENT TYPE ANALYSIS
# =========================================================

print("\n=================================================")
print("💳 PAYMENT TYPE ANALYSIS")
print("=================================================")

payment_analysis = master_df[
    'payment_type'
].value_counts()

print(payment_analysis)


# =========================================================
# FINAL MESSAGE
# =========================================================

print("\n=================================================")
print("✅ E-COMMERCE ANALYSIS COMPLETED SUCCESSFULLY!")
print("=================================================")
