import urllib.request


class Measurement():
        """
        Class which can be used to request different information from the Arduino
        webserver. The IP address must be checked before use.
        """

        def __init__(self):
                pass

        def get(self, value):
                """
                Send a request to the webserver page /value. The response is parsed and split
                by spaces. We formatted the server to display light/humidity/temperature
                data such that it is the second element: [1].
                """
                with urllib.request.urlopen(f'http://192.168.0.4/{value}') as response:
                        html = response.read().decode("utf-8")
                number_string = html.split()[1]

                # Convert the string to an integer for manipulation elsewhere.
                return int(number_string)

        def convert(self, fahrenheit):
                # Use a standard formula to convert Fahrenheit to degrees Celsius.
                return (fahrenheit - 32) * 5/9

        def get_humidity(self):
                return self.get('humidity')

        def get_temp(self):
                F = self.get('temp')
                return self.convert(F)

        def get_light_level(self):
                """
                Fetches the light level from the webserver on a scale from 0 to 1024.
                0 is fully bright and 1024 is fully dark.
                """
                return self.get('light_level')

        def get_temp_F(self):
                return self.get('temp')


if __name__=="__main__":
        meas = Measurement()
        print(meas.get_temp())
