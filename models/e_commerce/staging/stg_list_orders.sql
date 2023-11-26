with list_of_orders as (
    select 
        OrderID,
        OrderDate,
        CustomerName,
        State,
        City
    from {{ source('training', 'list_of_orders') }}
)

select * from list_of_orders