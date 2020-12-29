import re


class Meet(object):
    def __init__(self, meet_code, starting_hour, finishing_hour, connect_after):
        self.meet_code = meet_code
        self.connect_after = connect_after
        self.start_min = ''
        self.start_hour = ''
        self.finish_min = ''
        self.finish_hour = ''

        # HOUR FORMAT IS HH:MM

        # GET THE STARTING HOUR
        if re.search(r'\A[1-9]', starting_hour.split(':')[0]):
            self.start_hour = re.findall(r'\A[1-9]', starting_hour.split(':')[0])[0]
        self.start_hour += starting_hour[1]

        # GET THE STARTING MINUTE
        if re.search(r'\A[1-9]', starting_hour.split(':')[1]):
            self.start_min = re.findall(r'\A[1-9]', starting_hour.split(':')[1])[0]
        self.start_min += starting_hour[-1]

        # GET THE FINISHING HOUR
        if re.search(r'\A[1-9]', finishing_hour.split(':')[0]):
            self.finish_hour = re.findall(r'\A[1-9]', finishing_hour.split(':')[0])[0]
        self.finish_hour += finishing_hour[1]

        # GET THE FINISHING MINUTE
        if re.search(r'\A[1-9]', finishing_hour.split(':')[1]):
            self.finish_min = re.findall(r'\A[1-9]', finishing_hour.split(':')[1])[0]
        self.finish_min += finishing_hour[-1]


timetable = [['Monday', Meet('meet_code', '08:00', '09:45', 1), Meet('meet_code', '10:00', '11:45', 1),
              Meet('meet_code', '12:00', '12:45', 1)],
             ['Tuesday', Meet('meet_code', '08:00', '09:45', 0.2), Meet('meet_code', '10:00', '10:45', 1),
              Meet('meet_code', '11:00', '11:45', 1), Meet('meet_code', '12:00', '12:45', 1)],
             ['Wednesday ', Meet('meet_code', '8:00', '10:45', 1), Meet('meet_code', '11:00', '13:45', 1)],
             ['Thursday', Meet('meet_code', '8:30', '9:00', 1), Meet('meet_code', '9:00', '9:30', 1),
              Meet('meet_code', '9:30', '10:00', 1), Meet('meet_code', '10:00', '10:30', 1),
              Meet('meet_code', '11:00', '12:00', 1)],
             ['Friday', Meet('meet_code', '01:40', '14:10', 1), Meet('meet_code', '10:00', '11:45', 1),
              Meet('meet_code', '12:00', '13:45', 1)]]
