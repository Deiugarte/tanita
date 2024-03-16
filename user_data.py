from tanita_measures_parser import get_data_frame
from mapping import headerMapping


def get_user_info(user_id: int):
    data = get_data_frame(user_id)
    name = "Deivid" if user_id == 1 else "Yelba" 
    return {
        "name": name,
        "age": data.get(headerMapping["AG"])[0],
        "gender": "Male" if data.get(headerMapping["GE"])[0] == "1" else "Female",
        "height": data.get(headerMapping["Hm"])[0],
        "weight": data.get(headerMapping["Wk"])[0],
        "metabolicAge": data.get(headerMapping["rA"])[0],
    }


def get_body_composition_data(user_id: int):
    data = get_data_frame(user_id)
    return {
        "bodyFat": data.get(headerMapping["FW"])[0],
        "globalMuscle": data.get(headerMapping["mW"])[0],
        "bodyMassIndex": data.get(headerMapping["MI"])[0],
        "boneMass": data.get(headerMapping["bW"])[0],
        "visceralFatLevel": data.get(headerMapping["IF"])[0],
        "globalWater": data.get(headerMapping["ww"])[0],
        "dailyCaloryIntake": data.get(headerMapping["rD"])[0],
    }


def get_segment_data(user_id: int):
    data = get_data_frame(user_id)
    return [
        {
            "segment": "Left Arm",
            "fatMass": data.get(headerMapping["Fl"])[0],
            "leanBodyMass": data.get(headerMapping["ml"])[0],
        },
        {
            "segment": "Right Arm",
            "fatMass": data.get(headerMapping["Fr"])[0],
            "leanBodyMass": data.get(headerMapping["mr"])[0],
        },
        {
            "segment": "Trunk",
            "fatMass": data.get(headerMapping["FT"])[0],
            "leanBodyMass": data.get(headerMapping["mT"])[0],
        },
        {
            "segment": "Left Leg",
            "fatMass": data.get(headerMapping["FL"])[0],
            "leanBodyMass": data.get(headerMapping["mL"])[0],
        },
        {
            "segment": "Right Leg",
            "fatMass": data.get(headerMapping["FR"])[0],
            "leanBodyMass": data.get(headerMapping["mR"])[0],
        },
    ]


def get_historical_data(user_id: int, data_type: str):
    data = get_data_frame(user_id)
    result = []
    for index, row in data.iterrows():
      date = row[headerMapping["DT"]] + row[headerMapping["Ti"]]
      result.append({ "date": date , "value": row[headerMapping[data_type]]})
    result.reverse()
    return result
