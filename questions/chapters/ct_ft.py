"""CT-FT study chapters: plain-language finance testing guidance."""

CHAPTERS = [
    {
        'number': 1,
        'title': 'Introduction to the Financial Services Industry',
        'minutes': 50,
        'intro': 'Financial products move valuable money and sensitive data. Testing must account for their business rules, connected systems, and regulatory setting.',
        'sections': [
            {
                'title': '1.1 Fundamentals of Software Testing in Financial Services',
                'summary': 'Finance testing checks that transactions and financial services behave correctly, securely, and consistently across their workflows.',
                'points': [
                    'Testing aims to find defects, lower business risk, and provide evidence that financial workflows meet their requirements.',
                    'Financial systems include banking, payments, trading, insurance, and supporting platforms; each has distinct data and transaction rules.',
                    'Test environments may use masked production-like data, simulators, or controlled connections to external institutions.',
                ],
                'example': 'A payment test follows a card purchase from authorization through settlement and checks that each service records the same amount and status.',
            },
            {
                'title': '1.2 Challenges and the Role of Domain Knowledge in Finance Testing',
                'summary': 'Financial rules, terminology, integrations, and regulation make domain understanding important for choosing meaningful tests.',
                'points': [
                    'Complex workflows, legacy systems, high transaction volumes, and changing rules create interacting risks.',
                    'Domain knowledge helps testers recognize invalid business outcomes, such as a transfer that breaks an account limit.',
                    'Testers work with business experts and use realistic scenarios while protecting confidential data.',
                ],
                'example': 'A tester who knows that a bank transfer can be pending overnight checks that the customer sees a pending state rather than a false final balance.',
            },
        ],
        'key_terms': [
            ('Settlement', 'The process that completes and records the transfer of funds between parties.'),
            ('Financial workflow', 'A sequence of business and system steps that handles a financial event.'),
            ('Test environment', 'The configured systems and data used to perform testing.'),
            ('Domain knowledge', 'Understanding of financial products, rules, and processes.'),
        ],
        'exam_tips': [
            'Connect each test objective to a finance-specific risk, not just a screen or function.',
            'Be ready to explain why domain knowledge changes the scenarios a tester selects.',
        ],
    },
    {
        'number': 2,
        'title': 'Compliance Testing',
        'minutes': 80,
        'intro': 'Compliance testing checks that financial software follows applicable rules and can provide trustworthy evidence of how it behaved.',
        'sections': [
            {
                'title': '2.1 Compliance Testing Objectives and Approaches',
                'summary': 'A compliance test compares system behavior and records with obligations that apply to a product, institution, or jurisdiction.',
                'points': [
                    'Identify applicable obligations, translate them into verifiable conditions, and retain evidence of the results.',
                    'Use traceable test cases, controlled environments, and repeatable execution so results can be reviewed later.',
                    'Compliance testing complements functional testing; a feature can work technically but still violate a rule.',
                ],
                'example': 'For a customer onboarding rule, a team tests required identity checks and keeps timestamped evidence showing which checks passed.',
            },
            {
                'title': '2.2 Financial Regulations and Their Impact on Testing',
                'summary': 'Regulations and standards shape what a system must protect, record, report, and prove.',
                'points': [
                    'Determine which rules apply to the product, data, payment method, and operating region before designing tests.',
                    'Turn obligations into observable checks for controls such as identity verification, privacy, transaction monitoring, and audit records.',
                    'Non-compliance can lead to financial penalties, restricted operations, remediation costs, and loss of trust.',
                ],
                'example': 'A cross-border payment test verifies that the screening control flags a prohibited recipient and records why the transfer was held.',
            },
            {
                'title': '2.3 Distinctive Characteristics of Regulated Finance Testing',
                'summary': 'Regulated work requires stronger control of test evidence, data, approvals, and repeatability than many ordinary feature checks.',
                'points': [
                    'Keep test data protected and record who changed or approved test assets and results.',
                    'Maintain traceability from a rule to requirements, tests, outcomes, and any corrective action.',
                    'Plan for independent review and for changes to rules, platforms, and evidence retention needs.',
                ],
                'example': 'Before an audit, a team can trace a reporting requirement to its test cases, execution logs, and the approved release that included the control.',
            },
            {
                'title': '2.4 Auditability and Continuous Automated Compliance Testing',
                'summary': 'Auditability makes control operation and testing reconstructable; continuous automation can check selected controls repeatedly.',
                'points': [
                    'Audit trails should be attributable, time-ordered, protected from unapproved changes, and linked to the relevant transaction or decision.',
                    'Automated checks can monitor rule-based controls more frequently, but their configuration and outputs also need governance.',
                    'Human review remains important for exceptions, ambiguous cases, and changes that could invalidate a control.',
                ],
                'example': 'A daily automated check compares payment-limit settings with approved policy and raises a reviewable alert when they differ.',
            },
        ],
        'key_terms': [
            ('Compliance testing', 'Testing that checks whether a product or process meets applicable obligations.'),
            ('Audit trail', 'A protected record of actions and decisions that supports later review.'),
            ('Traceability', 'A link between obligations, requirements, tests, results, and defects.'),
            ('Continuous compliance testing', 'Repeated automated checking of selected controls over time.'),
        ],
        'exam_tips': [
            'Distinguish a feature test from evidence that an applicable obligation is met.',
            'Remember that automated compliance checks need controlled configuration and reviewable results.',
            'Relate auditability to traceable, attributable, and reproducible evidence.',
        ],
    },
    {
        'number': 3,
        'title': 'Risk-Based Testing',
        'minutes': 45,
        'intro': 'Risk-based testing directs limited test effort toward financial failures with the greatest likelihood or impact.',
        'sections': [
            {
                'title': '3.1 Categories of Risk in Financial Systems',
                'summary': 'Financial risk can arise from business rules, technology, security, operations, data, or external dependencies.',
                'points': [
                    'Business and financial risks include incorrect balances, mispriced products, or missed transactions.',
                    'Technical and operational risks include outages, interface errors, cyber threats, and failures in recovery.',
                    'Regulatory and data risks include non-compliance, privacy breaches, and inaccurate reporting.',
                ],
                'example': 'A delayed market-data feed can create both a technical availability risk and a business risk if trades use stale prices.',
            },
            {
                'title': '3.2 Principles of Risk-Based Testing in Financial Systems',
                'summary': 'Risk analysis estimates what can go wrong and how serious it would be, then uses that assessment to prioritize testing.',
                'points': [
                    'Assess likelihood and impact using product context, past defects, complexity, transaction exposure, and regulatory consequences.',
                    'Set test depth and priority in proportion to risk, and revisit the assessment when the system or environment changes.',
                    'Risk-based priorities guide effort; they do not remove the need to meet mandatory controls.',
                ],
                'example': 'A team tests overdraft calculations before a low-impact profile-color setting because an incorrect fee affects customer funds.',
            },
            {
                'title': '3.3 Test Activities Related to Risk-Based Testing',
                'summary': 'Risk priorities influence planning, test analysis, design, execution order, monitoring, and reporting.',
                'points': [
                    'Use high-risk conditions to shape coverage and select representative data and environments.',
                    'Run critical and time-sensitive checks early, then monitor whether remaining risk is acceptable.',
                    'Report residual risks and assumptions so release decisions are informed.',
                ],
                'example': 'When a release window shrinks, testers run settlement and duplicate-payment checks first and clearly report which lower-risk checks remain.',
            },
        ],
        'key_terms': [
            ('Risk-based testing', 'A testing approach that prioritizes work according to assessed risk.'),
            ('Impact', 'The consequence if a risk occurs.'),
            ('Likelihood', 'How probable it is that a risk will occur.'),
            ('Residual risk', 'Risk that remains after planned controls and tests.'),
        ],
        'exam_tips': [
            'Separate risk likelihood from risk impact when interpreting a scenario.',
            'Explain how risk changes both test priority and test depth.',
        ],
    },
    {
        'number': 4,
        'title': 'Data Testing and Data Management',
        'minutes': 90,
        'intro': 'Financial decisions depend on accurate, consistent, and appropriately protected data as it moves between systems.',
        'sections': [
            {
                'title': '4.1 Data Accuracy and Data Consistency',
                'summary': 'Data testing checks that financial values are correct and remain consistent across records and processing stages.',
                'points': [
                    'Validate values, formats, calculations, completeness, and relationships against business rules.',
                    'Check that updates do not create conflicting balances or stale copies across connected services.',
                    'Use controlled data with realistic ranges and boundary cases while limiting exposure of personal information.',
                ],
                'example': 'After a customer deposit, tests compare the ledger, account balance, and transaction history to confirm all show the same amount.',
            },
            {
                'title': '4.2 Data Reconciliation Across Financial Systems',
                'summary': 'Reconciliation compares related records from different systems and identifies missing, duplicated, or mismatched transactions.',
                'points': [
                    'Choose matching keys and comparison rules, then account for timing differences and legitimate status changes.',
                    'Investigate unmatched items rather than treating every difference as a software defect.',
                    'Verify that reconciliations produce complete exception records and can be repeated from retained inputs.',
                ],
                'example': 'A settlement test matches each card transaction to processor and bank records, then reports a transaction present at the processor but absent from the ledger.',
            },
            {
                'title': '4.3 Data Privacy and Data Protection in Finance Testing',
                'summary': 'Test data handling must protect personal and financial information throughout preparation, use, storage, and disposal.',
                'points': [
                    'Apply access controls, masking or synthetic data, secure transfer, and retention limits appropriate to the data.',
                    'Check that sensitive fields are not exposed in screens, logs, exports, or test reports.',
                    'Confirm data is removed or retained according to approved policy after testing ends.',
                ],
                'example': 'A test uses masked account numbers and verifies that an error log never prints a customer’s full card details.',
            },
        ],
        'key_terms': [
            ('Data reconciliation', 'Comparison of related data sets to find and resolve differences.'),
            ('Data consistency', 'Agreement of related values across records or systems.'),
            ('Data masking', 'Changing sensitive values so they cannot identify or expose a real person.'),
            ('Synthetic data', 'Artificially created data used in place of real customer records.'),
        ],
        'exam_tips': [
            'Recognize that reconciliation must consider valid timing and status differences.',
            'Include privacy controls in test-data preparation as well as in application behavior.',
        ],
    },
    {
        'number': 5,
        'title': 'Functional and Non-Functional Testing',
        'minutes': 165,
        'intro': 'Financial software must perform the right business actions while remaining responsive, secure, and available under demanding conditions.',
        'sections': [
            {
                'title': '5.1 Functional Testing of Financial Systems',
                'summary': 'Functional tests check transaction rules, account behavior, calculations, and the outcomes visible to users and other systems.',
                'points': [
                    'Derive scenarios from product rules, transaction lifecycles, user roles, and interfaces.',
                    'Check normal, invalid, boundary, reversal, and duplicate requests against expected financial results.',
                    'Verify that transaction states and records remain aligned across connected services.',
                ],
                'example': 'A transfer test checks a valid payment, an amount above the daily limit, and a repeated request to ensure funds move only once.',
            },
            {
                'title': '5.2 Performance Risks in Finance',
                'summary': 'Heavy transaction peaks and tight processing windows can expose delays, capacity limits, and failures in dependent systems.',
                'points': [
                    'Consider market openings, payroll dates, billing cycles, and settlement deadlines as load drivers.',
                    'Slow responses can cause retries, duplicate transactions, missed cutoffs, or customer-facing outages.',
                    'Dependencies, data growth, and uneven traffic can affect performance as much as application code.',
                ],
                'example': 'A payroll provider processes many salary payments at month-end; delayed responses could push settlements past the bank’s cutoff.',
            },
            {
                'title': '5.3 Performance Testing in Financial Contexts',
                'summary': 'Load and stress testing measure behavior at expected demand and beyond planned capacity using finance-relevant workloads.',
                'points': [
                    'Model realistic transaction mixes, concurrency, data volumes, and external-service responses.',
                    'Measure throughput, response time, resource use, error rates, and recovery behavior.',
                    'Stress tests explore limits and failure modes; load tests assess expected operating demand.',
                ],
                'example': 'A team replays a realistic mix of balance checks and transfers at expected peak volume, then increases load to find when response times exceed the service target.',
            },
            {
                'title': '5.4 Security Testing and Availability Testing',
                'summary': 'Security testing checks protections against misuse; availability testing checks that important services remain usable and recover reliably.',
                'points': [
                    'Test authentication, authorization, sensitive-data handling, secure interfaces, and resistance to relevant threats.',
                    'Exercise outages, failover, backup restoration, and recovery objectives for critical financial services.',
                    'Check that security controls do not silently block valid transactions and that failures do not bypass controls.',
                ],
                'example': 'During a payment-service failover exercise, the team verifies that only authorized users can retry a payment and that the ledger does not record it twice.',
            },
            {
                'title': '5.5 GenAI in Finance Software Testing',
                'summary': 'Generative AI can assist test work, but its outputs need human validation and careful treatment of confidential data.',
                'points': [
                    'Possible uses include drafting test ideas, summarizing logs, and helping generate test data or scripts.',
                    'Check generated material for factual errors, bias, insecure suggestions, and gaps in financial rules.',
                    'Do not expose regulated or personal data to an unapproved model; preserve review and traceability.',
                ],
                'example': 'A tester asks an approved assistant for edge cases on an interest calculation, then checks every suggestion against the bank’s signed product rules.',
            },
        ],
        'key_terms': [
            ('Throughput', 'The amount of work a system completes in a period.'),
            ('Load testing', 'Testing system behavior at expected or specified demand.'),
            ('Stress testing', 'Testing beyond expected capacity to understand limits and failure behavior.'),
            ('Failover', 'Switching service to a backup component when the primary component fails.'),
            ('Generative AI', 'AI that produces new text, code, or other content from prompts or context.'),
        ],
        'exam_tips': [
            'Distinguish expected-load testing from tests that deliberately exceed capacity.',
            'Relate performance scenarios to financial peaks and processing cutoffs.',
            'Treat generated test ideas as candidates that require domain review and data safeguards.',
        ],
    },
    {
        'number': 6,
        'title': 'Test Automation',
        'minutes': 105,
        'intro': 'Automation can speed up repeatable finance checks, but regulated systems require reliable evidence, maintainable tests, and controlled changes.',
        'sections': [
            {
                'title': '6.1 Role of Test Automation in Finance Testing',
                'summary': 'Automation is useful for frequent, repeatable checks and can strengthen feedback when its results are trustworthy.',
                'points': [
                    'Automated regression checks help detect unintended changes in critical workflows and calculations.',
                    'Select automation based on repeat frequency, stability, risk, and the cost of maintaining the tests.',
                    'Automation supports human judgment; it does not replace exploratory or expert review.',
                ],
                'example': 'A nightly automated suite repeats account-interest and payment-reversal checks after a shared finance library changes.',
            },
            {
                'title': '6.2 Test Automation Strategies',
                'summary': 'A strategy chooses what to automate, at which layer, and how automation fits both modern services and older systems.',
                'points': [
                    'Prefer stable, valuable checks and clear expected results; build reusable components where they reduce duplication.',
                    'Combine API, service, interface, and end-to-end checks to balance speed, coverage, and diagnostic clarity.',
                    'Plan for legacy interfaces, test data, environment control, and dependencies on external services.',
                ],
                'example': 'A bank automates fee calculations at the service layer and reserves a smaller end-to-end suite for complete transfer journeys.',
            },
            {
                'title': '6.3 Challenges of Test Automation in Regulated Environments',
                'summary': 'Regulated automation must be controlled, explainable, and capable of producing evidence suitable for review.',
                'points': [
                    'Control access, version changes, test data, execution configuration, and retention of results.',
                    'Make automated outcomes reproducible and traceable to the rule, test version, build, and environment.',
                    'Unstable tests and unreviewed scripts can create misleading evidence or hide important failures.',
                ],
                'example': 'An auditor can reproduce a failed limit-control test because the team retained its script version, data set, build identifier, and execution log.',
            },
            {
                'title': '6.4 Challenges in Different Types of Test Automation',
                'summary': 'Mobile, frontend, and backend automation face different sources of change and different limits on observability.',
                'points': [
                    'Mobile checks must account for device, operating-system, network, and screen variations.',
                    'Frontend checks can be fragile when layouts or selectors change; backend checks may need controlled data and service dependencies.',
                    'Choose the layer that gives stable feedback for the risk being tested, and keep a focused set of end-to-end checks.',
                ],
                'example': 'A team verifies transfer rules through stable API tests and uses a smaller device matrix to check that the mobile app displays confirmation correctly.',
            },
        ],
        'key_terms': [
            ('Test automation', 'Use of software to execute tests and compare results with expectations.'),
            ('Regression testing', 'Testing after a change to find unintended effects on existing behavior.'),
            ('Test oracle', 'A source used to decide whether an observed result is correct.'),
            ('Test evidence', 'Records that support conclusions about test execution and results.'),
        ],
        'exam_tips': [
            'Choose automation targets by value and stability, not simply because a test can be scripted.',
            'Remember that regulated automation requires controlled versions and reproducible evidence.',
            'Match mobile, frontend, and backend automation to the risks each layer can observe well.',
        ],
    },
]
