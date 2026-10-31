# Chrono references by topic: what to read to learn more

A short, curated "learn more" list for people who have just seen a Chrono overview talk: one or two
papers per topic, chosen by citation count among Chrono-related papers, with a recent paper kept only
when it is the current definitive description of a capability that was shown. First compiled on
2026-10-30 for the Toyota - UW-Madison meeting in Tokyo (talk "Overview of Chrono & Research Directions
in the Simulation-Based Engineering Lab", 2026-10-29); the picks were made independently by Claude and
Codex and reconciled against OpenAlex citation counts.

References are in Chicago style so the list can be pasted into correspondence. Each entry ends with
its key in this collection (`refs<Topic>.bib`) and its OpenAlex citation count on the date in the
section header, so the ranking can be redone later. For the deeper terramechanics record see
`terramechanics-lab-papers.md`; this file deliberately stays at one or two papers per topic.

To grow it: add the paper to the right `refs<Topic>.bib` first, then add it here in the same style with
its key and count. To turn it into slides: use the topic as a bold bullet and each reference as a
sub-bullet in short form (`First author et al., "Title," Venue, Year`), four to five topics per 16:9
slide at about 15 pt for topics and 11.5 pt for references; three slides hold the whole list.

Counts: OpenAlex `cited_by_count` on 2026-10-30 (Google Scholar usually runs higher).

---

## 1. Chrono overview: open-source, multi-physics simulation

Tasora, Alessandro, Radu Serban, Hammad Mazhar, Arman Pazouki, Daniel Melanz, Jonathan Fleischmann,
Michael Taylor, Hiroyuki Sugiyama, and Dan Negrut. "Chrono: An Open Source Multi-physics Dynamics
Engine." In *High Performance Computing in Science and Engineering*, Lecture Notes in Computer Science
9611, 19-49. Springer, 2016. https://doi.org/10.1007/978-3-319-40361-8_2.
`chronoOverview2016` (refsMBS), 285 citations. The canonical Chrono citation.

Mazhar, Hammad, Toby Heyn, Arman Pazouki, Daniel Melanz, Andrew Seidl, Aaron Bartholomew, Alessandro
Tasora, and Dan Negrut. "Chrono: A Parallel Multi-Physics Library for Rigid-Body, Flexible-Body, and
Fluid Dynamics." *Mechanical Sciences* 4, no. 1 (2013): 49-64. https://doi.org/10.5194/ms-4-49-2013.
`chronoOverview2013` (refsMBS), 79 citations.

## 2. Frictional contact: the complementarity (DVI) solvers behind Chrono

Tasora, Alessandro, and Mihai Anitescu. "A Matrix-Free Cone Complementarity Approach for Solving
Large-Scale, Nonsmooth, Rigid Body Dynamics." *Computer Methods in Applied Mechanics and Engineering*
200, no. 5-8 (2011): 439-453. https://doi.org/10.1016/j.cma.2010.06.030.
`TasoraAnitescuCMAME10` (refsMBS), 133 citations.

Mazhar, Hammad, Toby Heyn, Dan Negrut, and Mihai Anitescu. "Using Nesterov's Method to Accelerate
Multibody Dynamics with Friction and Contact." *ACM Transactions on Graphics* 34, no. 3 (2015): 32.
https://doi.org/10.1145/2735627. `Mazhar2015` (refsMBS), 85 citations.

## 3. Chrono::Vehicle

Serban, Radu, Michael Taylor, Dan Negrut, and Alessandro Tasora. "Chrono::Vehicle: Template-Based
Ground Vehicle Modeling and Simulation." *International Journal of Vehicle Performance* 5, no. 1 (2019):
18-39. https://doi.org/10.1504/IJVP.2019.097096. `chronoVehicle2019` (refsChronoSpecific), 48 citations.

## 4. Flexible (ANCF) tires and vehicle-tire-terrain co-simulation

Recuero, Antonio M., Radu Serban, B. Peterson, Hiroyuki Sugiyama, Paramsothy Jayakumar, and Dan
Negrut. "A High-Fidelity Approach for Vehicle Mobility Simulation: Nonlinear Finite Element Tires
Operating on Granular Material." *Journal of Terramechanics* 72 (2017): 39-54.
https://doi.org/10.1016/j.jterra.2017.04.002. `antonioVehicleTireGranMatSim2017` (refsTerramech),
103 citations.

Serban, Radu, Dan Negrut, Antonio M. Recuero, and Paramsothy Jayakumar. "An Integrated Framework for
High-Performance, High-Fidelity Simulation of Ground Vehicle-Tyre-Terrain Interaction." *International
Journal of Vehicle Performance* 5, no. 3 (2019): 233-259. `serbanCosimIJVP2019` (refsTerramech),
19 citations. (The title's "Tyre" is the journal's spelling.)

## 5. SynChrono: fleets of vehicles and robots

Taves, Jay, Asher Elmquist, Aaron Young, Radu Serban, and Dan Negrut. "SynChrono: A Scalable,
Physics-Based Simulation Platform for Testing Groups of Autonomous Vehicles and/or Robots." In
*Proceedings of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*, 2020.
https://doi.org/10.1109/IROS45743.2020.9341585. `synchrono2020` (refsAutonomousVehicles), 6 citations.

Young, Aaron, Jay Taves, Asher Elmquist, Simone Benatti, Alessandro Tasora, Radu Serban, and Dan
Negrut. "Enabling Artificial Intelligence Studies in Off-Road Mobility Through Physics-Based Simulation
of Multi-Agent Scenarios." *Journal of Computational and Nonlinear Dynamics* 17, no. 5 (2022): 051001.
https://doi.org/10.1115/1.4053321. `aaronAImultiAAsJCND2021` (refsAutonomousVehicles), 8 citations.
Alternate with a similar count: `end2endMUBO2022` (*Multibody System Dynamics*, 2022, 10 citations),
less specifically about multi-agent simulation.

## 6. SCM, Soil Contact Model

Tasora, Alessandro, Dario Mangoni, Dan Negrut, Radu Serban, and Paramsothy Jayakumar. "Deformable Soil
with Adaptive Level of Detail for Tracked and Wheeled Vehicles." *International Journal of Vehicle
Performance* 5, no. 1 (2019): 60-76. https://doi.org/10.1504/IJVP.2019.097098.
`chronoSCM2019` (refsChronoSpecific), 29 citations.

Serban, Radu, Jay Taves, and Zhenhao Zhou. "Real-Time Simulation of Ground Vehicles on Deformable
Terrain." *Journal of Computational and Nonlinear Dynamics* 18, no. 8 (2023): 081007.
https://doi.org/10.1115/1.4056851. `chronoSCM_JCND_2023` (refsTerramech), 15 citations.

Origin of the model, outside Chrono: Krenn, Rainer, and Andreas Gibbesch. "Soft Soil Contact Modeling
Technique for Multi-Body System Simulation." In *Trends in Computational Contact Mechanics*, 135-155.
Springer, 2011. https://doi.org/10.1007/978-3-642-22167-5_8. `Krenn2011` (refsTerramech), 44 citations.

## 7. CRM, Continuum Representation Model (SPH)

Hu, Wei, Milad Rakhsha, Lijing Yang, Ken Kamrin, and Dan Negrut. "Modeling Granular Material Dynamics
and Its Two-Way Coupling with Moving Solid Bodies Using a Continuum Representation and the SPH Method."
*Computer Methods in Applied Mechanics and Engineering* 385 (2021): 114022.
https://doi.org/10.1016/j.cma.2021.114022. `weiGranularSPH2021` (refsFSI), 45 citations.

Unjhawala, Huzaifa Mustafa, Luning Bakke, Harry Zhang, Michael Taylor, Ganesh Arivoli, Radu Serban, and
Dan Negrut. "A Physics-Based Continuum Model for Versatile, Scalable, and Fast Terramechanics
Simulation." *Journal of Terramechanics* 124 (2026): 101150.
https://doi.org/10.1016/j.jterra.2026.101150. `Huzaifa2026CRM` (refsRobotics), 0 citations (new; kept as
the current description of Chrono::CRM).

