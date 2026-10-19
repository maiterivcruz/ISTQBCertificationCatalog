CHAPTERS = [
    {
        'number': 1,
        'title': 'Quality Assistance',
        'minutes': 60,
        'intro': 'Quality assistance brings quality work closer to the people building the product, so teams can prevent problems instead of handing them off late.',
        'sections': [
            {
                'title': '1.1 What is Quality Assistance?',
                'summary': 'Quality assistance is a collaborative way to help a team make good quality decisions throughout delivery.',
                'points': [
                    'The quality specialist coaches and enables the team; quality remains a shared responsibility.',
                    'Build quality into discovery, design, coding and release rather than relying only on a final test phase.',
                    'Choose support that fits the team and risk instead of adding a fixed approval gate to every change.',
                ],
                'example': 'A tester joins a team planning a new checkout flow and helps clarify failure cases before development, then pairs with developers to add focused checks as the feature is built.',
            },
            {
                'title': '1.2 Skills for Quality Assistance',
                'summary': 'Quality assistance depends on influence and collaboration as much as on testing expertise.',
                'points': [
                    'Use active listening, facilitation and clear questions to uncover assumptions without blaming people.',
                    'Combine testing knowledge with technical, product and customer understanding.',
                    'Adapt coaching to the team’s maturity and encourage learning instead of taking over its work.',
                ],
                'example': 'When a product owner says a search screen is “fast enough,” a quality coach helps the group agree on a measurable response-time target and a way to check it.',
            },
        ],
        'key_terms': [
            ('Quality assistance', 'Collaborative support that helps teams build quality into their work.'),
            ('Shared responsibility', 'The idea that everyone on the team contributes to product quality.'),
            ('Quality mindset', 'A habit of considering customer value and risk in everyday decisions.'),
        ],
        'exam_tips': [
            'Distinguish enabling a team from acting as its separate quality gate.',
            'In scenarios, look for early collaboration and shared ownership of quality.',
        ],
    },
    {
        'number': 2,
        'title': 'Improve Quality and Flow in a Value-Driven Organization',
        'minutes': 120,
        'intro': 'A value stream shows how an idea becomes something useful for a customer. Seeing the whole flow helps leaders find delays and quality problems.',
        'sections': [
            {
                'title': '2.1 Facilitate Value Stream Mapping',
                'summary': 'Value stream mapping makes the steps, handoffs and waiting time between customer need and delivery visible.',
                'points': [
                    'Map the real current process with the people who do the work, including queues and feedback loops.',
                    'Separate time spent creating value from waiting or rework, then sketch a practical future state.',
                    'Use the map to start improvement, not as a one-time diagram or a way to blame a role.',
                ],
                'example': 'A bank maps a loan change from request to release and discovers that most elapsed time is spent waiting for a manual test environment, not running tests.',
            },
            {
                'title': '2.2 Analyze a Value Stream from a Quality and Testing Perspective',
                'summary': 'Quality-focused analysis uses flow evidence to find delays, unnecessary work and weak feedback.',
                'points': [
                    'Compare lead time, cycle time, throughput, queues and rework to understand how work moves.',
                    'Identify waste such as repeated approvals, duplicated checks and defects discovered late.',
                    'Prefer small experiments that shorten feedback while protecting the level of quality customers need.',
                ],
                'example': 'A delivery team tracks change lead time and defect escape rates; a long security-review queue and repeated late findings prompt an earlier threat-modeling session.',
            },
        ],
        'key_terms': [
            ('Value stream', 'The end-to-end work needed to deliver value to a customer.'),
            ('Value stream map', 'A visual representation of work steps, information flow and delays.'),
            ('Lead time', 'Elapsed time from a request or work item starting until delivery.'),
            ('Waste', 'Work or waiting that does not add customer value.'),
        ],
        'exam_tips': [
            'Distinguish elapsed lead time from time actively spent working on an item.',
            'A useful map describes the current reality and leads to a measurable experiment.',
        ],
    },
    {
        'number': 3,
        'title': 'Continuous Improvement of Quality and Testing',
        'minutes': 150,
        'intro': 'Continuous improvement uses evidence and systems thinking to address recurring problems rather than treating each symptom in isolation.',
        'sections': [
            {
                'title': '3.1 Structured Problem-Solving Approach for Quality and Testing Activities',
                'summary': 'A structured improvement cycle helps teams test whether a change actually improves their work.',
                'points': [
                    'Plan a change and a way to measure it, try the change, check the evidence and act on what was learned (PDCA).',
                    'Make the experiment small enough to learn safely, and repeat the cycle when results are uncertain.',
                    'Embed improvement in normal team routines so learning does not depend on a special project.',
                ],
                'example': 'A team plans to reduce escaped checkout defects by adding a short risk review, tries it for two sprints, compares escape data, and adjusts the review based on the results.',
            },
            {
                'title': '3.2 Systems Thinking and Analysis of Root Causes',
                'summary': 'Systems thinking looks at relationships and feedback across the organization, not just the person or event closest to a failure.',
                'points': [
                    'Ask why a problem can recur in the surrounding process, incentives, information and constraints.',
                    'Use causal-loop diagrams to show how factors reinforce or balance one another over time.',
                    'Choose actions that change the conditions producing defects, and watch for unintended effects elsewhere.',
                ],
                'example': 'A release misses testing repeatedly. A systems view shows that late scope changes create a queue, while rewarding only delivery dates discourages early risk reporting; the team changes planning and reporting incentives.',
            },
        ],
        'key_terms': [
            ('PDCA', 'Plan-Do-Check-Act, a repeating cycle for testing and refining an improvement.'),
            ('Root cause', 'An underlying condition that explains why a problem happened.'),
            ('Systems thinking', 'Understanding how connected parts influence a whole system.'),
            ('Causal loop', 'A set of linked causes whose effects feed back into the system.'),
        ],
        'exam_tips': [
            'PDCA is a learning cycle; checking evidence is essential before standardizing a change.',
            'Prefer actions on process conditions over blaming an individual for a symptom.',
        ],
    },
    {
        'number': 4,
        'title': 'Organizational Test Strategy in a Value-Driven Organization',
        'minutes': 165,
        'intro': 'An organizational test strategy gives teams shared direction while allowing approaches to fit the product, delivery model and risks.',
        'sections': [
            {
                'title': '4.1 Establish an Organizational Test Strategy',
                'summary': 'A strategy connects testing choices to business outcomes and the technical environment.',
                'points': [
                    'Use DevOps practices such as continuous integration, automated checks and production monitoring to shorten feedback.',
                    'Define principles, responsibilities and support that can be adapted by streams and products.',
                    'Check alignment with business goals, architecture, regulation and operational risks; revise when context changes.',
                ],
                'example': 'A retailer’s strategy calls for fast automated checks on every change, deeper payment-risk testing before release, and production monitoring for service-level objectives.',
            },
            {
                'title': '4.2 Fit Agile Test Leadership into a Value-Driven Organization',
                'summary': 'Test leadership supports quality at organizational, product and operational levels and evolves from command-and-control management.',
                'points': [
                    'Coordinate direction across teams without removing their ownership of day-to-day quality.',
                    'Link product-level testing to customer value and operational testing to reliability in use.',
                    'Move from assigning and inspecting test tasks toward coaching, removing obstacles and enabling collaboration.',
                ],
                'example': 'A test leader aligns teams on shared accessibility goals, coaches product teams on their own checks, and helps operations feed real user issues into improvement work.',
            },
        ],
        'key_terms': [
            ('Organizational test strategy', 'Shared guidance for how testing supports organizational goals.'),
            ('Continuous integration', 'Frequently combining code changes and checking them automatically.'),
            ('Test leadership', 'Enabling people and teams to make effective quality decisions.'),
            ('Operational level', 'The view of quality while a product is running for its users.'),
        ],
        'exam_tips': [
            'A strategy must align with both business outcomes and technical needs.',
            'Agile test leadership enables teams; it does not centralize every test decision.',
        ],
    },
    {
        'number': 5,
        'title': 'Test Processes in a Value-Driven Organization',
        'minutes': 195,
        'intro': 'Testing at scale coordinates different teams and processes while keeping feedback timely and focused on value.',
        'sections': [
            {
                'title': '5.1 Test Processes',
                'summary': 'A scalable test process coordinates work across stream-aligned and specialist teams and uses flow evidence to improve it.',
                'points': [
                    'Address scaled Agile challenges such as dependencies, shared environments, varied delivery cadences and specialist skills.',
                    'Coordinate Agile and non-Agile teams through clear interfaces, agreed expectations and visible work.',
                    'Use test and flow metrics to identify bottlenecks, then structure challenging activities where they provide useful feedback.',
                    'Let stream-aligned teams handle product-specific quality and use specialized teams for scarce expertise or cross-cutting needs.',
                ],
                'example': 'A product team runs its own service checks, while a security specialist helps several teams with threat modeling; a shared release view exposes a delayed external certification test early.',
            },
        ],
        'key_terms': [
            ('Stream-aligned team', 'A team organized around a continuous flow of value for a product or service.'),
            ('Specialized team', 'A team with focused expertise supporting multiple product teams.'),
            ('Flow metric', 'A measure such as work-item age or throughput that shows how work moves.'),
            ('Test process', 'The coordinated activities used to provide testing feedback.'),
        ],
        'exam_tips': [
            'Choose team structures based on needed expertise and flow, not on a universal rule.',
            'Use metrics to expose improvement opportunities rather than to rank individuals.',
        ],
    },
]
