
with sales as (
    select * 
    from {{ ref('int_sales')}}
)

select * from sales