"""CT-AuT study chapters: plain-language automotive testing guidance."""

CHAPTERS = [
    {
        'number': 1,
        'title': 'Introduction to Automotive Software Testing',
        'minutes': 30,
        'intro': 'Modern vehicles combine software, electronics, mechanics, and connected services. Testing must fit complex product goals and staged releases.',
        'sections': [
            {
                'title': '1.1 Requirements from Divergent Project Objectives and Increasing Product Complexity',
                'summary': 'Automotive projects balance safety, cost, delivery, performance, and customer expectations across many interacting components.',
                'points': [
                    'A vehicle function can depend on software, sensors, control units, networks, and physical behavior.',
                    'Different stakeholders may set competing goals, so requirements and test priorities need clear agreement.',
                    'Integration and change can create faults that are not visible when a component is tested alone.',
                ],
                'example': 'A driver-assistance feature must respond quickly and safely while meeting cost targets and working with several sensor suppliers.',
            },
            {
                'title': '1.2 Project Aspects Influenced by Standards',
                'summary': 'Standards affect project planning, engineering evidence, responsibilities, and the effort needed to demonstrate product quality.',
                'points': [
                    'Applicable standards can influence schedule, cost, required work products, review depth, and traceability.',
                    'The required process depends on the product and its safety or quality context; teams identify applicable obligations early.',
                    'Conformance evidence needs to be planned alongside implementation and testing.',
                ],
                'example': 'A project adds review and verification milestones to its schedule because a safety standard requires documented evidence before release.',
            },
            {
                'title': '1.3 The Six Generic Stages in the System Lifecycle',
                'summary': 'The system lifecycle organizes work from initial concept through development, use, and eventual retirement.',
                'points': [
                    'The six generic stages are concept, development, production, utilization, support, and retirement.',
                    'Testing and verification needs change as the product moves from defining needs to building, operating, and withdrawing it.',
                    'Lifecycle planning includes maintenance and changes after the first release, not only initial development.',
                ],
                'example': 'A vehicle control unit is tested against early requirements during development, monitored for field issues in use, and handled under a controlled support plan.',
            },
            {
                'title': '1.4 The Contribution and Participation of the Tester in the Release Process',
                'summary': 'Testers contribute evidence and risk information throughout release preparation, while release decisions involve multiple roles.',
                'points': [
                    'Testers review requirements and plans, design and execute tests, report defects, and summarize residual risk.',
                    'Release readiness depends on agreed criteria, resolved issues, and evidence from relevant verification activities.',
                    'Collaboration with developers, safety specialists, project managers, and suppliers helps clarify results and decisions.',
                ],
                'example': 'Before releasing a braking update, testers provide traceable test results and disclose an unresolved timing risk for the release authority to assess.',
            },
        ],
        'key_terms': [
            ('System lifecycle', 'The stages through which a system is conceived, developed, operated, supported, and retired.'),
            ('Release criteria', 'Conditions that must be considered before a product or change is released.'),
            ('Traceability', 'Links between requirements, tests, results, and related work products.'),
            ('Verification', 'Evaluation of whether a work product meets specified requirements.'),
        ],
        'exam_tips': [
            'Recall the lifecycle stages in order and connect testing to more than development alone.',
            'Explain how standards can affect project effort, timing, and evidence.',
            'Recognize that testers inform release decisions but do not replace the responsible decision makers.',
        ],
    },
    {
        'number': 2,
        'title': 'Standards for the Testing of Electric/Electronic Systems',
        'minutes': 300,
        'intro': 'Automotive projects use process and safety standards to structure development and show that risks and requirements were addressed.',
        'sections': [
            {
                'title': '2.1 Automotive SPICE',
                'summary': 'Automotive SPICE assesses process capability and describes engineering practices, including specific expectations for testing.',
                'points': [
                    'Its process dimension describes what activities are performed; the capability dimension describes how well processes are managed and improved.',
                    'Test processes cover planning, design, execution, results, work products, and traceability between test levels.',
                    'Verification of software units can use suitable measures such as reviews, analysis, and execution-based tests.',
                ],
                'example': 'An assessor follows a software requirement through its design, unit test, result record, and defect resolution to evaluate the team’s verification process.',
            },
            {
                'title': '2.2 ISO 26262',
                'summary': 'ISO 26262 addresses functional safety for road-vehicle electrical and electronic systems across a safety lifecycle.',
                'points': [
                    'Safety work spans concept, system, hardware, software, integration, and validation activities, with defined responsibilities and evidence.',
                    'Automotive Safety Integrity Levels (ASILs) express safety criticality and influence rigor and the methods selected.',
                    'Testers support a safety culture by checking safety requirements, independence where needed, and evidence of hazard controls.',
                ],
                'example': 'A steering-control project applies more rigorous verification to a safety-critical requirement than to a non-safety convenience display.',
            },
            {
                'title': '2.3 AUTOSAR',
                'summary': 'AUTOSAR defines standardized software architecture and interfaces intended to support reuse and integration in vehicles.',
                'points': [
                    'The architecture separates software functions from platform services through defined components and interfaces.',
                    'Testers check configuration, interface contracts, integration behavior, and compatibility with the intended platform.',
                    'Reuse can reduce duplicated development but does not remove the need to verify the configured system.',
                ],
                'example': 'A reused diagnostic component is tested with a new vehicle configuration to confirm its interfaces and messages remain correct.',
            },
            {
                'title': '2.4 Comparison of Automotive SPICE, ISO 26262, and CTFL',
                'summary': 'These references have different purposes: process assessment, functional safety, and general testing knowledge.',
                'points': [
                    'Automotive SPICE focuses on process capability and engineering process evidence.',
                    'ISO 26262 focuses on functional safety for vehicle electrical and electronic systems.',
                    'CTFL supplies general testing concepts and techniques; it does not replace either automotive standard.',
                ],
                'example': 'A project can use CTFL techniques to design tests, Automotive SPICE practices to organize process evidence, and ISO 26262 to address safety obligations.',
            },
        ],
        'key_terms': [
            ('Automotive SPICE', 'A process assessment model used in automotive software and system development.'),
            ('Capability level', 'A rating of how thoroughly a process is managed and established.'),
            ('ISO 26262', 'A road-vehicle functional safety standard for electrical and electronic systems.'),
            ('ASIL', 'Automotive Safety Integrity Level, a classification that influences safety rigor.'),
            ('AUTOSAR', 'A standardized automotive software architecture and interface approach.'),
        ],
        'exam_tips': [
            'Do not confuse process capability assessment with functional safety objectives.',
            'Know that ASIL affects rigor and method selection rather than naming a test level.',
            'Understand that CTFL provides general testing knowledge and does not substitute for domain standards.',
        ],
    },
    {
        'number': 3,
        'title': 'Testing in a Virtual Environment',
        'minutes': 160,
        'intro': 'Virtual test environments let teams exercise automotive software at different levels of realism before and alongside vehicle testing.',
        'sections': [
            {
                'title': '3.1 Test Environment in General',
                'summary': 'An automotive test environment combines the system under test with models, hardware, data, tools, and interfaces needed for controlled experiments.',
                'points': [
                    'Closed-loop setups feed system outputs back into the simulated environment; open-loop setups supply predefined inputs without that feedback.',
                    'An ECU typically combines processing, memory, input/output, communication interfaces, and software that controls vehicle behavior.',
                    'Environment choice depends on the test objective, reproducibility, realism, cost, and available interfaces.',
                ],
                'example': 'To test adaptive cruise behavior, a closed-loop simulator updates a virtual lead car’s position in response to the ECU’s acceleration commands.',
            },
            {
                'title': '3.2 Testing in XiL Test Environments',
                'summary': 'The XiL family ranges from testing models to testing software and real hardware, with different strengths and constraints.',
                'points': [
                    'Model-in-the-Loop (MiL) tests control models; Software-in-the-Loop (SiL) executes software in a simulated setup; Hardware-in-the-Loop (HiL) connects real ECU hardware to a simulated system.',
                    'Earlier, less hardware-dependent environments can support fast, repeatable checks; HiL adds hardware realism but costs more to operate.',
                    'Choose which tests belong at each level using risk, fidelity, speed, cost, and the behavior that must be observed.',
                ],
                'example': 'A control algorithm is first checked in MiL, compiled software is exercised in SiL, and timing on the production ECU is then measured in HiL.',
            },
        ],
        'key_terms': [
            ('ECU', 'Electronic Control Unit; an embedded computer that controls vehicle functions.'),
            ('Closed-loop system', 'A system in which outputs influence subsequent inputs through feedback.'),
            ('MiL', 'Model-in-the-Loop testing of models within a simulated environment.'),
            ('SiL', 'Software-in-the-Loop testing of software in a simulated environment.'),
            ('HiL', 'Hardware-in-the-Loop testing using real hardware connected to a simulated environment.'),
        ],
        'exam_tips': [
            'Compare MiL, SiL, and HiL by what is real in each setup.',
            'Choose an environment based on test objective and trade-offs, not on a fixed rule that one level replaces another.',
        ],
    },
    {
        'number': 4,
        'title': 'Static Testing and Dynamic Testing',
        'minutes': 230,
        'intro': 'Automotive verification combines examination of work products with execution of software under selected conditions.',
        'sections': [
            {
                'title': '4.1 Static Testing',
                'summary': 'Static testing evaluates work products without running the software, helping teams find ambiguity and coding problems early.',
                'points': [
                    'Reviews can examine requirements, designs, code, and testware for correctness, completeness, consistency, and testability.',
                    'MISRA-C guidance supports safer and more consistent use of the C language in embedded automotive software.',
                    'Review findings should be recorded, assigned, and followed through so defects are corrected and evidence is retained.',
                ],
                'example': 'A requirements review finds that a sensor-timeout requirement has no defined safe response, before that ambiguity is implemented in code.',
            },
            {
                'title': '4.2 Dynamic Testing',
                'summary': 'Dynamic testing executes software and compares observed behavior with requirements, models, and safety expectations.',
                'points': [
                    'Modified Condition/Decision Coverage (MC/DC) requires showing that each condition can independently affect the decision outcome.',
                    'Back-to-back tests compare results from two implementations or environments; fault injection checks behavior when faults are deliberately introduced.',
                    'Use requirements-based tests and context-dependent criteria to choose suitable coverage and techniques.',
                ],
                'example': 'For a braking decision with two Boolean conditions, tests vary each condition separately to show its independent effect on whether braking is requested.',
            },
        ],
        'key_terms': [
            ('Static testing', 'Evaluation of a work product without executing the software.'),
            ('MISRA-C', 'Guidelines for using the C language in safety- and security-related embedded systems.'),
            ('MC/DC', 'Modified Condition/Decision Coverage, a structural coverage criterion for decisions.'),
            ('Back-to-back testing', 'Comparison of outputs from corresponding implementations or execution environments.'),
            ('Fault injection', 'Deliberate introduction of faults to observe system response.'),
        ],
        'exam_tips': [
            'Distinguish reviews and static analysis from tests that execute code.',
            'For MC/DC, focus on each condition independently changing the decision result.',
            'Explain what back-to-back comparison and fault injection are intended to reveal.',
        ],
    },
]
