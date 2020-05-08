import jsonschema

schema = {
	"definitions": {},
	"$schema": "http://json-schema.org/draft-07/schema#",
	"$id": "https://example.com/object1588083106.json",
	"title": "Root",
	"type": "object",
	"required": [
		"title",
		"person"
	],
	"properties": {
		"title": {
			"$id": "#root/title",
			"title": "Title",
			"type": "string",
			"default": "",
			"examples": [
				"salam"
			],
			"pattern": "^.*$"
		},
		"person": {
			"$id": "#root/person",
			"title": "Person",
			"type": "array",
			"default": [],
			"items":{
				"$id": "#root/person/items",
				"title": "Items",
				"type": "object",
				"required": [
					"name",
					"age"
				],
				"properties": {
					"name": {
						"$id": "#root/person/items/name",
						"title": "Name",
						"type": "string",
						"default": "",
						"examples": [
							"ali"
						],
						"pattern": "^.*$"
					},
					"age": {
						"$id": "#root/person/items/age",
						"title": "Age",
						"type": "integer",
						"examples": [
							5
						],
						"default": 0
					}
				}
			}

		}
	},
	"additionalProperties": True
}


test = {
    "title": "salam",
    "person": [
        {
            "name": "fe",
            "age": 5
        },
        {
            "name": "fefe",
            "age": 5
        },
    ],
	"family":"asw",
}
#
# test = jsonschema.Draft7Validator(schema).validate(test)
test = jsonschema.Draft7Validator(schema).is_valid(test)
print(test)

# IN_BODY = 'body'  #:
# IN_PATH = 'path'  #:
# IN_QUERY = 'query'  #:
# IN_FORM = 'formData'  #:
# IN_HEADER = 'header'  #:

# test_param = openapi.Parameter('frfrfr', openapi.IN_BODY, description="test manual param", type=openapi.TYPE_STRING)
# @swagger_auto_schema(operation_description='POST /articles/today/',manual_parameters=[test_param],)
# @swagger_auto_schema(
#     operation_description="apiview post description override",
#     request_body=openapi.Schema(
#         type=openapi.TYPE_OBJECT,
#         required=['title','en_title','text','info'],
#         properties={
#             'title': openapi.Schema(type=openapi.TYPE_STRING),
#             'en_title': openapi.Schema(type=openapi.TYPE_STRING),
#             'text': openapi.Schema(type=openapi.TYPE_STRING),
#             'company_src': openapi.Schema(type=openapi.TYPE_INTEGER),
#             'info': openapi.Schema(type=openapi.TYPE_OBJECT)
#         },
#     ),
#     security=[]
# )