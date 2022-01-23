from datetime import datetime


class Tour:
    @staticmethod
    def start_timer(): # début du temps, saisit l'heure complète du système/start of time, captures the complete system time
        str(datetime.now().time())

    @staticmethod
    def end_timer(): # fin du temps, saisit l'heure sur le système/end of time, enters the time on the system
        str(datetime.now().time())

    @staticmethod
    def timme_elapsed(): # calcul le temps éoulé/ calculate elapsed time
        departure_time = Tour.start_timer()
        final_time = Tour.end_timer()
        time_difference = departure_time - final_time  #time difference = différence de temps
        print(time_difference)
