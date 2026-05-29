from ics import Calendar, Event
from ics.alarm import DisplayAlarm
from datetime import datetime, timedelta

# Create a new calendar instance
cal = Calendar()

# Define your standard timetable blocks
# (Adjust the hours/minutes here to match your exact dashboard setup)
sessions = [
    {
        "name": "Formula Blitz (PCM)",
        "start_time": "05:30:00",
        "end_time": "06:00:00",
        "desc": "Early morning core formula revision for maximum UACE points."
    },
    {
        "name": "Pure Math & Physics Deep Dive",
        "start_time": "20:00:00",
        "end_time": "23:00:00",
        "desc": "Late-night intensive problem solving and tough numbers tracking."
    },
    {
        "name": "Chemistry & Subsidiary ICT Review",
        "start_time": "23:00:00",
        "end_time": "01:00:00",
        "desc": "Final late-night block covering organic mechanisms and tech concepts."
    }
]

# Populate the calendar with a daily repeating rule for each session
for session in sessions:
    e = Event()
    e.name = session["name"]
    e.description = session["desc"]
    
    # Set a base date (Today) combined with the session times
    today_str = datetime.now().strftime("%Y-%m-%d")
    e.begin = f"{today_str} {session['start_time']}"
    e.end = f"{today_str} {session['end_time']}"
    
    # Crucial: Force the session to repeat every single day automatically
    e.extra.append("RRULE:FREQ=DAILY")
    
    # Attach an automated reminder popup alarm (10 minutes before session)
    alarm = DisplayAlarm(trigger=timedelta(minutes=-10))
    e.alarms.append(alarm)
    
    cal.events.add(e)

# Save to an installable file
with open("static/uace_schedule.ics", "w") as f:
    f.writelines(cal.serialize_iter())

print("Success: static/uace_schedule.ics has been generated with all sessions mapped!")
