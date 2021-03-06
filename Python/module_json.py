# #dict
# person={"name":"Fazlıhan","languages":["Python","C#"]}
# print(person["languages"][0])

import json
person_str='{"name":"Fazlıhan","languages":["Python","C#"]}'    #json da dict'ler string halinde olur.





# JSON string to Dict
result=json.loads(person_str)

# result=result["name"]
result=result["languages"][0]

# with open("islem.json") as f:
#     data = json.load(f)
#     print(data)
#     print(data["name"])
#     print(data["languages"])






# Dict to JSON string

person_dict={
    "name" : "Fazlıhan",
    "languages" : ["Python","PHP"] }

result=json.dumps(person_dict)


with open("islem.json","w",encoding="utf-8") as f:
    json.dump(person_dict,f)


person_dict=json.loads(person_str)

result=json.dumps(person_dict, indent=4, sort_keys=False)







print(person_dict)
print(result)