import json

def format_terms(key_terms_str: str):
    res = ""
    try:
        key_terms_str = key_terms_str.strip()
        start_index = key_terms_str.find("{")
        end_index = key_terms_str.rfind("}") + 1
        terms_dict = json.loads(key_terms_str[start_index:end_index])

        for i in range(1, 7):
            temp = f'{i}. {terms_dict[f'term{i}']}: {terms_dict[f'explanation{i}']}'
            res = res + temp + "\n"

        print(res)
        return res
    except Exception as e:
        print(f"Error occured: {e}")
        return 0