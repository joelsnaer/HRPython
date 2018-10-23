class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def str_update(self, time):
        times = time.split(":")
        self.hours = int(times[0])
        self.minutes = int(times[1])
        self.seconds = int(times[2])

    def add_clocks(self, clock2):
        #Fengið sekúndur, mínútur og klukkutíma
        seconds = self.seconds + clock2.seconds
        minutes = self.minutes + clock2.minutes
        hours = self.hours + clock2.hours
        #Reiknað hverus margar mínútur sekúndurnar eru
        math = divmod(seconds, 60)
        minutes += math[0]
        seconds = math[1]
        #Reikna hversu margir klukkutímar mínúturnar eru
        math = divmod(minutes, 60)
        hours += math[0]
        minutes = math[1]
        #reiknað ef klukkutímar eru meiri en einn sólahringur og lagað það
        math = divmod(hours, 24)
        if hours > 23:
            hours = math[1]
        clock3 = Clock(hours, minutes, seconds)
        return clock3

    def __str__(self):
        return "{} hours, {} minutes and {} seconds".format(self.hours, self.minutes, self.seconds)