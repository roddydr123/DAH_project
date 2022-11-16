import urllib.request


class Measurement():
        def __init__(self):
                pass

        def get(self, value):
                with urllib.request.urlopen(f'http://192.168.0.15/{value}') as response:
                        html = response.read()
                number = int(html.split()[1])
                return number

        def convert(self, fahrenheit):
                return (fahrenheit - 32) * 5/9

        def get_humidity(self):
                return self.get('humidity')

        def get_temp(self):
                F = self.get('temp')
                return self.convert(F)


meas = Measurement()
print(meas.get_temp())
