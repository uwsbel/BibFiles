# SBEL terramechanics publications, 2016 to present

Lab-authored work on the three terrain-modeling approaches developed and used at the
Simulation-Based Engineering Laboratory, University of Wisconsin-Madison:

- **SCM**, the semi-empirical Soil Contact Model, an expeditious model for vehicle-scale studies.
- **CRM**, the Continuum Representation Model, a GPU smoothed-particle-hydrodynamics treatment of
  granular terrain.
- **DEM**, the discrete element method, particle-resolved granular simulation.

References are in Chicago style so the list can be pasted into correspondence directly. Entries
are grouped by method, then journal articles before conference papers, each in reverse
chronological order.

Compiled 2026-08-12 from the shared `uwsbel/BibFiles` collection. To grow it: add the reference
here in the same style, and keep the BibTeX entry in the appropriate `refs<Topic>.bib` file so the
two stay in step. See "Scope" at the end for what is deliberately excluded.

---

## 1. SCM: semi-empirical soil contact model, and its calibration

### Journal articles

Zhang, Yuemin, Junpeng Dai, Wei Hu, and Dan Negrut. "Using High Fidelity Discrete Element
Simulation to Calibrate an Expeditious Terramechanics Model in a Multibody Dynamics Framework."
*Multibody System Dynamics* 65, no. 4 (2025): 505-544. https://doi.org/10.1007/s11044-024-10051-z.

Hu, Wei, Pei Li, Huzaifa Mustafa Unjhawala, Radu Serban, and Dan Negrut. "Calibration of an
Expeditious Terramechanics Model Using a Higher-Fidelity Model, Bayesian Inference, and a Virtual
Bevameter Test." *Journal of Field Robotics* 41, no. 3 (2024): 550-569.
https://doi.org/10.1002/rob.22276.

Serban, Radu, Jay Taves, and Zhenhao Zhou. "Real-Time Simulation of Ground Vehicles on Deformable
Terrain." *Journal of Computational and Nonlinear Dynamics* 18, no. 8 (2023): 081007.
https://doi.org/10.1115/1.4056851.

Tasora, Alessandro, Dario Mangoni, Dan Negrut, Radu Serban, and Paramsothy Jayakumar. "Deformable
Soil with Adaptive Level of Detail for Tracked and Wheeled Vehicles." *International Journal of
Vehicle Performance* 5, no. 1 (2019): 60-76. https://doi.org/10.1504/IJVP.2019.097098.

### Conference papers

Hu, Wei, Pei Li, Huzaifa Unjhawala, Radu Serban, and Dan Negrut. "Calibration of an Expeditious
Terramechanics Model Using a Higher-Fidelity Model, Bayesian Inference, and a Virtual Bevameter
Test." In *Proceedings of the ECCOMAS Thematic Conference on Multibody Dynamics*, 2023.

Serban, Radu, Jay Taves, and Zhenhao Zhou. "Real Time Simulation of Ground Vehicles on Deformable
Terrain." In *Proceedings of the ASME International Design Engineering Technical Conferences
(IDETC/CIE)*. St. Louis, MO, 2022.

---

## 2. CRM: continuum representation of granular terrain via SPH

### Journal articles

Unjhawala, Huzaifa Mustafa, Luning Bakke, Harry Zhang, Michael Taylor, Ganesh Arivoli, Radu
Serban, and Dan Negrut. "A Physics-Based Continuum Model for Versatile, Scalable, and Fast
Terramechanics Simulation." *Journal of Terramechanics* 124 (2026): 101150.
https://doi.org/10.1016/j.jterra.2026.101150.

Hu, Wei, Pei Li, Arno Rogg, Alexander Schepelmann, Samuel Chandler, Ken Kamrin, and Dan Negrut.
"A Study Demonstrating That Using Gravitational Offset to Prepare Extraterrestrial Mobility
Missions Is Misleading." *Journal of Field Robotics* 42, no. 7 (2025): 3772-3794.
https://doi.org/10.1002/rob.22597.

Hu, Wei, Zhenhao Zhou, Samuel Chandler, Dimitrios Apostolopoulos, Ken Kamrin, Radu Serban, and
Dan Negrut. "Traction Control Design for Off-Road Mobility Using an SPH-DAE Co-simulation
Framework." *Multibody System Dynamics* 55 (2022): 165-188.
https://doi.org/10.1007/s11044-022-09815-2.

