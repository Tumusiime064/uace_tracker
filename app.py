from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

# Complete Comprehensive UACE Syllabus Mapping for high performance
SYLLABUS_DATA = {
    "M1": {
        "title": "Pure Mathematics (Paper 1)",
        "topics": [
            "Algebra (Surds, Indices, Quadratics, Remainder Theorem, Progressions)",
            "Complex Numbers (Loci, Argand Diagrams, De Moivre's Theorem)",
            "Trigonometry (Compound/Double angles, Factor Formulae, Equations)",
            "Coordinate Geometry I & II (Straight lines, Circles, Parabola, Ellipse)",
            "Calculus: Differentiation (First Principles, Chain/Product Rules, Tangents/Normals)",
            "Calculus: Integration (Substitution, Parts, Definite Integrals, Areas, Volumes)",
            "Vectors in 2D & 3D (Scalar/Vector Products, Lines, Planes)",
            "Matrices & Transformations (Determinants, Inverses, Linear Systems)"
        ]
    },
    "M2": {
        "title": "Applied Mathematics (Paper 2)",
        "topics": [
            "Mechanics: Kinematics (Projectiles, Linear Motion Graphs)",
            "Mechanics: Kinetics (Newton's Laws, Pulleys, Connected Particles, Work, Energy, Power)",
            "Mechanics: Statistics (Statics, Friction, Moments, Centre of Gravity)",
            "Statistics: Data Presentation, Measures of Central Tendency & Dispersion",
            "Probability: Permutations & Combinations, Probability Trees, Conditional Probability",
            "Discrete & Continuous Probability Distributions (Binomial, Normal Distributions)",
            "Numerical Methods: Linear Interpolation, Errors (Truncation/Absolute), Newton-Raphson, Trapezoidal Rule"
        ]
    },
    "P1": {
        "title": "Physics Paper 1 (Mechanics & Heat)",
        "topics": [
            "Mechanics: Dimensions, Scalar & Vector quantities",
            "Mechanics: Circular Motion, Gravitation, Satellites, Planetary Orbits",
            "Mechanics: Rotational Motion (Moment of Inertia, Angular Momentum)",
            "Mechanics: Elasticity (Hooke's Law, Young's Modulus, Work done in stretching)",
            "Mechanics: Fluid Mechanics (Surface Tension, Capillarity, Viscosity, Poiseuille's Equation)",
            "Heat: Thermometry, Pyrometers (Thermocouple, Resistance thermometers)",
            "Heat: Calorimetry, Specific Heat Capacities (Continuous flow method)",
            "Heat: Kinetic Theory of Gases, Ideal Gas Equation, Gas Laws ($PV=\\frac{1}{3}Nmc^2$)",
            "Heat: Thermodynamics (First Law, Isothermal & Adiabatic expansions)",
            "Heat: Thermal Conduction (Searle's & Lees' methods, Black body radiation)"
        ]
    },
    "P2": {
        "title": "Physics Paper 2 (Waves, Optics, Electricity & Magnetism)",
        "topics": [
            "Waves: Progressive & Stationary waves, Velocity of sound (Gas/Strings)",
            "Waves: Superposition, Interference (Young's Double Slit), Diffraction grating",
            "Optics: Reflection & Refraction at plane/spherical surfaces (Prisms, Lenses)",
            "Optics: Defects of vision & Optical Instruments (Microscopes, Telescopes)",
            "Electricity: Electrostatics (Coulomb's Law, Electric Fields, Gauss's Law, Capacitors)",
            "Electricity: Current Electricity (Ohm's Law, Wheatstone Bridge, Potentiometer)",
            "Magnetism: Magnetic fields (Biot-Savart Law, Ampere's Law), Force on conductors",
            "Magnetism: Electromagnetic Induction (Faraday's/Lenz's laws, Generators, Transformers)",
            "Magnetism: Alternating Current (Root-mean-square values, RLC circuits)"
        ]
    },
    "P3": {
        "title": "Physics Paper 3 (Modern Physics & Practicals)",
        "topics": [
            "Atomic Structure: Cathode rays, Thomson's experiment, Millikan's Oil drop",
            "Quantum Physics: Photoelectric Effect, Einstein's Equation, X-ray production",
            "Nuclear Physics: Radioactivity (Decay constant, Half-life), Fusion & Fission",
            "Experimental Analysis: Graph plotting, Error limits, Gradient and Intercept calculations"
        ]
    },
    "C1": {
        "title": "Physical Chemistry (Paper 1)",
        "topics": [
            "Atomic Structure & Bonding (Quantum numbers, Orbitals, Hybridization, VSEPR Theory)",
            "Gaseous State (Dalton's law, Graham's law, Van der Waals forces)",
            "Chemical Energetics (Hess's Law, Born-Haber cycles, Entropy, Free Energy)",
            "Chemical & Ionic Equilibria ($K_c, K_p, K_w, K_a, K_b, K_{sp}$, Buffer solutions, Titration curves)",
            "Phase Equilibria (Two-component systems, Raoult's law, Distillation, Eutectic mixtures)",
            "Chemical Kinetics (Rate equations, Order of reaction, Arrhenius Equation, Catalysis)",
            "Electrochemistry (Standard Electrode Potentials, Nernst Equation, Electrolysis, Faraday's laws)"
        ]
    },
    "C2": {
        "title": "Inorganic Chemistry (Paper 1 & 2)",
        "topics": [
            "Periodicity: Physical and Chemical trends across Period 3",
            "Group II Elements (Alkaline earth metals: Solubility of hydroxides/sulphates, Thermal stability)",
            "Group VII Elements (Halogens: Oxidizing power, Hydrogen halides, Disproportionation)",
            "Transition Elements (d-block configurations, Variable oxidation states, Complex ion formation, Color, Catalysis)",
            "Qualitative Analysis: Systematic identification of cations ($Al^{3+}, Pb^{2+}, Cu^{2+}, Fe^{2+/3+}$, etc.) and anions"
        ]
    },
    "C3": {
        "title": "Organic Chemistry (Paper 1 & 3)",
        "topics": [
            "Hydrocarbons: Alkanes, Alkenes, Alkynes (Free radical substitution, Electrophilic addition)",
            "Aromatic Chemistry: Benzene structure, Electrophilic substitution (Nitration, Sulphonation, Halogenation)",
            "Halogenoalkanes & Hydroxy compounds (Nucleophilic substitution $S_N1/S_N2$, Elimination, Phenols)",
            "Carbonyl Compounds: Aldehydes & Ketones (Nucleophilic addition, Iodoform test, Brady's reagent)",
            "Carboxylic Acids & Derivatives (Esters, Acid halides, Amides, Amines, Amino acids)",
            "Polymers & Macromolecules (Addition vs Condensation polymerization, Natural polymers)"
        ]
    }
}

