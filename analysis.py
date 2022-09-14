# Analysis Example
# Get Device List
#
# Snippet to push data to MQTT. Follow this pattern within your application
# If you want more details about MQTT, search "MQTT" in TagoIO help center.
# You can find plenty of documentation about this topic.
# TagoIO Team.
#
# How to use?
# In order to trigger this analysis you must setup a Dashboard.
# Create a Widget "Form" and enter the variable 'push_payload' for the device you want to push with the MQTT.
# In User Control, select this Analysis in the Analysis Option.
# Save and use the form.

from tago import Analysis
from tago import Services


# The function myAnalysis will run when you execute your analysis
def myAnalysis(context,scope):
  # my_data_bucket = scope[0]['bucket'] # for legacy
  my_data_bucket = scope[0]['device'] # for immutable/mutable
  my_data_value = scope[0]['value']
  # Create your data object to push to MQTT
  # In this case we're sending a JSON.
  # You can send anything you want.
  my_data_json = {'variable': 'temperature_celsius','value': my_data_value,'unit': 'C'}
  # Create topic, retain and qos, you chooses
  topic = 'test'
  retain = False
  qos = 1
  # Publishing to MQTT
  MQTT = Services(context.token).MQTT
  result = MQTT.publish(my_data_json,my_data_bucket,topic,retain,qos)
  context.log(result)
# The analysis token in only necessary to run the analysis outside TagoIO
Analysis('my analysis token here').init(myAnalysis)
