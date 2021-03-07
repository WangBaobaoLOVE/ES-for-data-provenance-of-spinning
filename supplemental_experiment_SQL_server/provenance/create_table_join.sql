create table b2s1 (record_id_bingtiao bigint not null,record_id_shumian bigint not null,foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id),foreign key(record_id_shumian) references JWF1211_shumuan(record_id));
# 参考多对多关系：https://www.cnblogs.com/wjw1014/p/10851218.html

create table b2s2 (record_id_bingtiao bigint not null,record_id_shumian bigint not null,foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id),foreign key(record_id_shumian) references JWF1211_shumuan(record_id));

create table b2s3 (record_id_bingtiao bigint not null,record_id_shumian bigint not null,foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id),foreign key(record_id_shumian) references JWF1211_shumuan(record_id));

create table b2s4 (record_id_bingtiao bigint not null,record_id_shumian bigint not null,foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id),foreign key(record_id_shumian) references JWF1211_shumuan(record_id));

create table b2s5 (record_id_bingtiao bigint not null,record_id_shumian bigint not null,foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id),foreign key(record_id_shumian) references JWF1211_shumuan(record_id));

create table b2s6 (record_id_bingtiao bigint not null,record_id_shumian bigint not null,foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id),foreign key(record_id_shumian) references JWF1211_shumuan(record_id));


create table c2b1 (record_id_cusha bigint not null,record_id_bingtiao bigint not null,foreign key(record_id_cusha) references JWF1418_cusha(record_id),foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id));

create table c2b2 (record_id_cusha bigint not null,record_id_bingtiao bigint not null,foreign key(record_id_cusha) references JWF1418_cusha(record_id),foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id));

create table c2b3 (record_id_cusha bigint not null,record_id_bingtiao bigint not null,foreign key(record_id_cusha) references JWF1418_cusha(record_id),foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id));

create table c2b4 (record_id_cusha bigint not null,record_id_bingtiao bigint not null,foreign key(record_id_cusha) references JWF1418_cusha(record_id),foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id));

create table c2b5 (record_id_cusha bigint not null,record_id_bingtiao bigint not null,foreign key(record_id_cusha) references JWF1418_cusha(record_id),foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id));

create table c2b6 (record_id_cusha bigint not null,record_id_bingtiao bigint not null,foreign key(record_id_cusha) references JWF1418_cusha(record_id),foreign key(record_id_bingtiao) references JWF1312B_bingtiao(record_id));

create table x2tc1 (record_id_xisha bigint not null,record_id_cusha bigint not null,foreign key(record_id_xisha) references JWF1562_xisha(record_id),foreign key(record_id_cusha) references JWF1418_cusha(record_id));

create table x2tc2 (record_id_xisha bigint not null,record_id_cusha bigint not null,foreign key(record_id_xisha) references JWF1562_xisha(record_id),foreign key(record_id_cusha) references JWF1418_cusha(record_id));

create table x2tc3 (record_id_xisha bigint not null,record_id_cusha bigint not null,foreign key(record_id_xisha) references JWF1562_xisha(record_id),foreign key(record_id_cusha) references JWF1418_cusha(record_id));

create table x2tc4 (record_id_xisha bigint not null,record_id_cusha bigint not null,foreign key(record_id_xisha) references JWF1562_xisha(record_id),foreign key(record_id_cusha) references JWF1418_cusha(record_id));

create table x2tc5 (record_id_xisha bigint not null,record_id_cusha bigint not null,foreign key(record_id_xisha) references JWF1562_xisha(record_id),foreign key(record_id_cusha) references JWF1418_cusha(record_id));

create table x2tc6 (record_id_xisha bigint not null,record_id_cusha bigint not null,foreign key(record_id_xisha) references JWF1562_xisha(record_id),foreign key(record_id_cusha) references JWF1418_cusha(record_id));

create table l2x1 (record_id_luotong bigint not null,record_id_xisha bigint not null,foreign key(record_id_luotong) references SMARO_E_luotong(record_id),foreign key(record_id_xisha) references JWF1562_xisha(record_id));

create table l2x2 (record_id_luotong bigint not null,record_id_xisha bigint not null,foreign key(record_id_luotong) references SMARO_E_luotong(record_id),foreign key(record_id_xisha) references JWF1562_xisha(record_id));

create table l2x3 (record_id_luotong bigint not null,record_id_xisha bigint not null,foreign key(record_id_luotong) references SMARO_E_luotong(record_id),foreign key(record_id_xisha) references JWF1562_xisha(record_id));

create table l2x4 (record_id_luotong bigint not null,record_id_xisha bigint not null,foreign key(record_id_luotong) references SMARO_E_luotong(record_id),foreign key(record_id_xisha) references JWF1562_xisha(record_id));

create table l2x5 (record_id_luotong bigint not null,record_id_xisha bigint not null,foreign key(record_id_luotong) references SMARO_E_luotong(record_id),foreign key(record_id_xisha) references JWF1562_xisha(record_id));

create table l2x6 (record_id_luotong bigint not null,record_id_xisha bigint not null,foreign key(record_id_luotong) references SMARO_E_luotong(record_id),foreign key(record_id_xisha) references JWF1562_xisha(record_id));
