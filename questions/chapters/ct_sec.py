CHAPTERS = [
    {
        'number': 1,
        'title': 'The Basis of Security Testing',
        'minutes': 105,
        'intro': 'Security testing evaluates whether systems protect information and services against relevant threats and organizational risks.',
        'sections': [
            {
                'title': '1.1 Security Risks',
                'summary': 'Security risk connects a threat and a weakness to possible harm for an asset.',
                'points': [
                    'Identify assets, threats, vulnerabilities and the business consequences of compromise.',
                    'Estimate risk using likelihood and impact, recognizing that estimates depend on context.',
                    'Use risk to guide test priorities and explain why a finding matters.',
                ],
                'example': 'A public account-recovery page has a weak rate limit; testers assess how likely code guessing is and the impact of taking over customer accounts.',
            },
            {
                'title': '1.2 Information Security Policies and Procedures',
                'summary': 'Policies state security expectations and procedures describe how people carry them out.',
                'points': [
                    'Use policies and procedures as sources for testable controls and responsibilities.',
                    'Check whether the documented process is followed and whether the system supports it.',
                    'Keep rules current with changing technology, threats and organizational needs.',
                ],
                'example': 'A policy requires prompt removal of departing staff access; a procedure defines the owner and timing, and a test checks that disabled accounts can no longer sign in.',
            },
            {
                'title': '1.3 Security Auditing and Its Role in Security Testing',
                'summary': 'Audits assess evidence against defined obligations, while security tests examine controls and system behavior.',
                'points': [
                    'Know the audit scope and what evidence is expected before planning supporting tests.',
                    'Testing can contribute evidence, but a test result alone is not a complete audit or proof of compliance.',
                    'Preserve traceability, repeatability and controlled handling of sensitive evidence.',
                ],
                'example': 'An access-control test shows that roles behave as intended; an audit also checks approval records and whether periodic access reviews were completed.',
            },
        ],
        'key_terms': [
            ('Asset', 'A system, service or information item that has value.'),
            ('Threat', 'A potential cause of harm to an asset.'),
            ('Vulnerability', 'A weakness that a threat could exploit.'),
            ('Risk', 'The possibility and impact of loss under a threat.'),
            ('Security policy', 'A high-level rule describing required security behavior.'),
        ],
        'exam_tips': [
            'Separate threat, vulnerability, impact and risk when analyzing a scenario.',
            'Testing can support an audit but does not replace the audit’s broader evidence review.',
        ],
    },
    {
        'number': 2,
        'title': 'Security Testing Purposes, Goals and Strategies',
        'minutes': 130,
        'intro': 'A security test strategy explains why, where and how testing will provide evidence about protection goals.',
        'sections': [
            {
                'title': '2.1 Introduction',
                'summary': 'Security testing is a planned evaluation of whether security requirements and controls behave as intended.',
                'points': [
                    'Testing can uncover weaknesses, check controls and provide information for risk decisions.',
                    'No finite test set proves that a system has no vulnerabilities.',
                    'Use evidence and context to describe what the test can and cannot establish.',
                ],
                'example': 'A penetration test finds an exposed administration function, but the report also states which interfaces and configurations were not assessed.',
            },
            {
                'title': '2.2 The Purpose of Security Testing',
                'summary': 'Testing helps prevent, detect and understand security failures and supports decisions about residual risk.',
                'points': [
                    'Check confidentiality, integrity and availability expectations where relevant.',
                    'Provide actionable evidence for developers, security owners and decision makers.',
                    'Retest changes to confirm that weaknesses are fixed and controls remain effective.',
                ],
                'example': 'A document portal test checks that files cannot be read by another user, reports a confirmed access flaw and repeats the check after the authorization fix.',
            },
            {
                'title': '2.3 The Organizational Context',
                'summary': 'The organization’s assets, responsibilities, obligations and risk tolerance shape security testing.',
                'points': [
                    'Understand business goals, asset owners, policies, legal obligations and third-party relationships.',
                    'Consider who authorizes testing and how sensitive results should be managed.',
                    'Adapt the scope to organizational priorities without ignoring high-impact exposures.',
                ],
                'example': 'A hospital schedules intrusive tests with its operations team to avoid disrupting patient services and routes findings through a restricted security channel.',
            },
            {
                'title': '2.4 Security Testing Objectives',
                'summary': 'Objectives describe the specific security outcomes that a test is intended to evaluate.',
                'points': [
                    'Derive objectives from requirements, risk assessment, threat analysis and control expectations.',
                    'Make objectives specific enough to guide test design and result evaluation.',
                    'Prioritize outcomes by likelihood and impact rather than by ease of testing.',
                ],
                'example': 'A service objective states that only account owners may export their statements, leading directly to tests across valid and unauthorized identities.',
            },
            {
                'title': '2.5 The Scope and Coverage of Security Testing Objectives',
                'summary': 'Scope defines what is included, and coverage describes how much of the intended security basis has been examined.',
                'points': [
                    'Set boundaries for applications, interfaces, roles, environments and test methods.',
                    'Trace objectives to test cases and results so gaps are visible.',
                    'State exclusions and constraints; coverage numbers alone do not show that important threats were tested.',
                ],
                'example': 'A test covers the customer web interface and its public API but excludes a supplier system; the report names that boundary and its effect on conclusions.',
            },
            {
                'title': '2.6 Security Testing Approaches',
                'summary': 'Approaches combine techniques and test levels to fit the threat model and available knowledge.',
                'points': [
                    'Use black-box, white-box or grey-box perspectives according to information and access available.',
                    'Combine static analysis, dynamic testing, reviews and exploratory techniques where they complement each other.',
                    'Plan safe, authorized execution and choose depth according to risk.',
                ],
                'example': 'A team reviews authentication code, scans a running test instance and performs a limited external test to cover different views of the same login risk.',
            },
            {
                'title': '2.7 Improving the Security Testing Practices',
                'summary': 'Security testing improves when teams learn from findings, incidents and changes in technology or threats.',
                'points': [
                    'Review recurring defects and missed risks to find process or knowledge gaps.',
                    'Automate repeatable checks while keeping expert review for context-sensitive threats.',
                    'Update objectives and test assets as the product and attacker techniques change.',
                ],
                'example': 'After repeated dependency findings arrive late, a team adds component checks to its build pipeline and reviews the time-to-fix trend each month.',
            },
        ],
        'key_terms': [
            ('Security objective', 'A defined protection outcome that testing should assess.'),
            ('Scope', 'The boundaries of what a test includes.'),
            ('Coverage', 'The extent to which the chosen test basis or objectives have been examined.'),
            ('Residual risk', 'Risk that remains after security measures are applied.'),
            ('Security strategy', 'The planned approach for meeting security testing objectives.'),
        ],
        'exam_tips': [
            'An objective should be traceable to the risks or security requirements it addresses.',
            'Always state test boundaries and limitations when interpreting coverage.',
            'A good approach combines methods according to context; no single method finds every weakness.',
        ],
    },
    {
        'number': 3,
        'title': 'Security Testing Processes',
        'minutes': 140,
        'intro': 'A managed process makes security testing purposeful, repeatable and connected to risk decisions.',
        'sections': [
            {
                'title': '3.1 Security Test Process Definition',
                'summary': 'Process definition establishes the activities, roles and outputs used to conduct security testing.',
                'points': [
                    'Define how testing is initiated, planned, designed, executed, evaluated and reported.',
                    'Clarify responsibilities, authority, resources, dependencies and how results are handled.',
                    'Adapt the process to product risk and delivery practices while preserving necessary control.',
                ],
                'example': 'A product group defines who approves penetration tests, how test credentials are issued and who receives a critical finding outside business hours.',
            },
            {
                'title': '3.2 Security Test Planning',
                'summary': 'Planning converts objectives into a feasible schedule, approach and set of controlled test conditions.',
                'points': [
                    'Identify test scope, risks, environment, skills, data, tools, schedule and constraints.',
                    'Agree entry and exit criteria, dependencies, safety controls and escalation paths.',
                    'Communicate assumptions so stakeholders know what evidence the plan will produce.',
                ],
                'example': 'A plan for a payment service reserves a non-production environment, synthetic card data and a window when rate-limit tests will not affect customers.',
            },
            {
                'title': '3.3 Security Test Design',
                'summary': 'Design creates tests from threats, security requirements, architecture and the behavior of controls.',
                'points': [
                    'Identify relevant attack paths, roles, inputs, trust boundaries and expected protections.',
                    'Design positive and negative tests, including bypass attempts and misuse cases.',
                    'Prioritize tests according to risk and make expected results observable.',
                ],
                'example': 'For an upload feature, tests cover an allowed document, a disguised executable, an oversized file and an attempt to access another user’s upload.',
            },
            {
                'title': '3.4 Security Test Execution',
                'summary': 'Execution applies planned tests safely and records sufficient evidence to support analysis.',
                'points': [
                    'Verify authorization, environment and test data before running potentially intrusive checks.',
                    'Capture actions, outcomes, timestamps and relevant system evidence securely.',
                    'Stop or escalate if the test creates unexpected impact or reveals a serious exposure.',
                ],
                'example': 'During a test of a staging service, the tester detects that a request is reaching production data and stops immediately, then alerts the agreed contact.',
            },
            {
                'title': '3.5 Security Test Evaluation',
                'summary': 'Evaluation compares evidence with objectives and determines the meaning and severity of findings.',
                'points': [
                    'Validate observations and distinguish confirmed weaknesses from inconclusive results.',
                    'Assess exploitability, affected assets, likelihood and impact in the actual context.',
                    'Identify unmet objectives and limitations before making a conclusion.',
                ],
                'example': 'A scanner flags a weak cipher suite; testers confirm the live endpoint configuration and determine whether the affected interface carries sensitive information.',
            },
            {
                'title': '3.6 Security Test Maintenance',
                'summary': 'Test cases and environments need maintenance as threats, software and security requirements change.',
                'points': [
                    'Review tests after code changes, incidents, new vulnerabilities and architectural changes.',
                    'Remove obsolete checks and update data, tools and expected behavior.',
                    'Keep regression tests focused on important security controls and prior defects.',
                ],
                'example': 'When an identity provider changes its token format, the team updates integration tests and checks that expired and revoked tokens remain rejected.',
            },
        ],
        'key_terms': [
            ('Entry criterion', 'A condition required before a test activity starts.'),
            ('Exit criterion', 'A condition used to decide when a test activity can end.'),
            ('Attack path', 'A sequence of actions that could lead to an attacker’s objective.'),
            ('Security evidence', 'Information supporting a conclusion about a security objective.'),
            ('Test maintenance', 'Updating tests and supporting assets to keep them useful.'),
        ],
        'exam_tips': [
            'Plan authorization, safety and escalation before execution.',
            'Evaluate test evidence against objectives and note inconclusive areas.',
            'Maintain security tests when software, threats or controls change.',
        ],
    },
    {
        'number': 4,
        'title': 'Security Testing Throughout the Software Lifecycle',
        'minutes': 225,
        'intro': 'Security decisions made early affect later testability, and each lifecycle activity offers opportunities to reduce risk.',
        'sections': [
            {
                'title': '4.1 The Role of Security Testing in a Software Lifecycle',
                'summary': 'Security testing should connect to requirements, design, implementation, acceptance and maintenance.',
                'points': [
                    'Use lifecycle activities to identify security concerns before they become expensive defects.',
                    'Match review and test techniques to the artifacts available at each stage.',
                    'Continue security feedback during operation and maintenance as risks change.',
                ],
                'example': 'A team reviews data flow during design, checks input handling during implementation, tests access controls before acceptance and monitors vulnerabilities after deployment.',
            },
            {
                'title': '4.2 The Role of Security Testing in Requirements',
                'summary': 'Requirements define protection goals and should make security expectations clear enough to verify.',
                'points': [
                    'Review requirements for confidentiality, integrity, availability, privacy and access needs.',
                    'Ask about threat assumptions, data classification, misuse and measurable acceptance conditions.',
                    'Trace security requirements to design controls and tests.',
                ],
                'example': 'A requirement that only authorized staff can export records is refined to specify roles, audit logging and behavior when access is denied.',
            },
            {
                'title': '4.3 The Role of Security Testing in Design',
                'summary': 'Design review and threat analysis can expose insecure boundaries before implementation fixes become costly.',
                'points': [
                    'Examine architecture, trust boundaries, data flows, interfaces and security control placement.',
                    'Use threat modeling to identify attacker goals and derive testable mitigations.',
                    'Check that security mechanisms are consistent across components.',
                ],
                'example': 'A design review shows that a reporting service bypasses the normal authorization gateway, prompting a change before the endpoint is built.',
            },
            {
                'title': '4.4 The Role of Security Testing in Implementation Activities',
                'summary': 'Implementation-stage security checks examine code, dependencies and configuration while changes are still manageable.',
                'points': [
                    'Use code reviews and static checks to find unsafe patterns and missed controls.',
                    'Check component behavior, input validation, error handling and secrets management.',
                    'Include third-party components and deployment configuration in the test basis.',
                ],
                'example': 'A code review catches a service key committed to a configuration file, while a dependency check flags an outdated parsing library.',
            },
            {
                'title': '4.5 The Role of Security Testing in System and Acceptance Test Activities',
                'summary': 'System and acceptance testing validate security behavior across integrated workflows and user roles.',
                'points': [
                    'Test interactions between components, identity services and external systems.',
                    'Check realistic attack scenarios and security acceptance criteria in a representative environment.',
                    'Manage test data and access so verification does not expose real sensitive information.',
                ],
                'example': 'An end-to-end test checks that a customer can reset their password securely, that old sessions are invalidated and that support staff cannot view the new secret.',
            },
            {
                'title': '4.6 The Role of Security Testing in Maintenance',
                'summary': 'Maintenance testing protects systems as patches, configuration changes and new threats arrive.',
                'points': [
                    'Reassess risks after changes and confirm that security fixes work.',
                    'Run targeted regression tests around affected controls and interfaces.',
                    'Use vulnerability and incident information to refresh test priorities.',
                ],
                'example': 'After a framework upgrade, the team reruns authentication and session tests and checks whether newly published vulnerabilities affect the deployed version.',
            },
        ],
        'key_terms': [
            ('Threat modeling', 'A structured way to identify threats and decide how to address them.'),
            ('Trust boundary', 'A point where data or control passes between different trust levels.'),
            ('Static analysis', 'Examination of software artifacts without running them.'),
            ('Security requirement', 'A stated protection need that a system must satisfy.'),
        ],
        'exam_tips': [
            'Choose lifecycle-appropriate checks early and continue through maintenance.',
            'Threat modeling links architecture risks to security requirements and tests.',
            'System tests should verify integrated security behavior, not only isolated controls.',
        ],
    },
    {
        'number': 5,
        'title': 'Testing Security Mechanisms',
        'minutes': 240,
        'intro': 'Security mechanisms only reduce risk when correctly configured and effective against relevant misuse.',
        'sections': [
            {
                'title': '5.1 System Hardening',
                'summary': 'Hardening reduces unnecessary services, privileges and configuration weaknesses.',
                'points': [
                    'Compare system settings with an approved baseline and remove unused functionality.',
                    'Check that defaults, patches and administrative access follow policy.',
                    'Recheck configuration after deployment or major change.',
                ],
                'example': 'A server review finds an unused remote administration service enabled; the team disables it and verifies the service is no longer reachable.',
            },
            {
                'title': '5.2 Authentication and Authorization',
                'summary': 'Authentication verifies identity; authorization determines what an authenticated identity may do.',
                'points': [
                    'Test identity proof, credential handling, session behavior and recovery paths.',
                    'Verify least privilege, role boundaries, access revocation and protection from privilege escalation.',
                    'Check both permitted actions and attempts to access another user’s data or functions.',
                ],
                'example': 'A sales user can view assigned customer accounts but cannot change an administrator’s role or retrieve another region’s records.',
            },
            {
                'title': '5.3 Encryption',
                'summary': 'Encryption helps protect information, but correct key management and configuration are essential.',
                'points': [
                    'Check that sensitive data is protected in transit and where required at rest.',
                    'Review protocol and algorithm configuration, certificate validation and key access.',
                    'Verify that secrets are not exposed through logs, errors or insecure storage.',
                ],
                'example': 'A tester confirms that a customer portal rejects an invalid certificate and that exported records are encrypted in storage with keys unavailable to ordinary users.',
            },
            {
                'title': '5.4 Firewalls and Network Zones',
                'summary': 'Network controls restrict traffic between systems according to trust and business need.',
                'points': [
                    'Test allowed and denied paths between network zones and exposed services.',
                    'Check that rules are narrow, current and consistent with system responsibilities.',
                    'Consider alternate routes and misconfigurations that could bypass a boundary.',
                ],
                'example': 'An application server should reach the database on one approved port, but a test confirms that direct database access from the public network is blocked.',
            },
            {
                'title': '5.5 Intrusion Detection',
                'summary': 'Detection systems identify suspicious activity and support timely investigation.',
                'points': [
                    'Check whether relevant events are collected, correlated and alerted on.',
                    'Test detection with controlled scenarios and verify that normal activity does not create excessive noise.',
                    'Confirm alert ownership, escalation and log protection.',
                ],
                'example': 'A controlled sequence of failed logins should trigger an alert that reaches the on-call security analyst with enough context to investigate.',
            },
            {
                'title': '5.6 Malware Scanning',
                'summary': 'Malware scanning checks files or systems for known malicious content, but does not catch every threat.',
                'points': [
                    'Verify that scanning is enabled at intended upload and execution points and that signatures update.',
                    'Check handling of detected files, including quarantine, notification and recovery.',
                    'Combine scanning with other controls because new or disguised malware may evade detection.',
                ],
                'example': 'A file-sharing service uses a safe test signature to verify that uploaded content is quarantined and the uploader receives an appropriate message.',
            },
            {
                'title': '5.7 Data Obfuscation',
                'summary': 'Obfuscation hides or transforms data to reduce exposure while preserving enough utility for a purpose.',
                'points': [
                    'Choose masking or transformation appropriate to sensitivity and test needs.',
                    'Check that hidden values cannot be recovered through simple inference or linked records.',
                    'Protect mapping data and avoid using production information when safer alternatives work.',
                ],
                'example': 'A test environment replaces customer names and card numbers with synthetic values while preserving realistic formats for validation.',
            },
            {
                'title': '5.8 Training',
                'summary': 'People are part of security controls, so awareness and role-specific training should be evaluated in context.',
                'points': [
                    'Identify behaviors and decisions that employees need to perform securely.',
                    'Use realistic education and practice rather than relying on policy documents alone.',
                    'Evaluate understanding and improve training when incidents or tests reveal gaps.',
                ],
                'example': 'After a simulated phishing exercise, a support team practices verifying identity before resetting an account and reviews how to report suspicious requests.',
            },
        ],
        'key_terms': [
            ('Hardening', 'Reducing attack opportunities by securing system configuration.'),
            ('Authentication', 'Verifying that an identity is who it claims to be.'),
            ('Authorization', 'Deciding which actions an identity is permitted to perform.'),
            ('Intrusion detection', 'Monitoring for activity that may indicate an attack.'),
            ('Data obfuscation', 'Transforming data to hide sensitive values while retaining useful properties.'),
        ],
        'exam_tips': [
            'Do not confuse authentication with authorization.',
            'Test both control behavior and its configuration, monitoring and response.',
            'Treat malware scanning and encryption as parts of defense, not guarantees of safety.',
        ],
    },
    {
        'number': 6,
        'title': 'Human Factors in Security Testing',
        'minutes': 105,
        'intro': 'Security depends on how people behave, what attackers seek and how well people recognize and respond to manipulation.',
        'sections': [
            {
                'title': '6.1 Understanding the Attackers',
                'summary': 'Attacker profiles help explain motivation, capability, resources and likely targets.',
                'points': [
                    'Consider insider and external attackers, their goals, knowledge and access.',
                    'Use realistic motivation and capability when selecting scenarios instead of assuming every attacker is identical.',
                    'Connect attacker analysis to assets and likely paths of attack.',
                ],
                'example': 'A competitor seeking product plans and a criminal seeking payment data have different motives, so their likely entry points and impact differ.',
            },
            {
                'title': '6.2 Social Engineering',
                'summary': 'Social engineering uses manipulation to persuade people to reveal information or perform unsafe actions.',
                'points': [
                    'Test common tactics such as impersonation, urgency, authority and fabricated trust.',
                    'Use controlled, authorized simulations and protect participants from harm or public shaming.',
                    'Assess reporting and verification behavior as well as whether the initial request succeeds.',
                ],
                'example': 'In an approved exercise, a caller pretending to be IT asks an employee to reset a manager’s password; the expected response is to verify identity through an independent channel.',
            },
            {
                'title': '6.3 Security Awareness',
                'summary': 'Awareness helps people recognize risks and know how to report or respond to them.',
                'points': [
                    'Tailor guidance to job responsibilities and likely threats.',
                    'Provide simple reporting routes and reinforce safe behavior through practice.',
                    'Use exercise outcomes to improve training and processes rather than punish individuals.',
                ],
                'example': 'After several employees report a convincing fake invoice, the organization improves the payment-verification procedure and teaches staff where to forward suspicious messages.',
            },
        ],
        'key_terms': [
            ('Threat actor', 'A person or group that may attempt to compromise a system.'),
            ('Social engineering', 'Manipulating people to disclose information or take unsafe actions.'),
            ('Security awareness', 'Knowledge that helps people recognize and respond to security risks.'),
            ('Insider threat', 'Risk arising from someone with legitimate organizational access.'),
        ],
        'exam_tips': [
            'Analyze attacker motivation and capability in relation to assets and access.',
            'Social-engineering exercises should be authorized, controlled and used for learning.',
        ],
    },
    {
        'number': 7,
        'title': 'Security Test Evaluation and Reporting',
        'minutes': 70,
        'intro': 'Security evidence must be evaluated against objectives and communicated so that risks can be acted on.',
        'sections': [
            {
                'title': '7.1 Security Test Evaluation',
                'summary': 'Evaluation determines what the evidence shows, what remains uncertain and whether objectives were met.',
                'points': [
                    'Validate results and consider severity, exploitability, asset value and business impact.',
                    'Separate confirmed issues from false positives, assumptions and test limitations.',
                    'Use the evaluation to support risk treatment and retesting decisions.',
                ],
                'example': 'A scanner flags a public endpoint; testers reproduce the issue, determine which records are exposed and document any access conditions that affect severity.',
            },
            {
                'title': '7.2 Security Test Reporting',
                'summary': 'A report presents relevant findings and conclusions with the right amount of detail for its readers.',
                'points': [
                    'Include scope, approach, environment, evidence, limitations, risks and recommended actions.',
                    'Make findings understandable and reproducible while protecting sensitive details.',
                    'Deliver results to authorized stakeholders and establish follow-up ownership.',
                ],
                'example': 'A technical report gives developers safe reproduction steps, while an executive summary explains the business exposure and decision needed from leadership.',
            },
        ],
        'key_terms': [
            ('Security finding', 'A result that indicates a possible security weakness or control gap.'),
            ('Severity', 'An estimate of how serious a finding is in context.'),
            ('False positive', 'A reported issue that is not confirmed in the tested context.'),
            ('Test limitation', 'A constraint that affects what a result can establish.'),
        ],
        'exam_tips': [
            'A finding’s priority depends on exploitability and impact, not a tool score alone.',
            'Report both evidence and limitations, and protect sensitive details.',
        ],
    },
    {
        'number': 8,
        'title': 'Security Testing Tools',
        'minutes': 55,
        'intro': 'Tools support security testing at different levels, but their outputs require appropriate selection and interpretation.',
        'sections': [
            {
                'title': '8.1 Types and Purposes of Security Testing Tools',
                'summary': 'Tool categories support different activities such as code analysis, vulnerability discovery and monitoring.',
                'points': [
                    'Static tools examine source or binaries; dynamic tools probe running applications or services.',
                    'Other tools assess networks, configurations, dependencies, malware or security events.',
                    'Match tool output to the test objective and check findings with suitable evidence.',
                ],
                'example': 'A team uses a source analyzer to find risky code patterns, a web scanner against a test service and a log-monitoring tool to check alert behavior.',
            },
            {
                'title': '8.2 Tool Selection',
                'summary': 'A tool is useful when its technical coverage, operating constraints and result quality fit the project.',
                'points': [
                    'Assess compatibility with the target, environment, protocols and required scale.',
                    'Consider expertise, maintenance, cost, safety, reporting and false-positive handling.',
                    'Run a proof of concept and verify that findings can be understood and acted on.',
                ],
                'example': 'A team trials two web scanners on a safe test application, comparing detection of known flaws, disruptive behavior and the clarity of remediation advice.',
            },
        ],
        'key_terms': [
            ('Static tool', 'A tool that examines software artifacts without running them.'),
            ('Dynamic tool', 'A tool that tests behavior of a running system.'),
            ('False positive', 'A reported result that does not represent a real weakness.'),
            ('Proof of concept', 'A small trial used to check whether a tool suits the need.'),
        ],
        'exam_tips': [
            'Match a tool category to the artifact or behavior it can examine.',
            'Tool choice includes safety, integration and result quality, not just features.',
        ],
    },
    {
        'number': 9,
        'title': 'Standards and Industry Trends',
        'minutes': 40,
        'intro': 'Security standards and emerging practices can inform testing, but must be interpreted for the system and its risks.',
        'sections': [
            {
                'title': '9.1 Understanding Security Testing Standards',
                'summary': 'Standards organize accepted requirements and practices, with differing scope and authority.',
                'points': [
                    'Identify the publisher, intended audience, version and purpose of a standard.',
                    'Distinguish binding requirements from voluntary guidance and map applicable parts to the system.',
                    'Use standards as a consistent test basis while recognizing that they cannot cover every threat.',
                ],
                'example': 'A regulated service maps mandatory control requirements to tests, then uses a separate industry framework to add checks for risks outside the regulation.',
            },
            {
                'title': '9.2 Applying Security Standards',
                'summary': 'Applying a standard means tailoring relevant controls and verifying evidence in the target environment.',
                'points': [
                    'Select controls that apply to the product, data and organizational obligations.',
                    'Translate controls into testable expectations and retain traceability to results.',
                    'Document exceptions and reasons rather than claiming conformance from a checklist alone.',
                ],
                'example': 'A team tests a standard’s access-control requirement against its cloud roles, records the evidence and documents one approved exception for a legacy reporting account.',
            },
            {
                'title': '9.3 Industry Trends',
                'summary': 'New technologies and attacker practices change the risks and techniques that security testing must consider.',
                'points': [
                    'Monitor changes in platforms, delivery models, vulnerabilities and threat techniques.',
                    'Evaluate whether a new trend affects the organization’s assets and attack surface.',
                    'Update skills, tools and test priorities when evidence shows a relevant change.',
                ],
                'example': 'A team adopts container deployment and reviews image provenance, configuration and runtime isolation because its earlier server-only checks no longer cover the main risks.',
            },
        ],
        'key_terms': [
            ('Security standard', 'A published set of requirements or guidance for security.'),
            ('Control', 'A safeguard intended to reduce a security risk.'),
            ('Conformance', 'Meeting applicable requirements of a standard or policy.'),
            ('Attack surface', 'The exposed points through which a system could be attacked.'),
        ],
        'exam_tips': [
            'Check a standard’s scope and authority before applying it.',
            'A checklist supports evidence gathering but does not prove overall security.',
            'Adopt trends based on relevance to assets and exposure, not novelty alone.',
        ],
    },
]