Hu, Wei, Milad Rakhsha, Lijing Yang, Ken Kamrin, and Dan Negrut. "Modeling Granular Material
Dynamics and Its Two-Way Coupling with Moving Solid Bodies Using a Continuum Representation and
the SPH Method." *Computer Methods in Applied Mechanics and Engineering* 385 (2021): 114022.
https://doi.org/10.1016/j.cma.2021.114022.

### Conference papers

Hu, Wei, Jason Zhou, Radu Serban, and Dan Negrut. "Using an SPH-Based Continuum Representation of
Granular Terrain to Simulate the Rover Mobility." In *Proceedings of the ASME International Design
Engineering Technical Conferences (IDETC/CIE)*, 85468: V009T09A028, 2021.
https://doi.org/10.1115/DETC2021-71289.

---

## 3. DEM: particle-resolved discrete element simulation

### Journal articles

Zhang, Ruochun, Bonaventura Tagliafierro, Colin Vanden Heuvel, Shlok Sabarwal, Luning Bakke,
Yulong Yue, Xin Wei, Radu Serban, and Dan Negrut. "Chrono DEM-Engine: A Discrete Element Method
Dual-GPU Simulator with Customizable Contact Forces and Element Shape." *Computer Physics
Communications* 300 (2024): 109196. https://doi.org/10.1016/j.cpc.2024.109196.

Zhang, Ruochun, Colin Vanden Heuvel, Alexander Schepelmann, Arno Rogg, Dimitrios Apostolopoulos,
Samuel Chandler, Radu Serban, and Dan Negrut. "A GPU-Accelerated Simulator for the DEM Analysis of
Granular Systems Composed of Clump-Shaped Elements." *Engineering with Computers* 40, no. 4
(2024): 2559-2579. https://doi.org/10.1007/s00366-023-01921-9.

Foldager, Frederik F., Lars J. Munkholm, Ole Balling, Radu Serban, Dan Negrut, Richard J. Heck,
and Ole Green. "Modeling Soil Aggregate Fracture Using the Discrete Element Method." *Soil and
Tillage Research* 218 (2022): 105295.

Fang, Luning, Ruochun Zhang, Colin Vanden Heuvel, Radu Serban, and Dan Negrut. "Chrono::GPU: An
Open-Source Simulation Package for Granular Dynamics Using the Discrete Element Method."
*Processes* 9, no. 10 (2021): 1813. https://doi.org/10.3390/pr9101813.

Kelly, Conlain, Nicholas Olsen, and Dan Negrut. "Billion Degree of Freedom Granular Dynamics
Simulation on Commodity Hardware via Heterogeneous Data-Type Representation." *Multibody System
Dynamics* 50 (2020): 355-379.

Rakhsha, Milad, Conlain Kelly, Nicholas Olsen, Radu Serban, and Dan Negrut. "Multibody Dynamics
vs. Fluid Dynamics: Two Perspectives on the Dynamics of Granular Flows." *Journal of Computational
and Nonlinear Dynamics* 15, no. 9 (2020). https://doi.org/10.1115/1.4047237.

Pazouki, Arman, Michal Kwarta, Kyle Williams, William Likos, Radu Serban, Paramsothy Jayakumar,
and Dan Negrut. "Compliant Contact versus Rigid Contact: A Comparison in the Context of Granular
Dynamics." *Physical Review E* 96, no. 4 (2017): 042905.
https://doi.org/10.1103/PhysRevE.96.042905.

Melanz, Daniel, Paramsothy Jayakumar, and Dan Negrut. "Experimental Validation of a Differential
Variational Inequality-Based Approach for Handling Friction and Contact in Vehicle/Granular-Terrain
Interaction." *Journal of Terramechanics* 65 (2016): 1-13.
https://doi.org/10.1016/j.jterra.2016.01.004.

### Conference papers

Zhang, Ruochun, Colin Vanden Heuvel, Radu Serban, and Dan Negrut. "DEM Simulation of GRC-1
Simulant Using Two GPUs." In *Proceedings of the ASME International Design Engineering Technical
Conferences (IDETC/CIE)*, 2023.

Kelly, Conlain, Nicholas Olsen, Colin Vanden Heuvel, Radu Serban, and Dan Negrut. "Towards the
Democratization of Many-Body Dynamics: Billion Degree of Freedom Simulation of Granular Material
on Commodity Hardware." In *Proceedings of the ECCOMAS Thematic Conference on Multibody Dynamics*.
Duisburg, Germany, 2019.

