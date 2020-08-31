use information_schema;
select data_length,index_length
    from tables where
    table_schema='mashan'
    and table_name = 'xisha1';

select data_length,index_length
    from tables where
    table_schema='mashan'
    and table_name = 'xisha10';

select data_length,index_length
    from tables where
    table_schema='mashan'
    and table_name = 'xisha100';

select data_length,index_length
    from tables where
    table_schema='mashan'
    and table_name = 'xisha1000';

select data_length,index_length
    from tables where
    table_schema='mashan'
    and table_name = 'xisha10000';

select data_length,index_length
    from tables where
    table_schema='mashan'
    and table_name = 'xisha100000';
