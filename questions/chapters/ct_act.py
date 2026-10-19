CHAPTERS = [
    {
        'number': 1,
        'title': 'Introduction and Foundations',
        'minutes': 80,
        'intro': 'Acceptance testing checks whether a solution meets business needs and is ready for its intended users.',
        'sections': [
            {
                'title': '1.1 Fundamental Relationships',
                'summary': 'Business goals lead to needs and requirements, which can be expressed as stories, criteria and tests.',
                'points': [
                    'A business goal describes an outcome; a need explains what stakeholders require to reach it.',
                    'Acceptance criteria define conditions a story or requirement must satisfy, and acceptance tests check those conditions.',
                    'Clear, testable requirements reduce disagreement and help reveal missing or conflicting expectations.',
                ],
                'example': 'For a booking app, the goal is fewer abandoned reservations; a requirement says guests can reserve a room, and criteria define when a reservation is confirmed and how cancellation works.',
            },
            {
                'title': '1.2 Business Analysis and Acceptance Testing',
                'summary': 'Business analysts and testers use related perspectives to refine requirements and produce useful acceptance feedback.',
                'points': [
                    'Business analysis clarifies stakeholder problems, value and solution requirements; testing evaluates the resulting behavior.',
                    'Collaborate early to identify ambiguity, examples, boundary cases and risks before implementation.',
                    'Acceptance test-driven development (ATDD) and behavior-driven development (BDD) express expected behavior before coding.',
                ],
                'example': 'A business analyst and tester refine “send a reminder” by agreeing on the due date, time zone, opt-out behavior and a Given/When/Then example before developers implement it.',
            },
        ],
        'key_terms': [
            ('Business goal', 'An outcome an organization wants to achieve.'),
            ('Business need', 'A stakeholder requirement that supports a business goal.'),
            ('Acceptance criterion', 'A condition that a solution must meet to be accepted.'),
            ('ATDD', 'Acceptance test-driven development: define acceptance examples before implementation.'),
        ],
        'exam_tips': [
            'Keep business goals, needs, requirements, criteria and tests distinct but traceable.',
            'Look for collaboration early enough to prevent ambiguity from becoming code.',
        ],
    },
    {
        'number': 2,
        'title': 'Acceptance Criteria, Acceptance Tests and Experience-Based Practices',
        'minutes': 165,
        'intro': 'Good acceptance criteria make expectations explicit, while a mix of designed and experience-based testing checks them from useful angles.',
        'sections': [
            {
                'title': '2.1 Writing Acceptance Criteria',
                'summary': 'Acceptance criteria should be understandable, observable and specific enough to guide implementation and evaluation.',
                'points': [
                    'Write criteria from the user or business perspective and keep each condition focused.',
                    'Use examples and measurable outcomes to remove vague words such as “quick” or “easy.”',
                    'Review criteria with the people who will build, test and accept the solution.',
                ],
                'example': 'Instead of “search is fast,” specify that a product search with 10,000 items returns matching results within two seconds under the agreed test conditions.',
            },
            {
                'title': '2.2 Designing Acceptance Tests',
                'summary': 'Acceptance tests turn agreed criteria into checks that provide evidence about business behavior.',
                'points': [
                    'Use suitable black-box techniques such as equivalence partitioning, boundary-value analysis and decision tables.',
                    'Derive cases from criteria and business rules, including valid, invalid and important boundary conditions.',
                    'Gherkin scenarios use Given, When and Then to describe context, action and observable result.',
                ],
                'example': 'For a discount valid on orders from $50, test a $49.99 order, the exact $50 boundary and an order above $50, then express a representative case in Given/When/Then form.',
            },
            {
                'title': '2.3 Experience-Based Approaches for Acceptance Testing',
                'summary': 'Exploratory and beta testing use human judgment and real usage to find issues scripted cases may miss.',
                'points': [
                    'Exploratory testing combines learning, test design and execution; a charter or mission keeps the exploration purposeful.',
                    'Record observations and discoveries so that important findings can be communicated and repeated where appropriate.',
                    'Beta testing gathers feedback from representative users in their own context, with risks and support planned.',
                ],
                'example': 'Before a travel app launch, a tester explores the booking flow using a charter about interrupted payment; selected customers then try the beta on their own devices and report confusing recovery steps.',
            },
        ],
        'key_terms': [
            ('Equivalence partition', 'A group of inputs expected to be handled in the same way.'),
            ('Boundary-value analysis', 'Testing values at and near the edges of an input range.'),
            ('Gherkin', 'A structured Given/When/Then notation for behavior examples.'),
            ('Exploratory testing', 'Testing in which learning, design and execution happen together.'),
            ('Beta testing', 'Evaluation by selected users in a realistic environment.'),
        ],
        'exam_tips': [
            'Choose a test technique that targets the structure of the stated rule or input range.',
            'Exploratory testing is planned learning, not unstructured clicking.',
            'Beta testing takes place with users in a realistic setting, not just in the test lab.',
        ],
    },
    {
        'number': 3,
        'title': 'Business Process and Business Rules Modeling',
        'minutes': 150,
        'intro': 'Models make business decisions and process paths visible so acceptance tests can cover meaningful scenarios.',
        'sections': [
            {
                'title': '3.1 Modeling Business Processes and Rules',
                'summary': 'Process and rule models represent activities, choices and constraints in a business domain.',
                'points': [
                    'A process model shows the flow of activities and decision points; a rule model makes conditions and outcomes explicit.',
                    'Use a notation suited to the audience and keep models consistent with real business language.',
                    'Check models with stakeholders so that alternate paths and exceptions are not hidden.',
                ],
                'example': 'A returns process model shows the path for an in-period return, an expired return and a damaged item, while a decision table records which refund each case receives.',
            },
            {
                'title': '3.2 Deriving Acceptance Tests from Business Process/Rule Models',
                'summary': 'Each relevant route or rule outcome can be turned into an acceptance scenario with expected results.',
                'points': [
                    'Select paths that cover significant decisions, outcomes and interactions in the model.',
                    'Use decision tables to expose combinations and missing rules; use process paths to check end-to-end behavior.',
                    'Trace tests to model elements so changed business rules reveal which checks need review.',
                ],
                'example': 'A loan decision table varies income evidence and credit status; tests cover approval, rejection and manual review outcomes rather than testing only the usual approval path.',
            },
            {
                'title': '3.3 Business Process Modeling for Acceptance Testing',
                'summary': 'Well-formed process models support shared understanding and can drive collaborative examples and automated checks.',
                'points': [
                    'Keep the model readable, correctly scoped and validated with business stakeholders.',
                    'Connect model events and rules to concrete acceptance examples, including exceptional paths.',
                    'In ATDD, use the model to discuss examples before development and maintain alignment as the process changes.',
                ],
                'example': 'A team models a subscription cancellation process, checks the refund and access rules with the business owner, then derives acceptance scenarios for immediate and end-of-cycle cancellation.',
            },
        ],
        'key_terms': [
            ('Business process model', 'A representation of activities and decisions in a business workflow.'),
            ('Business rule', 'A constraint or condition that governs a business decision.'),
            ('Decision table', 'A table showing rule combinations and their expected outcomes.'),
            ('Process path', 'A particular route through a modeled workflow.'),
        ],
        'exam_tips': [
            'Use a decision table when several conditions combine to produce different outcomes.',
            'A model is useful only when it reflects agreed business behavior and exceptions.',
        ],
    },
    {
        'number': 4,
        'title': 'Acceptance Testing for Non-Functional Requirements',
        'minutes': 95,
        'intro': 'Acceptance covers not only what a system does but also how well users can use it and how safely and efficiently it operates.',
        'sections': [
            {
                'title': '4.1 Non-functional Characteristics and Quality in Use',
                'summary': 'Non-functional requirements describe quality characteristics, including outcomes experienced by users in a context.',
                'points': [
                    'Quality in use focuses on effectiveness, efficiency and satisfaction for specified users, goals and environments.',
                    'Translate broad quality expectations into observable conditions and measurable acceptance criteria.',
                    'Consider context: user groups, tasks, devices and operational conditions affect acceptable quality.',
                ],
                'example': 'A public-service form is evaluated for completion success and user satisfaction by first-time applicants using mobile phones and assistive technology.',
            },
            {
                'title': '4.2 Usability and User Experience',
                'summary': 'Usability concerns how effectively and efficiently users reach goals; user experience includes their wider perceptions and feelings.',
                'points': [
                    'Analyze user goals and context before writing experience and usability requirements.',
                    'Use representative tasks and participants to assess ease of learning, task completion and satisfaction.',
                    'Turn findings into specific changes and re-check them with users.',
                ],
                'example': 'A clinic tests whether patients can find an appointment and understand the confirmation on a phone, noting both task success and confidence in the result.',
            },
            {
                'title': '4.3 Performance Efficiency',
                'summary': 'Performance acceptance checks whether a solution responds and uses resources well enough for expected business use.',
                'points': [
                    'Set performance goals for realistic load, workload mix and operating conditions.',
                    'Use measurable criteria such as response time, throughput and resource use rather than impressions.',
                    'Relate test results to user and business impact, including peak periods.',
                ],
                'example': 'A ticket site agrees that search results must appear within two seconds for 2,000 concurrent users during a scheduled sale.',
            },
            {
                'title': '4.4 Security',
                'summary': 'Security acceptance checks that the solution protects information and enforces the agreed access rules.',
                'points': [
                    'Derive acceptance checks from security needs, threat context and relevant policies.',
                    'Verify that permitted actions work and that unauthorized access is denied without exposing sensitive details.',
                    'Plan who receives security findings and how they will be handled.',
                ],
                'example': 'A banking app verifies that a customer can view their own statement but cannot retrieve another customer’s statement by changing an account identifier.',
            },
        ],
        'key_terms': [
            ('Non-functional requirement', 'A requirement about a quality attribute rather than a specific feature.'),
            ('Quality in use', 'Quality experienced by users pursuing goals in a stated context.'),
            ('Usability', 'How effectively and efficiently specified users can achieve goals.'),
            ('Performance efficiency', 'Performance relative to the resources used.'),
            ('Security', 'Protection of information and systems against relevant threats.'),
        ],
        'exam_tips': [
            'Make a quality requirement measurable and state the usage context.',
            'Do not confuse usability (task interaction) with the broader user experience.',
            'For security, test both allowed behavior and meaningful denial of prohibited behavior.',
        ],
    },
    {
        'number': 5,
        'title': 'Collaborative Acceptance Testing',
        'minutes': 110,
        'intro': 'Acceptance testing works best when business, development and testing perspectives collaborate on examples, findings and decisions.',
        'sections': [
            {
                'title': '5.1 Collaboration',
                'summary': 'Collaboration brings stakeholders together to agree on what value and acceptable behavior mean.',
                'points': [
                    'Use shared examples and conversation to clarify expectations before they become costly rework.',
                    'Involve people with business, technical and user knowledge, while keeping acceptance decisions explicit.',
                    'Encourage constructive discussion of defects as information about the product, not blame.',
                ],
                'example': 'A product owner, developer and tester walk through a refund scenario together and agree what the customer, payment service and order history should each show.',
            },
            {
                'title': '5.2 Activities',
                'summary': 'Acceptance work includes analyzing defects, reporting useful evidence and supporting quality assurance.',
                'points': [
                    'Analyze a failure to understand its impact, reproducibility, affected rules and urgency.',
                    'Report results clearly to the people who need to decide, including status, evidence and open risks.',
                    'Use QA activities such as reviewing acceptance criteria and improving the process to prevent repeated misunderstandings.',
                ],
                'example': 'A tester reports that a late payment is accepted after an order expires, includes the steps and transaction ID, and works with the business owner to clarify the rule.',
            },
            {
                'title': '5.3 Tool Support',
                'summary': 'Tools help teams manage acceptance criteria, examples, execution evidence and shared results.',
                'points': [
                    'Choose tools that support traceability and fit the team’s collaboration workflow.',
                    'Automate repeatable checks where they provide fast and maintainable feedback.',
                    'Keep human review for context, usability and decisions that need stakeholder judgment.',
                ],
                'example': 'A team links an acceptance criterion to a tracked example and automated API check, while recording user-test feedback alongside the release decision.',
            },
        ],
        'key_terms': [
            ('Collaboration', 'Joint work in which stakeholders share understanding and decisions.'),
            ('Defect analysis', 'Investigation of a reported problem and its significance.'),
            ('Test report', 'A communication of testing scope, evidence, results and risks.'),
            ('Traceability', 'Links between requirements, acceptance checks and outcomes.'),
        ],
        'exam_tips': [
            'Effective defect reports contain evidence and impact, not blame.',
            'Tools support collaboration; they do not replace stakeholder agreement or judgment.',
        ],
    },
]
