import pickle
data=[1,2,3,4,5]
print(type(data))
# <class 'list'>

# pickling of data 

pickled_data=pickle.dumps(data)
print(pickled_data)
print(type(pickled_data))
# b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.'
# <class 'bytes'>

# unpickling of data

unpickled_data=pickle.loads(pickled_data)
print(unpickled_data)
print(type(unpickled_data))
# [1, 2, 3, 4, 5]
# <class 'list'>


dump_data={
    "name":"Kishan",
    "age":24,
    "degree":"B.E",
    "stream":"CSE",
}

try:
    with open ("Advance\JSON_Pickle\student.pkl","wb") as fh:
        if fh.writable():
            pickle.dump(dump_data,fh)    
            print("data is dumped")
# op: data is dumped
except Exception as e:
    print(e)

try:
    with open ("Advance\JSON_Pickle\student.pkl","rb") as fh:
        if fh.readable():
            new_data=pickle.load(fh)  
            print(new_data)  
except Exception as e:
    pass
# op:{'name': 'Kishan', 'age': 24, 'degree': 'B.E', 'stream': 'CSE'}