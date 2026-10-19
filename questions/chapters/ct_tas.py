"""Plain-language study chapters for ISTQB Test Automation Strategy."""

CHAPTERS = [
    {
        'number': 1,
        'title': 'Introduction and Objectives for Test Automation Strategy',
        'minutes': 45,
        'intro': 'Set a direction for test automation by clarifying goals, success factors, and candidate projects.',
        'sections': [
            {
                'title': '1.1 Success factors and investment choices',
                'summary': 'A test automation strategy explains why automation is needed and how it will support project and organizational goals. Investment decisions should consider feasibility and lasting value.',
                'points': [
                    'Define measurable objectives, scope, stakeholders, and the expected contribution to quality and delivery.',
                    'Assess technical success factors such as testability, architecture, interfaces, and suitable environments.',
                    'Compare candidate projects by risk reduction, repeatability, execution frequency, and lifecycle cost.',
                    'Do not assume that automating more tests automatically creates more value.',
                ],
                'example': 'A team prioritizes an API regression suite that runs on every build over a one-time report export test with frequent interface changes.',
            },
        ],
        'key_terms': [
            ('Test automation strategy', 'A plan that defines the goals, scope, approach, and organization of test automation.'),
            ('Testability', 'How readily a system can be tested through observable and controllable behavior.'),
            ('Investment criterion', 'A factor used to decide whether a project merits automation investment.'),
        ],
        'exam_tips': [
            'Start an automation decision by identifying the objective and candidate system characteristics.',
            'Balance expected benefits against implementation and long-term maintenance costs.',
        ],
    },
    {
        'number': 2,
        'title': 'Test Automation Resources',
        'minutes': 60,
        'intro': 'Account for ownership costs, risks, roles, and skills before selecting a technical solution.',
        'sections': [
            {
                'title': '2.1 Costs, risks, and licensing',
                'summary': 'The cost of an automation solution includes more than its purchase price. Technical choices, licensing, operating needs, and risk all affect total cost of ownership.',
                'points': [
                    'Compare acquisition, setup, integration, infrastructure, support, and maintenance costs.',
                    'Understand licensing limits, such as users, devices, parallel execution, or environments.',
                    'Consider vendor dependence, scalability, security, and the cost of changing tools.',
                ],
                'example': 'A team compares an open-source framework with a commercial platform by including hosting, support, training, and device concurrency costs.',
            },
            {
                'title': '2.2 Roles and responsibilities',
                'summary': 'Successful automation requires complementary technical, testing, and domain skills. Clear responsibilities help keep the solution maintainable and useful.',
                'points': [
                    'Identify skills for framework design, test analysis, coding, infrastructure, and product knowledge.',
                    'Assign ownership for maintenance, failures, reporting, and tool administration.',
                    'Plan training and collaboration so automation does not become isolated from the test team.',
                ],
                'example': 'A product team pairs a tester who understands refund rules with an engineer who owns the service-test framework and its pipeline integration.',
            },
        ],
        'key_terms': [
            ('Total cost of ownership', 'The full cost of acquiring, operating, supporting, and maintaining a solution.'),
            ('Licensing model', 'The terms defining how a tool may be used and how it is priced.'),
            ('Automation framework', 'Reusable components and conventions that support automated tests.'),
            ('Technical debt', 'Future cost created by shortcuts or design choices that make change harder.'),
        ],
        'exam_tips': [
            'Include lifecycle and maintenance costs when comparing automation solutions.',
            'Relate team skills and ownership to the sustainability of the automation approach.',
        ],
    },
    {
        'number': 3,
        'title': 'Preparing for Test Automation',
        'minutes': 225,
        'intro': 'Prepare a test automation approach that fits the architecture, lifecycle, and tests selected for automation.',
        'sections': [
            {
                'title': '3.1 Integration across test levels',
                'summary': 'Automation can be distributed across test levels and system boundaries. The architecture and test objective guide where checks should run and what interfaces they use.',
                'points': [
                    'Plan a balanced distribution across unit, component, API, and user-interface tests where applicable.',
                    'Select an approach based on the system architecture, interfaces, and availability of test seams.',
                    'Shift suitable checks earlier for faster feedback while retaining necessary end-to-end coverage.',
                    'Avoid relying heavily on a slow or fragile level when stable lower-level checks can cover the behavior.',
                ],
                'example': 'A shopping system tests discount calculations at service level and reserves a few browser tests for the complete purchase journey.',
            },
            {
                'title': '3.2 Lifecycle and development model considerations',
                'summary': 'Automation preparation differs with the software development lifecycle. Legacy, agile, and DevOps contexts have different constraints and opportunities.',
                'points': [
                    'For legacy systems, plan around existing interfaces, documentation, and limited testability.',
                    'Agile teams benefit when automation is considered during story design and built alongside product changes.',
                    'DevOps approaches integrate automated checks and feedback into delivery pipelines.',
                    'Adapt test selection and maintenance practices to the actual workflow rather than assuming one lifecycle model.',
                ],
                'example': 'A legacy claims system gains a service-level automation layer around its stable batch interface before the team attempts brittle screen automation.',
            },
            {
                'title': '3.3 Suitability and viability of tests',
                'summary': 'Not every test is a good automation candidate. Assess whether the test is repeatable, observable, controllable, and worth the cost to automate and maintain.',
                'points': [
                    'Automate tests that are repeated, time-consuming, data-heavy, or otherwise difficult to perform consistently by hand.',
                    'Consider stability, expected change, test oracle clarity, and setup complexity.',
                    'Tests relying on subjective judgment or rapidly changing interfaces may be difficult to automate reliably.',
                    'Automation can address scale and repeatability challenges, but it cannot replace all human evaluation.',
                ],
                'example': 'A team automates a thousand-record import check but keeps an expert usability review for a redesigned patient dashboard.',
            },
        ],
        'key_terms': [
            ('Test automation distribution', 'How automated tests are allocated across levels or system boundaries.'),
            ('Shift left', 'Moving suitable testing activities earlier in the lifecycle for earlier feedback.'),
            ('Test seam', 'An interface or point that allows a component to be controlled or observed for testing.'),
            ('Test oracle', 'A means of determining whether an actual result is acceptable.'),
            ('Viability', 'Whether an approach is practical and sustainable in its intended context.'),
        ],
        'exam_tips': [
            'Select the automation level based on architecture and feedback goals, not a fixed preferred layer.',
            'Assess test suitability using repeatability, stability, observability, oracle clarity, and maintenance effort.',
            'Consider the different constraints of legacy, agile, and DevOps contexts.',
        ],
    },
    {
        'number': 4,
        'title': 'Organizational Deployment and Release Strategies for Test Automation',
        'minutes': 135,
        'intro': 'Plan how automation enters operationally relevant scenarios and how its deployment risks are controlled.',
        'sections': [
            {
                'title': '4.1 Test automation solution planning',
                'summary': 'A solution plan connects automation to delivery needs, reported defects, realistic scenarios, and operational context.',
                'points': [
                    'Use automation to provide timely evidence that supports shorter time to market without weakening quality controls.',
                    'Include tests that verify reported defects and reduce the chance of recurrence.',
                    'Design scenarios that reflect operational use, data, integrations, and failure conditions.',
                ],
                'example': 'After fixing a payment timeout defect, the team adds an automated scenario that reproduces a delayed gateway response and checks safe retry behavior.',
            },
            {
                'title': '4.2 Deployment strategies and risks',
                'summary': 'Deploying automation into teams and pipelines requires an adoption strategy. Risks such as false confidence, unstable tests, and poor integration need planned mitigations.',
                'points': [
                    'Define rollout scope, ownership, success measures, and integration with delivery workflows.',
                    'Identify risks including unreliable results, lack of skills, tool incompatibility, and unmaintained assets.',
                    'Mitigate with pilots, monitoring, training, clear failure triage, and incremental expansion.',
                ],
                'example': 'A team pilots browser automation on one stable workflow, tracks flaky failures, and expands to other journeys after stabilizing the test setup.',
            },
            {
                'title': '4.3 Test environment dependencies',
                'summary': 'Automation depends on environments, infrastructure, data, interfaces, and services. Making dependencies explicit helps tests run consistently and safely.',
                'points': [
                    'Identify required tools, agents, browsers, devices, network services, and environment configuration.',
                    'Specify test data needs and how data is created, protected, reset, and cleaned up.',
                    'Document interfaces and dependencies so failures can be diagnosed and environments maintained.',
                ],
                'example': 'A mobile test suite documents device-farm access, test accounts, payment sandbox settings, and cleanup steps before running in CI.',
            },
        ],
        'key_terms': [
            ('Operational scenario', 'A test scenario that reflects how a system is used in its real operating context.'),
            ('Deployment strategy', 'A plan for introducing and integrating automation into teams and workflows.'),
            ('Flaky test', 'A test that produces inconsistent results without a relevant product change.'),
            ('Test environment dependency', 'A resource or service required for a test to execute reliably.'),
        ],
        'exam_tips': [
            'Include operationally relevant scenarios and defect verification when planning an automation solution.',
            'Pair deployment risks with concrete mitigations and staged adoption.',
            'Treat test data, infrastructure, and interfaces as explicit environment dependencies.',
        ],
    },
    {
        'number': 5,
        'title': 'Test Automation Impact Analysis',
        'minutes': 150,
        'intro': 'Measure the costs and effects of automation so reports and investment decisions support real objectives.',
        'sections': [
            {
                'title': '5.1 Investment, maintenance, and return',
                'summary': 'Automation has initial and continuing costs, while benefits may include faster feedback, repeatability, and broader execution. Analyze return over an appropriate time horizon.',
                'points': [
                    'Include setup, licensing, infrastructure, execution, failure analysis, and maintenance effort.',
                    'Compare automated and manual effort over repeated use rather than relying on a one-time cost comparison.',
                    'Consider qualitative effects such as consistency, risk reduction, and availability of tester time.',
                ],
                'example': 'A team estimates how many release cycles are needed for an automated nightly regression suite to offset its framework and upkeep costs.',
            },
            {
                'title': '5.2-5.3 Metrics and organizational value',
                'summary': 'Metrics indicate how automation assets and practices perform, but only meaningful measures help determine value. Project and organization characteristics affect the right implementation.',
                'points': [
                    'Classify measures such as execution time, reliability, maintenance effort, coverage, and defect detection.',
                    'Interpret metrics in context; a high number of automated cases does not prove useful risk coverage.',
                    'Consider project stability, release frequency, criticality, and organizational capability when judging value.',
                ],
                'example': 'A dashboard tracks execution time and flaky failures for the checkout suite, while the product owner reviews whether the suite covers priority payment risks.',
            },
            {
                'title': '5.4 Decisions from automation reports',
                'summary': 'Reports should help stakeholders make decisions about releases, investigation, and investment. Clear context prevents test results from being mistaken for a complete quality verdict.',
                'points': [
                    'Present status, trends, scope, environment, and known limitations alongside results.',
                    'Use failures and trends to focus investigation and improvement.',
                    'Avoid treating pass rates or automation counts as standalone measures of product quality.',
                ],
                'example': 'A release report separates product defects from environment failures and identifies which risk areas the executed suite did not cover.',
            },
        ],
        'key_terms': [
            ('Return on investment', 'Benefits compared with the costs of an investment over a defined period.'),
            ('Automation metric', 'A measure used to assess automation activity, assets, or outcomes.'),
            ('Flakiness', 'Inconsistent test outcomes that are not explained by a product change.'),
            ('Impact analysis', 'Assessment of how automation affects project or organizational outcomes.'),
        ],
        'exam_tips': [
            'Include maintenance and failure analysis costs when calculating automation value.',
            'Interpret test metrics with scope and context; automated case count alone is not quality.',
            'Use reports to support a defined decision, not merely to display a pass percentage.',
        ],
    },
    {
        'number': 6,
        'title': 'Implementation and Improvement Strategies for Test Automation',
        'minutes': 150,
        'intro': 'Manage transitions into continuous testing and improve automation practices across the organization.',
        'sections': [
            {
                'title': '6.1 Transitioning to continuous testing',
                'summary': 'Moving between manual and automated testing changes workflows, skills, and responsibilities. A planned transition protects useful testing while building repeatable feedback.',
                'points': [
                    'Assess existing test assets, skills, risks, and process constraints before changing the approach.',
                    'Plan how manual activities will be selected for automation, implemented, reviewed, and maintained.',
                    'When replacing or extending automation, preserve coverage and manage transition risks rather than switching abruptly.',
                ],
                'example': 'A team automates stable smoke checks first while keeping exploratory sessions for new features, then reviews coverage before retiring duplicated manual scripts.',
            },
            {
                'title': '6.2 Organization-wide strategy and improvement',
                'summary': 'An organizational strategy evaluates existing assets and practices, then directs improvements that align teams and reduce duplicated effort.',
                'points': [
                    'Inventory frameworks, test assets, tools, skills, and recurring maintenance problems.',
                    'Identify improvement opportunities through evidence such as reuse, reliability, feedback speed, and business value.',
                    'Coordinate standards and shared components while allowing teams to respond to local needs.',
                    'Review the strategy regularly as systems, tools, and delivery practices change.',
                ],
                'example': 'An organization finds three teams maintaining separate API test libraries and creates a shared core while retaining service-specific extensions.',
            },
        ],
        'key_terms': [
            ('Continuous testing', 'Testing feedback integrated throughout ongoing development and delivery.'),
            ('Test automation asset', 'A reusable artifact such as a script, framework component, data set, or configuration.'),
            ('Improvement strategy', 'A planned set of changes intended to improve automation outcomes over time.'),
            ('Transition plan', 'A sequence of activities for moving from a current way of working to a target approach.'),
        ],
        'exam_tips': [
            'Plan transitions with existing coverage, skills, and maintenance in mind; do not remove manual tests just because automation is possible.',
            'Organization-wide improvement begins by assessing current assets and practices and should be revisited over time.',
        ],
    },
]
