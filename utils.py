import camelot
import json

def sanitize_personal_info(data):
    return {
        "name": data[0]["1"],
        "register_number": data[0]["3"],
        "college": data[1]["1"],
        "branch": data[1]["3"],
        "semester": data[2]["1"],
    }

def sanitize_result(data):
    res = []
    for data_point in data[1:-2]:
        x = {
            "course": data_point["0"],
            "code": data_point["1"],
            "grade": data_point["2"],
            "credits": data_point["3"],
        }
        res.append(x)
    return res


def handle_pdf(pdf_file):
    tables = camelot.read_pdf(pdf_file, flavor="lattice", strip_text="\n")

    personal_info = json.loads(tables[0].df.to_json(orient="records"))  
    personal_info = sanitize_personal_info(personal_info)

    result = json.loads(tables[1].df.to_json(orient="records"))
    result = sanitize_result(result)

    return {"personal_info": personal_info, "result": result}
