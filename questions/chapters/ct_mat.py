"""Plain-language study chapters for ISTQB Mobile Application Testing."""

CHAPTERS = [
    {
        'number': 1,
        'title': 'Mobile World: Business and Technology Drivers',
        'minutes': 175,
        'intro': 'Understand what makes mobile products and their testing context different from desktop or web-only software.',
        'sections': [
            {
                'title': '1.1-1.2 Mobile analytics and business models',
                'summary': 'Mobile apps operate in a competitive, data-rich market. Usage analytics and the app’s business model influence product goals, user expectations, and test priorities.',
                'points': [
                    'Analytics can reveal usage patterns, retention, and problems, but measures need clear meaning and suitable privacy controls.',
                    'Apps may earn revenue through purchases, subscriptions, advertising, or supporting a larger service.',
                    'Consider business goals alongside usability, availability, performance, and user trust.',
                ],
                'example': 'A subscription fitness app tracks failed sign-ups and cancellation rates to prioritize testing of account renewal and payment flows.',
            },
            {
                'title': '1.3-1.5 Devices, applications, and architecture',
                'summary': 'Mobile applications run across varied devices, platforms, and architectures. These differences affect compatibility, connectivity, and the boundaries that should be tested.',
                'points': [
                    'Device variation includes screen size, hardware capabilities, operating system, and available resources.',
                    'Native, web, and hybrid apps differ in how they use platform features and how they are delivered.',
                    'A mobile app may include a client, network services, and backend systems; tests should cover their interactions.',
                ],
                'example': 'A food-delivery service tests its native app on several screen sizes and checks that orders remain correct when the mobile network briefly drops.',
            },
            {
                'title': '1.6-1.8 Mobile test strategy, challenges, and risks',
                'summary': 'A mobile strategy selects representative devices, platforms, and real-world conditions while accounting for rapid change and limited test resources.',
                'points': [
                    'Prioritize platform and device combinations using usage, business risk, and technical diversity.',
                    'Consider interruptions, unstable networks, battery use, permissions, and app-store policies.',
                    'Balance physical-device coverage with emulators and simulators, recognizing the limits of each.',
                    'Plan for risks such as fragmentation, privacy exposure, and dependence on third-party services.',
                ],
                'example': 'A transit app team prioritizes phones used by most riders but also tests low-connectivity journeys because service disruptions are a key user risk.',
            },
        ],
        'key_terms': [
            ('Mobile analytics', 'Usage data and measures used to understand how a mobile product is used.'),
            ('Native application', 'An app built for a particular mobile platform and its capabilities.'),
            ('Hybrid application', 'An app combining web technologies with native platform integration.'),
            ('Device fragmentation', 'Variation in devices, operating systems, and configurations that complicates compatibility.'),
        ],
        'exam_tips': [
            'Tie device coverage to user data, risk, and platform differences rather than attempting every possible combination.',
            'Distinguish app types by their implementation and implications for accessing device features.',
        ],
    },
    {
        'number': 2,
        'title': 'Mobile Application Test Types',
        'minutes': 265,
        'intro': 'Check how apps interact with device hardware, operating system services, and changing connectivity.',
        'sections': [
            {
                'title': '2.1 Compatibility with device hardware',
                'summary': 'Hardware behavior can vary substantially across mobile devices. Test the features the app relies on and the ways users interact with them.',
                'points': [
                    'Check camera, location, sensors, input methods, display behavior, and screen orientation where they affect the app.',
                    'Assess interruptions such as calls, notifications, and low-power states during important user journeys.',
                    'Verify permission grants and denials, plus power use and behavior under device temperature conditions.',
                    'Select representative hardware configurations based on risk and actual users.',
                ],
                'example': 'A photo-sharing app is tested while a call arrives during upload and after the user denies camera access.',
            },
            {
                'title': '2.2 Interactions with device software and other apps',
                'summary': 'Mobile operating systems provide preferences, notifications, shortcuts, and app lifecycle behavior that can change how an app works.',
                'points': [
                    'Test notifications, quick-access links, and user preferences supplied by the operating system.',
                    'Check compatibility across relevant operating system versions and platform types.',
                    'Evaluate coexistence with other apps, including resource contention and handling of shared links or files.',
                    'Verify app behavior when it is backgrounded, resumed, or removed from memory.',
                ],
                'example': 'A calendar app checks that a reminder opens the correct event from a lock-screen notification on supported operating system versions.',
            },
            {
                'title': '2.3 Connectivity methods',
                'summary': 'Mobile users move between networks and may lose connectivity entirely. Tests should cover transitions and their impact on saved work and service responses.',
                'points': [
                    'Exercise supported network types and changes between them.',
                    'Test slow, intermittent, and unavailable connections, including recovery after service resumes.',
                    'Check that retries do not duplicate transactions and that users receive understandable status.',
                ],
                'example': 'A ticket app loses connectivity after payment submission and verifies that reconnecting does not charge the customer twice.',
            },
        ],
        'key_terms': [
            ('Interruption testing', 'Testing app behavior when another event temporarily disrupts its current activity.'),
            ('Permission', 'An operating-system-controlled grant to access a device capability or user data.'),
            ('Coexistence', 'The ability of an app to operate alongside other installed apps.'),
            ('Connectivity transition', 'A change in network availability or network type during app use.'),
        ],
        'exam_tips': [
            'Map each device feature to a user-visible risk, including denied permissions and interruptions.',
            'Connectivity testing includes recovery and duplicate-action handling, not only a successful online path.',
            'Emulators and simulators do not reproduce every physical hardware condition.',
        ],
    },
    {
        'number': 3,
        'title': 'Common Test Types and Test Process for Mobile Applications',
        'minutes': 200,
        'intro': 'Apply broad software test types, mobile-specific test levels, and experience-based techniques to a mobile context.',
        'sections': [
            {
                'title': '3.1 Common mobile test types',
                'summary': 'Mobile products need familiar quality testing adapted to installation, device constraints, and diverse users.',
                'points': [
                    'Installability and upgrade tests cover install, update, removal, and recovery behavior.',
                    'Assess performance, stress, security, usability, accessibility, and database behavior according to risk.',
                    'Globalization and localization tests check language, formats, and region-specific expectations.',
                    'Select test types based on product goals and likely failure impact.',
                ],
                'example': 'A banking app is checked for screen-reader access, locale-specific currency formatting, and safe behavior during a large transaction load.',
            },
            {
                'title': '3.2 Field, store, and post-release testing',
                'summary': 'Some mobile behavior is best evaluated outside a controlled lab. Store review and real-world use can reveal issues that pre-release environments miss.',
                'points': [
                    'Field testing observes the app in the devices, places, and conditions where people use it.',
                    'Check platform and app-store approval requirements before submitting a release.',
                    'Plan post-release testing and monitoring to detect issues after deployment.',
                ],
                'example': 'A map app is field-tested in underground stations where location accuracy and network access differ from the office test lab.',
            },
            {
                'title': '3.3-3.4 Experience-based techniques and process',
                'summary': 'Experience-based techniques help testers explore mobile risks that are hard to specify as scripts. Session management keeps exploratory work focused and reportable.',
                'points': [
                    'Personas and mnemonics help organize user perspectives and areas to investigate.',
                    'Heuristics provide prompts for evaluating qualities such as usability and compatibility.',
                    'Tours guide exploration along a theme or user journey; session-based test management records charter, time, and findings.',
                    'Adapt the test process and approach to release cadence, risk, and the mobile product context.',
                ],
                'example': 'A tester takes a “new user” tour of a banking app, recording confusing identity checks and the exact device conditions in a time-boxed session.',
            },
        ],
        'key_terms': [
            ('Installability testing', 'Testing installation, upgrades, and removal of an application.'),
            ('Field testing', 'Testing in real-world settings and conditions.'),
            ('Heuristic', 'A practical rule or prompt used to guide evaluation or exploration.'),
            ('Tour', 'A themed path through an application used to guide exploratory testing.'),
            ('Session-based test management', 'A structured approach to chartering and recording exploratory test sessions.'),
        ],
        'exam_tips': [
            'Distinguish field testing from a lab-based test and consider what real-world conditions it can reveal.',
            'Match experience-based techniques to their role: personas frame users, heuristics prompt evaluation, and tours guide exploration.',
        ],
    },
    {
        'number': 4,
        'title': 'Mobile Application Platforms, Tools, and Environment',
        'minutes': 80,
        'intro': 'Choose development and test environments that represent the app’s supported platforms and devices.',
        'sections': [
            {
                'title': '4.1-4.2 Development platforms and tools',
                'summary': 'Development platforms and their tools shape how an app is built, integrated, and tested. Testers need enough awareness to understand platform-specific behavior and constraints.',
                'points': [
                    'Identify the mobile platforms and toolchains used by the application.',
                    'Use platform tools to inspect logs, configuration, and app behavior where appropriate.',
                    'Include development and service dependencies in environment planning.',
                ],
                'example': 'A tester uses platform logs to diagnose why a location permission prompt appears differently after an operating system update.',
            },
            {
                'title': '4.3-4.4 Emulators, simulators, and test labs',
                'summary': 'Emulators and simulators provide convenient coverage, while physical devices expose hardware and operating-system behavior that virtual tools may not reproduce.',
                'points': [
                    'Use virtual devices for rapid checks across configurations and repeatable scenarios.',
                    'Validate hardware-dependent behavior on suitable real devices.',
                    'Design a test lab around supported platforms, device diversity, connectivity, and maintenance needs.',
                ],
                'example': 'A team uses simulators for routine layout regression and physical phones to verify vibration, camera focus, and battery impact.',
            },
        ],
        'key_terms': [
            ('Emulator', 'Software that imitates a device or platform environment.'),
            ('Simulator', 'A virtual environment that models selected aspects of a device or platform.'),
            ('Test lab', 'A managed set of devices, tools, and environments used for testing.'),
        ],
        'exam_tips': [
            'Choose between virtual and physical devices based on what behavior must be observed.',
            'A test lab needs ongoing management of devices, versions, and configurations.',
        ],
    },
    {
        'number': 5,
        'title': 'Automating the Test Execution',
        'minutes': 55,
        'intro': 'Decide what mobile tests to automate and how to evaluate the supporting tools and lab.',
        'sections': [
            {
                'title': '5.1-5.2 Automation approaches and methods',
                'summary': 'Mobile test automation can speed repeatable checks, but device variation and frequent interface changes affect its cost and stability.',
                'points': [
                    'Select tests with repeatable setup, clear outcomes, and sufficient expected value.',
                    'Choose methods that fit the app architecture and supported platforms.',
                    'Keep human exploratory testing for changing or judgment-heavy behavior.',
                ],
                'example': 'A travel team automates repeatable sign-in and booking checks while testers explore new itinerary features across real devices.',
            },
            {
                'title': '5.3-5.4 Tools and automation test labs',
                'summary': 'Automation tools should be evaluated against project needs, platform coverage, integration, maintainability, and total cost. The device lab is part of the automation solution.',
                'points': [
                    'Assess tool compatibility, reliability, reporting, support, and required skills.',
                    'Plan device selection, provisioning, connectivity, and upkeep for an automated lab.',
                    'Track maintenance effort and review whether automation continues to provide useful feedback.',
                ],
                'example': 'A team compares two device-farm options using its supported operating systems, parallel-run needs, and the effort required to diagnose failed tests.',
            },
        ],
        'key_terms': [
            ('Test automation', 'Use of software to perform or support testing activities.'),
            ('Automation tool evaluation', 'Assessment of a tool against technical, operational, and project needs.'),
            ('Automation test lab', 'Devices and services arranged to run automated mobile checks.'),
        ],
        'exam_tips': [
            'Automate based on repeatability and value, not simply because a test can be scripted.',
            'Include device lab and maintenance costs when evaluating an automation approach.',
        ],
    },
]