## 8. DEM on GPUs: Chrono::GPU and Chrono DEM-Engine

Fang, Luning, Ruochun Zhang, Colin Vanden Heuvel, Radu Serban, and Dan Negrut. "Chrono::GPU: An
Open-Source Simulation Package for Granular Dynamics Using the Discrete Element Method." *Processes* 9,
no. 10 (2021): 1813. https://doi.org/10.3390/pr9101813. `chronoGranular2021` (refsDEM), 35 citations.

Zhang, Ruochun, Bonaventura Tagliafierro, Colin Vanden Heuvel, Shlok Sabarwal, Luning Bakke, Yulong Yue,
Xin Wei, Radu Serban, and Dan Negrut. "Chrono DEM-Engine: A Discrete Element Method Dual-GPU Simulator
with Customizable Contact Forces and Element Shape." *Computer Physics Communications* 300 (2024):
109196. https://doi.org/10.1016/j.cpc.2024.109196. `ruochun2024dem` (refsDEM), 21 citations (kept as the
current description of DEM-Engine).

Independent validation, by Idaho National Laboratory: Reger, David, Elia Merzari, Paolo Balestra, Ryan
Stewart, and Gerhard Strydom. "Discrete Element Simulation of Pebble Bed Reactors on Graphics Processing
Units." *Annals of Nuclear Energy* 190 (2023): 109896. https://doi.org/10.1016/j.anucene.2023.109896.
`dem-pbrIdaho2023` (refsDEM), 25 citations.

