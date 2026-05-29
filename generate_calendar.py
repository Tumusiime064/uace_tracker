from ics import Calendar, Event
from ics.alarm import DisplayAlarm
from datetime import datetime, timedelta

cal = Calendar()

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

for session in sessions:
    e = Event()
    e.name = session["name"]
    e.description = session["desc"]
    
    # Calculate correct dates
    base_date = datetime.now()
    start_dt = datetime.strptime(f"{base_date.strftime('%Y-%m-%d')} {session['start_time']}", "%Y-%m-%d %H:%M:%S")
    end_dt = datetime.strptime(f"{base_date.strftime('%Y-%m-%d')} {session['end_time']}", "%Y-%m-%d %H:%M:%S")
    
    # If the session ends past midnight, push the end date to tomorrow
    if end_dt <= start_dt:
        end_dt += timedelta(days=1)
        
    e.begin = start_dt
    e.end = end_dt
    
    e.extra.append("RRULE:FREQ=DAILY")
    
    alarm = DisplayAlarm(trigger=timedelta(minutes=-10))
    e.alarms.append(alarm)
    
    cal.events.add(e)

with open("static/uace_schedule.ics", "w") as f:
    f.writelines(cal.serialize_iter())

print("Success: static/uace_schedule.ics has been generated cleanly across midnight!")
