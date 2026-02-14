import json

# Python data
p_data = {
    "x": True,
    "y": False,
    "z": None
}

# # Python → JSON
j_data = json.dumps(p_data)

print(j_data)
print(type(j_data))

# j_data={"x":true,"y":false,"z":null}
# p_data=json.loads(j_data)
# print(p_data)