Alternate: Kelly, Olsen, and Negrut, "Billion Degree of Freedom Granular Dynamics Simulation on Commodity
Hardware via Heterogeneous Data-Type Representation," *Multibody System Dynamics* 50 (2020),
`conlainNicDan2020` (refsMBS), 27 citations.

## 9. GRC-1 lunar simulant in DEM, and rover wheel design

Zhang, Ruochun, Colin Vanden Heuvel, Alexander Schepelmann, Arno Rogg, Dimitrios Apostolopoulos, Samuel
Chandler, Radu Serban, and Dan Negrut. "A GPU-Accelerated Simulator for the DEM Analysis of Granular
Systems Composed of Clump-Shaped Elements." *Engineering with Computers* 40, no. 4 (2024): 2559-2579.
https://doi.org/10.1007/s00366-023-01921-9. `ruochunGRC-DEM2023` (refsDEM), 11 citations.

Unjhawala, Huzaifa Mustafa, Khizar Shaikh, Luning Bakke, Radu Serban, and Dan Negrut. "Co-Design of
Rover Wheels and Control Using Bayesian Optimization and Rover-Terrain Simulations." arXiv:2602.01535,
2026. https://arxiv.org/abs/2602.01535. `Huzaifa2026WheelDesign` (refsRobotics), 0 citations (new).

## 10. Testing on Earth for the Moon: gravity offset

Hu, Wei, Pei Li, Arno Rogg, Alexander Schepelmann, Samuel Chandler, Ken Kamrin, and Dan Negrut. "A
Study Demonstrating That Using Gravitational Offset to Prepare Extraterrestrial Mobility Missions Is
Misleading." *Journal of Field Robotics* 42, no. 7 (2025): 3772-3794. https://doi.org/10.1002/rob.22597.
`gravOffset2025` (refsTerramech), 7 citations.

## 11. Chrono::Sensor and lunar perception

Elmquist, Asher, Radu Serban, and Dan Negrut. "A Sensor Simulation Framework for Training and Testing
Robots and Autonomous Vehicles." *Journal of Autonomous Vehicles and Systems* 1, no. 2 (2021): 021001.
https://doi.org/10.1115/1.4050080. `asherSensorSimulation2021` (refsSensors), 19 citations.

Chen, Bo-Hsun, Peter Negrut, Thomas Liang, Nevindu Batagoda, Harry Zhang, and Dan Negrut. "POLAR-Sim:
Augmenting NASA's POLAR Dataset for Data-Driven Lunar Perception and Rover Simulation." *IEEE Aerospace
and Electronic Systems Magazine* 41 (2026). https://doi.org/10.1109/MAES.2025.3617426.
`bohsunPOLAR-Sim2025` (refsSensors), 2 citations (journal form of the 2023 preprint `chen2023polar3d`).

Alternate: Elmquist and Negrut, "Modeling Cameras for Autonomous Vehicle and Robot Simulation: An
Overview," *IEEE Sensors Journal* 21 (2021), `asherCameraOverview2021` (refsSensors), 20 citations.

## 12. Reduced-order and neural reduced dynamics (NRD)

