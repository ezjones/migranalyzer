# Migranalyzer
Migraines analyzer.

I started this project to find out what causes my migraines. I have tried at least 50 apps and none really helped me to understand the problem.

I am pretty sure my migraines are cause by weather changes but it's hard to predict. Some people think barometric pressure is the cause. There is a few migraine predictors out there but they didn't work for me at all.

The solution most doctors will give you is to take medicines until the end of time but who wants to do that.

# How it works
I have a python script that captures the weather for my location and then sends the data to Google Spreadsheets using their API.

I also have a Google Form where I enter my "Headache amount" that adds data to that same spreadsheet. I try to enter this data several times a day.

# Data
I capture every half hour the weather reports using the Yahoo API.

The "Headache Amount" has a field called "Took Medicine". We have to take this into account if the headache goes down.

Ideally we would have a site or app with user authentication and location awareness but for now this works.

# Future plans
I have several **Arduinos** and sensors that we can use to capture data. The next step will be to capture my "Room Weather" to see if that has any relationship. I think capturing the room is important because with AC and heaters the values are quite different from the weather reports.

Also, I have been wearing a **Fitbit** with heart rate monitor for a month or so. They have an API so we will be able to compare this data too once I add it to the python script.

# Project phases.
We are on Phase 1 now but I see these ones:
- Phase 1. Capture data. As much as we can from all kinds of sources, sensors and devices. Get more people to join so we can compare diffenret cities.
- Phase 2. Analyze the data and see what patterns we find.
- Phase 3. Predict the data. This has to be customized for each user taking into account their past data. Every "body" is different.
- Phase 4. Act before the migraine happens. Getting an alert would be easy but it doesn't solve the problem. I am thinking more about creating a smart device that would adjust the room values according to what it knows is good for you.

That' all.
I just made my headache open source!
