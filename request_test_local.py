try:
    import sys
    import json
    import types
    from apis.lead.get_lead import lambda_handler as get_lead_lambda_handler
    from apis.comparable.delete_compararable import lambda_handler as del_comp_lambda_handler
except ImportError as e_imp:
    print(f"The following import error ocurred: {e_imp}")

def pretty_print(func):
    def wrapper(endpoint):
        result = func(endpoint)
        result["body"] = json.loads(result["body"])
        result["endpoint_executed"] = endpoint
        pretty = json.dumps(result, indent=4)
        print(pretty)
    return wrapper

#get lead
@pretty_print
def get_lead(_):
    result = get_lead_lambda_handler(
        {
            "httpMethod": "GET",
            "queryStringParameters": {
                "nid": "9640486435",# CO:3532984603 MX: 9640486435
                "country": "MX", # MX, CO
            },
        },
        types.SimpleNamespace(),
    )
    return result

# drop comparable(delete_comparable)
@pretty_print
def delete_comparable(_):
    body_definition = {
        "object_list": [
            {"comparable_id": 52890, "reason": "out_median"},
            {"comparable_id": 52891, "reason": "high_coefficient"}
        ],
        "country": "MX", # MX, CO
        "property_deal_id": 1612,
    }
    parsed_body = json.dumps(body_definition)
    result = del_comp_lambda_handler(
        {
            "httpMethod": "POST",
            "body": parsed_body,
        },
        types.SimpleNamespace(),
    )
    return result

def invalid_arg(endpoint):
    print(f"El endpoint {endpoint} no existe")

func_dict = {
    "get_lead": get_lead,
    "delete_comparable": delete_comparable
}

if __name__ == "__main__":
    try:
        args_received = sys.argv[1:]
        # print(f"Argument received: {args_received}")
        if len(args_received) == 0:
            raise Exception("No arguments received")
        else:
            for functions in args_received:
                func_dict.get(functions, invalid_arg)(functions)
    except Exception as ex:
        print(f"The following error ocurred: {ex}")

# Dentro de la carpeta globack_utils/db/config/config.py poner credenciales para DEV
# Para ejecutar desde terminal poner algo como: python request_test_local.py get_lead
#                                               python request_test_local.py delete_comparable
# Y así sucesivamente agregando cada función para ejecutar un endpoint