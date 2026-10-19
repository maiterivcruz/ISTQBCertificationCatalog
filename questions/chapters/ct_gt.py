"""CT-GT study chapters: plain-language gambling industry testing guidance."""

CHAPTERS = [
    {
        'number': 1,
        'title': 'Introduction to the Gambling Industry',
        'minutes': 215,
        'intro': 'Gambling products combine games of chance, financial transactions, regulated operations, and player-facing services.',
        'sections': [
            {
                'title': '1.1 Objectives and Overview',
                'summary': 'Gambling testing applies general testing skills to products where fairness, compliance, and accurate outcomes are central.',
                'points': [
                    'Testers need to understand the player perspective as well as technical and regulatory expectations.',
                    'Testing may include functional, compliance, math, audio, and multiplayer concerns.',
                    'A result must be both correct for the player and acceptable under the relevant jurisdiction.',
                ],
                'example': 'A tester checks that a slot game shows the same win result to the player and records it accurately for compliance review.',
            },
            {
                'title': '1.2 Gambling Activities and Artifacts',
                'summary': 'Gambling products produce artifacts and records that support play, financial processing, operations, and regulatory evidence.',
                'points': [
                    'Artifacts can include game rules, configuration, transaction records, logs, reports, and certification evidence.',
                    'Testers check that records accurately represent what happened and can be matched across connected systems.',
                    'Player activity and financial activity must be handled securely and consistently.',
                ],
                'example': 'After a player buys a lottery ticket, the ticket record, payment confirmation, and draw entry should all refer to the same purchase.',
            },
            {
                'title': '1.3 Types of Gambling',
                'summary': 'Different gambling products have different rules, interfaces, timing, and transaction flows.',
                'points': [
                    'Casino games, lotteries, race and sports wagering, and online or mobile gambling each have distinct behavior to test.',
                    'The test approach should reflect whether outcomes are generated, selected, scheduled, or based on an external event.',
                    'Online products add browser, network, device, and account interactions to the gambling rules.',
                ],
                'example': 'A sports wager test checks that a bet is accepted before an event cutoff and that later settlement follows the official result.',
            },
            {
                'title': '1.4 Key Concepts in the Gambling Industry',
                'summary': 'Shared industry concepts include jackpots, random number generation, win selection, player privacy, and jurisdictional oversight.',
                'points': [
                    'A progressive jackpot grows as qualifying play contributes to a shared prize pool.',
                    'Random number generators and win-selection logic must produce outcomes according to approved game rules.',
                    'Privacy, geolocation, regulators, and jurisdiction rules affect which players and activities are permitted.',
                ],
                'example': 'A progressive jackpot test verifies that a qualifying wager updates the shared pool and that the displayed prize agrees with the recorded value.',
            },
            {
                'title': '1.5 Gambling Industry Metrics',
                'summary': 'Operational and quality metrics help teams understand how often products pass checks and where compliance problems escape.',
                'points': [
                    'First pass percentage measures the proportion of items or tests that pass on the first attempt, under the defined measure.',
                    'Escaped compliance defects are compliance problems found after the intended testing or approval stage.',
                    'Metrics need consistent definitions and context before teams compare results or choose corrective actions.',
                ],
                'example': 'A lab tracks first-pass certification results by game build and investigates why a newly introduced report format caused more failures.',
            },
            {
                'title': '1.6 Gambling Software Development Lifecycle',
                'summary': 'Gambling software moves through development and internal checks before formal independent or regulatory approval and release.',
                'points': [
                    'Build stages mature from initial development toward code completion, pre-certification, and a release candidate.',
                    'Internal quality assurance prepares and checks a product; an independent test lab evaluates it against applicable requirements.',
                    'A failed certification can require corrections, a new build, and repeated testing before release.',
                ],
                'example': 'A game that fails a jurisdictional rule check is corrected by its developer, then the revised release build is submitted for another certification test.',
            },
        ],
        'key_terms': [
            ('Independent test lab (ITL)', 'An independent organization that tests gambling products against requirements.'),
            ('Random number generator (RNG)', 'A mechanism used to produce values for chance-based outcomes.'),
            ('Progressive jackpot', 'A prize pool that can grow as qualifying play contributes to it.'),
            ('Jurisdiction', 'A region or authority whose rules govern gambling operations.'),
            ('Escape compliance defect', 'A compliance problem discovered after the intended testing or approval stage.'),
        ],
        'exam_tips': [
            'Match each gambling product type to the special conditions that its tests must consider.',
            'Distinguish internal pre-certification from independent certification activity.',
            'Remember that fairness, financial records, privacy, and jurisdiction rules can all be test concerns.',
        ],
    },
    {
        'number': 2,
        'title': 'The Gambling Industry Ecosystems',
        'minutes': 90,
        'intro': 'Gambling products operate within development, testing, operator, supplier, and regulator ecosystems.',
        'sections': [
            {
                'title': '2.1 Testing Phases within the Gambling Software Development Lifecycle',
                'summary': 'Different test activities occur at different lifecycle stages, from developer checks to compliance testing and approval.',
                'points': [
                    'Functional, integration, regression, and compliance checks address different questions and may occur at different phases.',
                    'Compliance testing determines whether a product satisfies applicable rules before it is accepted in a market.',
                    'Build identity and test evidence should remain clear as the product moves between teams and approval stages.',
                ],
                'example': 'A developer runs functional checks on a new game, then an internal team performs pre-certification checks before sending the identified build to an ITL.',
            },
            {
                'title': '2.2 The Gambling Ecosystem',
                'summary': 'The ecosystem connects game makers, platform and hardware suppliers, operators, payment services, test labs, and regulators.',
                'points': [
                    'Each participant has responsibilities and interfaces that can affect the final gambling service.',
                    'Video lottery terminals, slot machines, and lottery services have different system components and operational connections.',
                    'Testing must include interactions across relevant parties, platforms, and records rather than only the game software.',
                ],
                'example': 'A lottery purchase can involve a terminal, central lottery system, payment service, and draw service; an integration test follows the entry across all four.',
            },
        ],
        'key_terms': [
            ('Ecosystem', 'The organizations and systems that work together to provide a gambling service.'),
            ('Compliance testing', 'Testing that checks a product against applicable regulatory requirements.'),
            ('Video lottery terminal (VLT)', 'A player terminal connected to a lottery system for authorized games.'),
            ('Operator', 'An organization that runs gambling services for players.'),
        ],
        'exam_tips': [
            'Differentiate test phases by their purpose and the organizations involved.',
            'Follow a transaction through ecosystem interfaces to spot where integration evidence is needed.',
        ],
    },
    {
        'number': 3,
        'title': 'Testing in the Gambling Industry',
        'minutes': 435,
        'intro': 'Gambling testing covers game behavior, mathematics, platforms, casino systems, hardware, online services, and security.',
        'sections': [
            {
                'title': '3.1 Gambling and Wagering Testing',
                'summary': 'Functional and compliance tests check that games and wagers follow their rules and approved behavior.',
                'points': [
                    'Exercise wagering workflows, player interactions, game states, and common locations for defects.',
                    'Compliance checks compare game behavior and evidence with the requirements for the target jurisdiction.',
                    'Use approved game information, such as a par sheet, as a reference where applicable.',
                ],
                'example': 'A tester checks that a wager is debited once, the game result follows the approved rules, and the outcome is reflected in the player record.',
            },
            {
                'title': '3.2 Math Testing',
                'summary': 'Math testing checks the calculations and probability-related behavior that determine game outcomes and payouts.',
                'points': [
                    'Verify pay tables, payout calculations, game parameters, and expected relationships between wagers and results.',
                    'Use suitable statistical or mathematical analysis to check that implementation agrees with approved game specifications.',
                    'Investigate rounding, boundary values, and configuration changes that can affect payouts.',
                ],
                'example': 'A payout test covers a win on a pay-table boundary and confirms that the displayed prize matches the approved calculation.',
            },
            {
                'title': '3.3 Platform Testing',
                'summary': 'Platform tests check the software services and configurations that host or support gambling products.',
                'points': [
                    'Platform functional testing checks expected operation of services and interfaces.',
                    'Platform compliance testing checks platform controls and records against relevant requirements.',
                    'Include configuration, access, transaction processing, and reporting behaviors in the selected scope.',
                ],
                'example': 'A platform test verifies that only authorized staff can change a game configuration and that the change is logged.',
            },
            {
                'title': '3.4 Casino System Testing',
                'summary': 'Casino system testing checks how casino applications and connected services support play, accounting, and operational control.',
                'points': [
                    'Functional tests follow player, machine, and account activity through casino systems.',
                    'Compliance tests assess required records, controls, and reports for the casino system.',
                    'Check integration and reconciliation between machines, management systems, and financial records.',
                ],
                'example': 'A casino system test follows a machine payout into the floor-management system and confirms that accounting records match.',
            },
            {
                'title': '3.5 Protocol Testing',
                'summary': 'Protocol testing checks that connected gambling components exchange messages correctly and comply with interface rules.',
                'points': [
                    'Validate message structure, sequencing, values, acknowledgments, and error handling.',
                    'Test both expected messages and malformed, delayed, repeated, or out-of-order messages.',
                    'Where required, verify that protocol behavior also satisfies compliance constraints.',
                ],
                'example': 'A terminal sends a repeated wager message after a network delay; the receiving service must avoid creating a second wager.',
            },
            {
                'title': '3.6 Hardware Testing',
                'summary': 'Hardware testing checks physical gambling devices, their interfaces, and their integration with software.',
                'points': [
                    'Test controls, displays, printers, sensors, and other installed components for expected operation.',
                    'Compliance checks can cover physical controls, tamper evidence, and required device behavior.',
                    'Integration tests check that hardware events and software records remain aligned.',
                ],
                'example': 'A terminal test checks that a ticket printer reports an out-of-paper condition and that the system does not falsely mark the ticket as printed.',
            },
            {
                'title': '3.7 Remote Gambling Testing',
                'summary': 'Remote gambling tests cover play and transactions delivered to a player away from a casino floor.',
                'points': [
                    'Check account access, session behavior, wagering, result display, and financial processing across remote connections.',
                    'Exercise delays, interruptions, recovery, and device changes while preserving game and transaction state.',
                    'Verify that remote operation follows the applicable restrictions and records required by the service.',
                ],
                'example': 'A player loses connectivity during a wager; after reconnecting, the service must show the correct wager status without charging twice.',
            },
            {
                'title': '3.8 System and Network Security Testing',
                'summary': 'Security testing checks that gambling systems and their networks protect assets and meet applicable security requirements.',
                'points': [
                    'Review access controls, network boundaries, configuration, communications, and security monitoring.',
                    'Check both hardware and software controls against the threat and regulatory context.',
                    'Test that security failures are detected and do not permit unauthorized play, changes, or data access.',
                ],
                'example': 'A test attempts to alter a game configuration from an unauthorized network segment and verifies that access is denied and recorded.',
            },
            {
                'title': '3.9 Jackpot Controller Testing',
                'summary': 'Jackpot controller tests check the component that manages qualifying events and jackpot values across connected games.',
                'points': [
                    'Verify contribution calculations, displayed values, qualifying rules, and award processing.',
                    'Test communications and recovery so disruptions do not lose or duplicate contributions.',
                    'Check records and controls that support the integrity of jackpot operation.',
                ],
                'example': 'After a communication interruption, a test confirms that each qualifying wager contributes once to the jackpot total.',
            },
            {
                'title': '3.10 Online Gambling Testing',
                'summary': 'Online gambling combines game and account behavior with browsers, devices, networks, payments, and third-party services.',
                'points': [
                    'Test functional behavior, compatibility, accessibility, portability, interoperability, and performance as appropriate.',
                    'Check payment and backend transactions, interruption recovery, logs, and third-party dependencies.',
                    'Include time zones, date handling, messaging, application stability, and security in relevant scenarios.',
                ],
                'example': 'An online game test interrupts a payment-provider response and checks that the player sees a clear status while the account and transaction log remain consistent.',
            },
        ],
        'key_terms': [
            ('Par sheet', 'A game specification describing mathematical and payout-related characteristics.'),
            ('Protocol', 'Rules governing the format and exchange of messages between systems.'),
            ('Interoperability', 'The ability of different systems or components to work together.'),
            ('Jackpot controller', 'A system component that manages jackpot contributions and awards.'),
            ('Portability testing', 'Testing whether software works across different platforms or device types.'),
        ],
        'exam_tips': [
            'Match each test area to its target: game math, platform, casino system, protocol, hardware, or online service.',
            'Separate functional checks from compliance checks even when they examine the same product.',
            'Include failures and recovery in connected, remote, and online scenarios.',
            'Use the applicable game specification as the expected-result source for math testing.',
        ],
    },
    {
        'number': 4,
        'title': 'References',
        'minutes': 0,
        'intro': 'This reference chapter points learners to gambling regulators and standards that shape the industry. The syllabus assigns no training minutes to it.',
        'sections': [
            {
                'title': '4.1 Gambling Control Boards',
                'summary': 'Regulatory boards and inter-regional associations oversee or coordinate gambling requirements across jurisdictions.',
                'points': [
                    'A product may need approval from more than one authority when it is offered in multiple markets.',
                    'Requirements and oversight responsibilities vary by jurisdiction, so teams must identify the relevant authority.',
                    'Regulatory changes can affect certification scope and the evidence a product must provide.',
                ],
                'example': 'A casino game offered in two regions is checked against both regions’ approval requirements before distribution.',
            },
            {
                'title': '4.2 Standards',
                'summary': 'Industry standards provide requirements and guidance for gambling products, testing, and operational controls.',
                'points': [
                    'Select standards that apply to the product and target market rather than assuming one rule set covers all regions.',
                    'Use standards as sources for test conditions, compliance evidence, and approval planning.',
                    'Keep the version and jurisdiction of each applied standard clear in project records.',
                ],
                'example': 'A test plan records which regional game standard applies to a release and traces each required control to a test result.',
            },
        ],
        'key_terms': [
            ('Gambling control board', 'A regulatory body responsible for oversight in a gambling jurisdiction.'),
            ('Standard', 'A published set of requirements or guidance used to shape product or process expectations.'),
            ('Certification', 'Formal confirmation that a product meets specified requirements.'),
        ],
        'exam_tips': [
            'Check jurisdiction and applicable standard before interpreting a compliance requirement.',
            'Use this chapter as a reference source; the syllabus lists no dedicated training time for it.',
        ],
    },
]
