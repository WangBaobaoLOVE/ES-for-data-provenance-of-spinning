create database mashan;
use mashan;
create table b2s1 (	
	record_id_bingtiao bigint not null,
	record_id_shumian bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table b2s1 add foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id);
alter table b2s1 add foreign key(record_id_shumian) references JWF1211_shumuan(record_id);

create table b2s2 (	
	record_id_bingtiao bigint not null,
	record_id_shumian bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table b2s2 add foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id);
alter table b2s2 add foreign key(record_id_shumian) references JWF1211_shumuan(record_id);

create table b2s3(	
	record_id_bingtiao bigint not null,
	record_id_shumian bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table b2s3 add foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id);
alter table b2s3 add foreign key(record_id_shumian) references JWF1211_shumuan(record_id);

create table b2s4 (	
	record_id_bingtiao bigint not null,
	record_id_shumian bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table b2s4 add foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id);
alter table b2s4 add foreign key(record_id_shumian) references JWF1211_shumuan(record_id);

create table b2s5 (	
	record_id_bingtiao bigint not null,
	record_id_shumian bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table b2s5 add foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id);
alter table b2s5 add foreign key(record_id_shumian) references JWF1211_shumuan(record_id);

create table b2s6 (	
	record_id_bingtiao bigint not null,
	record_id_shumian bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table b2s6 add foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id);
alter table b2s6 add foreign key(record_id_shumian) references JWF1211_shumuan(record_id);

create table c2b1 (	
	record_id_cusha bigint not null,
	record_id_bingtiao bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table c2b1 add foreign key(record_id_cusha) references JWF1418_cusha(record_id);
alter table c2b1 add foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id);

create table c2b2 (	
	record_id_cusha bigint not null,
	record_id_bingtiao bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table c2b2 add foreign key(record_id_cusha) references JWF1418_cusha(record_id);
alter table c2b2 add foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id);

create table c2b3 (	
	record_id_cusha bigint not null,
	record_id_bingtiao bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table c2b3 add foreign key(record_id_cusha) references JWF1418_cusha(record_id);
alter table c2b3 add foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id);

create table c2b4 (	
	record_id_cusha bigint not null,
	record_id_bingtiao bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table c2b4 add foreign key(record_id_cusha) references JWF1418_cusha(record_id);
alter table c2b4 add foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id);

create table c2b5 (	
	record_id_cusha bigint not null,
	record_id_bingtiao bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table c2b5 add foreign key(record_id_cusha) references JWF1418_cusha(record_id);
alter table c2b5 add foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id);

create table c2b6 (	
	record_id_cusha bigint not null,
	record_id_bingtiao bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table c2b6 add foreign key(record_id_cusha) references JWF1418_cusha(record_id);
alter table c2b6 add foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id);

create table x2c1 (	
	record_id_xisha bigint not null,
	record_id_cusha bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table x2c1 add foreign key(record_id_xisha) references JWF1562_xisha(record_id);
alter table x2c1 add foreign key(record_id_cusha) references JWF1418_cusha(record_id);

create table x2c2 (	
	record_id_xisha bigint not null,
	record_id_cusha bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table x2c2 add foreign key(record_id_xisha) references JWF1562_xisha(record_id);
alter table x2c2 add foreign key(record_id_cusha) references JWF1418_cusha(record_id);

create table x2c3 (	
	record_id_xisha bigint not null,
	record_id_cusha bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table x2c3 add foreign key(record_id_xisha) references JWF1562_xisha(record_id);
alter table x2c3 add foreign key(record_id_cusha) references JWF1418_cusha(record_id);

create table x2c4 (	
	record_id_xisha bigint not null,
	record_id_cusha bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table x2c4 add foreign key(record_id_xisha) references JWF1562_xisha(record_id);
alter table x2c4 add foreign key(record_id_cusha) references JWF1418_cusha(record_id);

create table x2c5 (	
	record_id_xisha bigint not null,
	record_id_cusha bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table x2c5 add foreign key(record_id_xisha) references JWF1562_xisha(record_id);
alter table x2c5 add foreign key(record_id_cusha) references JWF1418_cusha(record_id);

create table x2c6 (	
	record_id_xisha bigint not null,
	record_id_cusha bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table x2c6 add foreign key(record_id_xisha) references JWF1562_xisha(record_id);
alter table x2c6 add foreign key(record_id_cusha) references JWF1418_cusha(record_id);

create table l2x1 (	
	record_id_luotong bigint not null,
	record_id_xisha bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table l2x1 add foreign key(record_id_luotong) references SMARO_E_luotong(record_id);
alter table l2x1 add foreign key(record_id_xisha) references JWF1562_xisha(record_id);

create table l2x2 (	
	record_id_luotong bigint not null,
	record_id_xisha bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table l2x2 add foreign key(record_id_luotong) references SMARO_E_luotong(record_id);
alter table l2x2 add foreign key(record_id_xisha) references JWF1562_xisha(record_id);

create table l2x3 (	
	record_id_luotong bigint not null,
	record_id_xisha bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table l2x3 add foreign key(record_id_luotong) references SMARO_E_luotong(record_id);
alter table l2x3 add foreign key(record_id_xisha) references JWF1562_xisha(record_id);

create table l2x4 (	
	record_id_luotong bigint not null,
	record_id_xisha bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table l2x4 add foreign key(record_id_luotong) references SMARO_E_luotong(record_id);
alter table l2x4 add foreign key(record_id_xisha) references JWF1562_xisha(record_id);

create table l2x5 (	
	record_id_luotong bigint not null,
	record_id_xisha bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table l2x5 add foreign key(record_id_luotong) references SMARO_E_luotong(record_id);
alter table l2x5 add foreign key(record_id_xisha) references JWF1562_xisha(record_id);

create table l2x6 (	
	record_id_luotong bigint not null,
	record_id_xisha bigint not null
);

# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html
alter table l2x6 add foreign key(record_id_luotong) references SMARO_E_luotong(record_id);
alter table l2x6 add foreign key(record_id_xisha) references JWF1562_xisha(record_id);
