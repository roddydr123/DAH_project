import urllib.request


class Measurement():
        def __init__(self):
                pass

        def get(self, value):
                with urllib.request.urlopen(f'http://192.168.0.10/{value}') as response:
                        html = response.read().decode("utf-8")
                number_string = html.split()[1]
                return int(number_string)

        def convert(self, fahrenheit):
                return (fahrenheit - 32) * 5/9

        def get_humidity(self):
                return self.get('humidity')

        def get_temp(self):
                F = self.get('temp')
                return self.convert(F)

        def get_light_level(self):
                return self.get('light_level')

        def get_temp_F(self):
                return self.get('temp')


if __name__=="__main__":
        meas = Measurement()
        print(meas.get_temp())
