<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Physics Quiz</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
    <h1>Physics Quiz</h1>
    <form id="quiz-form">
        <fieldset>
            <legend><h3>Participant Details</h3></legend>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required><br><br>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required><br><br>

            <label for="roll-number">Roll Number:</label>
            <input type="text" id="roll-number" name="rollNumber" required><br><br>

            <label for="class">Class:</label>
            <input type="text" id="class" name="class" required><br><br>
        </fieldset>

        <fieldset>
            <legend><h3>Questions</h3></legend>

            <!-- Questions Section -->

            <!-- Mechanics -->
           <div>
                <h3>1. A car moves along a straight path with a velocity given by \(v(t) = 3t^2 - 2t + 4\) (m/s). What is the acceleration at \(t = 2\) s?</h3>
                <label><input type="radio" name="q1" value="A"> 6 m/s<sup>2</sup></label><br>
                <label><input type="radio" name="q1" value="B"> 10 m/s<sup>2</sup></label><br>
                <label><input type="radio" name="q1" value="C"> 22 m/s<sup>2</sup></label><br>
                <label><input type="radio" name="q1" value="D"> 28 m/s<sup>2</sup></label><br>
            </div>

            <div>
                <h3>2. A ball is thrown upward with an initial velocity of 20 m/s. What is the maximum height it reaches? (\(g = 9.8\) m/s<sup>2</sup>)</h3>
                <label><input type="radio" name="q2" value="A"> 10.2 m</label><br>
                <label><input type="radio" name="q2" value="B"> 20.4 m</label><br>
                <label><input type="radio" name="q2" value="C"> 30.6 m</label><br>
                <label><input type="radio" name="q2" value="D"> 40.8 m</label><br>
            </div>

            <div>
                <h3>3. A 10-kg block slides down a frictionless incline of height 5 m. What is its velocity at the bottom?</h3>
                <label><input type="radio" name="q3" value="A"> 7.0 m/s</label><br>
                <label><input type="radio" name="q3" value="B"> 9.9 m/s</label><br>
                <label><input type="radio" name="q3" value="C"> 14.0 m/s</label><br>
                <label><input type="radio" name="q3" value="D"> 19.6 m/s</label><br>
            </div>

            <div>
                <h3>4. The moment of inertia of a uniform solid sphere rotating about its diameter is:</h3>
                <label><input type="radio" name="q4" value="A"> \(\frac{1}{2}MR^2\)</label><br>
                <label><input type="radio" name="q4" value="B"> \(\frac{2}{5}MR^2\)</label><br>
                <label><input type="radio" name="q4" value="C"> \(\frac{1}{3}MR^2\)</label><br>
                <label><input type="radio" name="q4" value="D"> \(\frac{3}{5}MR^2\)</label><br>
            </div>

            <div>
                <h3>5. A satellite is in a circular orbit around Earth at a height of 500 km. What is its orbital speed? (Radius of Earth = 6,400 km, \(g = 9.8\) m/s<sup>2</sup>)</h3>
                <label><input type="radio" name="q5" value="A"> 6.9 km/s</label><br>
                <label><input type="radio" name="q5" value="B"> 7.4 km/s</label><br>
                <label><input type="radio" name="q5" value="C"> 8.1 km/s</label><br>
                <label><input type="radio" name="q5" value="D"> 9.2 km/s</label><br>
            </div>

            <div>
                <h3>6. A particle of mass 2 kg is moving in a circular path of radius 0.5 m with a constant speed of 4 m/s. What is the centripetal force?</h3>
                <label><input type="radio" name="q6" value="A"> 16 N</label><br>
                <label><input type="radio" name="q6" value="B"> 32 N</label><br>
                <label><input type="radio" name="q6" value="C"> 64 N</label><br>
                <label><input type="radio" name="q6" value="D"> 8 N</label><br>
            </div>

            <div>
                <h3>7. A spring with a spring constant of 200 N/m is compressed by 0.1 m. What is the potential energy stored in the spring?</h3>
                <label><input type="radio" name="q7" value="A"> 1 J</label><br>
                <label><input type="radio" name="q7" value="B"> 2 J</label><br>
                <label><input type="radio" name="q7" value="C"> 0.5 J</label><br>
                <label><input type="radio" name="q7" value="D"> 10 J</label><br>
            </div>

            <div>
                <h3>8. A pendulum has a length of 1 m and is displaced by a small angle. What is its period? (\(g = 9.8\) m/s<sup>2</sup>)</h3>
                <label><input type="radio" name="q8" value="A"> 1.2 s</label><br>
                <label><input type="radio" name="q8" value="B"> 2.0 s</label><br>
                <label><input type="radio" name="q8" value="C"> 1.6 s</label><br>
                <label><input type="radio" name="q8" value="D"> 3.1 s</label><br>
            </div>

            <div>
                <h3>9. A ball of mass 0.5 kg is tied to a string and swung in a horizontal circle of radius 1 m with a speed of 2 m/s. What is the tension in the string?</h3>
                <label><input type="radio" name="q9" value="A"> 1 N</label><br>
                <label><input type="radio" name="q9" value="B"> 2 N</label><br>
                <label><input type="radio" name="q9" value="C"> 4 N</label><br>
                <label><input type="radio" name="q9" value="D"> 8 N</label><br>
            </div>

            <div>
                <h3>10. Two masses, \(m_1 = 2 \, \text{kg}\) and \(m_2 = 3 \, \text{kg}\), are connected by a light string over a frictionless pulley. What is the acceleration of the system? (\(g = 9.8 \, \text{m/s}^2\))</h3>
                <label><input type="radio" name="q10" value="A"> \(1.96 \, \text{m/s}^2\)</label><br>
                <label><input type="radio" name="q10" value="B"> \(3.92 \, \text{m/s}^2\)</label><br>
                <label><input type="radio" name="q10" value="C"> \(4.90 \, \text{m/s}^2\)</label><br>
                <label><input type="radio" name="q10" value="D"> \(5.88 \, \text{m/s}^2\)</label><br>
            </div>
            <div>
                <h3>11. A Carnot engine operates between two reservoirs at 500 K and 300 K. What is its efficiency?</h3>
                <label><input type="radio" name="q11" value="A"> 40%</label><br>
                <label><input type="radio" name="q11" value="B"> 50%</label><br>
                <label><input type="radio" name="q11" value="C"> 60%</label><br>
                <label><input type="radio" name="q11" value="D"> 80%</label><br>
            </div>

            <div>
                <h3>12. The internal energy of an ideal gas depends on:</h3>
                <label><input type="radio" name="q12" value="A"> Pressure only</label><br>
                <label><input type="radio" name="q12" value="B"> Volume only</label><br>
                <label><input type="radio" name="q12" value="C"> Temperature only</label><br>
                <label><input type="radio" name="q12" value="D"> Pressure and temperature</label><br>
            </div>

            <div>
                <h3>13. An ideal gas undergoes an isothermal process. What is the change in internal energy?</h3>
                <label><input type="radio" name="q13" value="A"> Positive</label><br>
                <label><input type="radio" name="q13" value="B"> Negative</label><br>
                <label><input type="radio" name="q13" value="C"> Zero</label><br>
                <label><input type="radio" name="q13" value="D"> Cannot be determined</label><br>
            </div>

            <div>
                <h3>14. In a cyclic process, the net work done by the system is equal to:</h3>
                <label><input type="radio" name="q14" value="A"> Change in internal energy</label><br>
                <label><input type="radio" name="q14" value="B"> Heat absorbed</label><br>
                <label><input type="radio" name="q14" value="C"> Heat released</label><br>
                <label><input type="radio" name="q14" value="D"> Net heat exchanged</label><br>
            </div>

            <div>
                <h3>15. The heat capacity at constant volume (\(C_v\)) for an ideal gas is related to its degrees of freedom (\(f\)) by:</h3>
                <label><input type="radio" name="q15" value="A"> \(C_v = \frac{f}{2}R\)</label><br>
                <label><input type="radio" name="q15" value="B"> \(C_v = fR\)</label><br>
                <label><input type="radio" name="q15" value="C"> \(C_v = \frac{f}{3}R\)</label><br>
                <label><input type="radio" name="q15" value="D"> \(C_v = \frac{f}{4}R\)</label><br>
            </div>

            <div>
                <h3>16. In an adiabatic process, the relationship between pressure and volume for an ideal gas is:</h3>
                <label><input type="radio" name="q16" value="A"> \(PV = \text{constant}\)</label><br>
                <label><input type="radio" name="q16" value="B"> \(P^2V = \text{constant}\)</label><br>
                <label><input type="radio" name="q16" value="C"> \(PV^\gamma = \text{constant}\)</label><br>
                <label><input type="radio" name="q16" value="D"> \(P^2V^2 = \text{constant}\)</label><br>
            </div>

            <div>
                <h3>17. Which of the following processes increases the entropy of the system?</h3>
                <label><input type="radio" name="q17" value="A"> Isothermal compression</label><br>
                <label><input type="radio" name="q17" value="B"> Adiabatic compression</label><br>
                <label><input type="radio" name="q17" value="C"> Isothermal expansion</label><br>
                <label><input type="radio" name="q17" value="D"> All of the above</label><br>
            </div>

            <div>
                <h3>18. For an ideal gas, the change in enthalpy (\(dH\)) during an isobaric process is given by:</h3>
                <label><input type="radio" name="q18" value="A"> \(dH = mC_pdT\)</label><br>
                <label><input type="radio" name="q18" value="B"> \(dH = mC_vdT\)</label><br>
                <label><input type="radio" name="q18" value="C"> \(dH = PdV\)</label><br>
                <label><input type="radio" name="q18" value="D"> \(dH = 0\)</label><br>
            </div>

            <div>
                <h3>19. The second law of thermodynamics states that:</h3>
                <label><input type="radio" name="q19" value="A"> Energy cannot be created or destroyed</label><br>
                <label><input type="radio" name="q19" value="B"> Heat flows naturally from cold to hot</label><br>
                <label><input type="radio" name="q19" value="C"> Entropy of an isolated system never decreases</label><br>
                <label><input type="radio" name="q19" value="D"> The work done is independent of path</label><br>
            </div>

            <div>
                <h3>20. The efficiency of a Carnot engine depends on:</h3>
                <label><input type="radio" name="q20" value="A"> The heat capacities of the working substance</label><br>
                <label><input type="radio" name="q20" value="B"> The temperature difference between the reservoirs</label><br>
                <label><input type="radio" name="q20" value="C"> The type of gas used</label><br>
                <label><input type="radio" name="q20" value="D"> The mass of the gas</label><br>
            </div>
            <div>
                <h3>21. The electric field inside a uniformly charged spherical shell is:</h3>
                <label><input type="radio" name="q21" value="A"> Zero</label><br>
                <label><input type="radio" name="q21" value="B"> Uniform</label><br>
                <label><input type="radio" name="q21" value="C"> Radially outward</label><br>
                <label><input type="radio" name="q21" value="D"> Radially inward</label><br>
            </div>

            <div>
                <h3>22. A current-carrying circular loop produces a magnetic field at its center. The direction of the field is given by:</h3>
                <label><input type="radio" name="q22" value="A"> Ampere's circuital law</label><br>
                <label><input type="radio" name="q22" value="B"> Right-hand rule</label><br>
                <label><input type="radio" name="q22" value="C"> Left-hand rule</label><br>
                <label><input type="radio" name="q22" value="D"> Biot-Savart law</label><br>
            </div>

            <div>
                <h3>23. The total flux through a closed surface is proportional to:</h3>
                <label><input type="radio" name="q23" value="A"> Electric field strength</label><br>
                <label><input type="radio" name="q23" value="B"> Charge enclosed</label><br>
                <label><input type="radio" name="q23" value="C"> Distance from the charge</label><br>
                <label><input type="radio" name="q23" value="D"> Surface area</label><br>
            </div>

            <div>
                <h3>24. The potential difference across a capacitor is halved. The energy stored in it becomes:</h3>
                <label><input type="radio" name="q24" value="A"> Halved</label><br>
                <label><input type="radio" name="q24" value="B"> Doubled</label><br>
                <label><input type="radio" name="q24" value="C"> One-fourth</label><br>
                <label><input type="radio" name="q24" value="D"> Unchanged</label><br>
            </div>

            <div>
                <h3>25. The time constant of an RC circuit is given by:</h3>
                <label><input type="radio" name="q25" value="A"> \(R \times C\)</label><br>
                <label><input type="radio" name="q25" value="B"> \(R / C\)</label><br>
                <label><input type="radio" name="q25" value="C"> \(1 / (R \times C)\)</label><br>
                <label><input type="radio" name="q25" value="D"> \(R^2 \times C^2\)</label><br>
            </div>

            <div>
                <h3>26. A long, straight current-carrying wire produces a magnetic field around it. The magnetic field strength at a distance \(r\) is proportional to:</h3>
                <label><input type="radio" name="q26" value="A"> \(1 / r^2\)</label><br>
                <label><input type="radio" name="q26" value="B"> \(1 / r\)</label><br>
                <label><input type="radio" name="q26" value="C"> \(r^2\)</label><br>
                <label><input type="radio" name="q26" value="D"> \(r\)</label><br>
            </div>

            <div>
                <h3>27. The force between two parallel current-carrying wires is:</h3>
                <label><input type="radio" name="q27" value="A"> Attractive if currents flow in the same direction</label><br>
                <label><input type="radio" name="q27" value="B"> Repulsive if currents flow in the same direction</label><br>
                <label><input type="radio" name="q27" value="C"> Zero</label><br>
                <label><input type="radio" name="q27" value="D"> Independent of the direction of current</label><br>
            </div>

            <div>
                <h3>28. Faraday's law of electromagnetic induction states that the induced emf is proportional to:</h3>
                <label><input type="radio" name="q28" value="A"> Rate of change of magnetic flux</label><br>
                <label><input type="radio" name="q28" value="B"> Magnetic field strength</label><br>
                <label><input type="radio" name="q28" value="C"> Electric field</label><br>
                <label><input type="radio" name="q28" value="D"> Resistance of the circuit</label><br>
            </div>

            <div>
                <h3>29. The SI unit of magnetic flux is:</h3>
                <label><input type="radio" name="q29" value="A"> Tesla</label><br>
                <label><input type="radio" name="q29" value="B"> Weber</label><br>
                <label><input type="radio" name="q29" value="C"> Henry</label><br>
                <label><input type="radio" name="q29" value="D"> Ampere</label><br>
            </div>

            <div>
                <h3>30. A transformer works on the principle of:</h3>
                <label><input type="radio" name="q30" value="A"> Electrostatic induction</label><br>
                <label><input type="radio" name="q30" value="B"> Mutual induction</label><br>
                <label><input type="radio" name="q30" value="C"> Self-induction</label><br>
                <label><input type="radio" name="q30" value="D"> Magnetic resonance</label><br>
            </div>
            <div>
                <h3>31. A convex lens has a focal length of 10 cm. An object is placed at a distance of 15 cm. What is the nature of the image?</h3>
                <label><input type="radio" name="q31" value="A"> Real and inverted</label><br>
                <label><input type="radio" name="q31" value="B"> Virtual and erect</label><br>
                <label><input type="radio" name="q31" value="C"> Real and erect</label><br>
                <label><input type="radio" name="q31" value="D"> Virtual and inverted</label><br>
            </div>

            <div>
                <h3>32. The critical angle for total internal reflection occurs when:</h3>
                <label><input type="radio" name="q32" value="A"> Angle of incidence equals angle of refraction</label><br>
                <label><input type="radio" name="q32" value="B"> Light passes from a denser to a rarer medium</label><br>
                <label><input type="radio" name="q32" value="C"> Angle of refraction is 90°</label><br>
                <label><input type="radio" name="q32" value="D"> None of the above</label><br>
            </div>

            <div>
                <h3>33. The interference pattern in Young’s double-slit experiment has bright fringes due to:</h3>
                <label><input type="radio" name="q33" value="A"> Constructive interference</label><br>
                <label><input type="radio" name="q33" value="B"> Destructive interference</label><br>
                <label><input type="radio" name="q33" value="C"> Diffraction</label><br>
                <label><input type="radio" name="q33" value="D"> Reflection</label><br>
            </div>

            <div>
                <h3>34. The resolving power of a microscope increases when:</h3>
                <label><input type="radio" name="q34" value="A"> Wavelength decreases</label><br>
                <label><input type="radio" name="q34" value="B"> Aperture increases</label><br>
                <label><input type="radio" name="q34" value="C"> Both A and B</label><br>
                <label><input type="radio" name="q34" value="D"> None of the above</label><br>
            </div>

            <div>
                <h3>35. Which color has the shortest wavelength in visible light?</h3>
                <label><input type="radio" name="q35" value="A"> Red</label><br>
                <label><input type="radio" name="q35" value="B"> Blue</label><br>
                <label><input type="radio" name="q35" value="C"> Green</label><br>
                <label><input type="radio" name="q35" value="D"> Yellow</label><br>
            </div>

            <div>
                <h3>36. A plane mirror produces an image that is:</h3>
                <label><input type="radio" name="q36" value="A"> Real and inverted</label><br>
                <label><input type="radio" name="q36" value="B"> Virtual and inverted</label><br>
                <label><input type="radio" name="q36" value="C"> Real and erect</label><br>
                <label><input type="radio" name="q36" value="D"> Virtual and erect</label><br>
            </div>

            <div>
                <h3>37. In a diffraction pattern, the angular width of the central maximum decreases if:</h3>
                <label><input type="radio" name="q37" value="A"> Slit width increases</label><br>
                <label><input type="radio" name="q37" value="B"> Wavelength increases</label><br>
                <label><input type="radio" name="q37" value="C"> Aperture decreases</label><br>
                <label><input type="radio" name="q37" value="D"> None of the above</label><br>
            </div>

            <div>
                <h3>38. A light ray passing through the focus of a convex lens emerges:</h3>
                <label><input type="radio" name="q38" value="A"> Parallel to the principal axis</label><br>
                <label><input type="radio" name="q38" value="B"> Diverging</label><br>
                <label><input type="radio" name="q38" value="C"> Converging</label><br>
                <label><input type="radio" name="q38" value="D"> Perpendicular to the axis</label><br>
            </div>

            <div>
                <h3>39. The refractive index of a medium depends on:</h3>
                <label><input type="radio" name="q39" value="A"> Wavelength of light</label><br>
                <label><input type="radio" name="q39" value="B"> Temperature</label><br>
                <label><input type="radio" name="q39" value="C"> Both A and B</label><br>
                <label><input type="radio" name="q39" value="D"> None of the above</label><br>
            </div>

            <div>
                <h3>40. In Huygens' principle, each point on a wavefront is considered as:</h3>
                <label><input type="radio" name="q40" value="A"> A source of secondary wavelets</label><br>
                <label><input type="radio" name="q40" value="B"> A reflection point</label><br>
                <label><input type="radio" name="q40" value="C"> A refraction point</label><br>
                <label><input type="radio" name="q40" value="D"> An absorption point</label><br>
            </div>
            <div>
                <h3>41. The energy levels in a hydrogen atom are proportional to:</h3>
                <label><input type="radio" name="q41" value="A"> \( n^2 \)</label><br>
                <label><input type="radio" name="q41" value="B"> \( 1/n \)</label><br>
                <label><input type="radio" name="q41" value="C"> \( -1/n^2 \)</label><br>
                <label><input type="radio" name="q41" value="D"> \( 1/n^3 \)</label><br>
            </div>

            <div>
                <h3>42. The photoelectric effect demonstrates the:</h3>
                <label><input type="radio" name="q42" value="A"> Wave nature of light</label><br>
                <label><input type="radio" name="q42" value="B"> Particle nature of light</label><br>
                <label><input type="radio" name="q42" value="C"> Dual nature of light</label><br>
                <label><input type="radio" name="q42" value="D"> Polarization of light</label><br>
            </div>

            <div>
                <h3>43. The de Broglie wavelength of a particle is inversely proportional to:</h3>
                <label><input type="radio" name="q43" value="A"> Its speed</label><br>
                <label><input type="radio" name="q43" value="B"> Its momentum</label><br>
                <label><input type="radio" name="q43" value="C"> Its mass</label><br>
                <label><input type="radio" name="q43" value="D"> Its frequency</label><br>
            </div>

            <div>
                <h3>44. The rest energy of an electron is approximately:</h3>
                <label><input type="radio" name="q44" value="A"> 0.511 MeV</label><br>
                <label><input type="radio" name="q44" value="B"> 1.022 MeV</label><br>
                <label><input type="radio" name="q44" value="C"> 2.044 MeV</label><br>
                <label><input type="radio" name="q44" value="D"> 0.255 MeV</label><br>
            </div>

            <div>
                <h3>45. In nuclear fission, the total mass of the products is:</h3>
                <label><input type="radio" name="q45" value="A"> Greater than the original nucleus</label><br>
                <label><input type="radio" name="q45" value="B"> Less than the original nucleus</label><br>
                <label><input type="radio" name="q45" value="C"> Equal to the original nucleus</label><br>
                <label><input type="radio" name="q45" value="D"> None of the above</label><br>
            </div>

            <div>
                <h3>46. The wavelength of X-rays is comparable to:</h3>
                <label><input type="radio" name="q46" value="A"> Infrared radiation</label><br>
                <label><input type="radio" name="q46" value="B"> Visible light</label><br>
                <label><input type="radio" name="q46" value="C"> Atomic dimensions</label><br>
                <label><input type="radio" name="q46" value="D"> Radio waves</label><br>
            </div>

            <div>
                <h3>47. The uncertainty principle relates:</h3>
                <label><input type="radio" name="q47" value="A"> Position and energy</label><br>
                <label><input type="radio" name="q47" value="B"> Position and velocity</label><br>
                <label><input type="radio" name="q47" value="C"> Position and momentum</label><br>
                <label><input type="radio" name="q47" value="D"> Energy and momentum</label><br>
            </div>

            <div>
                <h3>48. The Bohr model of the atom assumes:</h3>
                <label><input type="radio" name="q48" value="A"> Continuous energy levels</label><br>
                <label><input type="radio" name="q48" value="B"> Quantized energy levels</label><br>
                <label><input type="radio" name="q48" value="C"> Circular orbits</label><br>
                <label><input type="radio" name="q48" value="D"> Both B and C</label><br>
            </div>

            <div>
                <h3>49. Pair production is a process where:</h3>
                <label><input type="radio" name="q49" value="A"> An electron and a positron annihilate</label><br>
                <label><input type="radio" name="q49" value="B"> A photon creates an electron-positron pair</label><br>
                <label><input type="radio" name="q49" value="C"> Two photons collide</label><br>
                <label><input type="radio" name="q49" value="D"> A nucleus emits a photon</label><br>
            </div>

            <div>
                <h3>50. The Compton effect involves:</h3>
                <label><input type="radio" name="q50" value="A"> Photon scattering by electrons</label><br>
                <label><input type="radio" name="q50" value="B"> Photon absorption by nuclei</label><br>
                <label><input type="radio" name="q50" value="C"> Photon annihilation</label><br>
                <label><input type="radio" name="q50" value="D"> Photon splitting</label><br>
            </div>
            <div>
                <h3>51. A charged particle is moving in a circular path under the influence of a magnetic field. The frequency of its circular motion depends on:</h3>
                <label><input type="radio" name="q51" value="A"> Magnetic field strength</label><br>
                <label><input type="radio" name="q51" value="B"> Charge and mass of the particle</label><br>
                <label><input type="radio" name="q51" value="C"> Both A and B</label><br>
                <label><input type="radio" name="q51" value="D"> None of the above</label><br>
            </div>

            <div>
                <h3>52. The heat generated in a resistor connected to an AC source is proportional to:</h3>
                <label><input type="radio" name="q52" value="A"> \(I_{peak}\)</label><br>
                <label><input type="radio" name="q52" value="B"> \(I_{rms}\)</label><br>
                <label><input type="radio" name="q52" value="C"> \(I_{avg}\)</label><br>
                <label><input type="radio" name="q52" value="D"> Voltage frequency</label><br>
            </div>

            <div>
                <h3>53. The energy required to ionize a hydrogen atom from its ground state is:</h3>
                <label><input type="radio" name="q53" value="A"> 13.6 eV</label><br>
                <label><input type="radio" name="q53" value="B"> 0 eV</label><br>
                <label><input type="radio" name="q53" value="C"> 10.2 eV</label><br>
                <label><input type="radio" name="q53" value="D"> 3.4 eV</label><br>
            </div>

            <div>
                <h3>54. In Young’s double-slit experiment, the fringe width increases if:</h3>
                <label><input type="radio" name="q54" value="A"> Distance between slits increases</label><br>
                <label><input type="radio" name="q54" value="B"> Distance between slits decreases</label><br>
                <label><input type="radio" name="q54" value="C"> Wavelength decreases</label><br>
                <label><input type="radio" name="q54" value="D"> Wavelength increases</label><br>
            </div>

            <div>
                <h3>55. A Carnot engine operates between reservoirs at 400 K and 300 K. If it absorbs 100 J of heat from the hot reservoir, how much work is done?</h3>
                <label><input type="radio" name="q55" value="A"> 25 J</label><br>
                <label><input type="radio" name="q55" value="B"> 75 J</label><br>
                <label><input type="radio" name="q55" value="C"> 50 J</label><br>
                <label><input type="radio" name="q55" value="D"> 100 J</label><br>
            </div>

            <div>
                <h3>56. The wavelength of a photon required to eject an electron with zero kinetic energy from a metal surface with work function 2 eV is:</h3>
                <label><input type="radio" name="q56" value="A"> 620 nm</label><br>
                <label><input type="radio" name="q56" value="B"> 310 nm</label><br>
                <label><input type="radio" name="q56" value="C"> 1240 nm</label><br>
                <label><input type="radio" name="q56" value="D"> 155 nm</label><br>
            </div>

            <div>
                <h3>57. In an LCR circuit at resonance, the impedance of the circuit is:</h3>
                <label><input type="radio" name="q57" value="A"> Maximum</label><br>
                <label><input type="radio" name="q57" value="B"> Minimum</label><br>
                <label><input type="radio" name="q57" value="C"> Zero</label><br>
                <label><input type="radio" name="q57" value="D"> Infinite</label><br>
            </div>

            <div>
                <h3>58. The kinetic energy of an electron accelerated through a potential difference of 1 kV is:</h3>
                <label><input type="radio" name="q58" value="A"> 1 eV</label><br>
                <label><input type="radio" name="q58" value="B"> 100 eV</label><br>
                <label><input type="radio" name="q58" value="C"> 1 keV</label><br>
                <label><input type="radio" name="q58" value="D"> 10 keV</label><br>
            </div>

            <div>
                <h3>59. The change in entropy when 1 kg of water is converted to ice at 0°C is:</h3>
                <label><input type="radio" name="q59" value="A"> Positive</label><br>
                <label><input type="radio" name="q59" value="B"> Negative</label><br>
                <label><input type="radio" name="q59" value="C"> Zero</label><br>
                <label><input type="radio" name="q59" value="D"> Infinite</label><br>
            </div>

            <div>
                <h3>60. A photon and a neutron have the same momentum. Which has a longer wavelength?</h3>
                <label><input type="radio" name="q60" value="A"> Photon</label><br>
                <label><input type="radio" name="q60" value="B"> Neutron</label><br>
                <label><input type="radio" name="q60" value="C"> Both have the same wavelength</label><br>
                <label><input type="radio" name="q60" value="D"> Cannot be determined</label><br>
            </div>
            <div>
                <h3>61. A capacitor of 10 µF is charged to 50 V and then disconnected. What is the energy stored in the capacitor?</h3>
                <label><input type="radio" name="q61" value="A"> 0.0125 J</label><br>
                <label><input type="radio" name="q61" value="B"> 0.025 J</label><br>
                <label><input type="radio" name="q61" value="C"> 0.125 J</label><br>
                <label><input type="radio" name="q61" value="D"> 0.25 J</label><br>
            </div>

            <div>
                <h3>62. The focal length of a lens is 20 cm. An object is placed 60 cm from the lens. Where is the image formed?</h3>
                <label><input type="radio" name="q62" value="A"> 30 cm</label><br>
                <label><input type="radio" name="q62" value="B"> 40 cm</label><br>
                <label><input type="radio" name="q62" value="C"> 60 cm</label><br>
                <label><input type="radio" name="q62" value="D"> 80 cm</label><br>
            </div>

            <div>
                <h3>63. The magnetic flux through a coil changes from 0.02 Wb to 0.06 Wb in 0.1 seconds. The induced emf is:</h3>
                <label><input type="radio" name="q63" value="A"> 0.4 V</label><br>
                <label><input type="radio" name="q63" value="B"> 0.8 V</label><br>
                <label><input type="radio" name="q63" value="C"> 1.0 V</label><br>
                <label><input type="radio" name="q63" value="D"> 1.2 V</label><br>
            </div>

            <div>
                <h3>64. An electron in a hydrogen atom makes a transition from \(n=3\) to \(n=2\). The wavelength of the emitted photon is:</h3>
                <label><input type="radio" name="q64" value="A"> 656 nm</label><br>
                <label><input type="radio" name="q64" value="B"> 486 nm</label><br>
                <label><input type="radio" name="q64" value="C"> 434 nm</label><br>
                <label><input type="radio" name="q64" value="D"> 410 nm</label><br>
            </div>

            <div>
                <h3>65. The root mean square speed of gas molecules at temperature \(T\) is proportional to:</h3>
                <label><input type="radio" name="q65" value="A"> \(T\)</label><br>
                <label><input type="radio" name="q65" value="B"> \(\sqrt{T}\)</label><br>
                <label><input type="radio" name="q65" value="C"> \(1/T\)</label><br>
                <label><input type="radio" name="q65" value="D"> \(1/\sqrt{T}\)</label><br>
            </div>

            <div>
                <h3>66. The Doppler effect is observed when:</h3>
                <label><input type="radio" name="q66" value="A"> The source of waves and observer are stationary</label><br>
                <label><input type="radio" name="q66" value="B"> Only the source is moving</label><br>
                <label><input type="radio" name="q66" value="C"> Only the observer is moving</label><br>
                <label><input type="radio" name="q66" value="D"> Either the source or observer is moving</label><br>
            </div>

            <div>
                <h3>67. A monochromatic light of wavelength 500 nm falls on a single slit of width 0.1 mm. The angular width of the central maximum is approximately:</h3>
                <label><input type="radio" name="q67" value="A"> 0.1 radians</label><br>
                <label><input type="radio" name="q67" value="B"> 0.2 radians</label><br>
                <label><input type="radio" name="q67" value="C"> 0.5 radians</label><br>
                <label><input type="radio" name="q67" value="D"> 1 radians</label><br>
            </div>

            <div>
                <h3>68. A particle undergoes simple harmonic motion. Its total energy is proportional to:</h3>
                <label><input type="radio" name="q68" value="A"> Square of its amplitude</label><br>
                <label><input type="radio" name="q68" value="B"> Square of its frequency</label><br>
                <label><input type="radio" name="q68" value="C"> Both A and B</label><br>
                <label><input type="radio" name="q68" value="D"> None of the above</label><br>
            </div>

            <div>
                <h3>69. A Carnot refrigerator transfers heat at a rate of 200 W from a reservoir at 260 K to a reservoir at 300 K. The input power required is:</h3>
                <label><input type="radio" name="q69" value="A"> 50 W</label><br>
                <label><input type="radio" name="q69" value="B"> 60 W</label><br>
                <label><input type="radio" name="q69" value="C"> 67 W</label><br>
                <label><input type="radio" name="q69" value="D"> 77 W</label><br>
            </div>

            <div>
                <h3>70. A photon and an electron have the same energy. Which has the longer wavelength?</h3>
                <label><input type="radio" name="q70" value="A"> Photon</label><br>
                <label><input type="radio" name="q70" value="B"> Electron</label><br>
                <label><input type="radio" name="q70" value="C"> Both have the same wavelength</label><br>
                <label><input type="radio" name="q70" value="D"> Cannot be determined</label><br>
            </div>
            <div>
                <h3>71. A gas is confined in a cylinder with a piston. The piston is displaced sinusoidally, causing the gas to oscillate. If the process is adiabatic, the pressure and volume follow the relation:</h3>
                <label><input type="radio" name="q71" value="A"> \(PV = \text{constant}\)</label><br>
                <label><input type="radio" name="q71" value="B"> \(P^2V = \text{constant}\)</label><br>
                <label><input type="radio" name="q71" value="C"> \(PV^\gamma = \text{constant}\)</label><br>
                <label><input type="radio" name="q71" value="D"> \(P^2V^2 = \text{constant}\)</label><br>
            </div>

            <div>
                <h3>72. In a vertical cylinder, a gas is confined by a piston of mass \(m\). If the piston oscillates due to small displacements, the angular frequency of oscillation depends on:</h3>
                <label><input type="radio" name="q72" value="A"> Temperature of the gas</label><br>
                <label><input type="radio" name="q72" value="B"> Pressure and volume of the gas</label><br>
                <label><input type="radio" name="q72" value="C"> Mass of the piston</label><br>
                <label><input type="radio" name="q72" value="D"> All of the above</label><br>
            </div>

            <div>
                <h3>73. A gas in a cylinder undergoes an isothermal compression. The work done is proportional to:</h3>
                <label><input type="radio" name="q73" value="A"> Volume change</label><br>
                <label><input type="radio" name="q73" value="B"> Pressure change</label><br>
                <label><input type="radio" name="q73" value="C"> Temperature</label><br>
                <label><input type="radio" name="q73" value="D"> Logarithm of volume change</label><br>
            </div>

            <div>
                <h3>74. In an oscillating system, the spring constant \(k\) is replaced by a gas system confined in a cylinder. The effective spring constant of the gas is proportional to:</h3>
                <label><input type="radio" name="q74" value="A"> Volume of the gas</label><br>
                <label><input type="radio" name="q74" value="B"> Pressure of the gas</label><br>
                <label><input type="radio" name="q74" value="C"> Temperature of the gas</label><br>
                <label><input type="radio" name="q74" value="D"> All of the above</label><br>
            </div>

            <div>
                <h3>75. A piston oscillates with small amplitudes in a cylinder containing an ideal gas. If the process is isothermal, the restoring force is proportional to:</h3>
                <label><input type="radio" name="q75" value="A"> Displacement</label><br>
                <label><input type="radio" name="q75" value="B"> Displacement squared</label><br>
                <label><input type="radio" name="q75" value="C"> Temperature</label><br>
                <label><input type="radio" name="q75" value="D"> Volume change</label><br>
            </div>

            <div>
                <h3>76. In a cyclic process involving an ideal gas, the work done per cycle is equal to:</h3>
                <label><input type="radio" name="q76" value="A"> Change in internal energy</label><br>
                <label><input type="radio" name="q76" value="B"> Heat absorbed minus heat rejected</label><br>
                <label><input type="radio" name="q76" value="C"> Heat rejected minus heat absorbed</label><br>
                <label><input type="radio" name="q76" value="D"> Zero</label><br>
            </div>

            <div>
                <h3>77. A mass attached to a spring oscillates inside a heat reservoir. Over time, the amplitude of oscillation decreases due to:</h3>
                <label><input type="radio" name="q77" value="A"> Damping</label><br>
                <label><input type="radio" name="q77" value="B"> Heat exchange</label><br>
                <label><input type="radio" name="q77" value="C"> Both A and B</label><br>
                <label><input type="radio" name="q77" value="D"> None of the above</label><br>
            </div>

            <div>
                <h3>78. A gas in a cylinder undergoes rapid compression, leading to oscillations in pressure and temperature. The oscillations are a result of:</h3>
                <label><input type="radio" name="q78" value="A"> Isothermal changes</label><br>
                <label><input type="radio" name="q78" value="B"> Adiabatic changes</label><br>
                <label><input type="radio" name="q78" value="C"> Heat transfer</label><br>
                <label><input type="radio" name="q78" value="D"> Irreversible processes</label><br>
            </div>

            <div>
                <h3>79. An ideal gas undergoes simple harmonic motion in a vertical cylinder under a piston. The angular frequency of oscillation is proportional to:</h3>
                <label><input type="radio" name="q79" value="A"> \(\sqrt{P/V}\)</label><br>
                <label><input type="radio" name="q79" value="B"> \(\sqrt{V/P}\)</label><br>
                <label><input type="radio" name="q79" value="C"> \(P/V\)</label><br>
                <label><input type="radio" name="q79" value="D"> \(\sqrt{T}\)</label><br>
            </div>

            <div>
                <h3>80. A gas-filled balloon oscillates vertically in response to buoyant forces. The restoring force depends on:</h3>
                <label><input type="radio" name="q80" value="A"> Pressure inside the balloon</label><br>
                <label><input type="radio" name="q80" value="B"> Volume of displaced air</label><br>
                <label><input type="radio" name="q80" value="C"> Density of air</label><br>
                <label><input type="radio" name="q80" value="D"> All of the above</label><br>
            </div>
            <div>
                <h3>81. According to Gauss's law, the electric flux through a closed surface is proportional to:</h3>
                <label><input type="radio" name="q81" value="A"> Electric field</label><br>
                <label><input type="radio" name="q81" value="B"> Charge enclosed</label><br>
                <label><input type="radio" name="q81" value="C"> Area of the surface</label><br>
                <label><input type="radio" name="q81" value="D"> Permittivity of free space</label><br>
            </div>

            <div>
                <h3>82. A spherical shell of radius \(R\) is uniformly charged. What is the electric field at a distance \(r > R\) from the center of the shell?</h3>
                <label><input type="radio" name="q82" value="A"> \(kQ/r^2\)</label><br>
                <label><input type="radio" name="q82" value="B"> \(kQ/R^2\)</label><br>
                <label><input type="radio" name="q82" value="C"> \(0\)</label><br>
                <label><input type="radio" name="q82" value="D"> \(kQ/r\)</label><br>
            </div>

            <div>
                <h3>83. The electric field inside a uniformly charged spherical shell is:</h3>
                <label><input type="radio" name="q83" value="A"> Zero</label><br>
                <label><input type="radio" name="q83" value="B"> Uniform</label><br>
                <label><input type="radio" name="q83" value="C"> Radially outward</label><br>
                <label><input type="radio" name="q83" value="D"> Radially inward</label><br>
            </div>

            <div>
                <h3>84. Using Gauss's law, the electric field due to an infinitely long line of charge with linear charge density \(\lambda\) at a distance \(r\) is:</h3>
                <label><input type="radio" name="q84" value="A"> \(k\lambda/r\)</label><br>
                <label><input type="radio" name="q84" value="B"> \(\lambda/2\pi\epsilon_0r\)</label><br>
                <label><input type="radio" name="q84" value="C"> \(k\lambda/r^2\)</label><br>
                <label><input type="radio" name="q84" value="D"> \(0\)</label><br>
            </div>

            <div>
                <h3>85. A plane sheet of charge has a surface charge density \(\sigma\). Using Gauss's law, the electric field near the sheet is:</h3>
                <label><input type="radio" name="q85" value="A"> \(\sigma/\epsilon_0\)</label><br>
                <label><input type="radio" name="q85" value="B"> \(2\sigma/\epsilon_0\)</label><br>
                <label><input type="radio" name="q85" value="C"> \(\sigma/2\epsilon_0\)</label><br>
                <label><input type="radio" name="q85" value="D"> \(0\)</label><br>
            </div>

            <div>
                <h3>86. A point charge \(q\) is placed at the center of a spherical Gaussian surface. The electric flux through the surface depends on:</h3>
                <label><input type="radio" name="q86" value="A"> Radius of the sphere</label><br>
                <label><input type="radio" name="q86" value="B"> Magnitude of charge</label><br>
                <label><input type="radio" name="q86" value="C"> Both A and B</label><br>
                <label><input type="radio" name="q86" value="D"> Neither A nor B</label><br>
            </div>

            <div>
                <h3>87. Ampere's law relates the magnetic field along a closed path to:</h3>
                <label><input type="radio" name="q87" value="A"> Electric flux through the path</label><br>
                <label><input type="radio" name="q87" value="B"> Current enclosed by the path</label><br>
                <label><input type="radio" name="q87" value="C"> Total charge enclosed</label><br>
                <label><input type="radio" name="q87" value="D"> Magnetic flux through the path</label><br>
            </div>

            <div>
                <h3>88. A long, straight current-carrying wire produces a magnetic field. According to Ampere's law, the field strength at a distance \(r\) is proportional to:</h3>
                <label><input type="radio" name="q88" value="A"> \(1/r^2\)</label><br>
                <label><input type="radio" name="q88" value="B"> \(1/r\)</label><br>
                <label><input type="radio" name="q88" value="C"> \(r^2\)</label><br>
                <label><input type="radio" name="q88" value="D"> \(r\)</label><br>
            </div>

            <div>
                <h3>89. The magnetic field inside a solenoid of length \(L\), having \(N\) turns, carrying current \(I\), is given by:</h3>
                <label><input type="radio" name="q89" value="A"> \(\mu_0NI/L\)</label><br>
                <label><input type="radio" name="q89" value="B"> \(\mu_0I/L\)</label><br>
                <label><input type="radio" name="q89" value="C"> \(\mu_0N/L\)</label><br>
                <label><input type="radio" name="q89" value="D"> \(\mu_0NI\)</label><br>
            </div>

            <div>
                <h3>90. A toroid has \(N\) turns and carries a current \(I\). Using Ampere's law, the magnetic field inside the toroid is proportional to:</h3>
                <label><input type="radio" name="q90" value="A"> \(NI/r\)</label><br>
                <label><input type="radio" name="q90" value="B"> \(\mu_0NI/r\)</label><br>
                <label><input type="radio" name="q90" value="C"> \(N^2I/r\)</label><br>
                <label><input type="radio" name="q90" value="D"> \(NI/r^2\)</label><br>
            </div>
            <div>
                <h3>91. A charged particle of mass \(m\) and charge \(q\) is in a uniform electric field \(\mathbf{E}\) and uniform magnetic field \(\mathbf{B}\). If \(\mathbf{E}\) and \(\mathbf{B}\) are perpendicular to each other, what is the trajectory of the particle if its initial velocity is zero?</h3>
                <label><input type="radio" name="q91" value="A"> Straight line</label><br>
                <label><input type="radio" name="q91" value="B"> Circular</label><br>
                <label><input type="radio" name="q91" value="C"> Helical</label><br>
                <label><input type="radio" name="q91" value="D"> Cycloidal</label><br>
            </div>

            <div>
                <h3>92. In a Carnot cycle, the working substance is an ideal gas with molar heat capacity \(C_v = \frac{3}{2}R\). If the gas absorbs 100 J of heat from the hot reservoir, calculate the total work done by the gas if the temperature ratio is \(T_h/T_c = 2\).</h3>
                <label><input type="radio" name="q92" value="A"> 50 J</label><br>
                <label><input type="radio" name="q92" value="B"> 75 J</label><br>
                <label><input type="radio" name="q92" value="C"> 100 J</label><br>
                <label><input type="radio" name="q92" value="D"> 150 J</label><br>
            </div>

            <div>
                <h3>93. A spherical Gaussian surface encloses two point charges, \(q_1 = +5\mu C\) and \(q_2 = -3\mu C\). What is the net electric flux through the surface?</h3>
                <label><input type="radio" name="q93" value="A"> \(1.8 \times 10^5 \, \text{N·m}^2/\text{C}\)</label><br>
                <label><input type="radio" name="q93" value="B"> \(0.9 \times 10^5 \, \text{N·m}^2/\text{C}\)</label><br>
                <label><input type="radio" name="q93" value="C"> \(3.6 \times 10^5 \, \text{N·m}^2/\text{C}\)</label><br>
                <label><input type="radio" name="q93" value="D"> Zero</label><br>
            </div>

            <div>
                <h3>94. In Young’s double-slit experiment, a thin film of refractive index \(n\) and thickness \(t\) is introduced in front of one slit. The shift in the central fringe position is proportional to:</h3>
                <label><input type="radio" name="q94" value="A"> \(t\)</label><br>
                <label><input type="radio" name="q94" value="B"> \(n\)</label><br>
                <label><input type="radio" name="q94" value="C"> \(t(n-1)\)</label><br>
                <label><input type="radio" name="q94" value="D"> \(t(1-n)\)</label><br>
            </div>

            <div>
                <h3>95. An electron in a hydrogen atom makes a transition from \(n=4\) to \(n=2\). The wavelength of the emitted photon lies in which region of the electromagnetic spectrum?</h3>
                <label><input type="radio" name="q95" value="A"> Visible</label><br>
                <label><input type="radio" name="q95" value="B"> Infrared</label><br>
                <label><input type="radio" name="q95" value="C"> Ultraviolet</label><br>
                <label><input type="radio" name="q95" value="D"> X-rays</label><br>
            </div>

            <div>
                <h3>96. A cylindrical capacitor is filled with a dielectric of constant \(\kappa\). If the dielectric is replaced with two different dielectrics \(\kappa_1\) and \(\kappa_2\), how does the equivalent capacitance change?</h3>
                <label><input type="radio" name="q96" value="A"> Increases</label><br>
                <label><input type="radio" name="q96" value="B"> Decreases</label><br>
                <label><input type="radio" name="q96" value="C"> Depends on the arrangement</label><br>
                <label><input type="radio" name="q96" value="D"> Remains constant</label><br>
            </div>

            <div>
                <h3>97. A particle is moving in a potential field \(V(x) = \frac{1}{2}kx^2\). The time period of oscillation depends on:</h3>
                <label><input type="radio" name="q97" value="A"> \(k\)</label><br>
                <label><input type="radio" name="q97" value="B"> Mass of the particle</label><br>
                <label><input type="radio" name="q97" value="C"> Both A and B</label><br>
                <label><input type="radio" name="q97" value="D"> Neither A nor B</label><br>
            </div>

            <div>
                <h3>98. A gas in a cylinder undergoes a quasi-static adiabatic process. If the pressure is halved, the volume changes by a factor of:</h3>
                <label><input type="radio" name="q98" value="A"> \(2^{\gamma}\)</label><br>
                <label><input type="radio" name="q98" value="B"> \(2^{1/\gamma}\)</label><br>
                <label><input type="radio" name="q98" value="C"> \(2^{-\gamma}\)</label><br>
                <label><input type="radio" name="q98" value="D"> \(2^{-\gamma/2}\)</label><br>
            </div>

            <div>
                <h3>99. The Bohr radius for the hydrogen atom is approximately \(0.53 \, \text{Å}\). If the nucleus were replaced by a particle of double charge, the Bohr radius would:</h3>
                <label><input type="radio" name="q99" value="A"> Double</label><br>
                <label><input type="radio" name="q99" value="B"> Halve</label><br>
                <label><input type="radio" name="q99" value="C"> Remain the same</label><br>
                <label><input type="radio" name="q99" value="D"> Decrease by a factor of \(4\)</label><br>
            </div>

            <div>
                <h3>100. In a system of three charges placed at the corners of an equilateral triangle, the net electric potential at the center of the triangle depends on:</h3>
                <label><input type="radio" name="q100" value="A"> Sum of the charges</label><br>
                <label><input type="radio" name="q100" value="B"> Magnitudes of individual charges</label><br>
                <label><input type="radio" name="q100" value="C"> Distance from the charges to the center</label><br>
                <label><input type="radio" name="q100" value="D"> All of the above</label><br>
            </div>


        </fieldset>

        <h2>Download the excel file on your machine and upload it to the google form provided below</h2>
        <button type="button" onclick="submitQuiz()">Submit and Download</button>
    </form>

    <p>
        <a href="https://forms.gle/McvaDYB1vibnL3ZU7" target="_blank" style="font-size: 18px; color: blue; text-decoration: underline;">
            Upload the excel file
        </a>
    </p>

    <script>
        function submitQuiz() {
            const form = document.getElementById('quiz-form');
            const formData = new FormData(form);

            const answers = {};
            formData.forEach((value, key) => {
                answers[key] = value;
            });

            const correctAnswers = {
                <!-- Mechanics-->
                q1: "B",
                q2: "C",
                q3: "C",
                q4: "B",
                q5: "B",
                q6: "A",
                q7: "C",
                q8: "B",
                q9: "C",
                q10: "A",

                <!-- Thermodynamics-->
                q11: "C",
                q12: "C",
                q13: "C",
                q14: "D",
                q15: "A",
                q16: "C",
                q17: "C",
                q18: "A",
                q19: "C",
                q20: "B",

                <!-- Electromagnetism -->
                q21: "A",
                q22: "B",
                q23: "B",
                q24: "C",
                q25: "A",
                q26: "B",
                q27: "A",
                q28: "A",
                q29: "B",
                q30: "B",

            
                <!-- Optics-->
                q31: "A",
                q32: "C",
                q33: "A",
                q34: "C",
                q35: "B",
                q36: "D",
                q37: "A",
                q38: "A",
                q39: "C",
                q40: "A",

                <!-- Modern Physics-->
                q41: "C",
                q42: "B",
                q43: "B",
                q44: "A",
                q45: "B",
                q46: "C",
                q47: "C",
                q48: "D",
                q49: "B",
                q50: "A",

                <!-- Interdisciplinary (51–60)-->
                q51: "C",
                q52: "B",
                q53: "A",
                q54: "D",
                q55: "B",
                q56: "A",
                q57: "B",
                q58: "C",
                q59: "B",
                q60: "A",

                <!-- Thermodynamics and Mechanics (61–70)-->
                q61: "B",
                q62: "D",
                q63: "C",
                q64: "A",
                q65: "B",
                q66: "D",
                q67: "B",
                q68: "A",
                q69: "C",
                q70: "A",

                <!-- Thermodynamics and Oscillations (71–80)-->
                q71: "C",
                q72: "D",
                q73: "D",
                q74: "B",
                q75: "A",
                q76: "B",
                q77: "C",
                q78: "B",
                q79: "A",
                q80: "D",

                <!-- Electrostatics with Gauss’s and Ampere’s Law (81–90)-->
                q81: "B",
                q82: "A",
                q83: "A",
                q84: "B",
                q85: "A",
                q86: "B",
                q87: "B",
                q88: "B",
                q89: "D",
                q90: "B",

                <!-- Toughest Questions (91–100)-->
                q91: "D",
                q92: "A",
                q93: "A",
                q94: "C",
                q95: "C",
                q96: "C",
                q97: "C",
                q98: "B",
                q99: "B",
                q100: "D",
            };

            let score = 0;
            for (const [key, value] of Object.entries(answers)) {
                if (correctAnswers[key] === value) {
                    score++;
                }
            }

            const worksheetData = [["Field", "Response"]];
            for (const [key, value] of Object.entries(answers)) {
                worksheetData.push([key, value, correctAnswers[key]]);
            }
            worksheetData.push([], ["Total Score", score]);

            const worksheet = XLSX.utils.aoa_to_sheet(worksheetData);
            const workbook = XLSX.utils.book_new();
            XLSX.utils.book_append_sheet(workbook, worksheet, "Quiz Answers");
            XLSX.writeFile(workbook, "quiz_answers.xlsx");

            alert(`Your total score is: ${score}`);
        }
    </script>
</body>
</html>