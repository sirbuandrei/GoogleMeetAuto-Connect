import re


class Meet(object):
    def __init__(self, meet_code, starting_hour, finishing_hour, connect_after):
        self.meet_code = meet_code
        self.connect_after = connect_after

        # GET THE STARTING HOUR
        if re.search(r'\A[1-9]', starting_hour.split(':')[0]):
            self.start_hour = re.findall(r'\A[1-9]', starting_hour.split(':')[0])[0]
        self.start_hour += starting_hour[1]

        # GET THE STARTING MINUTE
        if re.search(r'\A[1-9]', starting_hour.split(':')[1]):
            self.start_min = re.findall(r'\A[1-9]', starting_hour.split(':')[1])[0]
        self.start_min += starting_hour[4]

        # GET THE FINISHING HOUR
        if re.search(r'\A[1-9]', finishing_hour.split(':')[0]):
            self.finish_hour = re.findall(r'\A[1-9]', finishing_hour.split(':')[0])[0]
        self.finish_hour += finishing_hour[1]

        # GET THE FINISHING MINUTE
        if re.search(r'\A[1-9]', finishing_hour.split(':')[1]):
            self.finish_min = re.findall(r'\A[1-9]', finishing_hour.split(':')[1])[0]
        self.finish_min += finishing_hour[4]


timetable = [['Monday', Meet('gea2wmsrk', '8:00', '9:45', 1), Meet('b3m3ury3c4', '10:00', '11:45', 1),
              Meet('cd2ztlzdtn', '12:00', '12:45', 1)],
             ['Tuesday', Meet('cj7753rg53', '8:00', '9:50', 1), Meet('gbxpkdxham', '10:00', '10:45', 1),
              Meet('gqcva4vb4i', '11:00', '11:45', 1), Meet('btiw6ocvpw', '12:00', '12:45', 1)],
             ['Wednesday ', Meet('b3m3ury3c4', '8:00', '10:45', 1), Meet('cganb4td5m', '11:00', '13:45', 1)],
             ['Thursday', Meet('hxqctw6jss', '8:30', '9:00', 1), Meet('fgq2a4dosj', '9:00', '9:30', 1),
              Meet('abu-hzbn-ocp', '9:30', '10:00', 1), Meet('dyuaa2mner', '10:00', '10:30', 1),
              Meet('alg5c2tonv', '11:00', '12:00', 1)],
             ['Friday', Meet('abu-hzbn-ocp', '01:40', '14:10', 1), Meet('gqcva4vb4i', '10:00', '11:45', 1),
              Meet('gea2wmsrka', '12:00', '13:45', 1)]]
