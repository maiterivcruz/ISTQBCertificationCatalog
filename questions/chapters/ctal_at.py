"""Plain-language study notes for the CTAL-AT syllabus."""

CHAPTERS = [
    {
        'number': 1,
        'title': 'Test Strategy and Test Approach Challenges',
        'minutes': 60,
        'intro': 'Agile testing changes shape as work moves through iterations and into release. This chapter helps choose sensible test types and regression checks.',
        'sections': [
            {'title': '1.1 Test Types', 'summary': 'Different test types answer different quality questions, and Agile teams spread them across the delivery cycle.', 'points': ['Use functional tests to check behavior and non-functional tests to examine qualities such as performance.', 'Run suitable tests during an iteration and repeat relevant checks after integration or release.', 'Choose timing based on risk, feedback needs and the cost of finding a problem late.'], 'example': 'A grocery team checks price calculations during development, then runs security and accessibility checks before a major release.'},
            {'title': '1.2 End-to-End Testing', 'summary': 'End-to-end tests follow a user journey through connected parts of a product. They are valuable for integration confidence but are slower and harder to diagnose.', 'points': ['Prioritize critical journeys that cross important system boundaries.', 'Use lower-level tests for fast, precise feedback and reserve end-to-end checks for behavior that needs the full flow.', 'Run end-to-end tests when the required components and environments are available.'], 'example': 'A travel site verifies search, seat selection, payment, and confirmation together in one booking journey.'},
            {'title': '1.3 Formal Testing and Holistic Testing', 'summary': 'Formal testing follows planned cases and recorded results; holistic testing explores the product as a whole, often with less scripted guidance.', 'points': ['Formal tests support repeatability, traceability and evidence against defined expectations.', 'Holistic testing can expose interactions and unexpected behavior that isolated checks miss.', 'Balance the approaches according to assurance needs, time, and how well requirements are understood.'], 'example': 'A payments team retains scripted authorization checks for audit evidence and holds an exploratory session to discover unusual interactions between refunds and account limits.'},
            {'title': '1.4 Regression Test Approaches', 'summary': 'Regression testing checks whether a change has harmed existing behavior. Teams can choose different scopes rather than rerun everything every time.', 'points': ['Select checks using change impact, product risk and the confidence required.', 'A broad regression suite gives wider assurance but costs more time and maintenance.', 'Keep critical regression checks reliable and update them as features and risks change.'], 'example': 'After changing tax calculations, a shop reruns checkout, returns, and invoice tests instead of the entire unrelated catalog suite.'},
        ],
        'key_terms': [('Regression testing', 'Checking that a change has not damaged existing behavior.'), ('End-to-end test', 'A test of a complete user or business flow across connected components.'), ('Holistic testing', 'Testing the product as a connected whole, often through exploration.'), ('Formal testing', 'Testing performed with planned, documented procedures and results.')],
        'exam_tips': ['Compare approaches by their purpose, feedback speed, cost, and coverage.', 'For a scenario, select test timing and regression scope based on risk and change impact.'],
    },
    {
        'number': 2,
        'title': 'People and Teams',
        'minutes': 60,
        'intro': 'Agile quality is a team responsibility. Testers contribute specialist knowledge while helping the whole team take part in testing.',
        'sections': [
            {'title': '2.1 Whole Team Approach', 'summary': 'The whole-team approach brings different skills together to prevent and find defects throughout delivery.', 'points': ['A specialist tester offers depth; a generalizing team member can contribute across activities.', 'Business representatives help clarify expected behavior and evaluate examples.', 'Shared responsibility does not remove the need for testing expertise or clear accountability.'], 'example': 'In a clinic app team, a nurse clarifies medication workflows, a developer adds checks, and the tester examines risky edge cases.'},
            {'title': '2.2 Tissue Testers', 'summary': 'Tissue testers are temporary people from outside the team who give quick, fresh-eyes feedback on an early design or feature.', 'points': ['Use them for exploratory feedback, usability observations or checking assumptions before formal validation is ready.', 'Give minimal explanation so prior knowledge does not bias their reaction.', 'Their value fades after they have seen the product, so use a different person for a later fresh-eyes session.'], 'example': 'Before finalizing a game menu, a designer asks a colleague from another team to try it without coaching and note confusing navigation.'},
        ],
        'key_terms': [('Whole-team approach', 'A way of working where all relevant team members contribute to quality.'), ('Generalizing specialist', 'A person with deep expertise who can also contribute beyond one specialty.'), ('Business representative', 'A stakeholder who explains business needs and expected outcomes.'), ('Tissue tester', 'A temporary outside tester who gives a fresh perspective on an early product idea.')],
        'exam_tips': ['Distinguish shared quality responsibility from replacing specialist testing.', 'In team scenarios, identify how business knowledge can improve examples and feedback.'],
    },
    {
        'number': 3,
        'title': 'Test Management and Test Process Improvement',
        'minutes': 210,
        'intro': 'Agile test management plans work, checks progress, communicates results, and improves the process using evidence.',
        'sections': [
            {'title': '3.1 Test Planning', 'summary': 'Planning aligns test work with iteration goals, product risks, and the wider test strategy.', 'points': ['Agree scope, responsibilities, environments, dependencies and completion conditions.', 'Testing quadrants help select a balanced set of business-facing and technology-facing tests.', 'Refine plans as the team learns; Agile plans are useful guides, not fixed scripts.'], 'example': 'For a new mobile wallet, the team plans fast unit and API checks alongside user-facing acceptance and exploratory sessions.'},
            {'title': '3.2 Test Monitoring and Test Control', 'summary': 'Monitoring compares actual progress with goals; control changes the work when evidence shows a gap.', 'points': ['Track meaningful measures such as test status, risk coverage and unresolved defects.', 'Use trends and context rather than treating one number as a complete quality verdict.', 'Reprioritize or adjust capacity when critical risks are not being addressed.'], 'example': 'When payment tests are blocked by an unstable environment, the lead moves testers to API checks and asks operations to restore the test service.'},
            {'title': '3.3 Test Reporting', 'summary': 'Reports give stakeholders a clear view of testing, product risk, and decisions that need attention.', 'points': ['Report status in relation to agreed objectives and coverage.', 'Explain important limitations, open defects and remaining risk.', 'Choose detail and format to suit the audience and the decision at hand.'], 'example': 'A release update shows which checkout risks were tested, which defects remain, and what the product owner must accept before launch.'},
            {'title': '3.4 Test Process Improvement', 'summary': 'Teams use observed outcomes to improve how they test and deliver, then check whether the changes help.', 'points': ['Use team metrics and retrospective evidence to locate a process problem.', 'Choose improvement actions that address causes rather than merely adding activity.', 'Reassess outcomes after implementation and adapt if the expected benefit does not appear.'], 'example': 'Repeated late test-data failures prompt the team to automate data setup, then compare blocked-test time over subsequent iterations.'},
        ],
        'key_terms': [('Testing quadrant', 'A model for grouping tests by purpose and business or technology focus.'), ('Test monitoring', 'Measuring and reviewing progress against test objectives.'), ('Test control', 'Taking action to keep testing aligned with objectives.'), ('Test process improvement', 'Changing the way work is done to achieve better testing outcomes.')],
        'exam_tips': ['Use test quadrants to reason about a balanced Agile test strategy.', 'Separate monitoring (observe) from control (act), and connect reports to stakeholder decisions.', 'Choose improvement actions that are measurable and address the demonstrated cause.'],
    },
    {
        'number': 4,
        'title': 'Shift Left',
        'minutes': 135,
        'intro': 'Shift left means bringing quality activities earlier so unclear or faulty work is found before it becomes expensive to change.',
        'sections': [
            {'title': '4.1 Using Shift Left to Improve Test Basis Quality', 'summary': 'Testers can help improve requirements and other test bases before implementation begins.', 'points': ['Use examples and test ideas to reveal ambiguity, missing cases and conflicting expectations.', 'Storyboarding and testboarding make journeys and test coverage visible to the team.', 'Example mapping organizes rules, examples and unanswered questions around a story.'], 'example': 'A booking team maps rules for child fares and discovers before coding that the age limit and proof requirements are unspecified.'},
            {'title': '4.2 Shift Left and Requirements Engineering', 'summary': 'Good requirements work gives development and testing a clearer, more testable basis.', 'points': ['Collaborate on requirements while they are being explored, not only after they are approved.', 'Slice large stories into smaller increments with observable outcomes.', 'Notice assumptions and bias that can make a requirement exclude real users or miss important needs.'], 'example': 'A team splits “manage profile” into separate, testable changes for updating contact details, changing a password, and closing an account.'},
        ],
        'key_terms': [('Shift left', 'Moving quality activities earlier in the delivery process.'), ('Test basis', 'Information used to derive tests, such as requirements or designs.'), ('Example mapping', 'A collaborative way to clarify a story using rules, examples and questions.'), ('User story slicing', 'Breaking a large story into smaller valuable increments.')],
        'exam_tips': ['Look for early collaboration and feedback as signs of shift-left behavior.', 'Select the technique that best reveals missing rules, journey gaps, or oversized stories.'],
    },
    {
        'number': 5,
        'title': 'Agile Approaches and Test Techniques',
        'minutes': 285,
        'intro': 'This chapter connects exploratory and collaborative testing practices with practical ways to assess test quality.',
        'sections': [
            {'title': '5.1 Exploratory Testing', 'summary': 'Exploratory testing combines learning, test design and execution as the tester investigates the product.', 'points': ['Use heuristics, mnemonics and tours to guide attention without limiting discovery.', 'A charter sets a focused mission; observations during the session can refine the next tests.', 'Record useful evidence and findings so the team can act on them.'], 'example': 'A tester explores a ticket exchange using a “data tour,” trying unusual names, dates and quantities while noting where validation differs.'},
            {'title': '5.2 Assisted Testing', 'summary': 'Pair, mob and other collaborative testing styles let people with different knowledge investigate together.', 'points': ['Pair testing puts two people on one testing activity, often sharing driver and observer roles.', 'Mob testing brings several participants to one shared test task.', 'Select participants and session goals deliberately so collaboration adds useful perspectives.'], 'example': 'A tester and product owner pair on a new refund flow, with the product owner explaining policy and the tester probing boundary cases.'},
            {'title': '5.3 Test Smells', 'summary': 'A test smell is a warning sign that a test may be hard to trust, understand or maintain.', 'points': ['Look for brittle checks, unclear intent, excessive duplication, and tests dependent on unrelated behavior.', 'Treat a smell as a prompt to investigate rather than proof that the test is defective.', 'Improve test design so failures communicate a clear product problem.'], 'example': 'A single checkout test fails whenever any of six unrelated services is unavailable, so the team separates focused checks and clarifies dependencies.'},
        ],
        'key_terms': [('Exploratory testing', 'Testing where learning and test design evolve during execution.'), ('Test charter', 'A brief mission that guides an exploratory session.'), ('Pair testing', 'Two people collaborate on one testing activity.'), ('Test smell', 'A warning sign of a possible weakness in a test.')],
        'exam_tips': ['Tell exploratory testing apart from unstructured execution: it still has a purpose and useful records.', 'Compare pair and mob testing by group size and collaboration setup.', 'Treat test smells as indicators to evaluate, not automatic proof of a fault.'],
    },
    {
        'number': 6,
        'title': 'Test Automation and Test Tools',
        'minutes': 30,
        'intro': 'Automation can support rapid feedback in Agile delivery, but it needs a clear purpose and suitable tools.',
        'sections': [
            {'title': '6.1 Test Automation in Agile Software Development', 'summary': 'Automated checks help teams repeat important tests quickly and often.', 'points': ['Match automation to test level, risk, maintenance cost and feedback speed.', 'Keep human exploration for questions that need judgment or discovery.', 'Automation does not replace test analysis or guarantee product quality.'], 'example': 'A team runs stable payment API checks on each change while testers manually explore a new checkout design.'},
            {'title': '6.2 Test Tools in Agile Software Development', 'summary': 'Tools support testing activities when they fit the workflow and the problem to solve.', 'points': ['Consider the tool’s users, integration, learning cost and maintenance needs.', 'Use tools to improve collaboration and visibility as well as execution.', 'Evaluate a tool against real team needs before adopting it broadly.'], 'example': 'A small team pilots a test-management integration with its issue tracker to see whether it reduces duplicate status updates.'},
        ],
        'key_terms': [('Test automation', 'Using software to perform or support test activities.'), ('Test tool', 'Software that assists one or more testing activities.'), ('Regression suite', 'A set of checks repeated to detect unintended changes.')],
        'exam_tips': ['Choose automation for repeatable checks where speed and repeatability justify upkeep.', 'When comparing tools, consider practical fit and long-term maintenance, not features alone.'],
    },
]
