create database mashan
use mashan
create table xisha (
	record_id bigint not null identity(1,1),
	record_timestamp datetime,
	machineNo int,
	PRIMARY KEY ( record_id ))
