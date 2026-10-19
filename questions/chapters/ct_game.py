"""CT-GaMe study chapters: plain-language game testing guidance."""

CHAPTERS = [
    {
        'number': 1,
        'title': 'Specificity of Game Testing',
        'minutes': 75,
        'intro': 'Games combine interactive software with creative content, hardware, and player expectations. Testing must examine both correct behavior and the experience of play.',
        'sections': [
            {
                'title': '1.1 Game Testing Basics',
                'summary': 'Game testing checks the product from a player perspective while also verifying requirements and technical behavior.',
                'points': [
                    'A game can be functionally correct yet still feel confusing, unfair, or unpleasant to play.',
                    'Playtesting observes real player behavior and experience; functional testing checks whether defined behavior works.',
                    'Game products may include code, levels, graphics, sound, controllers, online services, and platform-specific versions.',
                ],
                'example': 'Players repeatedly miss a jump because the visual cue is unclear, even though the jump code works as designed.',
            },
            {
                'title': '1.2 Typical Roles of the Game Development Team',
                'summary': 'Game quality is shared across design, engineering, art, audio, production, and testing roles.',
                'points': [
                    'Designers define rules and player goals; programmers implement behavior; artists and audio specialists create content.',
                    'Testers provide evidence about defects and player experience, and collaborate with the team to reproduce issues.',
                    'Production and project roles coordinate scope, priorities, milestones, and release readiness.',
                ],
                'example': 'A tester reports that a boss attack is hard to read; the designer adjusts its timing while the artist improves the warning animation.',
            },
            {
                'title': '1.3 Testing Activities throughout the Game Software Development Lifecycle',
                'summary': 'Testing starts with early concepts and continues through production, release preparation, and post-release work.',
                'points': [
                    'Pre-production explores concepts and risks; production builds content and features; post-production supports release and updates.',
                    'Testing can include reviews, playtests, compatibility checks, regression checks, and certification preparation.',
                    'The timing and depth of testing should match the maturity of the build and the risks of each development stage.',
                ],
                'example': 'The team playtests a paper prototype before coding, checks a playable level during production, and runs regression tests on the release candidate.',
            },
        ],
        'key_terms': [
            ('Playtest', 'An evaluation in which players experience a game to reveal usability and experience issues.'),
            ('Player perspective testing', 'Testing that considers how the product is understood and experienced by players.'),
            ('Pre-production', 'The stage in which game concepts, scope, and plans are shaped.'),
            ('Regression testing', 'Testing after a change to find unintended effects on existing behavior.'),
        ],
        'exam_tips': [
            'Distinguish player experience observations from checks of defined functionality.',
            'Relate testing activity to the game lifecycle stage and build maturity.',
        ],
    },
    {
        'number': 2,
        'title': 'Testing Game Mechanics',
        'minutes': 180,
        'intro': 'Game mechanics are the rules and interactions that let players act, make choices, and see consequences.',
        'sections': [
            {
                'title': '2.1 Game Mechanics',
                'summary': 'Mechanics define the actions, constraints, goals, and feedback that shape how a game is played.',
                'points': [
                    'Consider player actions, game state, rules, rewards, challenges, and feedback as connected parts of a mechanic.',
                    'Mechanics can interact, so a rule that works alone may fail when combined with another feature or player action.',
                    'Check consistency and fairness across valid, invalid, repeated, and unusual player choices.',
                ],
                'example': 'A stamina rule limits repeated attacks; testing checks that the meter, attack availability, and recovery behavior agree at the limit.',
            },
            {
                'title': '2.2 Approaches to Testing Game Mechanics',
                'summary': 'Mechanic testing combines planned checks with exploratory play to uncover rule, balance, and interaction problems.',
                'points': [
                    'Derive test conditions from the rules, player actions, state changes, and expected feedback.',
                    'Explore edge cases, sequences, timing, combinations, and multiplayer interactions as well as the normal path.',
                    'Repeat tests after tuning or code changes to check that fixes did not break related mechanics.',
                ],
                'example': 'For a trading mechanic, testers try valid trades, repeated confirmation, insufficient currency, and two players offering the same item at once.',
            },
        ],
        'key_terms': [
            ('Game mechanic', 'A rule or interaction that shapes player actions and game outcomes.'),
            ('Game state', 'The current values and conditions that determine what can happen in play.'),
            ('Exploratory testing', 'Testing in which learning, test design, and execution are performed together.'),
            ('Multiplayer testing', 'Testing behavior involving multiple players and their interactions.'),
        ],
        'exam_tips': [
            'Trace player action to rule, state change, and feedback when analyzing a mechanic.',
            'Include combinations and timing, not only isolated button presses.',
            'Explain why exploratory play can reveal issues that scripted checks miss.',
        ],
    },
    {
        'number': 3,
        'title': 'Graphics Testing',
        'minutes': 165,
        'intro': 'Graphics testing checks visual quality, rendering behavior, and presentation across scenes and target platforms.',
        'sections': [
            {
                'title': '3.1 Principles and Concepts of Game Graphics',
                'summary': 'Game visuals are produced from assets, models, textures, lighting, animation, and rendering choices.',
                'points': [
                    'Visual content must meet artistic intent while remaining readable and technically suitable for target devices.',
                    'A scene may combine 2D and 3D content, effects, camera behavior, and dynamic lighting.',
                    'Performance limits can affect image quality, frame stability, and player responsiveness.',
                ],
                'example': 'A low-end console may render fewer particles, but the remaining visual effects must still make an incoming hazard easy to see.',
            },
            {
                'title': '3.2 Approaches to Testing Graphics in Game Products',
                'summary': 'Graphics checks compare visual results with design intent and look for defects across content, settings, and devices.',
                'points': [
                    'Inspect assets and scenes for missing, corrupted, misplaced, clipped, or inconsistent visual elements.',
                    'Check different resolutions, aspect ratios, graphics settings, and hardware capabilities.',
                    'Assess whether visual cues communicate gameplay information clearly and consistently.',
                ],
                'example': 'A tester checks a menu at wide and standard screen ratios and finds that the confirmation button is clipped only on the wider display.',
            },
            {
                'title': '3.3 Graphics Test Execution',
                'summary': 'Good execution uses repeatable scenes, conditions, and observations to isolate visual and rendering problems.',
                'points': [
                    'Record the build, device, settings, scene, and steps needed to reproduce a visual defect.',
                    'Check static images and motion, including transitions, animation, camera movement, and effects.',
                    'Compare expected appearance while monitoring frame behavior and visual artifacts during play.',
                ],
                'example': 'A defect report records the graphics preset and camera path that causes a character texture to flicker during a scene transition.',
            },
            {
                'title': '3.4 Tools Support for Graphics Testing',
                'summary': 'Graphics tools help capture, compare, inspect, and diagnose rendered output and asset problems.',
                'points': [
                    'Capture tools and image comparisons help spot differences between builds or devices.',
                    'Profilers and frame inspection tools help investigate rendering cost and performance drops.',
                    'Automated image checks need thresholds and human review because expected visuals may vary by hardware.',
                ],
                'example': 'A screenshot comparison flags a changed HUD position after an update, and a tester confirms whether it is an intended redesign or a regression.',
            },
        ],
        'key_terms': [
            ('Rendering', 'The process of producing the visible image from game content and scene data.'),
            ('Asset', 'A content item such as a model, texture, animation, or visual effect.'),
            ('Frame rate', 'The number of rendered images shown in a time period.'),
            ('Visual regression', 'An unintended change in appearance after a product change.'),
        ],
        'exam_tips': [
            'Separate visual correctness from graphics performance, while checking how they affect each other.',
            'Include device, resolution, and settings when describing graphics test conditions.',
            'Treat automated image differences as findings to review, not automatic proof of a defect.',
        ],
    },
    {
        'number': 4,
        'title': 'Sound Testing',
        'minutes': 190,
        'intro': 'Sound communicates action, mood, and feedback. Testing checks both the audio content and its behavior during play.',
        'sections': [
            {
                'title': '4.1 Features of the Sound Content of the Game Product',
                'summary': 'Game sound includes music, effects, dialogue, and environmental audio that respond to play and support the intended experience.',
                'points': [
                    'Check sound timing, layering, spatial placement, volume, looping, and transitions.',
                    'Audio can be triggered by game events and can change with scene, distance, player state, or settings.',
                    'Sound should remain intelligible and appropriately balanced across supported output devices.',
                ],
                'example': 'When a player enters a cave, environmental audio should transition smoothly while nearby footsteps remain distinct from background ambience.',
            },
            {
                'title': '4.2 Types of Defects in Sound Content',
                'summary': 'Audio defects include missing or incorrect clips, timing problems, distortion, imbalance, and unwanted repetition.',
                'points': [
                    'Check for silence, clipping, pops, distortion, incorrect localization, and sound that plays at the wrong time.',
                    'Look for loops that do not join cleanly, cues that overlap badly, and dialogue that is difficult to understand.',
                    'Defects may occur only with particular devices, settings, languages, or event sequences.',
                ],
                'example': 'A victory sting restarts every time a player opens the results panel, creating an unintended repeated audio cue.',
            },
            {
                'title': '4.3 Approaches to Testing Sound Content in Game Products',
                'summary': 'Audio testing combines listening with checks of triggers, settings, transitions, and supported playback conditions.',
                'points': [
                    'Compare sound output with the intended event, timing, category, and mix.',
                    'Test controls such as mute, volume levels, subtitles, and audio accessibility settings where provided.',
                    'Vary scenes, rapid events, and output devices to reveal overlaps and missing cues.',
                ],
                'example': 'A tester rapidly triggers several menu actions while changing the effects volume to check that each sound remains correctly mixed and responsive.',
            },
            {
                'title': '4.4 Sound Test Execution',
                'summary': 'Repeatable audio execution captures the conditions and event sequence needed to evaluate a sound result.',
                'points': [
                    'Prepare known scenes and actions so timing and expected audio can be checked consistently.',
                    'Record device, output settings, build, and relevant game state when reporting a defect.',
                    'Listen in context and in isolation when needed to distinguish a source-asset issue from a mix or trigger issue.',
                ],
                'example': 'A report for delayed dialogue notes the headset, language, scene, and exact action that starts the line.',
            },
            {
                'title': '4.5 Tools Support for Sound Testing',
                'summary': 'Audio tools help inspect waveforms, events, levels, and playback while supporting diagnosis of sound defects.',
                'points': [
                    'Capture and analysis tools can reveal clipping, silence, timing, and unwanted noise.',
                    'Engine audio debuggers can show which events, sources, and settings produced a sound.',
                    'Tool output should be paired with listening because a measurement alone may not describe player impact.',
                ],
                'example': 'An audio event view shows that a footstep sound is triggered twice, while a recording confirms the resulting overlap.',
            },
        ],
        'key_terms': [
            ('Audio cue', 'A sound triggered to signal an event or state.'),
            ('Clipping', 'Distortion caused when an audio signal exceeds its usable level.'),
            ('Loop', 'Audio content designed to repeat over time.'),
            ('Spatial audio', 'Sound presented with a position or direction in the game environment.'),
        ],
        'exam_tips': [
            'Consider both the sound file and the event or state that triggers it.',
            'Test audio across settings and devices as well as in the default setup.',
            'Use tools to support listening, not to replace judging the player experience.',
        ],
    },
    {
        'number': 5,
        'title': 'Game Level Testing',
        'minutes': 65,
        'intro': 'Level testing checks whether a space is playable, understandable, balanced, and technically sound from entry to completion.',
        'sections': [
            {
                'title': '5.1 Level Design Principles and Concepts',
                'summary': 'Level design shapes navigation, challenge, pacing, player goals, and the relationship between space and game mechanics.',
                'points': [
                    'A level should communicate routes, objectives, hazards, and useful points of interest.',
                    'Difficulty and pacing should fit player ability and the progression expected by the game.',
                    'Geometry and objects must support intended movement while avoiding unintended barriers or exploits.',
                ],
                'example': 'A level meant to teach wall-jumping places a safe practice area before using the mechanic over a dangerous gap.',
            },
            {
                'title': '5.2 Stages and Execution of Game Level Testing',
                'summary': 'Level testing follows the experience through navigation, encounters, objectives, and completion conditions.',
                'points': [
                    'Check routes, spawn points, checkpoints, triggers, obstacles, and progression gates.',
                    'Explore different player strategies, including sequence breaks, getting stuck, and revisiting earlier areas.',
                    'Verify that level completion and failure states update the game consistently.',
                ],
                'example': 'A tester reaches a checkpoint, leaves the intended route, and returns to confirm the gate and objective state are still correct.',
            },
            {
                'title': '5.3 Tools Support for Game Level Testing',
                'summary': 'Level tools help testers inspect geometry, triggers, paths, object placement, and progression state.',
                'points': [
                    'Debug views can expose collision boundaries, navigation data, triggers, and hidden objects.',
                    'Automated traversal or checkpoint scripts can repeat common paths and regression scenarios.',
                    'Tool-assisted findings still need in-game confirmation from a player viewpoint.',
                ],
                'example': 'A collision overlay reveals a gap between two floor meshes that lets a character fall outside the playable area.',
            },
        ],
        'key_terms': [
            ('Level', 'A playable area or stage with defined objectives and progression.'),
            ('Checkpoint', 'A saved progression point from which play can resume.'),
            ('Trigger', 'A condition or region that starts a game event when activated.'),
            ('Collision boundary', 'The shape used to determine whether objects can pass through or contact one another.'),
        ],
        'exam_tips': [
            'Test more than the intended route; include alternate paths and boundary behavior.',
            'Connect level design goals such as pacing and navigation to observable player behavior.',
        ],
    },
    {
        'number': 6,
        'title': 'Game Controllers Testing',
        'minutes': 95,
        'intro': 'Controller testing checks that player inputs are recognized, mapped, and communicated reliably across supported devices and game states.',
        'sections': [
            {
                'title': '6.1 Principles and Concepts of Game Controllers',
                'summary': 'Controllers differ in inputs, layout, capabilities, connectivity, and accessibility options.',
                'points': [
                    'Inputs may include buttons, sticks, triggers, touch, motion, or specialized controls.',
                    'Mappings and feedback must be consistent with the game’s instructions and current context.',
                    'Device, platform, connection state, and accessibility configuration can change how input is experienced.',
                ],
                'example': 'A racing game should treat an analog trigger as a gradual throttle but still give a clear response when a player uses a digital button.',
            },
            {
                'title': '6.2 Approaches to Testing Controllers in Game Products',
                'summary': 'Controller tests check mappings, responsiveness, simultaneous inputs, disconnection, and behavior across game states.',
                'points': [
                    'Verify every documented input and remapping option in menus, gameplay, and pause states.',
                    'Check repeated, held, combined, and rapid inputs for missed or duplicated actions.',
                    'Test connection loss, reconnect, controller switching, and supported alternate devices.',
                ],
                'example': 'A tester disconnects a wireless controller during a pause menu and confirms that the game pauses safely and accepts input after reconnection.',
            },
            {
                'title': '6.3 Tools Support for Game Controllers Testing',
                'summary': 'Controller tools can show raw inputs, mappings, latency, and device status during gameplay.',
                'points': [
                    'Input monitors help compare physical actions with the signals received by the game.',
                    'Automated input playback can repeat common sequences but should be checked against real devices.',
                    'Capture device model, connection method, platform, and configuration when reporting an issue.',
                ],
                'example': 'An input monitor shows a trigger reaching full value before it is physically pressed halfway, helping isolate a calibration problem.',
            },
        ],
        'key_terms': [
            ('Input mapping', 'The association between a physical control and an in-game action.'),
            ('Analog input', 'An input that can represent a range of values rather than only on or off.'),
            ('Latency', 'Delay between an action and the system response.'),
            ('Haptic feedback', 'Tactile signals, such as vibration, produced by a controller.'),
        ],
        'exam_tips': [
            'Include controller configuration and platform details in test conditions.',
            'Test both ordinary controls and connection or remapping edge cases.',
            'Distinguish a physical device problem from an input-mapping or game-response defect.',
        ],
    },
    {
        'number': 7,
        'title': 'Localization Testing',
        'minutes': 155,
        'intro': 'Localization adapts a game for language and regional expectations. Testing checks that translated content and the full experience work in context.',
        'sections': [
            {
                'title': '7.1 Principles and Concepts of Localization Testing',
                'summary': 'Localization testing checks linguistic quality, cultural fit, technical presentation, and behavior in each target locale.',
                'points': [
                    'Language changes can affect text length, line breaks, fonts, dialogue timing, and user-interface layout.',
                    'Regional formats, symbols, units, reading direction, and cultural expectations may change product behavior.',
                    'Test localized content in context rather than relying only on isolated translation review.',
                ],
                'example': 'A translated menu label is longer than the original and overlaps the adjacent button in a localized build.',
            },
            {
                'title': '7.2 Types of Localization Defects and Their Causes',
                'summary': 'Localization defects can come from inaccurate translation, missing context, encoding, layout limits, or incorrect locale rules.',
                'points': [
                    'Look for untranslated or truncated text, inconsistent terminology, wrong fonts, broken characters, and inappropriate content.',
                    'Check date, number, currency, measurement, and sorting behavior for the selected locale.',
                    'Defects may originate in source content, translation workflow, encoding, or assumptions in the software.',
                ],
                'example': 'A price is displayed with the wrong decimal convention for a locale, making a valid amount appear ten times larger.',
            },
            {
                'title': '7.3 Localization Testing Approaches and Execution',
                'summary': 'A localization test approach combines language review with functional checks using locale-specific settings and content.',
                'points': [
                    'Check translations with context, approved terminology, and the intended audience in mind.',
                    'Exercise menus, subtitles, voice, input, and gameplay with different text lengths and writing systems.',
                    'Separate language defects from software defects while recording locale, build, and reproduction steps.',
                ],
                'example': 'A tester changes the game to a right-to-left language and verifies that menus, navigation order, and mixed-language player names remain usable.',
            },
            {
                'title': '7.4 Tools Support for Localization Testing',
                'summary': 'Localization tools help manage translated strings, compare versions, find missing content, and inspect display problems.',
                'points': [
                    'String-management systems can track source text, translation status, context, and review history.',
                    'Automated checks can detect missing translations, placeholder errors, and likely text overflow.',
                    'Human review is needed to assess meaning, tone, cultural suitability, and in-game context.',
                ],
                'example': 'A localization build check flags a missing placeholder in a translated quest message, then a reviewer verifies the corrected line in the scene.',
            },
        ],
        'key_terms': [
            ('Localization', 'Adapting a product for a language, region, or culture.'),
            ('Locale', 'A set of language and regional conventions used by software.'),
            ('Internationalization', 'Designing software so it can be adapted to different locales.'),
            ('Pseudo-localization', 'Using altered sample text to reveal layout and character-handling issues before translation.'),
            ('String placeholder', 'A marker in text that is replaced with a value at runtime.'),
        ],
        'exam_tips': [
            'Consider both linguistic correctness and technical presentation in localized builds.',
            'Test locale-specific formats and writing direction, not only translated words.',
            'Use automated tools to find candidates, then apply contextual human review.',
        ],
    },
]
