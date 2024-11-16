import json

def parse_response(response):
    # print("preproccessd response: ", response, "\n~~~~~~~~~~~~~\n")
    response = response.strip()
    start_index = response.find("{")
    end_index = response.rfind("]") + 1
    # print("area around end index: ", response[end_index-5:end_index], "\n~~~~~~~~~~~\n")
    response = response[start_index:end_index] + "}"
    response_dict = json.loads(response) 
    # print("processeed respons: ", response_dict)
    summary = response_dict["summary"]
    terms_as_string = ""
    i = 1
    for item in response_dict["key_terms"]:
        terms_as_string += (f"{i}. {item['term']}: {item['explanation']}\n")
        i += 1
    
    return summary, terms_as_string