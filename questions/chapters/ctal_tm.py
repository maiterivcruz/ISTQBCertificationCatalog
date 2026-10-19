"""Plain-language study notes for the CTAL-TM syllabus."""

CHAPTERS = [
    {
        'number': 1,
        'title': 'Managing the Test Activities',
        'minutes': 750,
        'intro': 'Test management coordinates people, activities and evidence so testing responds to the project context and product risk.',
        'sections': [
            {'title': '1.1 The Test Process', 'summary': 'Management plans test work, monitors progress, controls deviations and completes the work responsibly.', 'points': ['Planning defines objectives, scope, approach, resources, schedule and entry or exit conditions.', 'Monitoring compares progress and risks with the plan; control adjusts priorities or resources.', 'Completion records results, archives useful testware and captures lessons for later work.'], 'example': 'When a release is behind schedule, the test manager compares risk coverage with the plan, shifts effort to critical payment checks, and records deferred tests for stakeholders.'},
            {'title': '1.2 The Context of Testing', 'summary': 'Test management depends on stakeholder needs, lifecycle choices, test level, test type and the way development is organized.', 'points': ['Identify who needs testing information and what decisions they make.', 'Adapt management activities to sequential, iterative, Agile or hybrid delivery.', 'Coordinate test levels and types so coverage is appropriate without unnecessary duplication.'], 'example': 'A hybrid project uses frequent Agile team testing while retaining formal release evidence for a safety review board.'},
            {'title': '1.3 Risk-Based Testing', 'summary': 'Risk-based testing prioritizes effort according to product risks and responds as project knowledge changes.', 'points': ['Identify and assess product quality risks using stakeholder and technical input.', 'Select test activities and depth proportionate to risk level.', 'Monitor risk changes and communicate residual risk and mitigation choices.'], 'example': 'A medical portal gives extra testing to patient identity and prescription renewal because errors there could cause serious harm.'},
        ],
        'key_terms': [('Test planning', 'Defining objectives and how testing will be carried out.'), ('Test monitoring', 'Reviewing test progress and risk against objectives.'), ('Test control', 'Adjusting activities in response to monitoring.'), ('Product risk', 'A possible product problem and its potential consequences.'), ('Hybrid development', 'A lifecycle combining practices from more than one development approach.')],
        'exam_tips': ['Separate planning, monitoring, control and completion activities.', 'Adapt the process to lifecycle and stakeholder needs rather than assuming one template fits all.', 'Prioritize actions by product risk and explain what residual risk remains.'],
    },
    {
        'number': 2,
        'title': 'Managing the Product',
        'minutes': 390,
        'intro': 'Product management in testing uses measures, estimates and defect information to help teams and stakeholders make sound decisions.',
        'sections': [
            {'title': '2.1 Test Metrics', 'summary': 'Metrics provide evidence about progress and objectives when interpreted with context.', 'points': ['Select measures that answer a specific management or stakeholder question.', 'Use multiple indicators where one measure could give a misleading view.', 'Analyze results and trends before deciding what action they support.'], 'example': 'A manager reviews passed critical-risk tests alongside open severe defects and blocked environments instead of reporting only a pass percentage.'},
            {'title': '2.2 Test Estimation', 'summary': 'Estimates forecast testing effort or duration based on scope, context, available information and uncertainty.', 'points': ['Consider product complexity, team skills, environments, data and dependencies.', 'Use historical data, expert judgment or another suitable estimation approach.', 'State assumptions and revise estimates when evidence changes.'], 'example': 'A team estimates a new payment integration using effort from a similar service, then adjusts for unfamiliar authentication and certification work.'},
            {'title': '2.3 Defect Management', 'summary': 'A defect process helps teams record, evaluate, prioritize, resolve and learn from product defects.', 'points': ['Define an agreed workflow, roles and information needed in a useful report.', 'Adapt triage and communication for Agile or hybrid work while preserving visibility.', 'Analyze classifications and statistics to identify improvement opportunities.'], 'example': 'A defect report for a failed refund includes steps, expected and actual amounts, account data, environment and severity so the team can reproduce it.'},
        ],
        'key_terms': [('Test metric', 'A measured value used to assess or manage testing.'), ('Test estimate', 'A forecast of effort, duration or resources needed for test work.'), ('Defect workflow', 'The agreed states and transitions used to manage defects.'), ('Defect report', 'A record describing a defect and the evidence needed to act on it.')],
        'exam_tips': ['Choose metrics that support a decision and state their limitations.', 'For estimates, identify context and assumptions before selecting a method.', 'A defect workflow should fit the team while preserving clear ownership and useful data.'],
    },
    {
        'number': 3,
        'title': 'Managing the Team',
        'minutes': 225,
        'intro': 'A test manager develops the team and works with stakeholders to make testing valuable and understood.',
        'sections': [
            {'title': '3.1 The Test Team', 'summary': 'Effective teams need an appropriate mix of skills and a plan to build and sustain capability.', 'points': ['Assess technical, domain, testing and interpersonal skills in the project context.', 'Use mentoring, training, pairing or other development approaches to close gaps.', 'Motivation and working conditions influence performance and retention.'], 'example': 'A team lacking accessibility expertise pairs with a specialist and trains two testers to cover common checks independently.'},
            {'title': '3.2 Stakeholder Relationship and Value of Testing', 'summary': 'Good relationships connect test evidence to stakeholder concerns and show how testing contributes value.', 'points': ['Understand stakeholder expectations and communicate in a form they can use.', 'Consider cost of quality, including prevention, appraisal and the consequences of failures.', 'Use a cost-benefit view to explain the added value of a test activity.'], 'example': 'A release manager compares the cost of an extra load test with the likely business impact of a failed ticket sale during peak demand.'},
        ],
        'key_terms': [('Skill assessment', 'A structured view of a person’s capabilities and development needs.'), ('Cost of quality', 'Costs related to preventing, assessing and experiencing quality problems.'), ('Stakeholder', 'A person or group affected by or interested in the product or testing.'), ('Motivation factor', 'A condition that influences engagement and satisfaction at work.')],
        'exam_tips': ['Select team development actions based on the actual skill gap and project context.', 'In value questions, compare test cost with the risks and costs it can reduce.', 'Tailor communication to the stakeholder’s decision and information needs.'],
    },
]
