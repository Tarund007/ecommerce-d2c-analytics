-- Part A: Rank top-selling products by category based on total revenue
WITH product_revenue AS (
    SELECT 
        p.product_category_name,
        p.product_id,
        SUM(oi.price + oi.freight_value) AS total_revenue,
        ROW_NUMBER() OVER (PARTITION BY p.product_category_name ORDER BY SUM(oi.price + oi.freight_value) DESC) as product_rank
    FROM `olist-d2c-analytics.olist_warehouse.cleaned_order_items` oi
    JOIN `olist-d2c-analytics.olist_warehouse.cleaned_products` p 
        ON oi.product_id = p.product_id
    GROUP BY p.product_category_name, p.product_id
),

-- Part B: Calculate Week-over-Week Revenue Growth
weekly_sales AS (
    SELECT 
        DATE_TRUNC(o.order_purchase_timestamp, WEEK) AS order_week,
        SUM(oi.price + oi.freight_value) AS weekly_revenue
    FROM `olist-d2c-analytics.olist_warehouse.cleaned_orders` o
    JOIN `olist-d2c-analytics.olist_warehouse.cleaned_order_items` oi 
        ON o.order_id = oi.order_id
    GROUP BY order_week
)

SELECT 
    order_week,
    weekly_revenue,
    LAG(weekly_revenue) OVER (ORDER BY order_week) AS prev_week_revenue,
    ROUND(
        (weekly_revenue - LAG(weekly_revenue) OVER (ORDER BY order_week)) / 
        LAG(weekly_revenue) OVER (ORDER BY order_week) * 100, 2
    ) AS wow_growth_percentage
FROM weekly_sales
ORDER BY order_week DESC;
