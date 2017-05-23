import time
import json
from rest_framework import renderers

from hl7apy.parser import Message, parse_message

# TODO Understand hl7 better and make more dynamic

class Hl7Renderer(renderers.BaseRenderer):
    media_type = 'text/plain'
    format = 'hl7'

    def render(self, data, media_type=None, renderer_context=None):
        '''Renders hl7 ADT_A20 Bed Status Updates'''
        msgs = []
        if type(data) == list:
            for d in data:
                m = Message("ADT_A20")
                m.add_segment('MSH')
                m.msh.msh_7 = time.strftime("%Y%m%d") # date?

                # http://hl7-definition.caristix.com:9010/Default.aspx?version=HL7%20v2.5.1&segment=NPU

                if "room" in d and "status" in d:
                    m.add_segment('NPU')
                    m.npu.npu_1 = d["room"] # location
                    m.npu.npu_2 = d["status"] # status

                # http://hl7-definition.caristix.com:9010/Default.aspx?version=HL7%20v2.5.1&segment=NTE
                m.add_segment('NTE')
                m.nte.nte_2 = "open bed management" # Source of Comment
                m.nte.nte_3 = json.dumps(d) # Comment
                m.nte.nte_4 = "json" # Comment Type

                msgs.append(m.to_er7())
        else:
            m = Message("ADT_A20")
            m.add_segment('NTE')
            m.nte.nte_2 = "open bed management" # Source of Comment
            m.nte.nte_3 = json.dumps(data) # Comment
            m.nte.nte_4 = "json" # Comment Type
            msgs.append(m.to_er7())
        return "\n".join(msgs)

