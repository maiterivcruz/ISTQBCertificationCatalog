"""Plain-language study notes for the CTAL-TAE syllabus."""

CHAPTERS = [
    {
        'number': 1,
        'title': 'Introduction and Objectives for Test Automation',
        'minutes': 45,
        'intro': 'Test automation can improve speed and repeatability when it is selected and designed around a real testing need.',
        'sections': [
            {'title': '1.1 Purpose of Test Automation', 'summary': 'Automation offers benefits, but it also brings costs and risks that should be evaluated.', 'points': ['It can repeat checks quickly, consistently and frequently.', 'Creation, infrastructure, maintenance and result analysis require ongoing effort.', 'Automation supports testing; it does not replace test design, judgment or product understanding.'], 'example': 'A team automates stable account-balance checks nightly, but keeps a tester involved to investigate whether a changed display makes sense to customers.'},
            {'title': '1.2 Test Automation in the Software Development Lifecycle', 'summary': 'Automation can contribute at different lifecycle stages and test levels, using tools suited to the system and team.', 'points': ['Place checks where they provide useful feedback, from component tests to system-level flows.', 'Consider the SUT technology, interfaces, team skills and operating environment when choosing tools.', 'Build automation into delivery practices so results arrive early enough to act on.'], 'example': 'A service team runs component checks on each commit, API checks during integration, and a small browser journey after deployment.'},
        ],
        'key_terms': [('Test automation', 'Using software to perform or support test activities.'), ('SUT', 'The system under test.'), ('Test level', 'A group of test activities organized around a development stage or test object.')],
        'exam_tips': ['Balance automation benefits against setup, upkeep and result-analysis costs.', 'Choose tools based on the SUT and context rather than popularity alone.'],
    },
    {
        'number': 2,
        'title': 'Preparing for Test Automation',
        'minutes': 180,
        'intro': 'Preparation establishes the infrastructure, evaluation criteria and evidence needed for a suitable automation solution.',
        'sections': [
            {'title': '2.1 Infrastructure for Test Automation', 'summary': 'Automation depends on a reliable, repeatable environment that supports the SUT and its tests.', 'points': ['Identify hardware, software, network, access, data and environment requirements.', 'Account for differences among development, test, staging and production-like environments.', 'Plan configuration and recovery so failures can be reproduced and diagnosed.'], 'example': 'A mobile test lab defines supported device models, operating-system versions, network profiles and reset steps before the pilot begins.'},
            {'title': '2.2 Evaluation Process for Selecting Tools and Strategies', 'summary': 'A structured evaluation checks whether a proposed approach meets technical and business needs.', 'points': ['Start from requirements, constraints and selection criteria that stakeholders agree on.', 'Assess how candidate tools integrate with the SUT, delivery pipeline and team skills.', 'Use a representative proof of concept and communicate findings, assumptions and limitations.'], 'example': 'A team compares two API automation tools by implementing the same authentication and data-setup scenario against a representative service.'},
        ],
        'key_terms': [('Test automation infrastructure', 'The environments and supporting components needed to run automation.'), ('Proof of concept', 'A small practical exercise used to evaluate feasibility.'), ('Selection criteria', 'Agreed measures for comparing candidate tools or solutions.'), ('Environment', 'The hardware, software and configuration in which the SUT runs.')],
        'exam_tips': ['For an infrastructure scenario, include dependencies, data, access and environment repeatability.', 'Use realistic evaluation evidence and distinguish measured findings from assumptions.'],
    },
    {
        'number': 3,
        'title': 'Test Automation Architecture',
        'minutes': 210,
        'intro': 'A maintainable architecture separates responsibilities and provides dependable ways to interact with the test object.',
        'sections': [
            {'title': '3.1 Design Concepts for Test Automation', 'summary': 'Architecture defines the main capabilities and relationships needed by an automation solution.', 'points': ['Identify how tests are specified, executed, controlled and reported.', 'Separate test logic from lower-level interaction details where practical.', 'Design for reliable outcomes, clear diagnostics, reuse and change.'], 'example': 'A web test framework keeps customer journeys separate from browser-driver code so a browser upgrade does not rewrite every test.'},
            {'title': '3.2 Layering and Test Case Automation Approaches', 'summary': 'Layers and automation styles help organize reusable actions and choose the right amount of detail.', 'points': ['A layered framework can separate test cases, business actions and technical adapters.', 'Select approaches such as model-based, data-driven or keyword-driven automation to fit the test basis and maintainers.', 'Avoid abstractions that hide behavior or make failures difficult to understand.'], 'example': 'A booking suite stores fare variations as data while shared booking actions handle the repeated search and payment steps.'},
            {'title': '3.3 Design Principles and Patterns', 'summary': 'Sound design principles limit coupling and make automation easier to extend and diagnose.', 'points': ['Use clear interfaces, focused components and controlled dependencies.', 'Apply patterns only when they solve a recurring design problem.', 'Keep test intent visible so reused code does not obscure what is being checked.'], 'example': 'A team wraps a frequently changing API behind one adapter, allowing endpoint changes without editing every test scenario.'},
        ],
        'key_terms': [('Test automation architecture', 'The structure and capabilities of an automation solution.'), ('Layer', 'A part of a design that has a defined responsibility.'), ('Data-driven testing', 'Running a test flow with varied input data kept separate from its logic.'), ('Keyword-driven testing', 'Building test procedures from reusable named actions.'), ('Coupling', 'The degree to which one component depends on another.')],
        'exam_tips': ['Explain how layers separate responsibilities and how that supports change.', 'Select an automation approach that fits team skills, test data and expected maintenance.', 'Prefer visible test intent over unnecessary abstraction.'],
    },
    {
        'number': 4,
        'title': 'Implementing Test Automation',
        'minutes': 150,
        'intro': 'Implementation turns the design into working automation while controlling deployment risk and future maintenance effort.',
        'sections': [
            {'title': '4.1 Test Automation Development', 'summary': 'A focused pilot and disciplined development practices help build a solution that can be adopted safely.', 'points': ['Choose a representative pilot with achievable goals and clear success measures.', 'Integrate automation development with reviews, version control and team practices.', 'Expand only after learning from pilot results and operational constraints.'], 'example': 'A team pilots automation for one stable account workflow, measures maintenance time, then decides which other journeys are suitable.'},
            {'title': '4.2 Risks in Test Automation Development', 'summary': 'Automation projects can fail when risks around technology, skills, testability and expectations go unmanaged.', 'points': ['Identify technical dependencies and organizational barriers early.', 'Mitigate brittle tests, unstable environments and unrealistic coverage promises.', 'Make ownership and support responsibilities explicit.'], 'example': 'Before automating a frequently redesigned screen, the team agrees on stable test identifiers with developers to reduce brittle selectors.'},
            {'title': '4.3 Test Automation Solution Maintainability', 'summary': 'Maintainability depends on design, documentation, skills and how rapidly the SUT changes.', 'points': ['Keep components modular and failures understandable.', 'Track changes in the SUT, tools, libraries and test data that affect automation.', 'Plan regular maintenance rather than treating it as optional cleanup.'], 'example': 'After a pricing redesign, the team updates one shared page object and the related business rule tests instead of patching copied scripts individually.'},
        ],
        'key_terms': [('Pilot', 'A limited implementation used to validate an approach.'), ('Maintainability', 'How readily a solution can be understood, corrected and adapted.'), ('Testability', 'How easily a system can be tested.'), ('Automation risk', 'A condition that could prevent an automation effort from meeting its goals.')],
        'exam_tips': ['Use a pilot to test feasibility and value, not just to demonstrate a tool.', 'Connect each automation risk with a practical mitigation.', 'Include ongoing maintenance and ownership in the solution plan.'],
    },
    {
        'number': 5,
        'title': 'Implementation and Deployment Strategies for Test Automation',
        'minutes': 90,
        'intro': 'Automation becomes more valuable when it fits delivery pipelines and its dependencies are managed consistently.',
        'sections': [
            {'title': '5.1 Integration with CI/CD Pipelines', 'summary': 'Pipelines can run automated checks at appropriate stages and give teams feedback as changes move toward delivery.', 'points': ['Place checks at test levels that balance speed, scope and available environments.', 'Keep testware and configuration under version control.', 'Make API, service and infrastructure dependencies explicit and controllable.'], 'example': 'A pipeline runs fast component checks on every change, then deploys to a test environment for API checks requiring shared test services.'},
        ],
        'key_terms': [('CI/CD pipeline', 'An automated workflow that integrates, tests and delivers software changes.'), ('Testware configuration management', 'Control of test assets and their versions and settings.'), ('API dependency', 'A service or interface required by an automated check.')],
        'exam_tips': ['Match pipeline stage to test speed, scope and dependency needs.', 'Treat scripts, data and configuration as versioned testware.'],
    },
    {
        'number': 6,
        'title': 'Test Automation Reporting and Metrics',
        'minutes': 150,
        'intro': 'Automation generates data about tests and the SUT. Useful reporting turns that data into information for action.',
        'sections': [
            {'title': '6.1 Collecting and Analyzing Automation Data', 'summary': 'Collect data from both the automation solution and the product, then interpret it in context.', 'points': ['Capture useful results such as execution status, duration, failures and environment details.', 'Correlate test outcomes with SUT behavior and changes where possible.', 'Investigate trends and anomalies before drawing conclusions from counts.'], 'example': 'A rise in failed tests is correlated with a new service deployment, helping the team distinguish a product regression from a test-environment outage.'},
            {'title': '6.2 Test Progress Reporting', 'summary': 'A progress report communicates automation status and limitations to its intended audience.', 'points': ['State objectives, scope and reporting period.', 'Summarize meaningful results, blockers, trends and remaining risk.', 'Use a format and delivery path that helps stakeholders make timely decisions.'], 'example': 'A release report summarizes critical journey results, flaky checks and untested payment providers for the release manager.'},
        ],
        'key_terms': [('Metric', 'A measured value used to monitor or understand an activity.'), ('Test progress report', 'A communication of test status and relevant results.'), ('Flaky test', 'A test whose outcome varies without a meaningful product change.'), ('Trend', 'A pattern in observations over time.')],
        'exam_tips': ['Distinguish raw data from an interpreted measure and an actionable report.', 'Include scope and limitations so stakeholders do not overinterpret results.'],
    },
    {
        'number': 7,
        'title': 'Verifying the Test Automation Solution',
        'minutes': 135,
        'intro': 'Automation itself must be checked: a passing test is useful only when its environment, logic and results can be trusted.',
        'sections': [
            {'title': '7.1 Verification of the Test Automation Infrastructure', 'summary': 'Verification checks that the infrastructure and tools are configured correctly and support reliable execution.', 'points': ['Plan checks for installation, configuration, connectivity, data and environment readiness.', 'Confirm that test scripts and suites behave as intended.', 'Investigate unexpected outcomes to distinguish product, test and infrastructure causes.'], 'example': 'A known-good sample test is run after a browser image update to verify that the driver, network and reporting services still work.'},
            {'title': '7.2 Static Analysis and Automation Code Quality', 'summary': 'Static analysis examines automation code without executing it and can reveal maintainability or reliability problems.', 'points': ['Use suitable analysis rules to find defects such as unsafe constructs or inconsistent style.', 'Review findings in context and address issues that affect the solution.', 'Combine static checks with execution and review rather than treating one check as complete verification.'], 'example': 'A code analyzer flags duplicated waits and an unused exception handler in test scripts before the next pipeline run.'},
        ],
        'key_terms': [('Verification', 'Checking that a work product meets specified requirements.'), ('Infrastructure verification', 'Checking the setup that supports test automation.'), ('Static analysis', 'Examining code without running it.'), ('Unexpected result', 'An outcome that does not match the expected behavior of the test or SUT.')],
        'exam_tips': ['Consider the SUT, test logic, data and environment when diagnosing a surprising result.', 'Explain how static analysis complements, rather than replaces, execution-based checks.'],
    },
    {
        'number': 8,
        'title': 'Continuous Improvement',
        'minutes': 210,
        'intro': 'Automation should evolve with evidence and product change. Regular analysis helps keep tests useful and the solution sustainable.',
        'sections': [
            {'title': '8.1 Improvement Opportunities for Test Automation', 'summary': 'Data and experience can expose weak, redundant or poorly targeted automated checks.', 'points': ['Use test results and product changes to identify opportunities to improve test cases.', 'Review technical design, execution reliability and maintenance effort together.', 'Restructure testware when the SUT changes so it remains aligned with current behavior.'], 'example': 'Repeated false failures from a redesigned account page prompt the team to revise shared selectors and remove checks for retired fields.'},
            {'title': '8.2 Broadening Tool Support', 'summary': 'Additional tools may help with other testing needs when their value and costs are understood.', 'points': ['Identify a concrete gap before adding a tool.', 'Check integration, skills, licensing and ongoing support needs.', 'Measure whether the tool improves the desired outcome after adoption.'], 'example': 'A team evaluates a mobile-device cloud because local devices do not cover the operating-system combinations required by its users.'},
        ],
        'key_terms': [('Continuous improvement', 'Ongoing evidence-based changes to improve a process or solution.'), ('Testware restructuring', 'Reorganizing test assets to fit a changed test object or design.'), ('False failure', 'A reported test failure that is not caused by a product defect.'), ('Tool support', 'Use of tools to assist testing activities.')],
        'exam_tips': ['Use results and maintenance evidence to identify a specific improvement opportunity.', 'When updating testware, align it with changed SUT behavior instead of preserving obsolete assumptions.', 'Assess new tools by the problem they solve and their lifecycle cost.'],
    },
]
