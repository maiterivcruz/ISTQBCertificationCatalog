CHAPTERS = [
    {
        'number': 1,
        'title': 'Basic Concepts',
        'minutes': 60,
        'intro': 'Performance testing examines how responsive and stable a system is under defined workloads and conditions.',
        'sections': [
            {
                'title': '1.1 Principles of Performance Testing',
                'summary': 'Performance testing gives evidence about behavior and resource use under realistic workloads.',
                'points': [
                    'Start with goals and risks, then design a representative workload and environment.',
                    'Measure the system and its dependencies while the workload is applied.',
                    'Repeat tests consistently and interpret results in context rather than treating one number as proof.',
                ],
                'example': 'A retailer tests its full checkout journey with realistic product searches and payments before a seasonal sale, not just with a single fast request.',
            },
            {
                'title': '1.2 Types of Performance Testing',
                'summary': 'Different test types answer different questions about capacity, load, stress and growth.',
                'points': [
                    'Load testing checks behavior at expected usage; stress testing pushes beyond expected conditions.',
                    'Capacity testing finds the maximum sustainable workload, while scalability testing checks how growth affects performance.',
                    'Endurance testing looks for degradation during sustained use; spike testing examines sudden workload changes.',
                ],
                'example': 'A streaming service tests normal evening demand, doubles it to find capacity, holds a busy load overnight, and creates a sharp spike when a live event begins.',
            },
            {
                'title': '1.3 Testing Types in Performance Testing',
                'summary': 'Performance work includes static examination of requirements and design as well as dynamic measurement of a running system.',
                'points': [
                    'Static testing can find performance risks in architecture, code and workload assumptions without execution.',
                    'Dynamic testing applies load and measures actual behavior.',
                    'Combine both: early reviews reduce risk before executable software is available.',
                ],
                'example': 'A reviewer spots that every page request will make a separate database call; a later load test measures the effect with realistic traffic.',
            },
            {
                'title': '1.4 The Concept of Load Generation',
                'summary': 'Load generation creates user-like activity so the system can be observed under a defined workload.',
                'points': [
                    'Model user actions, pacing and concurrent activity rather than generating arbitrary requests.',
                    'Choose suitable generation methods such as protocol-level, API or graphical interaction based on the test goal.',
                    'Check that load generators themselves can produce the required workload without becoming the bottleneck.',
                ],
                'example': 'A booking test simulates users searching, pausing to compare rooms and then reserving, instead of sending identical searches as quickly as possible.',
            },
            {
                'title': '1.5 Common Performance Efficiency Failure Modes and Their Causes',
                'summary': 'Slowdowns and failures can result from resource limits, contention, poor design or an unrealistic test setup.',
                'points': [
                    'Common symptoms include long response times, low throughput, errors, resource exhaustion and unstable behavior.',
                    'Possible causes include inefficient queries, locks, memory leaks, overloaded dependencies or insufficient capacity.',
                    'Use measurements and logs to identify causes; a symptom alone does not prove which component is responsible.',
                ],
                'example': 'A store’s response time grows during a long test; memory measurements show a gradual increase, pointing to a leak rather than a sudden traffic spike.',
            },
        ],
        'key_terms': [
            ('Workload', 'The user and system activity applied during a performance test.'),
            ('Load testing', 'Testing behavior under an expected or specified workload.'),
            ('Stress testing', 'Testing behavior beyond normal operating conditions.'),
            ('Throughput', 'The amount of work completed in a given time.'),
            ('Scalability', 'The ability to handle increased demand by adding or using resources.'),
        ],
        'exam_tips': [
            'Match the test type to the question being asked: expected load, sustained use, growth or overload.',
            'Separate observed symptoms from possible root causes.',
            'A realistic workload models user behavior, not just a target request count.',
        ],
    },
    {
        'number': 2,
        'title': 'Performance Measurement Fundamentals',
        'minutes': 55,
        'intro': 'Measurements turn performance expectations into evidence that teams can compare and interpret.',
        'sections': [
            {
                'title': '2.1 Typical Metrics Collected in Performance Testing',
                'summary': 'Useful metrics describe service behavior, workload and resource use from the user and system perspectives.',
                'points': [
                    'Measure response time, throughput, concurrency and error rates against the test objective.',
                    'Collect resource metrics such as CPU, memory, disk and network use to help explain behavior.',
                    'Select metrics that relate to user or business outcomes and collect them consistently.',
                ],
                'example': 'A payment test records the 95th-percentile response time, successful payments per second, error rate and database CPU to connect user delays with system load.',
            },
            {
                'title': '2.2 Aggregating Results from Performance Testing',
                'summary': 'Aggregation summarizes many observations, but the chosen statistic affects what the result reveals.',
                'points': [
                    'Use averages with care because a small number of very slow requests can be hidden.',
                    'Report distributions or percentiles as well as suitable minimum, maximum and average values.',
                    'Compare runs only when workload, environment and measurement conditions are sufficiently alike.',
                ],
                'example': 'An average page time of one second looks acceptable, but the 95th percentile of eight seconds shows that a meaningful group of customers experiences a delay.',
            },
            {
                'title': '2.3 Key Sources of Performance Metrics',
                'summary': 'Measurements can come from the application, test tool, infrastructure and operational monitoring.',
                'points': [
                    'Application instrumentation can show transaction timing and internal component behavior.',
                    'Infrastructure monitors reveal resource pressure; load tools provide user-facing timing and workload evidence.',
                    'Correlate sources using consistent timestamps and identifiers to explain end-to-end results.',
                ],
                'example': 'A slow checkout is correlated with application traces and database metrics, showing that the delay begins in a saturated inventory query.',
            },
            {
                'title': '2.4 Typical Results of a Performance Test',
                'summary': 'A test result includes more than raw measurements: it should show conditions, findings and implications.',
                'points': [
                    'Record workload, environment, duration, configuration and relevant deviations.',
                    'Summarize whether objectives were met and identify trends, anomalies and limitations.',
                    'Explain what the findings mean for capacity, risk and stakeholder decisions.',
                ],
                'example': 'The report states that 500 concurrent shoppers met the response-time goal, while 700 caused elevated errors and exhausted the shared database connection pool.',
            },
        ],
        'key_terms': [
            ('Response time', 'Elapsed time between a request and its corresponding response.'),
            ('Percentile', 'A value at or below which a stated proportion of observations falls.'),
            ('Concurrency', 'The number of operations or users active at the same time.'),
            ('Metric', 'A measured value used to assess a performance objective.'),
        ],
        'exam_tips': [
            'Choose metrics that reflect the objective and the user experience.',
            'Averages can hide slow outliers; consider percentiles and distributions.',
        ],
    },
    {
        'number': 3,
        'title': 'Performance Testing in the Software Lifecycle',
        'minutes': 195,
        'intro': 'Performance risks can be addressed from requirements through operation, with test activities timed to the development lifecycle.',
        'sections': [
            {
                'title': '3.1 Principal Performance Testing Activities',
                'summary': 'Performance testing follows the familiar cycle of planning, analysis, design, implementation, execution and evaluation.',
                'points': [
                    'Clarify objectives and risks, then prepare workload, environment and measurements.',
                    'Run tests under controlled conditions and analyze results against agreed criteria.',
                    'Report findings, track fixes and perform confirmation or regression tests as appropriate.',
                ],
                'example': 'A team defines a search response-time objective, prepares a representative product catalog and load, runs the test, fixes a slow index and confirms the improvement.',
            },
            {
                'title': '3.2 Categories of Performance Risks for Different Architectures',
                'summary': 'Architecture shapes which components can limit performance or create bottlenecks.',
                'points': [
                    'Consider risks at clients, networks, application services, databases, queues and external dependencies.',
                    'Distributed and cloud systems introduce concerns such as network latency, shared resources and scaling behavior.',
                    'Use architecture knowledge to select monitoring points and realistic test boundaries.',
                ],
                'example': 'For a mobile service, testers check client rendering, wireless latency, API capacity and a third-party identity provider instead of blaming the application server alone.',
            },
            {
                'title': '3.3 Performance Risks Across the Software Development Lifecycle',
                'summary': 'Performance risk changes as requirements, designs, code and production conditions evolve.',
                'points': [
                    'Review performance requirements and architecture early, then use component and integration checks as software becomes available.',
                    'Test end-to-end workloads before release and monitor real usage after deployment.',
                    'Prioritize risks based on the product, architecture, user profile and consequences of slow or unavailable service.',
                ],
                'example': 'A financial service reviews transaction-volume assumptions during design, profiles a new calculation in component tests, then validates peak trading load before release.',
            },
            {
                'title': '3.4 Performance Testing Activities',
                'summary': 'Project context determines which performance activities are useful, when they occur and who contributes.',
                'points': [
                    'Plan for needed skills, test data, tools, environments, dependencies and stakeholder communication.',
                    'Choose a mix of early checks, realistic load tests and production monitoring that matches the risk.',
                    'Coordinate performance work with functional testing, delivery cadence and release decisions.',
                ],
                'example': 'A small online service adds a lightweight API load check to each build and schedules a broader multi-region test before a high-traffic launch.',
            },
        ],
        'key_terms': [
            ('Performance risk', 'A possibility that performance behavior will harm product or business outcomes.'),
            ('Bottleneck', 'A constrained part of a system that limits overall throughput or response.'),
            ('Architecture', 'The major components of a system and how they interact.'),
            ('Regression testing', 'Testing after a change to detect unintended effects on existing behavior.'),
        ],
        'exam_tips': [
            'Use lifecycle timing to catch risks early, but still validate end-to-end behavior.',
            'Analyze the whole architecture and its dependencies when explaining a bottleneck.',
            'Select activities based on project context and risk, not a fixed checklist alone.',
        ],
    },
    {
        'number': 4,
        'title': 'Performance Testing Tasks',
        'minutes': 475,
        'intro': 'A practical performance test moves from goals and workload design to scripting, execution and evidence-based reporting.',
        'sections': [
            {
                'title': '4.1 Planning',
                'summary': 'Planning turns stakeholder expectations and risk information into an achievable, communicable test approach.',
                'points': [
                    'Derive objectives from requirements, business needs, operational profiles and risks.',
                    'Document scope, approach, people, schedule, environment, data, metrics, entry and exit criteria.',
                    'Communicate assumptions and limitations so stakeholders understand what the test can conclude.',
                ],
                'example': 'For a concert sale, the plan defines ticket-search and checkout objectives, expected peak users, payment dependencies, monitoring, test dates and the rule for declaring success.',
            },
            {
                'title': '4.2 Analysis, Design and Implementation',
                'summary': 'Workload analysis and script design represent how users interact with the system and how the test will measure it.',
                'points': [
                    'Identify protocols and transactions, then derive an operational profile from expected user activity.',
                    'Create load profiles with user mix, pacing, concurrency and ramp-up that reflect the scenario.',
                    'Build scripts with valid data, checks and suitable error handling; prepare and verify the execution environment.',
                ],
                'example': 'An online shop profile assigns most simulated users to browsing, some to search and a smaller share to checkout, with think time and unique account data.',
            },
            {
                'title': '4.3 Execution',
                'summary': 'Execution applies the planned workload while confirming that the test and system are behaving as intended.',
                'points': [
                    'Check the environment and baseline before applying the planned load.',
                    'Observe virtual users, response data, errors and system monitors during execution.',
                    'Record deviations and stop or adjust safely if the test conditions invalidate the run.',
                ],
                'example': 'During a ramp-up, the team sees that half the simulated users fail authentication because test accounts are locked, so it stops and corrects the data before repeating the run.',
            },
            {
                'title': '4.4 Analyzing Results and Reporting',
                'summary': 'Analysis connects measured behavior to objectives and investigates likely causes before communicating conclusions.',
                'points': [
                    'Check data quality, compare results with criteria and examine patterns across workload levels.',
                    'Correlate client timings with application and infrastructure measurements to locate constraints.',
                    'Report conclusions, limitations, risks and recommended next actions in language suited to stakeholders.',
                ],
                'example': 'A report shows that response time rises only after a certain concurrency, correlates it with database queue growth and recommends retesting after connection-pool changes.',
            },
        ],
        'key_terms': [
            ('Operational profile', 'A description of how users or business processes use a system.'),
            ('Load profile', 'The workload pattern applied during a performance test.'),
            ('Transaction', 'A logical user or business operation measured as a unit.'),
            ('Think time', 'The pause between user actions that represents human pacing.'),
            ('Entry criterion', 'A condition that must hold before a test activity begins.'),
        ],
        'exam_tips': [
            'Keep operational profile (expected use) distinct from the load profile (test workload).',
            'Check script validity and environment readiness before interpreting results.',
            'A strong report includes conditions and limitations as well as conclusions.',
        ],
    },
    {
        'number': 5,
        'title': 'Tools',
        'minutes': 90,
        'intro': 'Performance tools generate workload and help measure system behavior, but tool selection must fit the test objective and environment.',
        'sections': [
            {
                'title': '5.1 Tool Support',
                'summary': 'Tools can support workload generation, measurement, monitoring, analysis and reporting.',
                'points': [
                    'Identify which parts of the test process need tool support and what evidence each tool provides.',
                    'Check integration with protocols, environments, monitoring and team workflows.',
                    'Remember that tools do not replace workload modeling, test design or interpretation.',
                ],
                'example': 'A team uses a load generator for web traffic, infrastructure monitoring for CPU and memory, and a dashboard to align events on a common timeline.',
            },
            {
                'title': '5.2 Tool Suitability',
                'summary': 'A suitable tool can create the needed workload and collect reliable evidence within practical constraints.',
                'points': [
                    'Evaluate protocol and application support, scale, script maintenance, monitoring, reporting and learning effort.',
                    'Consider licensing, deployment, compatibility, security and the skills available to the team.',
                    'Run a small proof of concept against representative conditions before committing to a tool.',
                ],
                'example': 'Before buying a tool, a team checks whether it can reproduce the application’s authentication flow and generate the target load from its available runners.',
            },
        ],
        'key_terms': [
            ('Load-generation tool', 'Software that creates simulated user or system activity.'),
            ('Monitoring', 'Collecting observations about system state and resource use.'),
            ('Proof of concept', 'A small practical trial used to test suitability or feasibility.'),
        ],
        'exam_tips': [
            'Evaluate tools against the test need, not popularity alone.',
            'A tool’s workload capability and monitoring coverage are separate suitability questions.',
        ],
    },
]
