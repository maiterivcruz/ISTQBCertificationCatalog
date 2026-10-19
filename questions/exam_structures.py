"""Official exam structure and rules per certification.

Tuple: (certification id, version, title, questions, points, passing score, minutes, minutes +25%).
Passing score is at least 65% of the points.
"""
EXAM_STRUCTURES = [
    ('ctfl', 'v4.0', 'Certified Tester Foundation Level v4.0', 40, 40, 26, 60, 75),
    ('ctal-at', 'v2.0', 'Certified Tester Advanced Level Agile Tester v2.0', 40, 52, 34, 90, 113),
    ('ctal-ta', 'v4.0', 'Certified Tester Advanced Level Test Analyst v4.0', 45, 78, 51, 120, 150),
    ('ctal-ta', 'v3.1', 'Certified Tester Advanced Level Test Analyst v3.1', 40, 80, 52, 120, 150),
    ('ctal-tae', 'v2.0', 'Certified Tester Advanced Level Test Automation Engineering v2.0', 40, 66, 43, 90, 113),
    ('ctal-tm', 'v3.0', 'Certified Tester Advanced Level Test Management v3.0', 50, 88, 58, 120, 150),
    ('ctal-tta', 'v4.0', 'Certified Tester Advanced Level Technical Test Analyst v4.0', 45, 78, 51, 120, 150),
    ('ct-act', '', 'Certified Tester Acceptance Testing', 40, 40, 26, 60, 75),
    ('ct-ai', 'v2.0', 'Certified Tester AI Testing v2.0', 40, 44, 29, 60, 75),
    ('ct-ai', 'v1.0', 'Certified Tester AI Testing v1.0', 40, 47, 31, 60, 75),
    ('ct-atlas', 'v2.0', 'Certified Tester Advanced Level Agile Test Leadership at Scale v2.0', 40, 71, 47, 120, 150),
    ('ct-atlas', 'v2.0 Upgrade', 'Certified Tester Advanced Level Agile Test Leadership at Scale v2.0 Upgrade', 23, 44, 29, 75, 94),
    ('ct-aut', 'v2.1', 'Certified Tester Automotive Software Tester v2.1', 40, 40, 26, 60, 75),
    ('ct-aut', 'v1.0', 'Certified Tester Automotive Software Tester v1.0', 40, 40, 26, 60, 75),
    ('ct-game', '', 'Certified Tester Game Testing', 40, 40, 26, 60, 75),
    ('ct-genai', '', 'Certified Tester Testing with Generative AI', 40, 46, 30, 60, 75),
    ('ct-gt', '', 'Certified Tester Gambling Industry Tester', 40, 40, 26, 60, 75),
    ('ct-ft', '', 'Certified Tester Finance Testing', 40, 45, 30, 60, 75),
    ('ct-mat', '', 'Certified Tester Mobile Application Testing', 40, 40, 26, 60, 75),
    ('ct-mbt', '', 'Certified Tester Model-Based Tester', 40, 40, 26, 60, 75),
    ('ct-pt', '', 'Certified Tester Performance Testing', 40, 40, 26, 90, 113),
    ('ct-qdo', '', 'Certified Tester Quality in DevOps', 40, 45, 30, 60, 75),
    ('ct-sec', '', 'Certified Tester Security Tester', 45, 80, 52, 120, 150),
    ('ct-ste', '', 'Certified Tester Security Test Engineer', 40, 43, 28, 75, 94),
    ('ct-tas', 'v1.0', 'Certified Tester Test Automation Strategy v1.0', 40, 49, 32, 60, 75),
    ('ct-ut', '', 'Certified Tester Usability Testing', 40, 40, 26, 60, 75),
]
