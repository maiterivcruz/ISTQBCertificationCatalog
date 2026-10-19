CHAPTERS = [
    {
        'number': 1,
        'title': 'Security Paradigms',
        'minutes': 135,
        'intro': 'Security testing starts with understanding valuable assets, protection needs and the assumptions behind trust.',
        'sections': [
            {
                'title': '1.1 Asset Security Levels',
                'summary': 'Assets need protection proportionate to their sensitivity, value and likely harm if exposed or changed.',
                'points': [
                    'Identify information and other assets, then classify them by protection needs.',
                    'Sensitivity affects the safeguards and security tests needed for confidentiality, integrity and availability.',
                    'Use the asset context to prioritize testing and avoid treating all data as equally sensitive.',
                ],
                'example': 'A clinic classifies a public opening-hours page differently from patient records, so access-control and disclosure tests focus most strongly on the records.',
            },
            {
                'title': '1.2 Security Audits',
                'summary': 'Security testing can provide evidence for audits, while an audit evaluates controls and compliance against defined criteria.',
                'points': [
                    'Understand the audit scope, applicable rules, evidence requirements and responsibilities.',
                    'Provide repeatable test results and traceable evidence without claiming that one test proves complete security.',
                    'Coordinate testing with audit work while preserving the distinct purpose of each activity.',
                ],
                'example': 'An auditor checks whether privileged access is reviewed quarterly; security testers provide evidence from role and access tests, while the audit also examines review records.',
            },
            {
                'title': '1.3 The Concept of Zero Trust',
                'summary': 'Zero trust assumes that access must be verified continually rather than granted solely because a user is inside a network.',
                'points': [
                    'Authenticate identity and authorize each request using context and least privilege.',
                    'Test access boundaries across users, devices, services and changing sessions.',
                    'Do not treat network location as proof that a request is safe or authorized.',
                ],
                'example': 'A support employee who signs in from the office still needs explicit permission to view a customer’s payment details, and the permission is checked again when the session changes.',
            },
            {
                'title': '1.4 Open-Source Software',
                'summary': 'Reusing open-source components can speed delivery but introduces dependencies that need visibility and maintenance.',
                'points': [
                    'Know which components and versions are included and where they come from.',
                    'Assess known vulnerabilities, maintenance health, license conditions and update paths.',
                    'Include component risks in the security test approach rather than treating reused code as automatically safe.',
                ],
                'example': 'A team inventories a logging library, finds that its version is no longer maintained, checks for exposure to known issues and plans a safe upgrade.',
            },
        ],
        'key_terms': [
            ('Asset', 'Information or another resource that has value and needs protection.'),
            ('Information sensitivity', 'The degree of harm that could follow from inappropriate disclosure or change.'),
            ('Zero trust', 'An approach that verifies access rather than trusting a user or device by location.'),
            ('Open-source component', 'Reusable software whose source is available under a stated license.'),
        ],
        'exam_tips': [
            'Relate the protection level to the asset’s sensitivity and business impact.',
            'Zero trust means verify each access decision, not simply move the network boundary.',
            'Component reuse still requires inventory, vulnerability and maintenance checks.',
        ],
    },
    {
        'number': 2,
        'title': 'Security Test Techniques',
        'minutes': 150,
        'intro': 'Security techniques are selected according to the tester’s access, the project context and the controls that need evidence.',
        'sections': [
            {
                'title': '2.1 Applying Security Test Types According to a Test Context',
                'summary': 'Black-box, white-box and grey-box perspectives provide different levels of knowledge, and static and dynamic tests examine different evidence.',
                'points': [
                    'Black-box tests use little internal knowledge, white-box tests use implementation knowledge, and grey-box tests combine partial knowledge.',
                    'Static security testing examines artifacts without executing the system; dynamic testing observes running behavior.',
                    'Choose the perspective and test type to match the risk, access available and question being asked.',
                ],
                'example': 'A tester first probes a public sign-in endpoint without source access, then reviews its authentication code and tests the running service with a known account.',
            },
            {
                'title': '2.2 Applying Security Test Types According to a Project and Technical Context',
                'summary': 'Security checks should reflect the system’s identities, permissions, data and protective mechanisms.',
                'points': [
                    'Check that identity and access-management controls grant only intended privileges and remove stale access.',
                    'Test data protection in storage, transit and use, including handling of sensitive information.',
                    'Evaluate protective technologies such as filters, monitoring and security gateways in the target architecture.',
                    'Select cases from the security approach and verify both normal use and relevant bypass attempts.',
                ],
                'example': 'For a cloud document service, testers verify that a removed employee loses access, files are encrypted in transit, and a gateway blocks a prohibited upload.',
            },
        ],
        'key_terms': [
            ('Black-box testing', 'Testing with little or no knowledge of internal implementation.'),
            ('White-box testing', 'Testing using knowledge of internal code or design.'),
            ('Grey-box testing', 'Testing with partial knowledge of internal details.'),
            ('Static security testing', 'Security examination of artifacts without executing the software.'),
            ('Access control', 'Rules that determine which identities may perform which actions.'),
        ],
        'exam_tips': [
            'Select black-, white- or grey-box testing based on the information available.',
            'Static testing examines artifacts; dynamic testing observes a running system.',
            'Include identity, data and protective controls when matching tests to a system context.',
        ],
    },
    {
        'number': 3,
        'title': 'The Security Test Process',
        'minutes': 120,
        'intro': 'A security test process organizes planning, design, execution, evaluation and maintenance around security objectives.',
        'sections': [
            {
                'title': '3.1 The Security Test Process',
                'summary': 'Security testing is planned and managed as a repeatable process with clear objectives, responsibilities and evidence.',
                'points': [
                    'Define scope, risk, roles, resources, constraints and success criteria before execution.',
                    'Design tests from assets, threats, security requirements and the available test basis.',
                    'Execute safely, evaluate evidence, report results and maintain tests as the product changes.',
                ],
                'example': 'Before testing an online banking release, the team agrees which test accounts and endpoints are in scope, who can run intrusive checks and how urgent findings will be escalated.',
            },
            {
                'title': '3.2 Designing Security Tests for Test Levels',
                'summary': 'Security tests should provide useful evidence at component, integration and end-to-end levels.',
                'points': [
                    'At component level, check security behavior close to the code, such as input handling and authorization decisions.',
                    'At integration level, verify that connected components preserve identity, permissions and data protections.',
                    'End-to-end tests confirm that a user-visible security objective holds across the complete system.',
                ],
                'example': 'A service tests its permission function in isolation, verifies permissions survive calls to the account service, then checks that one customer cannot view another customer’s invoice.',
            },
        ],
        'key_terms': [
            ('Security test process', 'Planned activities used to assess and communicate security behavior.'),
            ('Test basis', 'Information used to design tests, such as requirements, code or threat models.'),
            ('Security objective', 'A stated protection outcome that testing should evaluate.'),
            ('End-to-end test', 'A test of behavior across the complete user or system workflow.'),
        ],
        'exam_tips': [
            'Security testing needs explicit scope and safe execution responsibilities.',
            'Use multiple test levels: component checks do not replace end-to-end evidence.',
        ],
    },
    {
        'number': 4,
        'title': 'Security Testing Standards and Best Practices',
        'minutes': 195,
        'intro': 'Standards and good practices offer a shared vocabulary and guidance, but must be applied to the product’s actual risks.',
        'sections': [
            {
                'title': '4.1 Introduction to Security Standards and Best Practices',
                'summary': 'Standards, regulations and industry guidance differ in authority, scope and intended use.',
                'points': [
                    'Identify the source and purpose of a standard before using it as a test basis.',
                    'Determine whether it is mandatory, contractual or advisory in the project context.',
                    'Translate relevant guidance into testable objectives rather than assuming a checklist guarantees security.',
                ],
                'example': 'A payment provider separates legally required safeguards from optional framework guidance, then maps the applicable obligations to product tests.',
            },
            {
                'title': '4.2 Apply Important Standards and Best Practices for Security Testing',
                'summary': 'Security guidance can help organize vulnerability checks and controls for web applications and other systems.',
                'points': [
                    'Use a framework such as OWASP guidance to identify common web risks and suitable checks.',
                    'Apply standards to the technologies and threats that actually exist in the system.',
                    'Record exclusions and rationale when a recommendation does not fit the product or scope.',
                ],
                'example': 'A team uses a web-security checklist to review access control and injection risks, then adds tests for its own custom authorization model.',
            },
            {
                'title': '4.3 Leveraging Security Testing Standards and Best Practices',
                'summary': 'Oracles and standards help judge security behavior, but each has limits that testers must understand.',
                'points': [
                    'A test oracle supplies a basis for deciding whether observed behavior is correct or secure.',
                    'Standards can improve consistency and coverage, but may be generic, outdated or incomplete for a specific threat.',
                    'Combine guidance with system knowledge, threat analysis and evidence from tests.',
                ],
                'example': 'A standard suggests checking session management, while the team adds a test for the product’s unusual shared-device workflow that the generic guidance does not describe.',
            },
        ],
        'key_terms': [
            ('Standard', 'An agreed set of requirements or recommendations for a defined subject.'),
            ('Best practice', 'A recommended approach supported by experience or guidance.'),
            ('Test oracle', 'A source used to decide whether a test result is acceptable.'),
            ('OWASP', 'An open community that publishes guidance for application security.'),
        ],
        'exam_tips': [
            'Know whether a security source is mandatory or advisory in the given context.',
            'A standard supports test design but does not prove that a product is secure.',
            'Account for gaps between generic guidance and a system’s specific threats.',
        ],
    },
    {
        'number': 5,
        'title': 'Adjusting Security Testing to the Organizational Context',
        'minutes': 195,
        'intro': 'The organization’s structure, rules and threat landscape influence which security tests matter and how they should be carried out.',
        'sections': [
            {
                'title': '5.1 The Impact of Organizational Structures in the Context of Security Test',
                'summary': 'Responsibilities and communication paths affect security testing scope, independence and response.',
                'points': [
                    'Understand who owns assets, controls, test environments and security decisions.',
                    'Consider suppliers, partners and separated teams when establishing access and evidence responsibilities.',
                    'Adapt reporting and escalation to organizational roles without losing clarity about risk.',
                ],
                'example': 'A retailer’s payment provider owns one part of the transaction flow, so the test plan defines which party supplies logs and who investigates a suspected exposure.',
            },
            {
                'title': '5.2 The Impact of Regulations on Security Policies and How to Test Them',
                'summary': 'Regulations shape security policies and create obligations that need evidence and ongoing review.',
                'points': [
                    'Identify relevant laws, contractual obligations and policy controls for the data and service.',
                    'Translate obligations into verifiable behavior, records or process checks.',
                    'Consider jurisdiction and data lifecycle when testing collection, access, retention and deletion.',
                ],
                'example': 'A health portal tests that a patient can access their own record, that staff access is logged, and that a deletion request follows the organization’s retention policy.',
            },
            {
                'title': '5.3 Analyze an Attack Scenario',
                'summary': 'Attack-scenario analysis considers an attacker’s motivation, capabilities, targets and possible routes.',
                'points': [
                    'Identify valuable assets, likely adversaries, motives and access opportunities.',
                    'Trace a plausible attack path and note controls that could prevent, detect or limit harm.',
                    'Use the scenario to prioritize tests and explain why a weakness matters.',
                ],
                'example': 'For a gift-card site, testers consider a fraudster motivated by resale, trace how repeated balance checks could reveal valid codes, and test rate limits and monitoring.',
            },
        ],
        'key_terms': [
            ('Organizational context', 'The structure, responsibilities and constraints that shape security work.'),
            ('Regulation', 'A legal or binding requirement affecting how an organization handles systems or data.'),
            ('Attack scenario', 'A plausible sequence of actions an adversary could use to reach an objective.'),
            ('Threat actor', 'A person or group capable of attempting harmful actions.'),
        ],
        'exam_tips': [
            'Map security responsibilities and information flows across organizational boundaries.',
            'Convert regulatory obligations into evidence that can actually be checked.',
            'Prioritize attack scenarios by assets, motivation, access and plausible impact.',
        ],
    },
    {
        'number': 6,
        'title': 'Adjusting Security Testing to Software Development Lifecycle Models',
        'minutes': 165,
        'intro': 'Security testing should span the lifecycle and adapt to the cadence and risks of development and maintenance.',
        'sections': [
            {
                'title': '6.1 The Effects of Different Software Development Lifecycle Models on Security Testing',
                'summary': 'Lifecycle models influence when security evidence is available and how often tests should run.',
                'points': [
                    'Plan security reviews and checks from requirements and design through implementation, integration and operation.',
                    'In iterative delivery, automate repeatable checks and revisit risks as changes arrive frequently.',
                    'In staged delivery, coordinate early analysis with later verification so security is not postponed until release.',
                ],
                'example': 'An Agile team adds dependency and static checks to its continuous pipeline, while arranging a deeper penetration test before a major service launch.',
            },
            {
                'title': '6.2 Security Testing During Maintenance',
                'summary': 'Maintenance changes can introduce vulnerabilities, so confirmation and regression tests protect existing security behavior.',
                'points': [
                    'Use confirmation testing to check a specific vulnerability fix.',
                    'Use security regression tests to check that the fix and surrounding controls still work after change.',
                    'Interpret results to determine whether the issue is resolved, remains exploitable or has shifted elsewhere.',
                ],
                'example': 'After fixing an authorization bypass in an API, testers confirm the original exploit is blocked and rerun role-based access tests on related endpoints.',
            },
        ],
        'key_terms': [
            ('Software development lifecycle', 'The activities and stages through which software is built and maintained.'),
            ('Security regression test', 'A test checking that a change has not weakened existing security behavior.'),
            ('Confirmation test', 'A test checking whether a particular fix resolved the reported problem.'),
            ('Maintenance', 'Changes made after software has been delivered or deployed.'),
        ],
        'exam_tips': [
            'Security activities should start early and continue through operation.',
            'Confirmation testing checks a fix; regression testing checks for unintended effects.',
        ],
    },
    {
        'number': 7,
        'title': 'Security Testing as Part of an Information Security Management System',
        'minutes': 105,
        'intro': 'Security testing supplies evidence that can help an organization manage information-security risks and improve its controls.',
        'sections': [
            {
                'title': '7.1 Acceptance Criteria for Security Testing',
                'summary': 'Acceptance criteria make the expected security outcome and decision threshold explicit.',
                'points': [
                    'Base criteria on security requirements, risk tolerance and the intended test scope.',
                    'Define what evidence and residual risk are acceptable before interpreting results.',
                    'Use criteria to support a decision, not to imply that all possible vulnerabilities have been found.',
                ],
                'example': 'A service release requires no unresolved critical access-control findings and documented approval for any accepted medium-risk issue.',
            },
            {
                'title': '7.2 Input for an Information Security Management System',
                'summary': 'Security-test findings give the management system evidence about risk, control effectiveness and needed action.',
                'points': [
                    'Share relevant results with risk owners and people responsible for security controls.',
                    'Use trends and recurring findings to identify weaknesses in policies, processes or technology.',
                    'Protect sensitive test evidence and route it through agreed channels.',
                ],
                'example': 'Repeated findings about former employees retaining access lead the organization to review its account-removal process, not just close individual test defects.',
            },
            {
                'title': '7.3 Improving an Information Security Management System by Adjusting Security Testing',
                'summary': 'Testing practices can be adjusted as the organization learns about maturity, performance and changing risk.',
                'points': [
                    'Assess whether security processes are repeatable, measured and improved rather than relying on isolated activities.',
                    'Use meaningful measures to show coverage, timeliness and outcomes without rewarding superficial counts.',
                    'Refine test focus when incidents, changes or evidence reveal new risks.',
                ],
                'example': 'A team notices that vulnerability scans happen regularly but fixes remain open for months, so it tracks remediation age and adds ownership and escalation targets.',
            },
        ],
        'key_terms': [
            ('Acceptance criteria', 'Conditions used to decide whether a security test outcome is acceptable.'),
            ('Information security management system', 'A coordinated set of policies and activities for managing information-security risk.'),
            ('Security maturity', 'How consistently and effectively security practices are established and improved.'),
            ('Residual risk', 'Risk that remains after controls and treatment are applied.'),
        ],
        'exam_tips': [
            'Criteria and risk tolerance should be agreed before results drive a release decision.',
            'Use test findings to improve the management system, not only to close individual defects.',
            'Prefer outcome and trend measures to raw activity counts alone.',
        ],
    },
    {
        'number': 8,
        'title': 'Reporting Security Test Results',
        'minutes': 135,
        'intro': 'Security results need clear, controlled reporting so that findings can be understood, prioritized and resolved responsibly.',
        'sections': [
            {
                'title': '8.1 Security Test Reporting',
                'summary': 'A security report communicates scope, evidence, impact and recommended action to the right audience.',
                'points': [
                    'State what was tested, under what conditions, and what was not covered.',
                    'Describe findings with reproducible evidence, affected assets, severity rationale and practical recommendations.',
                    'Limit sensitive details to authorized recipients and follow the agreed escalation process.',
                ],
                'example': 'A report for a payment API explains a repeatable authorization bypass, identifies affected account data, gives safe reproduction steps and is shared only with the incident team and service owner.',
            },
            {
                'title': '8.2 Identifying and Analyzing Vulnerabilities',
                'summary': 'Test evidence must be evaluated to determine whether a weakness is real, exploitable and significant.',
                'points': [
                    'Validate results and distinguish confirmed vulnerabilities from false positives or incomplete evidence.',
                    'Assess exploitability, affected assets and business impact in the actual context.',
                    'Consider dependencies and attack paths when prioritizing remediation.',
                ],
                'example': 'A scanner reports an exposed administrative page; testers confirm whether authentication is missing and whether the page reveals sensitive operations before assigning priority.',
            },
            {
                'title': '8.3 Close Vulnerabilities',
                'summary': 'Closing a vulnerability requires an appropriate treatment, confirmation evidence and traceable ownership.',
                'points': [
                    'Select a response such as fix, mitigation, risk acceptance or removal of the affected component.',
                    'Retest the original weakness and relevant neighboring controls after the change.',
                    'Document remaining risk, decisions and closure evidence.',
                ],
                'example': 'A team fixes an unsafe file upload by validating type and content, then retests malicious and valid files and records the accepted residual risk for legacy formats.',
            },
        ],
        'key_terms': [
            ('Vulnerability', 'A weakness that could be used to compromise a system or its information.'),
            ('False positive', 'A reported finding that is not a real issue in the tested context.'),
            ('Exploitability', 'How feasible it is for an attacker to use a weakness.'),
            ('Risk acceptance', 'A decision to retain a known risk within defined authority and tolerance.'),
        ],
        'exam_tips': [
            'A report should include scope, reproducible evidence, impact and audience-appropriate detail.',
            'Validate a finding before assigning severity or declaring it closed.',
            'Retest after remediation and record any residual risk.',
        ],
    },
    {
        'number': 9,
        'title': 'Security Testing Tools',
        'minutes': 90,
        'intro': 'Security tools automate or assist parts of testing, but their outputs need skilled selection and interpretation.',
        'sections': [
            {
                'title': '9.1 Categorization of Security Testing Tools',
                'summary': 'Tools can be grouped by the kind of evidence they examine and the security activity they support.',
                'points': [
                    'Static analysis examines source or compiled artifacts; dynamic tools test a running application.',
                    'Other tools support dependency analysis, configuration review, network testing or monitoring.',
                    'Use complementary categories when a single technique cannot cover the relevant risks.',
                ],
                'example': 'A web team combines source analysis for unsafe code patterns, a dependency scanner for vulnerable libraries and dynamic testing against a deployed test instance.',
            },
            {
                'title': '9.2 Selecting Security Testing Tools',
                'summary': 'Tool selection depends on the target, test objective, environment, expertise and ability to verify results.',
                'points': [
                    'Check technology and protocol support, scope, integration, reporting and operational safety.',
                    'Consider false positives, maintenance, training, cost and protection of test data.',
                    'Validate that the tool can reveal the intended issue and that findings can be independently assessed.',
                ],
                'example': 'Before adopting a scanner, a team tries it against a known test application to see whether it detects expected issues without disrupting the shared environment.',
            },
        ],
        'key_terms': [
            ('Static analysis tool', 'A tool that checks software artifacts without running the application.'),
            ('Dynamic analysis tool', 'A tool that examines behavior while software is running.'),
            ('False positive', 'A tool finding that does not represent a real vulnerability in context.'),
            ('Tool suitability', 'How well a tool fits the target, objective and operating constraints.'),
        ],
        'exam_tips': [
            'Different tool categories examine different evidence; combine them where useful.',
            'Assess safety, result quality and maintainability as well as feature lists.',
        ],
    },
]
