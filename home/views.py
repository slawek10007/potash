from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from parser import Weather
from django.template import Template, Context

class Widok(View):
	def get(self,request, *args, **kwargs):

		city = request.GET.get('city','Warsaw')


		template = Template("""

			<html>
			<head>
			<title>Weather Potasz</title>
			</head>
			<body>
			<h1>Weather for: {{ city }}</h1>
			Pressure: <b>{{ pressure }}hPa</b>
			<br>
			Temperature: <b>{{ temp }}C</b>
			<br>
			Humidity: <b>{{ humidity }}%</b>
			
			<form>{% csrf_token %}
            	Weather for city: <input type="text" name="city"><br>
            	<input type="submit" value="Show">
        	</form>
        	</body>
        	</html>

		""")
		
		context = Context(Weather.get_weather(city)) 

		return HttpResponse(template.render(context))