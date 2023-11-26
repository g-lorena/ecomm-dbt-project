with order_details as (
    select * from {{ ref ('stg_order_details') }}
),

list_orders as (
    select * from {{ ref ('stg_list_orders') }}
),

sales as (
    select 
        lO.OrderDate,
        lO.CustomerName,
        lO.State, 
        lO.City,
        oD.Amount, 
        oD.Profit,
        oD.Quantity,
        oD.Category,
        oD.sub_category
    from list_orders as lO 
    left join order_details as oD using (OrderID)
    group by lO.OrderDate,lO.CustomerName,lO.State,lO.City,oD.Amount,oD.Profit,oD.Quantity,oD.Category,oD.sub_category
)

select * from sales