TIMETABLE = [
    {"time": "05:30 - 06:00 AM", "mon": "Formula Blitz", "tue": "Formula Blitz", "wed": "Formula Blitz", "thu": "Formula Blitz", "fri": "Formula Blitz", "sat": "Formula Blitz", "sun": "Formula Blitz"},
    {"time": "06:00 - 08:30 AM", "mon": "P1:Mechanics", "tue": "C1:Physical", "wed": "M1:Pure Math", "thu": "P2:Waves/Light", "fri": "C2:Inorganic", "sat": "M2:Mechanics", "sun": "FULL MOCK"},
    {"time": "08:30 - 09:00 AM", "mon": "BREAK", "tue": "BREAK", "wed": "BREAK", "thu": "BREAK", "fri": "BREAK", "sat": "BREAK", "sun": "BREAK"},
    {"time": "09:00 - 11:30 AM", "mon": "Syllabus Advance", "tue": "Syllabus Advance", "wed": "Syllabus Advance", "thu": "Syllabus Advance", "fri": "Syllabus Advance", "sat": "Ace Academy", "sun": "MOCK REVIEW"},
    {"time": "11:30 - 12:30 PM", "mon": "Story Reading", "tue": "Story Reading", "wed": "Story Reading", "thu": "Story Reading", "fri": "Story Reading", "sat": "Story Reading", "sun": "BREAK"},
    {"time": "12:30 - 02:00 PM", "mon": "LUNCH & NAP", "tue": "LUNCH & NAP", "wed": "LUNCH & NAP", "thu": "LUNCH & NAP", "fri": "LUNCH & NAP", "sat": "LUNCH & NAP", "sun": "Topic Self-Test"},
    {"time": "02:00 - 04:30 PM", "mon": "C3:Organic", "tue": "M1:Pure Math", "wed": "P3:Modern Ph.", "thu": "C1:Physical", "fri": "M2:Statistics", "sat": "General Paper", "sun": "Weak Areas"},
    {"time": "04:30 - 05:30 PM", "mon": "ACTIVE REST", "tue": "ACTIVE REST", "wed": "ACTIVE REST", "thu": "ACTIVE REST", "fri": "ACTIVE REST", "sat": "ACTIVE REST", "sun": "ACTIVE REST"},
    {"time": "05:30 - 08:00 PM", "mon": "M1:Pure Math", "tue": "P1:Heat/Ther.", "wed": "C3:Organic", "thu": "M1:Pure Math", "fri": "Sub ICT", "sat": "Past Papers", "sun": "Week Review"},
    {"time": "08:00 - 09:00 PM", "mon": "SUPPER", "tue": "SUPPER", "wed": "SUPPER", "thu": "SUPPER", "fri": "SUPPER", "sat": "SUPPER", "sun": "SUPPER"},
    {"time": "09:00 - 11:30 PM", "mon": "Past Papers", "tue": "Past Papers", "wed": "Past Papers", "thu": "Past Papers", "fri": "Past Papers", "sat": "Feynman Recon", "sun": "Planning"},
    {"time": "11:30 - 12:00 AM", "mon": "Feynman Recon", "tue": "Feynman Recon", "wed": "Feynman Recon", "thu": "Feynman Recon", "fri": "Feynman Recon", "sat": "Mind Cleanse", "sun": "Mind Cleanse"}
]

