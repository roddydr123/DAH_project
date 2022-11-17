import urllib.request


class Measurement():
        def __init__(self):
                pass

        def get(self, value):
                with urllib.request.urlopen(f'http://192.168.0.10/{value}') as response:
                        html = response.read()
                result_string = html.split()[1]
                if len(result_string) == 3:
                        number = result_string[:-1]
                else:
                        number = result_string
                return number

        def convert(self, fahrenheit):
                return (fahrenheit - 32) * 5/9

        def get_humidity(self):
                return self.get('humidity')

        def get_temp(self):
                F = self.get('temp')
                return self.convert(F)


if __name__=="__main__":
        meas = Measurement()
        print(meas.get_temp())
