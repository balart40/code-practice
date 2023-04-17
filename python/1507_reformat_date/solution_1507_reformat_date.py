class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        months = {
            "Jan": "01", "Feb": "02", "Mar": "03",
            "Apr": "04", "May": "05", "Jun": "06", "Jul":"07",
            "Aug": "08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"
        }
        date = date.split(' ')
        day = date[0]
        month = months.get(date[1])
        year = date[2]
        if day[1].isdigit():
            day = day[0:2]
        else:
            day = "0"+day[0]
        return year+"-"+month+"-"+day