from typing import List

import bdateutil.parser as dp
import tzlocal
import pytz


class DateLikesConversion:

    def __init__(self, dates, likes):
        self.dates = dates
        self.like_list = likes

    def convert_date_and_likes(self):
        dates = self.dates
        like_list = self.like_list
        date_time_array = []
        date_dict, date_double_dict = {}, {}

        # print(len(dates))

        for date in dates:

            parsed_t = dp.parse(date)
            local_time_zone = str(tzlocal.get_localzone())
            t_time = parsed_t.astimezone(pytz.timezone(local_time_zone)).strftime('%m/%d/%Y, %H:%M:%S')
            date_time_array.append(t_time)

        for i in range(len(date_time_array)):
            date_dict[i] = date_time_array[i][:48], date_time_array[i][12:], like_list[i]

        return date_dict

