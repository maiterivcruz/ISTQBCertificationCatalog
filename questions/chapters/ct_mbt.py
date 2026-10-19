"""Plain-language study chapters for ISTQB Model-Based Testing."""

CHAPTERS = [
    {
        'number': 1,
        'title': 'Introduction to Model-Based Testing',
        'minutes': 90,
        'intro': 'See how a model can represent behavior and help derive tests while remaining connected to project goals.',
        'sections': [
            {
                'title': '1.1 Motivations, activities, and work products',
                'summary': 'Model-based testing (MBT) uses a model of the system or its behavior to support test design or generation. It can improve consistency, but it does not remove the need for tester judgment.',
                'points': [
                    'MBT can help explore complex behavior, generate many tests, and keep tests aligned with a changing model.',
                    'Typical work includes creating, validating, and maintaining a model, selecting tests, and connecting generated cases to execution.',
                    'Inputs can include requirements or design information; outputs can include test cases, procedures, and traceability.',
                    'Avoid expecting a model to discover every requirement or automatically guarantee useful tests.',
                ],
                'example': 'A team models an online checkout’s states and transitions to systematically derive tests for payment success, cancellation, and retry.',
            },
            {
                'title': '1.2 Integrating MBT into the lifecycle',
                'summary': 'MBT can be used in sequential or iterative development and may also support requirements engineering. Its timing and outputs should fit the team’s lifecycle.',
                'points': [
                    'In sequential projects, a model may be based on approved specifications and used to prepare tests before execution.',
                    'In iterative work, update and review the model as requirements and implementation evolve.',
                    'A model can expose missing, ambiguous, or conflicting requirements early.',
                ],
                'example': 'During refinement, a product team uses a state model of account suspension to identify an undefined rule before the feature is coded.',
            },
        ],
        'key_terms': [
            ('Model-based testing', 'Testing that uses a model to support test analysis, design, generation, or execution.'),
            ('MBT model', 'A representation of system behavior or structure used to derive or guide tests.'),
            ('Work product', 'An artifact created or used during a development or testing activity.'),
            ('Traceability', 'Links among requirements, model elements, tests, and results.'),
        ],
        'exam_tips': [
            'Distinguish MBT’s potential benefits from claims that it eliminates test design or guarantees coverage.',
            'Consider model maintenance and validation as part of the MBT process.',
        ],
    },
    {
        'number': 2,
        'title': 'MBT Modeling',
        'minutes': 250,
        'intro': 'Build models that represent the right behavior at a useful level of detail for the test objective.',
        'sections': [
            {
                'title': '2.1 Modeling activities and focus',
                'summary': 'An MBT model is deliberately scoped around what must be tested. Modelers identify relevant elements, behavior, and abstractions before using the model to derive tests.',
                'points': [
                    'Define the test objective and select model elements that support it.',
                    'Model the system, environment, data, or process depending on the question the tests must answer.',
                    'Model detail should be sufficient for test generation without becoming harder to maintain than the tests it supports.',
                ],
                'example': 'For a parcel locker, a state model may focus on available, reserved, collected, and expired states rather than model every screen animation.',
            },
            {
                'title': '2.2 Modeling languages and quality',
                'summary': 'Different modeling languages represent different kinds of systems and behavior. Good model design makes assumptions visible and supports review, reuse, and test generation.',
                'points': [
                    'Choose a notation suited to the system, team skills, and intended test selection.',
                    'Check the model for consistency, completeness for its purpose, readability, and accurate correspondence to the test basis.',
                    'Avoid common pitfalls such as excessive complexity, missing behavior, and unclear guards or actions.',
                    'Link requirements and process information when needed for traceability and impact analysis.',
                ],
                'example': 'A team uses a state-transition notation for a connected door lock because its behavior depends on modes, events, and guards.',
            },
            {
                'title': '2.3 Reuse, tools, and iterative validation',
                'summary': 'Existing requirements or design models may be reused, but they should be checked for testing suitability. Tool support and iterative reviews help keep a model useful as the product changes.',
                'points': [
                    'Reuse source models where they are accurate and appropriate, adapting them to the test objective.',
                    'Use tools to create, inspect, analyze, and generate from models, while understanding their limitations.',
                    'Review and validate a model with domain and testing knowledge before relying on generated cases.',
                    'Revise the model when requirements, behavior, or test goals change.',
                ],
                'example': 'A team imports a workflow model from business analysis, then adds error paths and reviews it with support staff before generating tests.',
            },
        ],
        'key_terms': [
            ('Abstraction', 'A simplified representation that retains details relevant to a purpose.'),
            ('Guard', 'A condition that must be true for a modeled transition to occur.'),
            ('Model validation', 'Checking that a model is suitable and represents intended behavior.'),
            ('Modeling language', 'A notation with defined concepts for expressing a model.'),
        ],
        'exam_tips': [
            'Start modeling choices with the test objective; the same system can need different models for different goals.',
            'Assess whether a reused model is suitable for testing rather than assuming design artifacts are test-ready.',
            'Include iteration, review, and validation in model development.',
        ],
    },
    {
        'number': 3,
        'title': 'Selection Criteria for Test Case Generation',
        'minutes': 205,
        'intro': 'Choose criteria that guide which paths, states, or data combinations a generated test suite should cover.',
        'sections': [
            {
                'title': '3.1 Classes of test selection criteria',
                'summary': 'Selection criteria define what parts or behaviors of a model generated tests should exercise. Different criteria provide different levels and kinds of coverage.',
                'points': [
                    'Possible criteria focus on states, transitions, paths, requirements, data, or combinations of model elements.',
                    'More demanding criteria can increase test count and execution cost without always improving risk coverage proportionally.',
                    'Compare criteria using the test objective, model structure, and risks of missed behavior.',
                ],
                'example': 'A vending-machine model may use transition coverage to ensure every action is exercised, then add specific sequences for refunds and rejected coins.',
            },
            {
                'title': '3.2 Applying criteria in practice',
                'summary': 'Applying a criterion requires understanding the generated cases, the automation available, and the limits of the model. Practical selection balances confidence with execution and maintenance effort.',
                'points': [
                    'Choose criteria that are achievable and meaningful for the objective and model.',
                    'Decide how much generation and test implementation can be automated and where review is needed.',
                    'Consider strengths and limitations of each criterion, including redundancy and infeasible paths.',
                    'Use risk and experience to supplement model coverage where the model omits relevant behavior.',
                ],
                'example': 'For a medical device mode model, the team selects transition criteria for routine checks and adds expert-designed cases for a high-risk alarm combination.',
            },
        ],
        'key_terms': [
            ('Test selection criterion', 'A rule that determines which tests are selected from a model.'),
            ('State coverage', 'Coverage based on visiting modeled states.'),
            ('Transition coverage', 'Coverage based on exercising modeled transitions.'),
            ('Test generation', 'Deriving test cases or procedures from a model using selected criteria.'),
        ],
        'exam_tips': [
            'Do not assume that one selection criterion is best for every model or test goal.',
            'Consider generated test volume, feasibility, and execution cost when comparing criteria.',
            'Model coverage is not proof that requirements or product risks are fully covered.',
        ],
    },
    {
        'number': 4,
        'title': 'MBT Test Implementation and Execution',
        'minutes': 120,
        'intro': 'Turn model-derived cases into executable tests and keep generated assets aligned with changes.',
        'sections': [
            {
                'title': '4.1 Test cases and execution kinds',
                'summary': 'MBT outputs may describe tests at different levels. Implementation connects those descriptions to the system, tools, data, and execution environment.',
                'points': [
                    'High-level cases express goals and behavior; lower-level cases include more implementation detail.',
                    'Execution may be manual, automated, or a combination, depending on the model and test environment.',
                    'Keep a clear link between generated tests, their source model, and observed results.',
                ],
                'example': 'A model-generated high-level test says “lock after three failed codes”; an implementation maps it to keypad actions and a device test harness.',
            },
            {
                'title': '4.2 Change impact and test adaptation',
                'summary': 'Changes to requirements, models, or products can affect generated cases and their implementation. Impact analysis helps teams update the right artifacts and avoid stale tests.',
                'points': [
                    'Identify which model elements, generated cases, and execution scripts depend on a changed behavior.',
                    'Regenerate or adapt tests when model changes invalidate previous outputs.',
                    'Review the impact on data, environments, and automation interfaces as well as case steps.',
                ],
                'example': 'When a locker adds a temporary-access state, the team identifies affected transitions, regenerates cases, and updates the device automation mapping.',
            },
        ],
        'key_terms': [
            ('High-level test case', 'A test description focused on purpose and behavior rather than implementation steps.'),
            ('Test adaptation', 'Changing a test or its implementation to remain valid after system or model changes.'),
            ('Impact analysis', 'Identifying artifacts and activities affected by a change.'),
        ],
        'exam_tips': [
            'Distinguish high-level test intent from low-level executable steps.',
            'When a model changes, consider the impact on generated cases and their implementation, data, and interfaces.',
        ],
    },
    {
        'number': 5,
        'title': 'Evaluating and Deploying an MBT Approach',
        'minutes': 60,
        'intro': 'Judge whether MBT is delivering value and plan a rollout that fits organizational needs.',
        'sections': [
            {
                'title': '5.1 Evaluation, objectives, and metrics',
                'summary': 'Evaluate MBT against the objectives that motivated its introduction. A useful assessment considers both measurable results and the characteristics of the approach that produced them.',
                'points': [
                    'Consider investment, maintenance effort, coverage, test quality, speed, and defect detection as relevant ROI factors.',
                    'Select metrics that reflect organizational objectives and avoid optimizing a single measure in isolation.',
                    'Monitor the deployment to see whether expected benefits and quality outcomes are being achieved.',
                ],
                'example': 'A team compares the time to update model-based regression tests with its previous manual process and checks that defect detection remains effective.',
            },
            {
                'title': '5.2 Deployment and cost management',
                'summary': 'Successful deployment needs suitable skills, tool integration, and manageable costs. Starting with a focused pilot can reveal organizational and technical needs before broader adoption.',
                'points': [
                    'Plan training, stakeholder involvement, support, and integration with existing test processes.',
                    'Account for licenses, model creation, tool integration, and ongoing maintenance.',
                    'Use lessons from an initial deployment to refine the approach before expanding it.',
                ],
                'example': 'A team pilots MBT on a stable booking workflow, measures maintenance and execution effort, then decides whether other services merit the same investment.',
            },
        ],
        'key_terms': [
            ('Return on investment', 'A comparison of benefits achieved with the costs required to achieve them.'),
            ('Key performance indicator', 'A measure used to assess progress toward an organizational objective.'),
            ('Deployment', 'Introducing an approach into the organization and integrating it into ongoing work.'),
        ],
        'exam_tips': [
            'Tie MBT measures to the original organizational objective and include maintenance costs.',
            'A pilot and incremental rollout can uncover integration and skills needs before wider adoption.',
        ],
    },
]