Kelly, Conlain, Nicholas Olsen, and Dan Negrut. "Billion Degree-of-Freedom Granular Dynamics
Simulation on Commodity Hardware." In *Proceedings of the ASME International Design Engineering
Technical Conferences (IDETC/CIE)*. Anaheim, CA, 2019.

Olsen, Nicholas, and Dan Negrut. "A Co-simulation Framework for the Analysis of Complex Granular
Dynamics Problems." In *Proceedings of the ASME International Design Engineering Technical
Conferences (IDETC/CIE)*, 2019.

Olsen, Nicholas, Radu Serban, Alessandro Tasora, and Dan Negrut. "Hybrid OpenMP-MPI Simulation for
Large-Scale Granular Dynamics in Chrono." In *Proceedings of the International Multibody Systems
Dynamics Conference*. Lisbon, Portugal, 2018.

Negrut, Dan, and Hammad Mazhar. "Sand to Mud to Fording: Modeling and Simulation for Off-Road
Ground Vehicle Mobility Analysis." In *Proceedings of the International Workshop on Bifurcation
and Degradation in Geomaterials*, 235-247, 2017.

---

## 4. Vehicle-terrain co-simulation, validation, and applications

### Journal articles

Zhang, Harry, Ganesh Arivoli, Huzaifa Unjhawala, Luning Bakke, Radu Serban, and Dan Negrut.
"Data-Driven Bulldozer Blade Control for Autonomous Terrain Leveling." *Advanced Robotics
Research* (2026): e202500180. https://doi.org/10.1002/adrr.202500180.

Serban, Radu, Dan Negrut, Antonio M. Recuero, and Paramsothy Jayakumar. "An Integrated Framework
for High-Performance, High-Fidelity Simulation of Ground Vehicle-Tyre-Terrain Interaction."
*International Journal of Vehicle Performance* 5, no. 3 (2019): 233-259.

Recuero, Antonio M., Radu Serban, B. Peterson, Hiroyuki Sugiyama, Paramsothy Jayakumar, and Dan
Negrut. "A High-Fidelity Approach for Vehicle Mobility Simulation: Nonlinear Finite Element Tires
Operating on Granular Material." *Journal of Terramechanics* 72 (2017): 39-54.
https://doi.org/10.1016/j.jterra.2017.04.002.

### Conference papers

Witt, Bret, Jamiul Haque, Patrick Chen, Huzaifa Unjhawala, Ganesh Arivoli, Harry Zhang, Json Zhou,
Matteo Santelia, Federico Reato, Alessandro Tasora, Luning Bakke, Radu Serban, and Dan Negrut. "An
Analysis of the Mobility Performance of the Apollo Mission Lunar Roving Vehicle (LRV)." In
*Proceedings of the 12th ECCOMAS Thematic Conference on Multibody Dynamics*. Innsbruck, Austria,
2025.

Serban, Radu, Dan Negrut, and Wei Hu. "A Flexible Co-simulation Framework for Vehicle-Terrain
Interaction." In *Proceedings of the ECCOMAS Thematic Conference on Multibody Dynamics*, 2023.

Serban, Radu, Nicholas Olsen, Dan Negrut, Antonio M. Recuero, and Paramsothy Jayakumar. "A
Co-simulation Framework for High-Performance, High-Fidelity Simulation of Ground Vehicle-Terrain
Interaction." In *AVT-265: Integrated Virtual NATO Vehicle Development*. Vilnius, Lithuania, 2017.

Serban, Radu, Nicholas Olsen, and Dan Negrut. "High Performance Computing Framework for
Co-simulation of Vehicle-Terrain Interaction." In *Proceedings of the NDIA Ground Vehicle Systems
Engineering and Technology Symposium (GVSETS)*, 2017.

---

## 5. SBEL technical reports

Technical reports are not peer reviewed, but several document validation work that has no journal
counterpart. All are at https://sbel.wisc.edu/tech-reports/.

Bakke, Luning, Zhenhao Zhou, and Dan Negrut. "A Framework for Designing NASA's RASSOR Rover Using
Project Chrono." Technical Report TR-2024-02. Simulation-Based Engineering Laboratory, University
of Wisconsin-Madison, 2024.

