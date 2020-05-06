SCHMMA = {
    "definitions": {},
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "https://example.com/object1588756450.json",
    "title": "Root",
    "type": "object",
    "required": [
        "gender",
        "ability"
    ],
    "properties": {
        "gender": {
            "$id": "#root/gender",
            "title": "Gender",
            "type": "object",
            "required": [
                "id",
                "title"
            ],
            "properties": {
                "id": {
                    "$id": "#root/gender/id",
                    "title": "Id",
                    "type": "integer",
                    "examples": [
                        1
                    ],
                    "default": 0
                },
                "title": {
                    "$id": "#root/gender/title",
                    "title": "Title",
                    "type": "string",
                    "default": "",
                    "examples": [
                        "woman"
                    ],
                    "pattern": "^.*$"
                }
            }
        }
        ,
        "ability": {
            "$id": "#root/ability",
            "title": "Ability",
            "type": "array",
            "default": [],
            "items": {
                "$id": "#root/ability/items",
                "title": "Items",
                "type": "object",
                "required": [
                    "id",
                    "title"
                ],
                "properties": {
                    "id": {
                        "$id": "#root/ability/items/id",
                        "title": "Id",
                        "type": "integer",
                        "examples": [
                            1
                        ],
                        "default": 0
                    },
                    "title": {
                        "$id": "#root/ability/items/title",
                        "title": "Title",
                        "type": "string",
                        "default": "",
                        "examples": [
                            "barber"
                        ],
                        "pattern": "^.*$"
                    }
                }
            }

        }
    },
    "additionalProperties": True

}
