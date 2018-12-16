from day33.database import MysqldbHelper
def excute_limit(page_id,is_next):
    helper=MysqldbHelper()
    if is_next:
        sql='select * from tb1 where id > %s limit 10'

    else:
        sql='select * from tb1 where id<%s order by id desc limit 10'
    result=helper.executeSelect ( sql, (page_id), rtype='dict' )
    helper.close()
    return result



pre_id=0
last_id=0

while True:
    num=input("1:下一页;2.上一页")
    if num=='1':
        is_next=True
        ret=excute_limit(last_id,is_next)
    elif num=='2':
        is_next=False
        ret=list(reversed(excute_limit(pre_id,is_next)))
    pre_id=ret[0]['id']
    last_id=ret[-1]['id']
    for i in ret:
        print(i)