Unjhawala, Huzaifa, Thomas Hansen, Harry Zhang, Stefan Caldraru, Shouvik Chatterjee, Luning Bakke,
Jinlong Wu, Radu Serban, and Dan Negrut. "An Expeditious and Expressive Vehicle Dynamics Model for
Applications in Controls and Reinforcement Learning." *IEEE Access* 12 (2024).
https://doi.org/10.1109/ACCESS.2024.3368874. `huzaifaIEEE-AccessCalibration2024` (refsRobotics),
4 citations.

Zhang, Harry, and Dan Negrut. "Learning the Right Abstraction: Neural Reduced Dynamics for Complex
Robot Control." arXiv:2608.19375, 2026. https://arxiv.org/abs/2608.19375. `harryNeDM2026` (refsML-AI),
0 citations (new). Project page: https://uwsbel.github.io/NeDM/ (`NeDMprojectPage`, refsSBELspecific).

## 13. AI for Chrono: LLM-generated models and agentic simulation

Wang, Jingquan, Andrew Negrut, Harry Zhang, Khailanii Slaton, Shu Wang, Radu Serban, Jinlong Wu, and Dan
Negrut. "ChronoLLM: Customizing Language Models for Physics-Based Simulation Code Generation."
*Multibody System Dynamics* (2026). https://doi.org/10.1007/s11044-026-10152-x.
`jingquanChronoLLM2026` (refsML-AI), 1 citation.

Wang, Hongyu, Jingquan Wang, Bocheng Zou, Radu Serban, and Dan Negrut. "Coding Agent Is Good As World
Simulator." arXiv:2605.14398, 2026. https://arxiv.org/abs/2605.14398.
`justinCodingAgentChrono2026` (refsML-AI), 0 citations (new; the ChronoAgentic pipeline).

Alternate: Wang, Negrut, Wang, Zhang, and Negrut, "SimBench: A Framework for Evaluating and Diagnosing
LLM-Based Digital-Twin Generation for Multi-Physics Simulation," *IEEE Access* (2026),
`jingquanSimbench2026` (refsML-AI), 0 citations.

## 14. Space missions and high-throughput uncertainty quantification

Rezich, Erin, Valentin T. Bickel, Parker L. Francis, Arno Rogg, Antoine Tardy, Colin Creager, Heather A.
Oravec, Alexander Schepelmann, Kimberly Ennico-Smith, et al. "Investigating the Geotechnical Properties
of the Lunar South Pole with NASA VIPER's Mobility System." *The Planetary Science Journal* 6 (2025).
https://doi.org/10.3847/PSJ/add13f. `Rezich-VPER-Chrono-2025` (refsTerramech), 6 citations.

Slaton, Khailanii, and Dan Negrut. "Chrono::Ray: A Distributed Framework for High-Throughput
Simulation-Based Analysis of Multibody Systems." arXiv:2605.13767, 2026.
https://arxiv.org/abs/2605.13767. `khailanii-Chrono-Ray-UQ-2026` (refsChronoSpecific), 0 citations (new).

## 15. Simulation in robotics and the sim2real gap

Choi, HeeSun, Cindy Crump, Christian Duriez, Asher Elmquist, Gregory Hager, David Han, Frank Hearl,
Jessica Hodgins, Abhinandan Jain, Frederick Leve, et al. "On the Use of Simulation in Robotics:
Opportunities, Challenges, and Suggestions for Moving Forward." *Proceedings of the National Academy of
Sciences* 118, no. 1 (2021): e1907856118. https://doi.org/10.1073/pnas.1907856118.
`PNASsimRobotics2021` (refsRobotics), 162 citations.

---

## Scope and selection rule

1. Chrono-related papers only: papers that describe Chrono or a module, or lab work carried out with
   Chrono, plus one independent third-party validation (section 8) and one model-origin note (section 6).
2. Within a topic, the highest OpenAlex count wins. A paper from 2024 or later is kept only when it is
   the current definitive description of a capability (Chrono::CRM, DEM-Engine, ChronoLLM, NRD) and is
   marked as such; counts in the single digits do not rank anything.
3. Not included: website and repository entries, technical reports (the RASSOR report TR-2024-02 and
   the SCM implementation report TR-2017-01 are in `terramechanics-lab-papers.md`), PyChrono
   (`pychrono2022`, 11 citations) and FMI co-simulation (`raduFMIChrono2025`, 2 citations), which did not
   make the cut of two per topic.
