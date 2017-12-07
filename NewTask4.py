import webbrowser

class MyClass:
    latitude = None
    longitude = None
 
    def __str__(self):
        return str(self.latitude) + ' : ' + str(self.longitude)
      
    def __add__(self, other):
        result = MyClass()
        result.latitude = float(self.latitude) + float(other.latitude)
        result.longitude = float(self.longitude) + float(other.longitude)
        return result

    def goOnMap(self):
        url = "http://maps.google.com/maps?q=%s,%s"% (self.latitude, self.longitude)
        webbrowser.open(url)
        
