# test_create_model_from_dict.py

from models.base_model import BaseModel

# Create a dictionary representation of a BaseModel instance
base_model_dict = {
    'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
    'created_at': '2017-09-28T21:03:54.052298',
    '__class__': 'BaseModel',
    'my_number': 89,
    'updated_at': '2017-09-28T21:03:54.052302',
    'name': 'My_First_Model'
}

# Create a new BaseModel instance from the dictionary
new_base_model = BaseModel.from_dict(base_model_dict)

# Print the new BaseModel instance
print(new_base_model)

