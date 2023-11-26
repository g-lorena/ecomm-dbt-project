with order_details as (
    select 
        'OrderID',
        'Amount',
        'Profit',
        'Quantity',
        'Category',
        'Sub-Category' as sub_category
    from {{ source('training', 'order_details') }}
)

select * from order_details