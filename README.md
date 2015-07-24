# Migranalyzer
Migraines analyzer.

I started this project to find out what causes my migraines. I have tried at least 50 apps and none really helped me to understand the problem.

I am pretty sure my migraines are cause by weather changes but it's hard to predict. Some people think barometric pressure is the cause. There is a few migraine predictors out there but they didn't work for me at all.

The solution most people will give you is to take medicines until the end of time but I don't want to do that.

I have a python script that captures the weather for my location and then sends the data to Google Spreadsheets using their API.

I also have a Google Form where I enter my "Headache amount" that adds data to that same spreadsheet. I try to enter this data several times a day.

I exported the data here for everybody to see and analyze. Ideally we would have a site or app with user authentication and location awareness but for now this works.

I have several **Arduinos** and sensors that we can use to capture data. The next step will be to capture my "Room Weather" to see if that has any relationship. I think capturing the room is important because with AC and heaters the values are quite different from the weather reports.

Also, I have been wearing a **Fitbit** with heart rate monitor for a month or so. They have an API so we will be able to compare this data too once I add it to the python script.

The project is in the initial stages. I see these ones:
- Phase 1. Capture data. As much as we can from all kinds of sources, sensors and devices.
- Phase 2. Analyze the data and see if we find any patters.
- Phase 3. Predict the data.
- Phase 4. Act before the migraine happens. Getting an alert would be easy but doesn't solve the problem. I am thinking more about creating a smart device that would adjust the room values according to what it knows is good for you.

That' all.
I just made my headache open source!
