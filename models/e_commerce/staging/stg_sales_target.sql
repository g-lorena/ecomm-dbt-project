with sales_target as (
    select 
        MonthofOrderDate,
        Category,
        Target
    from {{ source('training', 'sales_target') }}
)

select * from sales_target