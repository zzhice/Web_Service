import pyowm

import xml.etree.cElementTree as ET


def call_weather(api_key, location="Dearborn"):
    owm = pyowm.OWM(api_key)

    observation = owm.weather_at_place(location+', US')
    w = observation.get_weather()
    w = w.to_XML(xml_declaration=True, xmlns=False)
    print(w)
    root = ET.fromstring(w)
    status = root.find('detailed_status')
    return "Current weather in "+location+": "+status.text
    # print(root)
    # for child in root:
    #     if not child.text:
    #         child.text = "None"
    #     print(child.tag+": "+child.text)


