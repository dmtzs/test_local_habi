try:
    import sys
    import json
    import types
    import traceback
    # from test_local_const import *
    from apis.lead.get_lead import lambda_handler as get_lead_lambda_handler
    from apis.lead.get_leads import lambda_handler as get_leads_lambda_handler
    from apis.lead.get_leads_by_nid import lambda_handler as get_leads_by_nid_lambda_handler
    from apis.city.get_city_list import lambda_handler as get_city_list_lambda_handler
    from apis.lead.get_calculations import lambda_handler as get_calculations_lambda_handler
    from apis.comparable.delete_compararable import lambda_handler as del_comp_lambda_handler
    from apis.lead.get_leads_filters import lambda_handler as get_leads_filters_lambda_handler
    from apis.lead.get_historic_leads import lambda_handler as get_historic_leads_lambda_handler
    from apis.comparable.get_comparables import lambda_handler as get_comparables_lambda_handler
    from apis.lead.post_status_pricing import lambda_handler as post_status_pricing_lambda_handler
    from apis.historical_polygon.get_historical_polygon import lambda_handler as get_historical_polygon_lambda_handler
except ImportError as e_imp:
    print(f"The following import error ocurred: {e_imp}")

def pretty_print(func):
    def wrapper(endpoint):
        result = func(endpoint)
        print(f"type of result: {type(result)}")
        print(f"result: {result}")
        print(f"result: {result['body']}")
        result["body"] = json.loads(result["body"])
        result["endpoint_executed"] = endpoint
        pretty = json.dumps(result, indent=4)
        print(pretty)
    return wrapper

# get historical polygon
@pretty_print
def get_historical_polygon(_):
    result = get_historical_polygon_lambda_handler(
        {
            "httpMethod": "GET",
            "queryStringParameters": {
                "country": "MX",
                "property_deal_id": "53906",
            },
        },
        types.SimpleNamespace(),
    )
    return result

# get lead
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

# get leads
@pretty_print
def get_leads(_):
    result = get_leads_lambda_handler(
        {
            "httpMethod": "GET",
            "queryStringParameters": {
                #"nid": "9125994861",
                "country": "CO",
                #"city":"1,",
                #"limit":"1",
                "page": "0",
                #"baths": "1",
                #"half_baths":"2"
                #"elevator": "1",
                #"antiquity": "10",
                #"garages": "2",
                #"rooms": "3",
                #"waiting_time": "48",
                "pricing_status": "pending",
                #"source_id": "1,",
                #"agent": "7,2,",
                "date_create_min": "2022-06-06",
                "date_create_max": "2022-06-16",
                "filter": "initial_pricing"
            },
        },
        types.SimpleNamespace(),
    )
    return result

# get comparable
# Fechas de información
# Baños y recámaras
@pretty_print
def get_comparables(_):
    result = get_comparables_lambda_handler(
        {
            "httpMethod": "GET",
            "queryStringParameters": {
                "nid": "10638433904",
                "country": "MX",
                "from_date_create": "6",
                "property_type_id": "2",
                "baths": "3",
                "rooms": "3",
                "elevator": "0",
                "garage": "0",
                "area_min": "22",
                "area_max": "42",
                "price_per_m2_min": "0",
                "price_per_m2_max": "100000",
                "years_old_min": "24",
                "years_old_max": "40",
                "radius": 1,
                "scale": "km",
                "appraisal_date": "2022,2021,2020,2019"
                #"latitude":19.3479,
                #"longitude":-99.124,
                # "elevator":1,
                # "garage_number":1,
                #"meters": 1000,
                # "ask_price": 2750000,
                # "area":73,
                # "years_old": 2,
                # "diff_years": 3,
                # "property_type_id":1,
                #"area": 73,
            },
        },
        types.SimpleNamespace(),
    )
    return result

# #get lead
# @pretty_print
# def get_lead2(_):
#     for to_test in get_lead_const:
#         result = get_lead_lambda_handler(
#             {
#                 "httpMethod": "GET",
#                 "queryStringParameters": to_test,
#             },
#             types.SimpleNamespace(),
#         )
#         return result

# Put pricing status (status=progress)
@pretty_print
def put_pricing_status_progress(_):
    req_post_pricing_status = {
    "id": "1142091",
    "agent": "sebastian@mail.com",
    "status": 'progress',
    "country": "CO",
    "price_type": "initial_pricing"
    }

    result = post_status_pricing_lambda_handler(
        {
            "httpMethod": "POST",
            "body": json.dumps(req_post_pricing_status)
        },
        types.SimpleNamespace(),
    )
    return result