Hu, Wei, and Dan Negrut. "A Summary of Continuum Representation Model Results of Single Wheel and
Full Rover Tests Using GRC-1 and GRC-3 Simulant." Technical Report TR-2023-02. Simulation-Based
Engineering Laboratory, University of Wisconsin-Madison, 2023.

Fang, Luning, Ruochun Zhang, Jason Zhou, and Dan Negrut. "On the Validation of Chrono::Granular."
Technical Report TR-2020-06. Simulation-Based Engineering Laboratory, University of
Wisconsin-Madison, 2020.

Hu, Wei, Radu Serban, and Dan Negrut. "Using an SPH-Based Continuum Representation of Granular
Terrain to Simulate the Mobility of an Eight-Wheel Rover." Technical Report TR-2020-02.
Simulation-Based Engineering Laboratory, University of Wisconsin-Madison, 2020.

Tasora, Alessandro, Dario Mangoni, and Dan Negrut. "An Overview of the Chrono Soil Contact Model
(SCM) Implementation." Technical Report TR-2017-01. Simulation-Based Engineering Laboratory,
University of Wisconsin-Madison, 2017.

Serban, Radu, R. Gerike, Asher Elmquist, and Dan Negrut. "NG-NRMM Phase II Benchmarking: Chrono
Wheeled-Vehicle Platform Simulation Results Summary." Technical Report TR-2017-05.
Simulation-Based Engineering Laboratory, University of Wisconsin-Madison, 2017.

Kwarta, Michal, and Dan Negrut. "Using the Complementarity and Penalty Methods for Solving
Frictional Contact Problems in Chrono: Validation for the Shear-Test with Particle Image
Velocimetry." Technical Report TR-2016-18. Simulation-Based Engineering Laboratory, University of
Wisconsin-Madison, 2016.

Kwarta, Michal, and Dan Negrut. "Using the Complementarity and Penalty Methods for Solving
Frictional Contact Problems in Chrono: Validation for the Cone Penetrometer Test." Technical Report
TR-2016-16. Simulation-Based Engineering Laboratory, University of Wisconsin-Madison, 2016.

Serban, Radu, Michael Taylor, Daniel Melanz, and Dan Negrut. "NG-NRMM Phase I Benchmarking: Chrono
Tracked Vehicle Simulation Results Summary." Technical Report TR-2016-08. Simulation-Based
Engineering Laboratory, University of Wisconsin-Madison, 2016.

Recuero, Antonio M., Radu Serban, B. Peterson, Hiroyuki Sugiyama, and Dan Negrut. "Wheeled Vehicle
Mobility Studies in Chrono: Nonlinear Finite Element Tires Operating on Granular Terrain."
Technical Report TR-2016-07. Simulation-Based Engineering Laboratory, University of
Wisconsin-Madison, 2016.

---

## Scope

Included: lab-authored, published work from 2016 forward whose subject is soil-contact, continuum
granular, or discrete element terrain modeling, plus the vehicle-terrain co-simulation and
validation work that carries those models.

Deliberately excluded, to keep the list defensible as a terramechanics record:

1. Simulation videos, data repositories, and public-metadata deposits (there are roughly thirty of
   these for VIPER, Curiosity, and DEM-Engine demonstrations). They are citable artifacts but not
   papers. They live in `refsFSI.bib`, `refsDEM.bib`, and `refsSBELspecific.bib` if needed.
2. SPH work whose subject is fluid rather than granular flow, which is methodological ancestry for
   CRM rather than terramechanics: for example the consistent multi-resolution SPH papers in
   *Computer Methods in Applied Mechanics and Engineering* (2017, 2019) and the multiphase
   incompressible SPH paper in the *Journal of Computational Physics* (2022).
3. Sensor simulation and perception work (POLAR-Sim, the lunar sensor simulation environment),
   autonomy and machine-learning work on off-road mobility, and model-predictive-control path
   tracking. Relevant to rover simulation, but not terrain modeling.
4. Work in preparation, notably a continuum comparison of mu(I) rheology against Modified Cam Clay
   for terramechanics, which exists only as a dissertation-repository manuscript and should not be
   cited outside the lab until it is published.

Two entries appear in both a journal and a conference form (the SCM real-time paper and the
bevameter calibration paper); both forms are listed because the conference versions are sometimes
the ones already known to a reader.
