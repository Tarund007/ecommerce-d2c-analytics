WITH customer_first_purchase AS (
    -- Step 1: Find the first purchase month for every customer
    SELECT 
        c.customer_unique_id,
        MIN(DATE_TRUNC(DATE(o.order_purchase_timestamp), MONTH)) AS cohort_month
    FROM `olist-d2c-analytics.olist_warehouse.cleaned_orders` o
    JOIN `olist-d2c-analytics.olist_warehouse.cleaned_customers` c 
        ON o.customer_id = c.customer_id
    GROUP BY c.customer_unique_id
),

customer_activity AS (
    -- Step 2: Map all customer orders to their respective months
    SELECT DISTINCT
        c.customer_unique_id,
        DATE_TRUNC(DATE(o.order_purchase_timestamp), MONTH) AS order_month
    FROM `olist-d2c-analytics.olist_warehouse.cleaned_orders` o
    JOIN `olist-d2c-analytics.olist_warehouse.cleaned_customers` c 
        ON o.customer_id = c.customer_id
),

cohort_indexed AS (
    -- Step 3: Calculate the month index (age of cohort) for each order
    SELECT 
        cfp.customer_unique_id,
        cfp.cohort_month,
        ca.order_month,
        (EXTRACT(YEAR FROM ca.order_month) - EXTRACT(YEAR FROM cfp.cohort_month)) * 12 +
        (EXTRACT(MONTH FROM ca.order_month) - EXTRACT(MONTH FROM cfp.cohort_month)) AS month_number
    FROM customer_first_purchase cfp
    JOIN customer_activity ca 
        ON cfp.customer_unique_id = ca.customer_unique_id
)

-- Step 4: Pivot into a retention matrix view
SELECT 
    cohort_month,
    COUNT(DISTINCT CASE WHEN month_number = 0 THEN customer_unique_id END) AS m0_users,
    COUNT(DISTINCT CASE WHEN month_number = 1 THEN customer_unique_id END) AS m1_users,
    COUNT(DISTINCT CASE WHEN month_number = 2 THEN customer_unique_id END) AS m2_users,
    COUNT(DISTINCT CASE WHEN month_number = 3 THEN customer_unique_id END) AS m3_users
FROM cohort_indexed
GROUP BY cohort_month
ORDER BY cohort_month;