# Put pricing status (status=aborted)
@pretty_print
def put_pricing_status_aborted(_):
    req_post_pricing_status = {
      "id": "45390",
      "agent": "seba@mail.com,",
      "status": 'aborted',
      "country": "MX"
      }

    result = post_status_pricing_lambda_handler(
        {
            "httpMethod": "POST",
            "body": json.dumps(req_post_pricing_status)
        },
        types.SimpleNamespace(),
    )
    return result

# Put pricing status (status=completed)
@pretty_print
def put_pricing_status_completed(_):
    req_post_pricing_status = {
    "id": "1142091",
    "agent": "sebastian@mail.com",
    "status": 'completed',
    "country": "CO",
    #   "no_price_reason": "no_habi",
    #   "no_price_reason_detail": "descartado_por_antiguedad",
    "price": "100000000",
    "price_type": "initial_pricing",
    "comment": "prueba 22/09"
    }

    result = post_status_pricing_lambda_handler(
        {
            "httpMethod": "POST",
            "body": json.dumps(req_post_pricing_status)
        },
        types.SimpleNamespace(),
    )
    return result

#get historic leads
@pretty_print
def get_historic_leads(_):
    result = get_historic_leads_lambda_handler(
        {
            "httpMethod": "GET",
            "queryStringParameters": {
                "country": "MX",
                "limit":"5",
                "page": "0",
                "date_create_min": "2022-04-15",
                "date_create_max": "2022-04-15",
                #"pricing_phases": "initial_pricing",
                #"avg_customer_service": "avg_1,",
                "baths": "3",
                #"half_baths": "2",
                #"rooms": "4",
                "garages": "3",
                #"elevator": "2",
                #"no_price_reason_no_pricing": "coeficiente_elevado",
                #"no_price_reason_no_habi": "descartado_por_precio_elevado,sin_zona_mediana",
                # "min_price": "888888",
                # "max_price": "999999",
                #"agent": "4,5,6,7,8,9,10",
                #"source_id": "1,3,31",
                #"city": "15081",
                #"antiquity": "10"
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

# Get cities
@pretty_print
def get_cities(_):
    result = get_city_list_lambda_handler(
        {
            "httpMethod": "GET",
            "queryStringParameters": {
                "country": "MX",
                "name":"cuau"
            },
        },
        types.SimpleNamespace(),
    )
    return result

# Get filters
@pretty_print
def get_filters(_):
    result = get_leads_filters_lambda_handler(
        {
            "httpMethod": "GET",
            "queryStringParameters": {
                "country": "MX"
            },
        },
        types.SimpleNamespace(),
    )
    return result

# get calculations
@pretty_print
def get_calculations(_):
    result = get_calculations_lambda_handler(
        {
            "httpMethod": "GET",
            "queryStringParameters": {
                # "nid": "9116208157",# CO que trae porcentje de venta: 1601644232
                # "country": "CO",
                # "list_comparables_id": "1746153,2579995,1879652,841383,2201032,564209,1459495,2145130,2511836,1770440,445404",
                ###
                "nid": "10196481172",#7267296544, 9132001171
                "country": "MX",
                "list_comparables_id": "5557584,5524642,2115717", #"1153551,1877524,1958268,2102831,2250490,2299287"

                # "nid": "10517355807",
                # "country": "MX",
                # "list_comparables_id": "6233490,6584479,4484462,4230553,4879105,7712093,196670,5419635,7736484,3860729,1319290,4771617,7713326",
                # "manual_percentile": "23"
            },
        },
        types.SimpleNamespace(),
    )
    return result

def invalid_arg(endpoint):
    print(f"El endpoint {endpoint} no existe")

func_dict = {
    "get_lead": get_lead,
    "get_comparables": get_comparables,
    "get_leads": get_leads,
    "put_pricing_status_progress": put_pricing_status_progress,
    "put_pricing_status_aborted": put_pricing_status_aborted,
    "put_pricing_status_completed": put_pricing_status_completed,
    "get_historic_leads": get_historic_leads,
    "delete_comparable": delete_comparable,
    "get_cities": get_cities,
    "get_filters": get_filters,
    "get_calculations": get_calculations,
    "get_historical_polygon": get_historical_polygon
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
    except Exception:
        print(f"The following error ocurred: {traceback.format_exc()}")

# Dentro de la carpeta globack_utils/db/config/config.py poner credenciales para DEV
# Para ejecutar desde terminal poner algo como: python request_test_local.py get_lead
#                                               python request_test_local.py delete_comparable
# Y así sucesivamente agregando cada función para ejecutar un endpoint