Exploratory Analysis of Combination Lock Tolerances and Keyspace Implications
Author: Tracktor97
Date: 2/17/26

Abstract
This project explores the mechanical tolerances of a consumer combination lock and examines their potential impact on effective keyspace and security. By systematically testing variations from the original combination, I identified the range of acceptable inputs that still allowed the lock to open. The analysis highlights trade-offs between usability and security and demonstrates the application of experimental methodology to physical security systems.

Introduction
Combination locks rely on the precise alignment of multiple rotating discs to release a locking mechanism, typically a ball bearing. Standard operation assumes that only the exact combination will allow access. However, mechanical tolerances in manufacturing may create a window where near-correct combinations can succeed, effectively reducing the keyspace and potentially impacting security.
The goal of this experiment was to:
Determine the tolerance window for each disc.
Examine how deviations from the original combination affect successful unlocking.
Explore potential causes and security implications of these tolerances.

Methodology
Baseline: The lock’s original combination was recorded: 33-4-13.
Testing variation: Each disc was adjusted one unit clockwise and counterclockwise.
Refinement: When an inadequate input was identified, a half-unit adjustment was tested to locate the boundary of success.
Observation: Results were recorded as:
Adequate: Lock opens easily.
Adequate with wiggling: Lock opens with minor manipulation.
Inadequate: Lock fails to open.
Due to time constraints, the second and third discs were only partially tested, leaving scope for further exploration.

Results
Combination Attempt
Result
33-4-13
Original code — Adequate
32-4-13
Adequate
32.5-4-13
Adequate with wiggling
31-4-13
Adequate with wiggling
30-4-13
Inadequate
34-4-13
Adequate
35-4-13
Intense wiggling, Adequate
36-4-13
Inadequate
33-3-13
Adequate
33-2-13
Inadequate
33-2.5-13
Inadequate
33-5-13
Adequate
33-6-13
Adequate
33-7-13
Inadequate
33-6.5-13
Inadequate
33-4-12
Adequate with light wiggling
33-4-12.5
Adequate
33-4-14
Adequate
33-4-13.5
Adequate

Key observations:
The first disc tolerates ±2 units from the original combination.
Some combinations require manipulation (“wiggling”) to succeed.
The second and third discs show narrower tolerances based on limited testing.
There may be mechanical factors — material properties, disc/channel width, or actuator tolerances — contributing to these results.

Analysis and Discussion
Tolerance Implications:
Mechanical tolerances expand the effective keyspace beyond the nominal combination. This could increase susceptibility to brute-force attacks or manipulation by experienced operators.
Engineering Considerations:
Looser tolerances may be intentional to reduce user frustration from failed attempts.
Tighter tolerances would increase manufacturing complexity and potential for lock failure.
Security Trade-offs:
Usability and customer satisfaction may come at the cost of reduced effective security. The experiment highlights that even small deviations in disc alignment can impact lock performance and security.

Connection to Cybersecurity:
Just as timing differences in web applications can reveal information about valid users, mechanical tolerances can reveal information about valid combinations. The principle of observing subtle system behavior to infer hidden information is consistent across physical and digital security domains.

Limitations and Future Work
Testing was limited to a single lock and model; results may not generalize.
Only the first disc was tested extensively; second and third discs require further exploration.
Future work could examine:
Dual or multi-disc offsets.
Physical indicators of channel alignment.
Effects of repeated use and wear on tolerance.
Comparative analysis across lock brands and models.

Conclusion
This exploratory analysis demonstrates that mechanical tolerances in a consumer combination lock can widen the effective keyspace and create potential vulnerabilities. More broadly, it illustrates the value of systematic observation, hypothesis generation, and analytical reasoning — core skills in cybersecurity research and vulnerability analysis.
