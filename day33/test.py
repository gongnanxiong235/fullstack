# author:gongnanxiong
# date:2018/12/13

from day33.database import MysqldbHelper

helper=MysqldbHelper()
print('host:',helper.host)
# result=helper.executeSql('select * from user',rtype='dict')
# print(result)

result=helper.executeSql('select * from user where id=%s',(1),rtype='dict')
print(result)

ddd=helper.executeInsert('insert into user (`name`,age,dp_id) values(%s,%s,%s)',('dddfdfdf',30,111))
print(ddd)
