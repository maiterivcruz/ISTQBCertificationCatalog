"""CTFL v4.0 study chapters. Plain-language summaries with real-world examples.

Schema per chapter: number, title, minutes, intro, sections[], key_terms[(term, meaning)], exam_tips[].
Schema per section: title, summary, points[], example (optional).
"""

CHAPTERS = [
    # ------------------------------------------------------------------ 1
    {
        'number': 1,
        'title': 'Fundamentals of Testing',
        'minutes': 180,
        'intro': 'The big picture: what testing is, why we do it, and the habits '
                 'every good tester shares.',
        'sections': [
            {
                'title': '1.1 What is testing?',
                'summary': 'Testing is a set of activities to find defects and to check that the software '
                           'does what people need. It includes running the software (dynamic testing) '
                           'and examining it without running it (static testing, such as reviews).',
                'points': [
                    'Typical objectives: find failures, build confidence, provide information for decisions, '
                    'prevent defects, check requirements are met, reduce risk.',
                    'Testing is not debugging. Testing shows a failure; debugging finds and fixes its cause.',
                    'Confirmation testing then checks the fix worked.',
                ],
                'example': 'A tester enters an order for 0 items in an online shop and the order is accepted. '
                           'That is the test showing a failure. The developer then tracks down the faulty '
                           'code and fixes it. That is debugging.',
            },
            {
                'title': '1.2 Why is testing necessary?',
                'summary': 'Testing reduces the risk of failures in production. It is part of quality '
                           'management, but testing alone is not quality assurance (QA). QA is about '
                           'preventing problems through good processes.',
                'points': [
                    'Error (mistake): a human action that produces a wrong result.',
                    'Defect (bug, fault): the flaw in the work product caused by the error.',
                    'Failure: the visible wrong behaviour when the defect is executed.',
                    'Root cause: the earliest reason the error happened, such as time pressure or unclear '
                    'requirements. Finding it helps prevent the same defects again.',
                    'Not every defect leads to a failure. Some are never triggered.',
                ],
                'example': 'A developer, rushed and tired, writes <code>price * quantity - discount</code> '
                           'instead of subtracting the discount per item (error). The wrong formula sits in the '
                           'code (defect). A customer buying 10 items is overcharged (failure). The root cause '
                           'was an ambiguous requirement and deadline pressure.',
            },
            {
                'title': '1.3 Seven testing principles',
                'summary': 'Seven ideas that guide good testing in any project.',
                'points': [
                    '1. Testing shows the presence, not the absence, of defects. Passing tests never prove '
                    'there are no bugs.',
                    '2. Exhaustive testing is impossible. Use risk and priorities to choose what to test.',
                    '3. Early testing saves time and money (shift-left).',
                    '4. Defects cluster together. A few modules usually hold most of the bugs.',
                    '5. Tests wear out (pesticide paradox). Repeating the same tests stops finding new '
                    'bugs, so update them.',
                    '6. Testing is context dependent. A pacemaker and a game are tested differently.',
                    '7. Absence-of-defects fallacy. A bug-free system that does not meet user needs is still a failure.',
                ],
                'example': 'A bank finds 60% of bugs in the payments module. Following principle 4, the team '
                           'adds more testing there. Following principle 5, they rewrite old payment tests '
                           'every release so they keep finding new problems.',
            },
            {
                'title': '1.4 Test activities, testware and roles',
                'summary': 'Testing follows a flexible process. The exact steps depend on the project.',
                'points': [
                    'Test planning: define objectives and approach.',
                    'Test monitoring and control: compare progress to the plan and adjust.',
                    'Test analysis: decide <em>what</em> to test (test conditions).',
                    'Test design: decide <em>how</em> to test it (test cases).',
                    'Test implementation: prepare data, environments and test procedures.',
                    'Test execution: run tests and compare actual to expected results.',
                    'Test completion: archive testware, report, and collect lessons learned.',
                    'Testware = everything produced (plans, cases, data, reports). Traceability links '
                    'requirements to tests and results.',
                    'Two roles: test management (plan and control) and testing (analysis, design, '
                    'execution). One person can hold both.',
                ],
                'example': None,
                'examples': [
                    {
                        'title': 'Test planning: concert ticket-booking app',
                        'body': 'Before the release, the test manager decides:<ul>'
                                '<li>Objective: no double-booked seats and no payment errors.</li>'
                                '<li>Scope: booking and payment are in, the "about us" page is out.</li>'
                                '<li>Approach: automated regression plus exploratory testing of payments.</li>'
                                '<li>Exit criteria: no open critical bugs, 95% of planned tests passed.</li></ul>',
                    },
                    {
                        'title': 'Test monitoring and control: halfway through the sprint',
                        'body': 'Monitoring: only 40% of planned tests have run, and 5 critical bugs are open.<br>'
                                'Control: the team moves a tester from low-risk screens to payment testing and '
                                'asks developers to fix the critical bugs first.',
                    },
                    {
                        'title': 'Test analysis: what to test',
                        'body': 'Requirement: "A seat can only be booked once." Analysis turns it into test conditions:<ul>'
                                '<li>Two users book the same seat at the same time.</li>'
                                '<li>A user books a seat that was just released.</li>'
                                '<li>A booking times out and the seat becomes free again.</li></ul>'
                                'It also reveals a gap: what happens when the payment fails after the seat is held?',
                    },
                    {
                        'title': 'Test design: how to test it',
                        'body': 'Condition: two users book the same seat.'
                                '<table class="example-table"><thead><tr><th>Step</th><th>Input / action</th>'
                                '<th>Expected result</th></tr></thead><tbody>'
                                '<tr><td>1</td><td>User A selects seat 12A and pays</td><td>Booking confirmed</td></tr>'
                                '<tr><td>2</td><td>User B selects seat 12A</td><td>Seat shown as unavailable</td></tr>'
                                '</tbody></table>',
                    },
                    {
                        'title': 'Test implementation: getting ready to run',
                        'body': '<ul><li>Create two test accounts and a test event with seat 12A free.</li>'
                                '<li>Set up a test payment gateway (no real money).</li>'
                                '<li>Order the tests: booking first, then cancellation, then refunds.</li>'
                                '<li>Automate the repeatable ones in the CI pipeline.</li></ul>',
                    },
                    {
                        'title': 'Test execution: run and compare',
                        'body': 'The tester runs the double-booking test. Expected: User B is refused. '
                                'Actual: User B also gets a confirmation.<br>'
                                'The result is logged as a <strong>failure</strong> and a defect report is raised: '
                                '"Seat 12A can be booked twice". After the fix, the same test is rerun '
                                '(confirmation testing).',
                    },
                    {
                        'title': 'Test completion: wrap up',
                        'body': '<ul><li>Close or defer the open defects and record the decision.</li>'
                                '<li>Archive test cases, data and environment setup for the next release.</li>'
                                '<li>Write the test completion report: what was tested, what passed, known risks.</li>'
                                '<li>Hold a retrospective: "unclear payment requirements caused late bugs, so '
                                'involve testers in refinement."</li></ul>',
                    },
                    {
                        'title': 'Testware and traceability',
                        'body': 'Testware here: the plan, the test cases, the test data, the logs and the defect reports.'
                                '<table class="example-table"><thead><tr><th>Requirement</th><th>Test case</th>'
                                '<th>Result</th><th>Defect</th></tr></thead><tbody>'
                                '<tr><td>REQ-12 Seat booked once</td><td>TC-045</td><td>Failed, then passed</td>'
                                '<td>BUG-231</td></tr></tbody></table>'
                                'If REQ-12 changes, traceability shows exactly which tests to update.',
                    },
                    {
                        'title': 'Roles: test management and testing',
                        'body': '<ul><li><strong>Test manager:</strong> writes the plan, tracks progress, '
                                'reports to stakeholders.</li>'
                                '<li><strong>Tester:</strong> analyses, designs and executes tests, and reports defects.</li>'
                                '<li>In a small Agile team, one person often does both.</li></ul>',
                    },
                ],
            },
            {
                'title': '1.5 Essential skills and good practices',
                'summary': 'Good testers combine technical, social and thinking skills.',
                'points': [
                    'Skills: testing knowledge, thoroughness, curiosity, communication, critical thinking, '
                    'technical and domain knowledge.',
                    'Whole-team approach: everyone shares responsibility for quality, and testers, developers '
                    'and business people work together.',
                    'Independence of testing: testers who are not the authors find different bugs and are '
                    'less biased, but may be isolated. Independence is a benefit, not a replacement for '
                    'developer testing.',
                ],
                'example': 'When reporting a defect, say "the total shows 90 instead of 100 when two coupons '
                           'are applied", not "your code is wrong". Facts keep communication constructive.',
            },
        ],
        'key_terms': [
            ('Defect', 'A flaw in a work product that can cause a failure.'),
            ('Failure', 'An event where the system does not do what is expected.'),
            ('Root cause', 'The fundamental reason a defect was introduced.'),
            ('Test condition', 'Something that could be tested (a feature or behaviour).'),
            ('Testware', 'Work products created during the test process.'),
            ('Traceability', 'Links between test basis, tests and results.'),
        ],
        'exam_tips': [
            'Know the difference between error, defect and failure.',
            'Be able to match each of the 7 principles to a short scenario.',
            'Remember: test analysis = what, test design = how.',
        ],
    },
    # ------------------------------------------------------------------ 2
    {
        'number': 2,
        'title': 'Testing Throughout the Software Development Lifecycle',
        'minutes': 130,
        'intro': 'How testing fits into different ways of building software, and the levels '
                 'and types of testing you will meet.',
        'sections': [
            {
                'title': '2.1 Testing in the context of an SDLC',
                'summary': 'The way a team builds software (sequential, iterative, Agile) shapes how and '
                           'when it tests. Good testing practices apply in every model.',
                'points': [
                    'Every development activity should have a matching test activity.',
                    'Each test level has its own objectives.',
                    'Test analysis and design start during development, not after it.',
                    'Testers review work products as soon as drafts exist.',
                    'Test-driven development (TDD): write automated tests first, then code to pass them.',
                    'Acceptance test-driven development (ATDD): derive tests from acceptance criteria '
                    'before coding.',
                    'Behavior-driven development (BDD): write behaviour as Given/When/Then examples.',
                    'DevOps: automated pipelines with continuous integration and delivery give fast feedback. '
                    'Risk: it needs good automation and monitoring.',
                    'Shift-left: test earlier (reviews, unit tests) to find defects cheaper.',
                    'Retrospectives: regular meetings to learn and improve the process.',
                ],
                'example': None,
                'examples': [
                    {
                        'title': 'Matching test and development activities: V-model vs Agile',
                        'body': '<table class="example-table"><thead><tr><th>Model</th><th>How testing fits</th></tr></thead><tbody>'
                                '<tr><td>Sequential (V-model)</td><td>Requirements are reviewed first, system tests are '
                                'planned while design is written, and tests run in stages after coding.</td></tr>'
                                '<tr><td>Agile</td><td>Every 2-week sprint includes analysis, coding and testing of '
                                'small user stories, so testing never waits for the end.</td></tr></tbody></table>',
                    },
                    {
                        'title': 'Each test level has its own objective: a bank transfer feature',
                        'body': '<ul><li>Unit level: does <code>calculateFee()</code> return the right fee?</li>'
                                '<li>Integration level: does the transfer service update the account service correctly?</li>'
                                '<li>System level: can a user log in, transfer money and see the new balance?</li>'
                                '<li>Acceptance level: does it satisfy the bank\'s business rules?</li></ul>'
                                'Each level has a different goal, so one level cannot replace another.',
                    },
                    {
                        'title': 'Analysis and design start during development',
                        'body': 'While developers build the cart, the tester already writes test conditions from the '
                                'user story ("coupon cannot be used twice"). When the build arrives on Monday, the '
                                'tests are ready to run instead of just starting to be designed.',
                    },
                    {
                        'title': 'Reviewing drafts early',
                        'body': 'The tester reads a draft user story: "Users can upload a profile photo." '
                                'Questions raised: What file types? What maximum size? What if the upload fails? '
                                'The answers are added before any code is written.',
                    },
                    {
                        'title': 'TDD: test first, then code',
                        'body': 'A developer needs a function that checks password length (minimum 8 characters).<ul>'
                                '<li>Write the test first: <code>isValid("abc")</code> must be false. It fails (red).</li>'
                                '<li>Write the minimum code to pass (green).</li>'
                                '<li>Clean up the code and rerun the test (refactor).</li></ul>',
                    },
                    {
                        'title': 'ATDD: tests come from acceptance criteria',
                        'body': 'The product owner, developer and tester meet for the story "Reset my password" and agree on:<ul>'
                                '<li>The reset link expires after 24 hours.</li>'
                                '<li>The new password cannot equal the last 3 passwords.</li></ul>'
                                'These become acceptance tests before coding starts. The story is done when they pass.',
                    },
                    {
                        'title': 'BDD: Given / When / Then',
                        'body': '<pre class="example-code">Given a user with 100 euros\n'
                                'When they transfer 30 euros\n'
                                'Then the balance is 70 euros</pre>'
                                'Business people can read it, and a tool can run it as an automated test.',
                    },
                    {
                        'title': 'DevOps and continuous integration',
                        'body': 'A developer pushes code at 10:00. The pipeline automatically builds it, runs unit and '
                                'API tests, deploys to a test environment and reports at 10:12 that 2 tests failed. '
                                'The developer fixes it before lunch.<br>'
                                '<strong>Risk:</strong> if the tests are unreliable or nobody watches the results, '
                                'the pipeline gives false confidence.',
                    },
                    {
                        'title': 'Shift-left: cost of finding a defect',
                        'body': 'A missing rule "minors cannot open an account" is found in:'
                                '<table class="example-table"><thead><tr><th>Stage</th><th>Effort to fix</th></tr></thead><tbody>'
                                '<tr><td>Requirements review</td><td>Edit one sentence</td></tr>'
                                '<tr><td>Unit test</td><td>Change a few lines</td></tr>'
                                '<tr><td>Production</td><td>Fix code, retest, redeploy, handle affected customers</td></tr>'
                                '</tbody></table>'
                                'The earlier it is found, the cheaper it is.',
                    },
                    {
                        'title': 'Retrospective: learning after each sprint',
                        'body': 'The team notes that 4 of 6 bugs came from unclear stories.<ul>'
                                '<li>Action: testers join story refinement from the next sprint.</li>'
                                '<li>Next retrospective: check whether the bug count dropped.</li></ul>',
                    },
                ],
            },
            {
                'title': '2.2 Test levels and test types',
                'summary': 'Test levels are groups of activities organised together. Test types focus on a '
                           'particular quality characteristic.',
                'points': [
                    'Component (unit) testing: one piece of code in isolation, usually by developers.',
                    'Component integration testing: how components work together through their interfaces.',
                    'System testing: the whole system end to end, including non-functional behaviour.',
                    'System integration testing: the system with other systems or services.',
                    'Acceptance testing: is the system ready for users? Forms: UAT (users), operational (OAT: '
                    'backup, recovery, maintenance), contractual and regulatory, alpha (at developer site), beta '
                    '(at customer site).',
                    'Functional testing: what the system does.',
                    'Non-functional testing: how well it does it (performance, usability, security, reliability).',
                    'Black-box: based on specifications. White-box: based on internal structure.',
                    'Confirmation testing: was the fix successful? Regression testing: did the change break '
                    'something else?',
                ],
                'example': 'Online shop: a unit test checks the discount function. Integration tests check that '
                           'the cart talks to the stock service. A system test buys a product from login to '
                           'receipt. Acceptance tests have real customers try it. After a bug fix, '
                           'confirmation retests that bug, and regression reruns checkout tests.',
            },
            {
                'title': '2.3 Maintenance testing',
                'summary': 'Software changes after release. Maintenance testing checks those changes and '
                           'looks for side effects.',
                'points': [
                    'Triggers: modification (fixes, enhancements), migration (new platform), retirement '
                    '(archiving data).',
                    'Impact analysis finds which areas a change may affect and so guides regression testing.',
                    'It can be hard when documentation is missing or the original team has left.',
                ],
                'example': 'A bank upgrades its database. Tests focus on data migration accuracy, and impact '
                           'analysis picks the reports and batch jobs that use the database for regression.',
            },
        ],
        'key_terms': [
            ('Test level', 'A group of test activities organised and managed together.'),
            ('Test type', 'A group of activities focused on specific quality characteristics.'),
            ('Regression testing',
             'Checking that a change has not harmed existing behaviour.'),
            ('Shift-left', 'Doing testing earlier in the lifecycle.'),
            ('Impact analysis', 'Identifying the consequences of a change.'),
        ],
        'exam_tips': [
            'Be able to name the level from a short scenario (unit, integration, system, acceptance).',
            'Confirmation = the bug is fixed. Regression = nothing else broke.',
            'Know TDD vs ATDD vs BDD at a glance.',
        ],
    },
    # ------------------------------------------------------------------ 3
    {
        'number': 3,
        'title': 'Static Testing',
        'minutes': 80,
        'intro': 'Finding problems without running the software: by reading, reviewing and analysing work products.',
        'sections': [
            {
                'title': '3.1 Static testing basics',
                'summary': 'Static testing examines work products (requirements, code, designs, user '
                           'stories, test cases) manually (reviews) or with tools (static analysis).',
                'points': [
                    'It finds defects early, when they are cheapest to fix.',
                    'It can find things dynamic testing cannot: requirement gaps, contradictions, '
                    'unreachable code, standards violations.',
                    'Dynamic testing finds failures; static testing finds defects directly.',
                    'Static testing also improves communication and shared understanding.',
                ],
                'example': 'Reading a requirement "the system shall respond quickly" a reviewer asks '
                           '"how quickly?". A vague requirement is fixed before any code exists.',
            },
            {
                'title': '3.2 Review process',
                'summary': 'Reviews follow a clear process and bring benefits when done well.',
                'points': [
                    'Activities: planning, review initiation, individual review, communication and '
                    'analysis, fixing and reporting.',
                    'Roles: author, management, facilitator, review leader, reviewers, scribe.',
                    'Informal review: no formal process, quick and cheap.',
                    'Walkthrough: the author leads, for learning and feedback.',
                    'Technical review: experts reach consensus on technical content.',
                    'Inspection: the most formal, with defined roles, metrics and checklists, aiming to find defects '
                    'and improve the process.',
                    'Success factors: clear objectives, right people, defects welcomed as findings (not '
                    'blame), enough time, management support.',
                ],
                'example': 'Before coding a login feature, the BA, developer and tester hold a walkthrough of '
                           'the user story. The tester spots that "locked account" behaviour is missing. It is '
                           'added in minutes rather than found as a production bug.',
            },
        ],
        'key_terms': [
            ('Static testing', 'Testing a work product without executing it.'),
            ('Review', 'Evaluating a work product by people to find defects or improve it.'),
            ('Inspection', 'The most formal review type, with defined roles and metrics.'),
            ('Walkthrough', 'A review led by the author to share understanding.'),
            ('Static analysis', 'Tool-based examination of code or models.'),
        ],
        'exam_tips': [
            'Know the 5 review activities in order.',
            'Match each review type to its main purpose and formality.',
            'Static testing finds defects; dynamic testing finds failures.',
        ],
    },
    # ------------------------------------------------------------------ 4
    {
        'number': 4,
        'title': 'Test Analysis and Design',
        'minutes': 390,
        'intro': 'The heart of the syllabus: techniques to choose good test cases. '
                 'This is the longest chapter and is worth the most exam points.',
        'sections': [
            {
                'title': '4.1 Test techniques overview',
                'summary': 'Techniques help you pick a small set of tests with a good chance of finding defects.',
                'points': [
                    'Black-box: uses requirements and behaviour, not the code.',
                    'White-box: uses the code structure.',
                    'Experience-based: uses the tester\'s skill and intuition.',
                ],
                'example': None,
                'examples': [
                    {
                        'title': 'Which technique fits? Pick by the situation',
                        'body': '<table class="example-table"><thead><tr><th>Situation</th><th>Technique</th></tr></thead><tbody>'
                                '<tr><td>Input is a range (age 18-65, amount 1-500)</td><td>Equivalence Partitioning + BVA</td></tr>'
                                '<tr><td>Several conditions combine into one outcome (loan approval rules)</td><td>Decision table</td></tr>'
                                '<tr><td>Behaviour depends on history (order: Placed, Paid, Shipped, Cancelled)</td><td>State transition</td></tr>'
                                '<tr><td>You have the code and need to know what was never run</td><td>Statement / branch coverage</td></tr>'
                                '<tr><td>No specification, little time</td><td>Exploratory testing / error guessing</td></tr>'
                                '<tr><td>Team wants shared understanding before coding</td><td>ATDD with acceptance criteria</td></tr>'
                                '</tbody></table>',
                    },
                ],
            },
            {
                'title': '4.2 Black-box techniques',
                'summary': 'Four techniques are required knowledge.',
                'points': [
                    'Equivalence Partitioning (EP): split inputs into groups that the system treats the same. '
                    'Test one value from each group. Cover valid and invalid partitions.',
                    'Boundary Value Analysis (BVA): defects love edges, so test at the boundary and just '
                    'beside it. 2-value BVA uses the boundary and its nearest neighbour in the next '
                    'partition. 3-value BVA also adds the neighbour on the other side.',
                    'Decision table testing: list combinations of conditions and the resulting actions. '
                    'Each column is a rule. Good for business logic.',
                    'State transition testing: model states, events and transitions. Cover states or '
                    'transitions, including invalid ones.',
                ],
                'example': None,
                'examples': [
                    {
                        'title': 'Equivalence Partitioning: age field on a gym signup form',
                        'body': 'The form accepts ages <strong>18 to 65</strong>.<ul>'
                                '<li>Partitions: below 18 (invalid), 18-65 (valid), above 65 (invalid).</li>'
                                '<li>Tests: <code>10</code>, <code>40</code>, <code>80</code>, one per partition.</li>'
                                '<li>3 partitions means 3 tests instead of trying every age.</li></ul>',
                    },
                    {
                        'title': 'Boundary Value Analysis: the same age field',
                        'body': 'Bugs hide at the edges, e.g. <code>&gt; 18</code> written instead of '
                                '<code>&gt;= 18</code>.<ul>'
                                '<li>2-value BVA: <code>17</code>, <code>18</code>, <code>65</code>, <code>66</code>.</li>'
                                '<li>3-value BVA: <code>17</code>, <code>18</code>, <code>19</code>, '
                                '<code>64</code>, <code>65</code>, <code>66</code>.</li></ul>',
                    },
                    {
                        'title': 'Decision table: discount rules in an online shop',
                        'body': 'Rules: members get 10% off, and orders over 100 euros get free shipping.'
                                '<table class="example-table"><thead><tr><th>Rule</th><th>Member?</th>'
                                '<th>Order &gt; 100?</th><th>Result</th></tr></thead><tbody>'
                                '<tr><td>1</td><td>Yes</td><td>Yes</td><td>10% off + free shipping</td></tr>'
                                '<tr><td>2</td><td>Yes</td><td>No</td><td>10% off</td></tr>'
                                '<tr><td>3</td><td>No</td><td>Yes</td><td>Free shipping</td></tr>'
                                '<tr><td>4</td><td>No</td><td>No</td><td>No benefit</td></tr></tbody></table>'
                                'Each rule becomes one test case.',
                    },
                    {
                        'title': 'State transition: ATM card',
                        'body': 'States: <strong>Active</strong> and <strong>Blocked</strong>.<ul>'
                                '<li>Event "wrong PIN" keeps the card Active for attempts 1 and 2.</li>'
                                '<li>The 3rd wrong PIN moves it to Blocked.</li>'
                                '<li>Test: a 4th attempt, even with the right PIN, must be refused. '
                                'This is an invalid transition test.</li></ul>',
                    },
                    {
                        'title': 'Practice: count the tests (EP with two inputs)',
                        'body': 'A ticket form has <strong>age</strong> (child 0-12, adult 13-64, senior 65+) and '
                                '<strong>day</strong> (weekday, weekend).<ul>'
                                '<li>Age has 3 partitions and day has 2.</li>'
                                '<li>Each-choice coverage: you need at least <strong>3</strong> tests '
                                '(the largest number of partitions), reusing day values.</li>'
                                '<li>All combinations: 3 x 2 = <strong>6</strong> tests.</li>'
                                '<li>Exam tip: read whether the question asks for the minimum to cover each partition '
                                'or for all combinations.</li></ul>',
                    },
                    {
                        'title': 'Practice: BVA on a discount field',
                        'body': 'A coupon gives a discount when the cart total is <strong>50 to 200 euros</strong>.<ul>'
                                '<li>Valid partition: 50-200. Invalid: below 50 and above 200.</li>'
                                '<li>2-value BVA: <code>49</code>, <code>50</code>, <code>200</code>, <code>201</code> '
                                '(4 tests).</li>'
                                '<li>3-value BVA: <code>49</code>, <code>50</code>, <code>51</code>, '
                                '<code>199</code>, <code>200</code>, <code>201</code> (6 tests).</li>'
                                '<li>If the amount can have cents, the neighbour of 50 is <code>49.99</code>, not 49.</li></ul>',
                    },
                    {
                        'title': 'Practice: decision table with a minimised rule',
                        'body': 'Loan approval: approve if <strong>income is enough</strong> AND <strong>no '
                                'missed payments</strong>.'
                                '<table class="example-table"><thead><tr><th>Rule</th><th>Income OK?</th>'
                                '<th>No missed payments?</th><th>Approve?</th></tr></thead><tbody>'
                                '<tr><td>1</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>'
                                '<tr><td>2</td><td>Yes</td><td>No</td><td>No</td></tr>'
                                '<tr><td>3</td><td>No</td><td>-</td><td>No</td></tr></tbody></table>'
                                'With 2 conditions there are 4 combinations, but if income is not OK the second '
                                'condition does not matter, so rules 3 and 4 merge (the dash means "any"). '
                                'Coverage = rules tested / total rules.',
                    },
                    {
                        'title': 'Practice: state transition table with an invalid transition',
                        'body': 'Online order states and events:'
                                '<table class="example-table"><thead><tr><th>State</th><th>Pay</th><th>Ship</th>'
                                '<th>Cancel</th></tr></thead><tbody>'
                                '<tr><td>Placed</td><td>Paid</td><td>invalid</td><td>Cancelled</td></tr>'
                                '<tr><td>Paid</td><td>invalid</td><td>Shipped</td><td>Cancelled</td></tr>'
                                '<tr><td>Shipped</td><td>invalid</td><td>invalid</td><td>invalid</td></tr>'
                                '<tr><td>Cancelled</td><td>invalid</td><td>invalid</td><td>invalid</td></tr>'
                                '</tbody></table>'
                                '<ul><li>Valid transitions: 5. Covering all of them gives 100% transition coverage.</li>'
                                '<li>Test an invalid one too: trying to ship a Placed order must be rejected.</li></ul>',
                    },
                ],
            },
            {
                'title': '4.3 White-box techniques',
                'summary': 'Coverage measures how much of the code your tests execute.',
                'points': [
                    'Statement coverage = executed statements / total statements.',
                    'Branch coverage = executed branches / total branches (each decision outcome, true and false).',
                    '100% branch coverage guarantees 100% statement coverage, but not the other way round.',
                    'High coverage does not guarantee the code is correct, only that it was run.',
                ],
                'example': 'Code: <code>if (age &gt;= 18) { allow(); }</code>. One test with age 20 gives 100% '
                           'statement coverage but only 50% branch coverage. Add age 10 to cover the false branch.',
                'examples': [
                    {
                        'title': 'Practice: compute statement and branch coverage',
                        'body': '<pre class="example-code">1  total = price * qty\n'
                                '2  if member:\n'
                                '3      total = total * 0.9\n'
                                '4  if total &gt; 100:\n'
                                '5      shipping = 0\n'
                                '6  else:\n'
                                '7      shipping = 5\n'
                                '8  return total + shipping</pre>'
                                'Statements: lines 1, 2, 3, 4, 5, 7, 8 (7 in total). Decisions: lines 2 and 4, so 4 branch outcomes.'
                                '<table class="example-table"><thead><tr><th>Test</th><th>member</th><th>total</th>'
                                '<th>Statements run</th><th>Branches run</th></tr></thead><tbody>'
                                '<tr><td>T1</td><td>True</td><td>&gt; 100</td><td>1, 2, 3, 4, 5, 8 = 6/7 (86%)</td>'
                                '<td>2 of 4 (50%)</td></tr>'
                                '<tr><td>T1 + T2 (False, total &le; 100)</td><td></td><td></td>'
                                '<td>7/7 (100%)</td><td>4 of 4 (100%)</td></tr></tbody></table>'
                                'After T1 alone: 86% statement and 50% branch coverage. '
                                'Exam tip: count statements and branch outcomes first, then divide.',
                    },
                ],
            },
            {
                'title': '4.4 Experience-based techniques',
                'summary': 'Use knowledge, skill and intuition, especially when specs are poor or time is short.',
                'points': [
                    'Error guessing: predict likely defects from past experience, then design tests to hit them.',
                    'Exploratory testing: learn, design and run tests at the same time, often in a time-boxed '
                    'session with a charter.',
                    'Checklist-based testing: use a list of conditions to cover, built from experience or standards.',
                ],
                'example': 'Testing a signup form, you guess: empty fields, very long names, emojis, an email '
                           'with spaces, or double-clicking Submit. These are classic problem spots.',
            },
            {
                'title': '4.5 Collaboration-based approaches',
                'summary': 'Quality is built together with business and developers.',
                'points': [
                    'User story = Card (the story), Conversation (talking about it), Confirmation '
                    '(acceptance criteria): the 3 Cs.',
                    'Good stories follow INVEST: Independent, Negotiable, Valuable, Estimable, Small, Testable.',
                    'Acceptance criteria can be rule-oriented (bullet list), scenario-oriented (Given/When/Then) '
                    'or custom.',
                    'ATDD: write acceptance tests before implementing, from the examples agreed by the team.',
                ],
                'example': 'Story: "As a customer I want to reset my password so I can log in again." '
                           'Criteria: link expires after 24 hours; the new password cannot equal the last 3.',
            },
        ],
        'key_terms': [
            ('Equivalence partition',
             'A group of values treated the same by the system.'),
            ('Boundary value', 'The edge value of a partition.'),
            ('Decision table', 'A table of condition combinations and their outcomes.'),
            ('Statement coverage', 'Percentage of statements executed.'),
            ('Branch coverage', 'Percentage of decision outcomes executed.'),
            ('Exploratory testing', 'Simultaneous learning, test design and execution.'),
        ],
        'exam_tips': [
            'Practise EP and BVA calculations until they are automatic: count tests, list values.',
            'Be able to compute statement and branch coverage from a small code snippet.',
            'Know which technique fits a scenario (rules = decision table, lifecycle = state transition).',
        ],
    },
    # ------------------------------------------------------------------ 5
    {
        'number': 5,
        'title': 'Managing the Test Activities',
        'minutes': 335,
        'intro': 'Planning, estimating, handling risk, reporting and managing defects: running testing as a well-organised effort.',
        'sections': [
            {
                'title': '5.1 Test planning',
                'summary': 'A test plan describes objectives, scope, approach, resources and schedule.',
                'points': [
                    'Entry criteria: conditions to start (environment ready, build available).',
                    'Exit criteria (definition of done): conditions to stop (coverage reached, no critical bugs open).',
                    'Estimation techniques: ratio-based (use past project ratios), extrapolation (use early '
                    'iterations to predict), Wideband Delphi (experts estimate then discuss), three-point '
                    '(E = (a + 4m + b) / 6).',
                    'Prioritising test cases: risk-based, coverage-based, or requirements-based.',
                    'Test pyramid: many fast unit tests, fewer integration tests, very few slow end-to-end tests.',
                    'Testing quadrants (Agile): technology vs business facing, and support the team vs critique the product.',
                ],
                'example': None,
                'examples': [
                    {
                        'title': 'Entry and exit criteria: release of a food-delivery app',
                        'body': '<ul><li><strong>Entry:</strong> test environment is up, build 2.4 is deployed, '
                                'test data is loaded.</li>'
                                '<li><strong>Exit:</strong> 100% of high-risk tests run, 95% passed, no open critical '
                                'bugs.</li></ul>',
                    },
                    {
                        'title': 'Ratio-based estimation: use ratios from past projects',
                        'body': 'On earlier projects the team spent <strong>3 days of development for every 2 days of '
                                'testing</strong> (ratio 3:2).<ul>'
                                '<li>New project: development is estimated at 90 days.</li>'
                                '<li>Test effort = 90 x 2 / 3 = <strong>60 days</strong>.</li></ul>'
                                'Works best when the new project is similar to the old ones.',
                    },
                    {
                        'title': 'Extrapolation: use data from the current project',
                        'body': 'Testing effort in the first 3 two-week iterations was 8, 10 and 9 person-days.<ul>'
                                '<li>Average = (8 + 10 + 9) / 3 = 9 days per iteration.</li>'
                                '<li>10 iterations are planned, so 7 remain: 7 x 9 = <strong>63 days</strong> more.</li></ul>'
                                'The estimate improves as more real data arrives.',
                    },
                    {
                        'title': 'Wideband Delphi: experts estimate, then discuss',
                        'body': 'Three experts estimate testing the new payment module, without seeing each other\'s numbers:'
                                '<table class="example-table"><thead><tr><th>Expert</th><th>Round 1</th><th>Round 2</th></tr></thead><tbody>'
                                '<tr><td>Tester (experienced)</td><td>10 days</td><td>12 days</td></tr>'
                                '<tr><td>Developer</td><td>6 days</td><td>11 days</td></tr>'
                                '<tr><td>Business analyst</td><td>20 days</td><td>13 days</td></tr></tbody></table>'
                                'After round 1 they discuss why the numbers differ (the developer forgot refund flows; '
                                'the analyst assumed three payment providers). Round 2 converges to about 12 days.',
                    },
                    {
                        'title': 'Three-point estimation: handle uncertainty',
                        'body': 'Testing a data migration: <strong>a</strong> (best case) = 4 days, '
                                '<strong>m</strong> (most likely) = 6 days, <strong>b</strong> (worst case) = 14 days.<ul>'
                                '<li>E = (a + 4m + b) / 6 = (4 + 24 + 14) / 6 = <strong>7 days</strong>.</li>'
                                '<li>Uncertainty (standard deviation) = (b - a) / 6 = 10 / 6 = about <strong>1.7 days</strong>.</li>'
                                '<li>Report it as <strong>7 &plusmn; 1.7 days</strong>, not as a single exact number.</li></ul>',
                    },
                    {
                        'title': 'Risk-based prioritisation: test the scariest things first',
                        'body': 'Online store, limited time:'
                                '<table class="example-table"><thead><tr><th>Test</th><th>Likelihood of failure</th>'
                                '<th>Impact</th><th>Order</th></tr></thead><tbody>'
                                '<tr><td>Card payment</td><td>High</td><td>High</td><td>1</td></tr>'
                                '<tr><td>Stock count after purchase</td><td>Medium</td><td>High</td><td>2</td></tr>'
                                '<tr><td>Wish-list sharing</td><td>Medium</td><td>Low</td><td>3</td></tr>'
                                '<tr><td>Footer links</td><td>Low</td><td>Low</td><td>4</td></tr></tbody></table>'
                                'If time runs out, only the least important tests are left unrun.',
                    },
                    {
                        'title': 'Coverage-based prioritisation: run the test that adds the most new coverage',
                        'body': 'Three tests with their statement coverage:<ul>'
                                '<li>T1 covers 40% of the code.</li>'
                                '<li>T2 covers 30%, but 25% of that was already covered by T1 (adds only 5%).</li>'
                                '<li>T3 covers 20% that nobody else covers.</li></ul>'
                                'Order: <strong>T1, T3, T2</strong> (T3 adds 20% more, T2 only 5%). '
                                'The first run brings coverage to 40%, the second to 60%, the third to 65%.',
                    },
                    {
                        'title': 'Requirements-based prioritisation: follow business priority',
                        'body': 'Stakeholders ranked the requirements:'
                                '<table class="example-table"><thead><tr><th>Requirement</th><th>Priority</th>'
                                '<th>Tests run first</th></tr></thead><tbody>'
                                '<tr><td>REQ-1 Place an order</td><td>Must have</td><td>TC-01 to TC-08</td></tr>'
                                '<tr><td>REQ-2 Track delivery</td><td>Should have</td><td>TC-09 to TC-12</td></tr>'
                                '<tr><td>REQ-3 Dark mode</td><td>Nice to have</td><td>TC-13 (last)</td></tr></tbody></table>',
                    },
                    {
                        'title': 'Dependencies can override the order',
                        'body': 'Even if "Cancel order" has higher priority, it cannot be tested before "Place order" '
                                'works. So Place order runs first, then the higher-priority test that depends on it.',
                    },
                    {
                        'title': 'Test pyramid: where to put the tests',
                        'body': 'For a shop with 100 automated tests, a healthy split could be about 70 unit tests '
                                '(seconds to run), 20 API/integration tests, and 10 end-to-end UI tests (minutes). '
                                'An inverted pyramid (mostly UI tests) is slow and breaks often.',
                    },
                    {
                        'title': 'Testing quadrants (Agile)',
                        'body': '<ul><li>Q1 technology-facing, supports the team: unit and component tests.</li>'
                                '<li>Q2 business-facing, supports the team: acceptance tests, examples from stories.</li>'
                                '<li>Q3 business-facing, critiques the product: exploratory and usability testing.</li>'
                                '<li>Q4 technology-facing, critiques the product: performance and security testing.</li></ul>',
                    },
                ],
            },
            {
                'title': '5.2 Risk management',
                'summary': 'Risk is the chance of an event with a negative effect. Its level depends on likelihood and impact.',
                'points': [
                    'Project risks: affect the project (late delivery, staff shortage).',
                    'Product risks: affect quality (wrong calculations, poor performance).',
                    'Risk analysis identifies and assesses risks; risk control responds to them.',
                    'Responses: mitigation (reduce it, e.g. more testing), acceptance, transfer (insurance), contingency (a backup plan).',
                    'Risk-based testing puts the most effort on the highest risks.',
                ],
                'example': 'A medical app dosage calculator has high impact and moderate likelihood, so it gets '
                           'the deepest testing. The colour theme gets a quick check.',
            },
            {
                'title': '5.3 Test monitoring, control and completion',
                'summary': 'Measure progress, report it clearly and act on it.',
                'points': [
                    'Common metrics: test cases run/passed/failed, defect counts, coverage, cost, effort.',
                    'Test progress report: status, impediments, metrics, risks, next steps.',
                    'Test completion report: summary at the end of a project or level.',
                    'Control actions: reprioritise, change the schedule, add resources.',
                    'Choose the communication form for the audience: dashboards, meetings, short messages.',
                ],
                'example': 'Mid-sprint, only 40% of tests have run and 5 critical bugs are open. The report '
                           'flags the risk, and control action moves two testers from low-priority work.',
            },
            {
                'title': '5.4 Configuration management',
                'summary': 'Keeps track of versions of all items so test results are reliable and reproducible.',
                'points': [
                    'Identify and version code, tests, data and environments.',
                    'Ensures you know exactly what build a test ran against.',
                    'Supports traceability between items.',
                ],
                'example': 'A bug is reported against "build 2.3.1". Without version control nobody could '
                           'reproduce it.',
            },
            {
                'title': '5.5 Defect management',
                'summary': 'Defects are recorded, tracked and resolved through a workflow.',
                'points': [
                    'A good defect report: unique ID, title, steps to reproduce, expected vs actual result, '
                    'environment, severity, priority, status.',
                    'Typical life cycle: new, open, fixed, retested, closed (or rejected / reopened).',
                    'Severity is the technical impact; priority is how soon to fix.',
                ],
                'example': 'Title: "Checkout total ignores coupon". Steps: add item, apply code SAVE10, open '
                           'cart. Expected: 10% off. Actual: full price.',
            },
        ],
        'key_terms': [
            ('Entry criteria', 'Preconditions that must be met before starting an activity.'),
            ('Exit criteria', 'Conditions that must be met to declare an activity finished.'),
            ('Risk level', 'Likelihood combined with impact.'),
            ('Product risk', 'A risk to the quality of the product.'),
            ('Project risk', 'A risk to the project\'s success.'),
            ('Test pyramid', 'Model showing more low-level tests than high-level ones.'),
        ],
        'exam_tips': [
            'Learn the three-point formula and practise one calculation.',
            'Separate project risks from product risks in scenarios.',
            'Know the four risk responses and one example of each.',
        ],
    },
    # ------------------------------------------------------------------ 6
    {
        'number': 6,
        'title': 'Test Tools',
        'minutes': 20,
        'intro': 'A short chapter: what tools can do for testers and what to watch out for.',
        'sections': [
            {
                'title': '6.1 Tool support for testing',
                'summary': 'Tools can support almost every test activity.',
                'points': [
                    'Test management and ALM tools: plans, cases, results, traceability.',
                    'Static testing tools: code analysis and review support.',
                    'Test design and implementation tools: generate tests or data.',
                    'Test execution and coverage tools: run automated tests and measure coverage.',
                    'Non-functional tools: performance and security testing.',
                    'DevOps tools: pipelines and continuous integration.',
                    'Collaboration tools: communication and shared boards.',
                ],
                'example': 'A CI server runs 2,000 automated tests every night and e-mails the team a report each morning.',
            },
            {
                'title': '6.2 Benefits and risks of test automation',
                'summary': 'Automation is powerful but not free and not always right.',
                'points': [
                    'Benefits: saves time on repetitive work, more consistent, faster feedback, more tests '
                    'run, objective measurements.',
                    'Risks: unrealistic expectations, underestimated effort for set-up and maintenance, '
                    'over-reliance on the tool, vendor or open-source risks, unsuitable tool.',
                    'Automate stable, repetitive, high-value tests such as regression.',
                    'Keep manual and exploratory testing where human judgement matters.',
                ],
                'example': 'Automating the login regression test pays back quickly because it runs on every build. '
                           'Automating a one-off visual check of a promotional page does not.',
            },
        ],
        'key_terms': [
            ('Test automation', 'Using software to execute tests and compare results.'),
            ('Test management tool', 'A tool to plan, track and report on testing.'),
            ('Continuous integration',
             'Frequently merging and automatically testing code.'),
        ],
        'exam_tips': [
            'Expect questions on benefits and risks of automation.',
            'Automation does not replace manual testing.',
        ],
    },
]
