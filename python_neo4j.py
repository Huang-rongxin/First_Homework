#coding=utf-8
from py2neo import Node,Relationship,Graph
from pandas import DataFrame
graph=Graph("http://localhost:7474",username="neo4j",password="12345")

node_1=Node('Person',name="黄容鑫",age="20",sex="男",id="1715080119")
node_2=Node('Person',name="庞家俊",age="21",sex="男",id="1715080117")
node_3=Node('Person',name="李维杰",age="20",sex="男",id="1715080113")
node_4=Node('Person',name="吴欢",age="20",sex="男",id="1715080112")
node_5=Node('Person',name="张琳",age="19",sex="女",id="1715080111")
node_6=Node('Person',name="吴诗玥",age="22",sex="女",id="1515080117")
node_7=Node('Person',name="黄伟刚",age="20",sex="男",id="1715080108")
node_8=Node('Person',name="覃晓",age="18",sex="女")
node_9=Node('Person',name="刘旭鹏",age="17",sex="男",id="1815080117")
node_10=Node('Person',name="王党强",age="22",sex="男",id="1515080117")

r1=Relationship(node_1,'舍友',node_2)
r2=Relationship(node_1,'同学',node_3)
r3=Relationship(node_1,'同学',node_4)
r4=Relationship(node_1,'同学',node_7)
r5=Relationship(node_1,'师弟',node_10)
r6=Relationship(node_4,'情侣',node_5)
r7=Relationship(node_9,'学弟',node_3)
r8=Relationship(node_6,'助班',node_1)
r9=Relationship(node_6,'助班',node_2)
r10=Relationship(node_6,'助班',node_3)
r11=Relationship(node_6,'助班',node_4)
r12=Relationship(node_6,'助班',node_7)
r13=Relationship(node_8,'班主任',node_1)
r14=Relationship(node_8,'班主任',node_2)
r15=Relationship(node_8,'班主任',node_3)
r16=Relationship(node_8,'班主任',node_4)
r17=Relationship(node_8,'班主任',node_7)

S=node_1|node_2|node_3|node_4|node_5|node_6|node_7|node_8|node_9|node_10
s=r1|r2|r3|r4|r5|r6|r7|r8|r9|r10|r11|r12|r13|r14|r1|r15|r16|r17
graph.create(S)
graph.create(s)
A = graph.data("Match(female:Person) where female.sex = '女' return female")
print("\t查询数据库中的女性信息:")
for a in A:
    print(a)

B = graph.data("MATCH(n:Person)-[:班主任]->(student:Person) return student")
print("\n\t输出覃老师的学生信息:")
for b in B:
    print(b)

node = graph.find_one(label='Person', property_key='name', property_value="覃晓")
node['age'] =30
graph.push(node)
Data = graph.find_one(label='Person',property_key='name', property_value="覃晓")
print("\n\t输出覃老师修改后的信息:")
print(Data)

#删除刘旭鹏的个人信息以及关系
graph.run('MATCH (p:Person{name:"刘旭鹏"})-[r]-() detach delete r,p ')