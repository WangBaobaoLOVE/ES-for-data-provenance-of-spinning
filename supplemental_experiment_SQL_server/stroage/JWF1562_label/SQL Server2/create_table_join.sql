create database mashan;
use mashan;
create table cusha_to_xisha1 (record_id_xisha bigint not null,record_id_cusha bigint not null,foreign key (record_id_xisha) references xisha10000(record_id),foreign key(record_id_cusha) references cusha(record_id));
# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html

create table cusha_to_xisha2 (record_id_xisha bigint not null,record_id_cusha bigint not null,foreign key (record_id_xisha) references xisha10000(record_id),foreign key(record_id_cusha) references cusha(record_id));

create table cusha_to_xisha3 (record_id_xisha bigint not null,record_id_cusha bigint not null,foreign key (record_id_xisha) references xisha10000(record_id),foreign key(record_id_cusha) references cusha(record_id));

create table cusha_to_xisha4 (record_id_xisha bigint not null,record_id_cusha bigint not null,foreign key (record_id_xisha) references xisha10000(record_id),foreign key(record_id_cusha) references cusha(record_id));

create table cusha_to_xisha5 (record_id_xisha bigint not null,record_id_cusha bigint not null,foreign key (record_id_xisha) references xisha10000(record_id),foreign key(record_id_cusha) references cusha(record_id));

create table cusha_to_xisha6 (record_id_xisha bigint not null,record_id_cusha bigint not null,foreign key (record_id_xisha) references xisha10000(record_id),foreign key(record_id_cusha) references cusha(record_id));

create table cusha_to_xisha7 (record_id_xisha bigint not null,record_id_cusha bigint not null,foreign key (record_id_xisha) references xisha10000(record_id),foreign key(record_id_cusha) references cusha(record_id));

create table cusha_to_xisha8 (record_id_xisha bigint not null,record_id_cusha bigint not null,foreign key (record_id_xisha) references xisha10000(record_id),foreign key(record_id_cusha) references cusha(record_id));

create table cusha_to_xisha9 (record_id_xisha bigint not null,record_id_cusha bigint not null,foreign key (record_id_xisha) references xisha10000(record_id),foreign key(record_id_cusha) references cusha(record_id));

create table cusha_to_xisha10 (record_id_xisha bigint not null,record_id_cusha bigint not null,foreign key (record_id_xisha) references xisha10000(record_id),foreign key(record_id_cusha) references cusha(record_id));

create table cusha_to_xisha11 (record_id_xisha bigint not null,record_id_cusha bigint not null,foreign key (record_id_xisha) references xisha10000(record_id),foreign key(record_id_cusha) references cusha(record_id));

create table cusha_to_xisha12 (record_id_xisha bigint not null,record_id_cusha bigint not null,foreign key (record_id_xisha) references xisha10000(record_id),foreign key(record_id_cusha) references cusha(record_id));

