create database mashan;
use mashan;
create table cusha_to_xisha (	
	record_id_xisha bigint not null,
	record_id_cusha bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table cusha_to_xisha add foreign key(record_id_xisha) references xisha10000(record_id);
alter table cusha_to_xisha add foreign key(record_id_cusha) references cusha(record_id);