@app.route("/")
def index():
    # Calculate exact dynamic countdown to UACE exams (Starting approx Nov 1, 2026)
    target_date = datetime(2026, 11, 1)
    days_left = (target_date - datetime.now()).days
    
    return render_template("index.html", timetable=TIMETABLE, syllabus=SYLLABUS_DATA, days_left=days_left)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    app.run(debug=True)

@app.route('/download-calendar')
def download_calendar():
    ics_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Moses UACE Tracker//EN
BEGIN:VEVENT
SUMMARY:Formula Blitz (PCM)
DESCRIPTION:Early morning core formula revision for maximum UACE points.
DTSTART;TZID=Africa/Kampala:20260530T053000
DTEND;TZID=Africa/Kampala:20260530T060000
RRULE:FREQ=DAILY
BEGIN:VALARM
TRIGGER:-PT10M
ACTION:DISPLAY
DESCRIPTION:Reminder
END:VALARM
END:VEVENT
BEGIN:VEVENT
SUMMARY:Pure Math & Physics Deep Dive
DESCRIPTION:Late-night intensive problem solving and tough numbers tracking.
DTSTART;TZID=Africa/Kampala:20260530T200000
DTEND;TZID=Africa/Kampala:20260530T230000
RRULE:FREQ=DAILY
BEGIN:VALARM
TRIGGER:-PT10M
ACTION:DISPLAY
DESCRIPTION:Reminder
END:VALARM
END:VEVENT
BEGIN:VEVENT
SUMMARY:Chemistry & Subsidiary ICT Review
DESCRIPTION:Final late-night block covering organic mechanisms and tech concepts.
DTSTART;TZID=Africa/Kampala:20260530T230000
DTEND;TZID=Africa/Kampala:20260531T010000
RRULE:FREQ=DAILY
BEGIN:VALARM
TRIGGER:-PT10M
ACTION:DISPLAY
DESCRIPTION:Reminder
END:VALARM
END:VEVENT
END:VCALENDAR"""
    from flask import Response
    return Response(ics_content, mimetype='text/calendar', headers={'Content-Disposition': 'attachment; filename=uace_schedule.ics'})
