# ES-for-data-provenance-of-spinning

这是《纺织学报》在投论文《基于Elasticsearch的纺纱生产数据追溯方法》中的实验数据和相关代码的配套仓库。

### 目录结构
1. data文件夹：这里存放的是Elasticsearch和MySQL实现数据追溯在存储性能上的结果；
   1. JWF1562_origin:该文件夹下存放的是原始纺纱数据的内存占用结果；
      1. MySQL
         1. JWF1562.csv：这是从纺纱现场采集的原始细纱数据，JWF1562是该系列设备的型号；
         2. create_table.sql：该sql脚本的作用是在MySQL数据库中构建表结构，或者说设计表；
         3. import_mysql.py：该Python脚本的作用是将JWF1562.csv中的原始数据导入到create_table.sql构建的数据表中；
         4. size_store.sql：该sql脚本的作用是得到各数据表在MySQL的内存占用结果。
      2. CSV
         1. export_data.sql：从MySQL中导出相关数据的脚本；
         2. xisha1.csv：1个数据，从属性中查看内存占用；
         3. xisha10.csv：10个数据；
         4. xisha100.csv：100个数据；
         5. xisha1000.csv：1000个数据；
         6. xisha10000.csv：10000个数据；
         7. xisha100000.csv：100000个数据。
      3. Elasticsearch
         1. csv2json.py：将CSV中的6个数据文件转换为JSON文件，对应下面几个文件；
         2. xisha1.json；
         3. xisha10.json；
         4. xisha100.json；
         5. xisha1000.json；
         6. xisha10000.json；
         7. xisha100000.json；
         8. import_xisha.py：将xisha1.json~xisha10000.json批量导入到Elasticsearch；
         9. import_xisha100000.py：将xisha100000.json导入到Elasticsearch；
         10. size_store.png：内存占用截图。
   2. JWF1562_label：该文件夹下存放的是按照论文中提到的方法在原始纺纱数据中添加标识后并存储的内存占用结果。
      1. MySQL：数据表方法
         1. create_table.sql:创建表或设计表；
         2. import_mysql.py：导入数据（带标识数据）；
         3. size_store.sql：得到内存占用情况；
         4. label_1_2_3_4_5.png ， label_6_7_8_9_10.png ，label_11_12.png ：实验结果截图。
      2. MySQL2：关联表方法
         1. JWF1418.csv：原始粗纱数据；
         2. create_table_before.sql：设计粗纱的表结构；
         3. create_table_join.sql：设计关联表的表结构；
         4. import_mysql_before.py：导入粗纱数据；
         5. import_mysql_join.py：简历粗纱和细纱的关联；
         6. size_store.sql：得到内存占用情况；
         6. size_stroe_1_to_4.png，size_stroe_5_to_8.png ，size_stroe_9_to_12.png ：这只是关联表的内存占用结果，进行比对还应该加上原始数据在MySQL的内存占用，否则会得到错误的实验结果。
      3. Elasticsearch:
         1. csv2json.py ：数据转换；
         2. import_xisha.py ：数据存储；
         3. label_1_to_8.png，label_9_to_12.png ：实验结果。
