import json 

data='{"one":1,"two":2,"three":3}'
print(type(data))
# <class 'str'>

new_data=json.loads(data)
print(type(new_data))
# <class 'dict'>
print(new_data)
# {'one': 1, 'two': 2, 'three': 3}

old_data=json.dumps(data)
print(type(old_data))
# <class 'str'>
print(old_data)
# "{\"one\":1,\"two\":2,\"three\":3}"

try: 
    with open("Advance\JSON_Pickle\info.json",'r') as f:
        if f.readable():
            load_data=json.load(f)
            for i,j in load_data.items():
                print(i ,"->", j)
# op:
# name -> Keerthana
# age -> 21
# address -> Chitradurga

except Exception as e:
    print(e) 

# op:[Errno 2] No such file or directory: 'info.json' - If file doesnt exist

load_data["person3"]={
    "name":"Kishan",
    "age":24,
    "degree":"B.E",
    "stream":"CSE",
}

try:
    with open ("Advance\JSON_Pickle\info.json","w") as fh:
        if fh.writable():
            json.dump(load_data,fh,indent=4)    
            print("data is dumped")
# data is dumped
except Exception as e:
    print(e)

 # indent is for spaces but When we use indent, Python automatically switches to 
 # pretty print mode, which includes new line