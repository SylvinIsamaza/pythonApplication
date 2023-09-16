import json


data="""
[
{
id:'49390',
name:"Isamaza",
age:29
},
{
id:'49338',
name:"Sylvain",
age:30
}
]"""

info=json.loads(data)
for info in info:
    print('Name',info['Name'])