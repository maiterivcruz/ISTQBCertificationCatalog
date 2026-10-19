"""Plain-language study chapters for ISTQB Quality in DevOps."""

CHAPTERS = [
    {
        'number': 1,
        'title': 'Fundamentals of DevOps',
        'minutes': 140,
        'intro': 'Understand how collaboration, flow, and feedback connect development, operations, and quality.',
        'sections': [
            {
                'title': '1.1 Quality assurance within DevOps',
                'summary': 'DevOps combines people, processes, and technology so teams can deliver changes frequently and reliably. Quality is shared across the value stream rather than delegated to a final testing group.',
                'points': [
                    'The CALMS view highlights culture, automation, lean flow, measurement, and sharing.',
                    'DORA metrics help teams observe delivery performance, including lead time, deployment frequency, change failure rate, and recovery time.',
                    'The Three Ways emphasize flow, fast feedback, and continuous learning from the whole system.',
                    'A wall between development and operations slows feedback and can make teams optimize for conflicting goals.',
                ],
                'example': 'A product team adds automated deployment checks and shares incident findings with developers, so the next change can be both faster and safer.',
            },
            {
                'title': '1.2 Implementing DevOps in an organization',
                'summary': 'DevOps adoption changes responsibilities and team interactions. Organizations need appropriate structures, skills, and improvement plans rather than simply installing a pipeline tool.',
                'points': [
                    'Cross-functional teams bring development, operations, testing, and product knowledge closer together.',
                    'Site reliability engineering (SRE) applies engineering practices to service reliability and operational work.',
                    'Choose team patterns that enable collaboration; avoid creating a new handoff silo under a DevOps label.',
                    'Use feedback and organizational context to evolve the adoption approach.',
                ],
                'example': 'An online retailer forms a product team with developers, testers, and operations staff who jointly own checkout changes and production incidents.',
            },
        ],
        'key_terms': [
            ('CALMS', 'Culture, Automation, Lean, Measurement, and Sharing, a lens for DevOps adoption.'),
            ('DORA metrics', 'Measures used to understand software delivery performance and stability.'),
            ('SRE', 'Site reliability engineering: applying engineering methods to service operations and reliability.'),
            ('Three Ways', 'DevOps principles centered on flow, feedback, and continual learning.'),
        ],
        'exam_tips': [
            'Connect DevOps quality to shared ownership and fast feedback, not to testing at the end of delivery.',
            'Know what each DORA metric indicates and distinguish delivery speed from stability.',
        ],
    },
    {
        'number': 2,
        'title': 'Quality Assurance and Testing in DevOps',
        'minutes': 360,
        'intro': 'See how quality engineering contributes from discovery through integration, delivery, and release.',
        'sections': [
            {
                'title': '2.1 Contribution to the value stream',
                'summary': 'Quality engineering helps a team learn whether a change provides value and meets its quality needs. Testing objectives and timing vary with the development lifecycle.',
                'points': [
                    'Plan test activities to support the team’s risks, feedback needs, and release model.',
                    'Continuous testing provides timely evidence across the value stream; it is not simply running every test continuously.',
                    'Pull requests create an opportunity for review and focused checks before changes are integrated.',
                ],
                'example': 'A team runs fast unit and API checks on each pull request, then uses broader exploratory testing for a risky change to its payment flow.',
            },
            {
                'title': '2.2 DevOps loop implementation',
                'summary': 'A DevOps loop links discovery and planning with integration, delivery, deployment, and learning from released software. Quality checks should provide useful feedback at each stage.',
                'points': [
                    'In continuous discovery, test ideas and user feedback help refine what should be built.',
                    'Continuous integration checks small changes early; delivery prepares releasable software, while deployment automates putting changes into use.',
                    'Release on demand separates the decision to expose a feature from the act of deploying its code.',
                    'A CI/CD pipeline automates repeatable activities but still needs monitored quality gates and recovery plans.',
                ],
                'example': 'A feature is deployed behind a toggle after automated checks, then enabled for a small customer group while the team watches service behavior.',
            },
        ],
        'key_terms': [
            ('Value stream', 'The end-to-end activities that turn an idea into value delivered to a customer.'),
            ('Continuous testing', 'Providing testing feedback throughout delivery rather than waiting for a separate final phase.'),
            ('Continuous integration', 'Frequently integrating changes and checking them in a shared codebase.'),
            ('Pull request', 'A proposed code change reviewed and checked before it is merged.'),
            ('Release on demand', 'Making a completed change available when the business chooses to release it.'),
        ],
        'exam_tips': [
            'Distinguish continuous delivery, continuous deployment, and release on demand; they describe related but different decisions.',
            'When asked where testing fits, map the activity to discovery, integration, delivery, deployment, or feedback.',
        ],
    },
    {
        'number': 3,
        'title': 'Automated and Manual Tasks in DevOps',
        'minutes': 510,
        'intro': 'Combine reliable automation with human investigation so teams get both repeatability and insight.',
        'sections': [
            {
                'title': '3.1 Automation supporting quality assurance',
                'summary': 'Automation can keep testware, data, environments, and quality evidence consistent and accessible across a fast-moving delivery pipeline.',
                'points': [
                    'A single source of truth and traceability connect requirements, testware, changes, and results.',
                    'Automated reporting should present relevant pipeline quality evidence, not just a pass count.',
                    'Manage test data and environments in a controlled, repeatable way that supports safe reuse.',
                    'Statistical analysis can reveal trends and outliers that a single run does not show.',
                ],
                'example': 'A pipeline report links a failed payment test to the changed requirement, test data set, code revision, and environment used.',
            },
            {
                'title': '3.2 Automated testing in DevOps teams',
                'summary': 'Automated tests provide rapid, repeatable checks, especially for regression risk and service interfaces. Their design should fit the architecture and the team’s delivery model.',
                'points': [
                    'Run a focused regression suite in the CI/CD pipeline and reserve longer suites for suitable stages.',
                    'API tests check contracts and behavior at service boundaries without requiring every scenario to use the user interface.',
                    'Choose automation boundaries that provide useful feedback while keeping maintenance manageable.',
                    'Automation practices differ across lifecycle models, but testability and early feedback are valuable in each.',
                ],
                'example': 'A travel service checks the fare API after each change, then runs a smaller end-to-end booking suite before a release candidate is approved.',
            },
            {
                'title': '3.3 Manual testing in DevOps teams',
                'summary': 'People remain essential for questions that need judgment, exploration, or experience beyond scripted checks. Manual activity can fit into a rapid pipeline without becoming a release bottleneck.',
                'points': [
                    'Exploratory testing uses learning, test design, and execution together to investigate an area.',
                    'Crowd testing can expose a product to diverse devices, locations, and user perspectives.',
                    'Quality-hunting events invite a team to search collaboratively for risks and defects.',
                    'Use human testing to complement automation, not to repeat the same checks without purpose.',
                ],
                'example': 'Before a map app release, testers explore interrupted navigation on unfamiliar devices while automated checks cover routine route calculations.',
            },
        ],
        'key_terms': [
            ('Testware', 'Artifacts used or produced by testing, such as tests, data, and results.'),
            ('Traceability', 'Links between test basis, testware, changes, and outcomes.'),
            ('Regression testing', 'Testing to detect unintended effects of a change on existing behavior.'),
            ('Exploratory testing', 'An approach where learning, test design, and execution are interleaved.'),
            ('Quality hunting', 'A collaborative activity in which participants actively search for quality risks.'),
        ],
        'exam_tips': [
            'Automation is best for repeatable feedback; exploratory and crowd testing add human insight and environmental variety.',
            'Relate test automation to API boundaries, pipeline timing, traceability, and maintainability.',
            'Quality reporting should support decisions by providing context, not merely a green or red status.',
        ],
    },
    {
        'number': 4,
        'title': 'Tools and Practices in DevOps',
        'minutes': 200,
        'intro': 'Select tools and technical practices that enable reliable flow, visibility, and controlled change.',
        'sections': [
            {
                'title': '4.1 Tools supporting DevOps',
                'summary': 'DevOps tools support collaboration, automation, integration, deployment, observability, and testing. Tool choice should follow the work and connect with the team’s existing practices.',
                'points': [
                    'Assess capabilities and integration rather than choosing tools by popularity alone.',
                    'Testing and QA tools can support management of testware, execution, reporting, and feedback.',
                    'Consider usability, maintainability, security, and the skills needed to operate a tool.',
                ],
                'example': 'A small team selects a CI service that integrates with its repository and test framework, instead of maintaining a separate tool that duplicates pipeline data.',
            },
            {
                'title': '4.2 Technologies and practices for quality',
                'summary': 'Technical practices make system changes safer and production behavior more visible. Teams combine deployment controls, infrastructure automation, observability, and resilience work.',
                'points': [
                    'Infrastructure as code (IaC) versions environment definitions and makes provisioning repeatable.',
                    'Feature toggles and release strategies control exposure; branching choices affect integration flow.',
                    'Chaos engineering tests resilience through controlled experiments, while telemetry supports observability.',
                    'Containers package software consistently; a software bill of materials (SBOM) records included components.',
                ],
                'example': 'A service is deployed to a small canary group with telemetry watched, while a feature toggle allows the team to disable the new checkout path quickly.',
            },
        ],
        'key_terms': [
            ('Infrastructure as code', 'Managing infrastructure definitions as versioned, reviewable code.'),
            ('Feature toggle', 'A control that enables or disables a feature independently of deployment.'),
            ('Chaos engineering', 'Controlled experiments that test how a system behaves under disruption.'),
            ('Observability', 'Using system outputs such as logs, metrics, and traces to understand internal behavior.'),
            ('SBOM', 'A software bill of materials listing components included in a software product.'),
        ],
        'exam_tips': [
            'Distinguish deployment from feature release: toggles and canary strategies can limit exposure after deployment.',
            'Choose tools and practices based on the quality problem they address and the feedback they provide.',
        ],
    },
]
