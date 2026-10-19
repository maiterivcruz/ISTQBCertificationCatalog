CHAPTERS = [
    {
        'number': 1,
        'title': 'Basic Concepts',
        'minutes': 200,
        'intro': 'Usability testing studies whether people can achieve their goals effectively, efficiently and satisfactorily in a defined context.',
        'sections': [
            {
                'title': '1.1 Fundamentals',
                'summary': 'Usability, user experience and accessibility describe related but distinct aspects of interaction with a product.',
                'points': [
                    'Usability concerns effectiveness, efficiency and satisfaction for specified users and goals.',
                    'User experience includes perceptions and responses before, during and after use.',
                    'Accessibility considers whether people with varied abilities can perceive, understand, navigate and interact with the product.',
                ],
                'example': 'A transit app may let most riders buy a ticket quickly, yet a screen-reader user cannot select a fare; the task is usable for some but not accessible to all.',
            },
            {
                'title': '1.2 Evaluating Usability, User Experience and Accessibility',
                'summary': 'Evaluation combines observation and measurement to understand how a product works for its intended users.',
                'points': [
                    'Use representative users, tasks and environments when evaluating interaction.',
                    'Combine qualitative evidence, such as user comments, with quantitative measures like completion or error rates.',
                    'Apply appropriate accessibility checks and interpret findings in the user’s context.',
                ],
                'example': 'A team observes older adults using a medicine app, measures successful refill completion, and notes that small text and unclear error messages cause repeated mistakes.',
            },
            {
                'title': '1.3 Usability Evaluation in Human-Centered Design',
                'summary': 'Human-centered design uses iterative evaluation to understand users and refine solutions around their needs.',
                'points': [
                    'Understand users, tasks and context before deciding what to build.',
                    'Create and evaluate prototypes early, then improve the design using evidence.',
                    'Repeat evaluation as the solution and user understanding develop.',
                ],
                'example': 'A library prototypes a self-checkout screen with patrons, learns that the return option is hard to find, changes the layout and tests the revised version.',
            },
        ],
        'key_terms': [
            ('Usability', 'How effectively, efficiently and satisfactorily specified users can achieve goals.'),
            ('User experience', 'People’s perceptions and responses arising from use or expected use.'),
            ('Accessibility', 'The extent to which people with varied abilities can use a product.'),
            ('Human-centered design', 'An iterative design approach grounded in users and their context.'),
            ('Effectiveness', 'Accuracy and completeness with which users achieve their goals.'),
        ],
        'exam_tips': [
            'Usability is evaluated for specified users, goals and context of use.',
            'Keep usability, user experience and accessibility related but distinct.',
            'Human-centered design evaluates and improves solutions iteratively.',
        ],
    },
    {
        'number': 2,
        'title': 'Risks in Usability, User Experience and Accessibility',
        'minutes': 80,
        'intro': 'Poor interaction can make users fail tasks, feel uncertain or be excluded, creating risks for people and organizations.',
        'sections': [
            {
                'title': '2.1 Introduction',
                'summary': 'Usability, experience and accessibility risks arise when product qualities do not fit users or their context.',
                'points': [
                    'Consider the likelihood and impact of users making errors, abandoning tasks or misunderstanding outcomes.',
                    'Include accessibility barriers and negative emotional responses in product risk analysis.',
                    'Prioritize risks by user harm, business importance and the frequency of the affected task.',
                ],
                'example': 'If customers cannot distinguish a successful payment from a pending one, some may pay twice and others may leave without completing an order.',
            },
            {
                'title': '2.2 Typical Risks',
                'summary': 'Common risks include confusing language, poor feedback, inaccessible controls and workflows that do not match user needs.',
                'points': [
                    'Look for mismatches between mental models, terminology, layout and actual system behavior.',
                    'Check that controls are perceivable and operable using varied devices and assistive technologies.',
                    'Consider context factors such as interruptions, lighting, time pressure and user experience.',
                ],
                'example': 'A booking page uses color alone to show selected seats; a color-blind customer may not see which seat is reserved and can select the wrong one.',
            },
        ],
        'key_terms': [
            ('Usability risk', 'The chance that interaction problems will harm task success or satisfaction.'),
            ('Mental model', 'A user’s understanding of how a system behaves.'),
            ('Assistive technology', 'Software or equipment that helps a person interact with a product.'),
            ('Context of use', 'The users, goals, tasks, equipment and environment involved in use.'),
        ],
        'exam_tips': [
            'Describe a risk in terms of affected users, task and consequence.',
            'Accessibility risks can be caused by design choices such as color-only cues.',
        ],
    },
    {
        'number': 3,
        'title': 'Usability and Accessibility Standards',
        'minutes': 105,
        'intro': 'Standards and guidelines provide reference points for designing and evaluating usable, inclusive products.',
        'sections': [
            {
                'title': '3.1 Usability Standards and Manufacturer Guidelines',
                'summary': 'Usability standards and platform guidance describe principles and practices that can inform evaluation.',
                'points': [
                    'Identify which standard or manufacturer guideline applies to the product and platform.',
                    'Use guidance to form review questions and testable expectations, not as a substitute for user evidence.',
                    'Consider the target users and context when interpreting compliance or deviations.',
                ],
                'example': 'A team checks a mobile checkout against platform guidance for navigation and touch controls, then verifies the flow with representative shoppers.',
            },
            {
                'title': '3.2 Accessibility Standards',
                'summary': 'Accessibility standards describe criteria that help people with disabilities use digital products.',
                'points': [
                    'Check applicable criteria for perceivable content, operable controls, understandable interaction and robust technology support.',
                    'Combine automated checks with manual evaluation and assistive-technology use.',
                    'Test the actual user journey because isolated criterion checks may miss barriers between screens.',
                ],
                'example': 'A registration flow passes an automated contrast check but still fails a keyboard user because focus disappears after an error; a manual journey test finds the issue.',
            },
        ],
        'key_terms': [
            ('Accessibility criterion', 'A stated condition intended to improve access for people with disabilities.'),
            ('Guideline', 'Advice that helps shape or evaluate product design.'),
            ('Assistive technology', 'Technology that enables or supports access to digital content.'),
            ('Manual evaluation', 'Human examination of behavior that automation may not assess reliably.'),
        ],
        'exam_tips': [
            'Use standards as a useful test basis, but check real user journeys too.',
            'Automated accessibility checks cannot replace manual and assistive-technology evaluation.',
        ],
    },
    {
        'number': 4,
        'title': 'Usability Reviews',
        'minutes': 90,
        'intro': 'Usability reviews inspect designs and work products to find interaction problems before or alongside user testing.',
        'sections': [
            {
                'title': '4.1 Introduction and Approach',
                'summary': 'A review compares a product or design with user needs, usability principles and relevant standards.',
                'points': [
                    'Define review scope, criteria, participants and the work product to inspect.',
                    'Use checklists or heuristics to structure the review while recording concrete evidence.',
                    'Prioritize findings by user impact and make recommendations that can be evaluated.',
                ],
                'example': 'Before a patient portal is built, reviewers inspect a prototype using common usability principles and identify that the sign-out option is hard to find.',
            },
            {
                'title': '4.2 Types of Usability Review',
                'summary': 'Reviews may use expert inspection, heuristic evaluation, checklist assessment or walkthroughs.',
                'points': [
                    'Choose the review type based on the available artifact, expertise, time and questions.',
                    'Heuristic evaluation examines designs against usability principles; walkthroughs follow user tasks step by step.',
                    'Reviews efficiently find many issues but do not fully predict how actual users will behave.',
                ],
                'example': 'An expert walks through an online tax form as a first-time filer and notes where instructions do not explain required evidence.',
            },
        ],
        'key_terms': [
            ('Usability review', 'An inspection of a product or design for interaction problems.'),
            ('Heuristic evaluation', 'An expert review using a set of usability principles.'),
            ('Walkthrough', 'A step-by-step inspection of a user task through an interface.'),
            ('Checklist', 'A structured list of items to consider during evaluation.'),
        ],
        'exam_tips': [
            'Select review methods based on artifact and evaluation goal.',
            'Reviews reveal issues early but do not replace observing representative users.',
        ],
    },
    {
        'number': 5,
        'title': 'Usability Testing',
        'minutes': 270,
        'intro': 'Usability testing observes representative participants doing realistic tasks and uses the evidence to improve the product.',
        'sections': [
            {
                'title': '5.1 Introduction',
                'summary': 'A usability test gathers evidence about how users interact with a product in a chosen context.',
                'points': [
                    'Define the research questions, target users, tasks and environment before recruiting participants.',
                    'Observe behavior and outcomes without steering users toward the expected path.',
                    'Protect participant privacy and explain consent and recording arrangements.',
                ],
                'example': 'A team asks new customers to create an account and records where they pause, make mistakes or ask for help.',
            },
            {
                'title': '5.2 Step-By-Step Approach to Usability Testing',
                'summary': 'A systematic approach moves from planning and preparation through sessions, analysis and reporting.',
                'points': [
                    'Set objectives, design tasks, recruit participants and prepare the test environment.',
                    'Conduct sessions consistently while allowing natural user behavior.',
                    'Analyze observations, prioritize findings and share recommendations with stakeholders.',
                ],
                'example': 'For a travel site, the team prepares a hotel-search task, observes each participant using the same starting conditions, then groups repeated booking errors into findings.',
            },
            {
                'title': '5.3 Prepare Usability Test',
                'summary': 'Preparation ensures the tasks, participants, setting and materials support the evaluation goal.',
                'points': [
                    'Recruit people who reflect the intended users and relevant experience levels.',
                    'Write neutral task scenarios and prepare consent, notes, equipment and test data.',
                    'Pilot the session to catch confusing instructions or technical problems.',
                ],
                'example': 'Before testing a grocery app, the moderator pilots the task “order ingredients for dinner” to ensure the test account contains suitable products and no hidden setup issue.',
            },
            {
                'title': '5.4 Conduct Usability Test Sessions',
                'summary': 'A session should create a comfortable setting and collect observations without biasing participants.',
                'points': [
                    'Welcome participants, explain the session and distinguish testing the product from testing the person.',
                    'Use neutral prompts and avoid teaching the interface while observing task behavior.',
                    'Record actions, errors, comments and task outcomes consistently.',
                ],
                'example': 'When a participant cannot find the refund option, the moderator waits and observes rather than pointing to the menu, then notes the hesitation and workaround.',
            },
            {
                'title': '5.5 Analysis of Findings',
                'summary': 'Analysis turns observations into findings about user impact and likely design causes.',
                'points': [
                    'Review notes, recordings and measures across participants for patterns and differences.',
                    'Separate direct observation from interpretation and link findings to test objectives.',
                    'Prioritize by severity, frequency and consequence for users.',
                ],
                'example': 'Several users miss a required delivery choice; the team distinguishes the observed missed field from the hypothesis that its placement caused the problem.',
            },
            {
                'title': '5.6 Communicate Results and Findings',
                'summary': 'Results should help stakeholders understand what happened and decide what to improve.',
                'points': [
                    'Report objectives, participants, tasks, methods, limitations and evidence.',
                    'Explain user impact in clear language and provide actionable recommendations.',
                    'Use concise clips or examples when appropriate, with participant privacy protected.',
                ],
                'example': 'A report pairs a short anonymized clip of a failed password reset with the task-success rate and a recommendation to clarify the recovery steps.',
            },
            {
                'title': '5.7 Quality Control of a Usability Test',
                'summary': 'Quality control checks that the study is consistent, ethical and strong enough to support its conclusions.',
                'points': [
                    'Use clear procedures, trained moderators and a pilot to reduce avoidable variation.',
                    'Check that participant selection and task wording fit the research question.',
                    'State limitations and avoid generalizing beyond the evidence collected.',
                ],
                'example': 'A usability study with only expert users reports that limitation rather than claiming the workflow is easy for new customers.',
            },
            {
                'title': '5.8 Challenges and Frequent Mistakes',
                'summary': 'Poorly designed sessions can bias results or confuse participant difficulty with a study problem.',
                'points': [
                    'Avoid leading questions, coaching, unrealistic tasks and unrepresentative participants.',
                    'Do not treat a small qualitative study as a statistical estimate of all users.',
                    'Check technology and test data so equipment failures are not mistaken for usability problems.',
                ],
                'example': 'A moderator who asks “Was the green button easy to see?” may bias feedback; an open prompt such as “What would you do next?” gives less leading evidence.',
            },
        ],
        'key_terms': [
            ('Usability test', 'A study observing users performing tasks with a product.'),
            ('Participant', 'A person who takes part in a usability evaluation.'),
            ('Moderator', 'The person who guides a session while minimizing influence on behavior.'),
            ('Task scenario', 'A description that asks a participant to achieve a realistic goal.'),
            ('Finding', 'An evidence-based observation about a usability issue or success.'),
            ('Pilot test', 'A trial session used to check and refine the study procedure.'),
        ],
        'exam_tips': [
            'Recruit participants who match the intended user group and context.',
            'Use neutral prompts and distinguish observed behavior from interpretation.',
            'Report study limitations; small usability studies are not automatically statistically representative.',
        ],
    },
    {
        'number': 6,
        'title': 'User Surveys',
        'minutes': 30,
        'intro': 'Surveys gather users’ stated opinions and experiences through carefully designed questions.',
        'sections': [
            {
                'title': '6.1 Introduction',
                'summary': 'A survey can collect attitudes, preferences and self-reported experience from a group of users.',
                'points': [
                    'Choose a survey when the question concerns reported opinion or experience rather than observed task behavior.',
                    'Define the target respondents, sampling approach and intended use of the answers.',
                    'Protect privacy and make questions understandable and unbiased.',
                ],
                'example': 'After a library app redesign, a survey asks visitors how confident they feel about renewing a book, while session observation checks whether they can actually complete the renewal.',
            },
            {
                'title': '6.2 Step-By-Step Approach to User Surveys',
                'summary': 'Survey work includes defining questions, selecting respondents, piloting, collecting and analyzing answers.',
                'points': [
                    'Set a clear objective and use concise, neutral questions with suitable response options.',
                    'Pilot the questionnaire and distribute it to the intended population.',
                    'Analyze response patterns and non-response limits before making claims.',
                ],
                'example': 'A transport team pilots a short satisfaction questionnaire with several riders, revises an ambiguous scale and then sends it to passengers after a completed journey.',
            },
            {
                'title': '6.3 Standardized Questionnaires',
                'summary': 'Standard questionnaires use established questions and scoring to support comparable measurements.',
                'points': [
                    'Choose an instrument that matches the construct and target population.',
                    'Follow its wording, administration and scoring guidance to preserve comparability.',
                    'Interpret scores alongside context and other usability evidence.',
                ],
                'example': 'A team uses a recognized usability questionnaire after participants complete the same task set, then compares the score with observed completion problems.',
            },
        ],
        'key_terms': [
            ('Survey', 'A method for collecting respondents’ answers to structured questions.'),
            ('Questionnaire', 'A set of questions used to gather information from respondents.'),
            ('Response bias', 'A pattern in answers caused by question wording or respondent behavior.'),
            ('Standardized questionnaire', 'An instrument with established wording and scoring guidance.'),
        ],
        'exam_tips': [
            'Surveys measure what people report, which may differ from observed behavior.',
            'Pilot questions and use standardized scoring as instructed.',
        ],
    },
    {
        'number': 7,
        'title': 'Selecting Appropriate Methods',
        'minutes': 40,
        'intro': 'Method selection depends on the question, lifecycle stage, people, resources and type of evidence required.',
        'sections': [
            {
                'title': '7.1 Criteria for Selecting a Method',
                'summary': 'A suitable evaluation method balances the goal, user access, product maturity, time and needed evidence.',
                'points': [
                    'Choose observation, review, survey or another method according to the question being answered.',
                    'Consider prototype maturity, participant availability, risk, cost and environmental realism.',
                    'Combine methods when one source of evidence leaves important uncertainty.',
                ],
                'example': 'A team uses an expert review on an early wireframe, then schedules task-based testing with customers when a working prototype is ready.',
            },
        ],
        'key_terms': [
            ('Evaluation method', 'A way to collect evidence about usability, experience or accessibility.'),
            ('Research question', 'A question that defines what an evaluation needs to learn.'),
            ('Evidence', 'Information used to support an evaluation conclusion.'),
        ],
        'exam_tips': [
            'Select methods by objective and product maturity, not by habit.',
            'Use complementary methods when review, observation or survey evidence alone is insufficient.',
        ],
    },
    {
        'number': 8,
        'title': 'Summary of Roles and Responsibilities',
        'minutes': 30,
        'intro': 'A well-run study depends on clear responsibilities for facilitation, observation, analysis and decision making.',
        'sections': [
            {
                'title': '8.1 Usability Tester',
                'summary': 'The usability tester plans the study, protects its quality and turns evidence into useful findings.',
                'points': [
                    'Define objectives, tasks and methods, and ensure the study is conducted responsibly.',
                    'Analyze evidence carefully and communicate findings and limitations.',
                    'Work with designers and product stakeholders while maintaining an evidence-based perspective.',
                ],
                'example': 'A usability tester prepares tasks for a new claims portal, reviews session notes and presents the most harmful user obstacles with supporting evidence.',
            },
            {
                'title': '8.2 Moderator and Note-Taker',
                'summary': 'The moderator guides participants while the note-taker captures behavior and context for later analysis.',
                'points': [
                    'The moderator welcomes participants, gives neutral instructions and avoids coaching their actions.',
                    'The note-taker records observable actions, comments, timing and problems consistently.',
                    'The roles coordinate before and after sessions while respecting participant privacy.',
                ],
                'example': 'During a mobile checkout session, the moderator gives the task and stays neutral while the note-taker records where the participant hesitates and which error message appears.',
            },
        ],
        'key_terms': [
            ('Usability tester', 'A practitioner who designs, conducts or analyzes usability evaluation.'),
            ('Moderator', 'A facilitator who guides a participant through a research session.'),
            ('Note-taker', 'A person who records observations during a session.'),
            ('Stakeholder', 'A person or group affected by or able to influence the product.'),
        ],
        'exam_tips': [
            'The moderator facilitates neutrally; the note-taker records observable evidence.',
            'Make roles and responsibilities clear before sessions begin.',
        ],
    },
]
