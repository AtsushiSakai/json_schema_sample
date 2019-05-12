""" 

json schema validate sample

author: Atsushi Sakai

"""

from jsonschema import validate
import json


def main():
    print("start!!")

    f = open("sample.json")
    jsond = json.load(f)
    f.close()
    print("JSON data:")
    print(jsond)

    f = open("json.schema")
    schema = json.load(f)
    f.close()

    print("JSON schema:")
    print(schema)


    validate(instance=jsond, schema=schema)

    validate(instance={"name" : "Eggs", "price" : 34.99}, schema=schema)


    print("done!!")


if __name__ == '__main__':
    main()

