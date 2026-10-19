"""Plain-language study chapters for ISTQB Testing with Generative AI."""

CHAPTERS = [
    {
        'number': 1,
        'title': 'Introduction to Generative AI for Software Testing',
        'minutes': 100,
        'intro': 'Learn what generative AI can do for testing and where a tester’s judgment remains essential.',
        'sections': [
            {
                'title': '1.1 Generative AI foundations',
                'summary': 'Generative AI creates new content from learned patterns. Large language models (LLMs) generate text, while multimodal models can work across text, images, or other input and output types.',
                'points': [
                    'Symbolic AI uses explicit representations and rules; classical ML learns patterns, and deep learning uses layered neural networks.',
                    'An LLM predicts likely tokens from the prompt and context; fluent output is not a guarantee of truth.',
                    'Foundation models are broadly trained, instruction-tuned models follow requests more effectively, and reasoning models are optimized for multi-step tasks.',
                    'Multimodal and vision-language models can process combinations of text and visual information.',
                ],
                'example': 'A vision-language model can inspect a screenshot and describe a missing checkout label, but a tester still verifies that the observation is correct.',
            },
            {
                'title': '1.2 Applying GenAI to testing',
                'summary': 'Generative AI can assist with language-heavy testing tasks, but it is an assistant whose output must be checked against real requirements and system behavior.',
                'points': [
                    'Potential uses include summarizing requirements, proposing test ideas, drafting test data, and helping explain failures.',
                    'Chatbots offer conversational access, while testing applications may connect models to repositories, test tools, or workflow data.',
                    'Choose tasks with reviewable output and clear value; retain human responsibility for important test decisions.',
                ],
                'example': 'A tester asks an internal assistant to propose boundary cases for a booking rule, then checks every suggestion against the approved specification.',
            },
        ],
        'key_terms': [
            ('Generative AI', 'AI that creates new content such as text, images, or code.'),
            ('Large language model', 'A model trained to process and generate language, often by predicting the next token.'),
            ('Foundation model', 'A broadly trained model that can be adapted to a range of tasks.'),
            ('Multimodal model', 'A model that accepts or produces more than one type of content.'),
        ],
        'exam_tips': [
            'A plausible LLM answer can still be wrong; separate fluency from factual correctness.',
            'Match a GenAI testing use case to the model capability and preserve human review.',
        ],
    },
    {
        'number': 2,
        'title': 'Prompt Engineering for Effective Software Testing',
        'minutes': 365,
        'intro': 'Create prompts that give a model useful context and evaluate its results instead of accepting them blindly.',
        'sections': [
            {
                'title': '2.1 Effective prompt development',
                'summary': 'A prompt frames the task and supplies information that influences the response. Clear structure makes it easier for a model to produce relevant, reviewable material.',
                'points': [
                    'State the objective, role or perspective, relevant context, constraints, and desired output format.',
                    'Core techniques include zero-shot instructions, examples (few-shot), and decomposing a larger task into steps.',
                    'System prompts establish persistent behavior; user prompts provide the immediate task and input.',
                    'Avoid exposing confidential data and remove ambiguity that could lead to unsupported assumptions.',
                ],
                'example': 'Instead of asking for “tests,” a tester provides a versioned refund rule, asks for boundary cases, and requests a table with condition, expected result, and rationale.',
            },
            {
                'title': '2.2 Using prompts across test activities',
                'summary': 'Prompting can support test analysis, design, implementation, regression, monitoring, and control. The prompt should fit the task and the available test basis.',
                'points': [
                    'For analysis, ask for conditions, ambiguities, and risk areas grounded in supplied requirements.',
                    'For design and implementation, request cases or code in a specified format, then review coverage and correctness.',
                    'For regression or monitoring, provide relevant change and result context and keep generated actions under control.',
                    'Choose prompting techniques according to task complexity, repeatability, and the need for traceability.',
                ],
                'example': 'A tester supplies a change request and existing test inventory, then asks the model to identify affected regression cases with a reason for each link.',
            },
            {
                'title': '2.3 Evaluate results and refine prompts',
                'summary': 'Prompt quality is judged by the usefulness of its outputs for the testing task. Evaluation and iterative refinement can improve results, but do not replace independent verification.',
                'points': [
                    'Assess correctness, relevance, completeness, clarity, consistency, and effort saved using task-appropriate measures.',
                    'Compare responses against a known test basis or reviewed reference set where available.',
                    'Change one prompt element at a time when practical, then re-evaluate on varied examples.',
                    'Record prompt versions and model settings when output quality must be compared or reproduced.',
                ],
                'example': 'A team scores generated test cases for requirement alignment and missing boundaries, then revises its prompt and repeats the same evaluation set.',
            },
        ],
        'key_terms': [
            ('Prompt', 'Instructions and context provided to a generative model.'),
            ('Few-shot prompting', 'Giving the model a small number of examples to guide its response.'),
            ('System prompt', 'Instructions that establish persistent behavior for a model interaction.'),
            ('Prompt refinement', 'Iteratively adjusting a prompt based on evaluation of its outputs.'),
            ('Evaluation metric', 'A defined measure used to judge the quality of model output for a task.'),
        ],
        'exam_tips': [
            'Choose prompts that give relevant context, constraints, and a reviewable output format.',
            'Know the difference between system and user prompts and between zero-shot and example-based prompting.',
            'Evaluate outputs against task criteria and the test basis; prompt improvement alone does not establish correctness.',
        ],
    },
    {
        'number': 3,
        'title': 'Managing Risks of Generative AI in Software Testing',
        'minutes': 160,
        'intro': 'Recognize model, data, security, and environmental risks before using GenAI in testing work.',
        'sections': [
            {
                'title': '3.1 Hallucinations, reasoning errors, and bias',
                'summary': 'Generated responses may invent facts, reason incorrectly, or reflect bias in training data and model behavior. Non-deterministic outputs mean the same request may not always produce the same answer.',
                'points': [
                    'Verify claims against trusted sources and requirements; do not treat confident wording as evidence.',
                    'Use independent review, structured checks, and representative examples to expose reasoning gaps and bias.',
                    'Reduce variability through controlled prompts and settings, but design for output differences that remain.',
                    'Keep a human decision-maker responsible for consequential test outcomes.',
                ],
                'example': 'A model invents a non-existent API option in a test script; a reviewer checks the generated code against the real interface before execution.',
            },
            {
                'title': '3.2 Privacy and security risks',
                'summary': 'Prompts, model services, and connected tools can expose sensitive information or create new attack paths. Safe use depends on data handling and the security of the full workflow.',
                'points': [
                    'Do not submit secrets, personal information, or proprietary material unless approved controls explicitly permit it.',
                    'Assess retention, access, processing location, and provider terms for external services.',
                    'Consider prompt injection, insecure generated code, and vulnerabilities in model-enabled test tools.',
                    'Apply least privilege, input filtering, output review, and security testing to connected components.',
                ],
                'example': 'A tester replaces real patient identifiers with synthetic data before asking an approved model to help draft test scenarios.',
            },
            {
                'title': '3.3-3.4 Energy impact, regulation, and frameworks',
                'summary': 'Use of GenAI consumes computing resources and may be subject to regulatory or organizational obligations. Teams should choose proportionate models and account for governance needs.',
                'points': [
                    'Consider the energy and environmental cost of model training and repeated inference.',
                    'Select a model size and usage pattern appropriate to the task rather than defaulting to the largest option.',
                    'Identify applicable AI laws, standards, and internal policies for the system and its intended use.',
                    'Document risk controls, ownership, and evidence needed to demonstrate responsible use.',
                ],
                'example': 'A team uses a small local model for routine test-name suggestions and reserves a more resource-intensive model for tasks that need its broader capability.',
            },
        ],
        'key_terms': [
            ('Hallucination', 'Plausible-sounding generated content that is unsupported or false.'),
            ('Prompt injection', 'Malicious or unexpected instructions that attempt to override intended model behavior.'),
            ('Non-determinism', 'Variation in outputs across repeated runs of the same nominal task.'),
            ('Data minimization', 'Limiting the amount of personal or sensitive information used to what is necessary.'),
        ],
        'exam_tips': [
            'Treat hallucination, bias, privacy, security, and variability as distinct risks with suitable controls.',
            'Consider the full model-enabled toolchain, not only the model’s generated text.',
            'Check governance and environmental impact as part of selecting and operating a GenAI solution.',
        ],
    },
    {
        'number': 4,
        'title': 'LLM-Powered Test Infrastructure for Software Testing',
        'minutes': 110,
        'intro': 'Understand the infrastructure patterns that connect LLMs with testing information, tools, and operations.',
        'sections': [
            {
                'title': '4.1 Architecture and retrieval-augmented generation',
                'summary': 'LLM-powered test infrastructure can connect a model to approved knowledge, testing tools, and application services. Retrieval-augmented generation (RAG) adds relevant retrieved material to the model’s context.',
                'points': [
                    'Identify model, prompt, data, retrieval, tool, and user-interface components and their trust boundaries.',
                    'RAG retrieves relevant sources at request time, helping responses use current project information without retraining the model.',
                    'Check source relevance, access control, freshness, and whether the generated response is actually supported by retrieved content.',
                ],
                'example': 'A test assistant retrieves the current checkout specification and links its suggested cases to the exact requirement passages it used.',
            },
            {
                'title': '4.2 Agents, fine-tuning, and LLMOps',
                'summary': 'Agents can use tools in a sequence, while fine-tuning adapts a model using additional examples. LLMOps supplies practices for deploying, monitoring, and maintaining such systems.',
                'points': [
                    'Constrain agent permissions and actions; require confirmation before destructive or externally visible operations.',
                    'Fine-tuning may adapt behavior, but requires suitable data, evaluation, and ongoing maintenance.',
                    'LLMOps covers model and prompt versioning, deployment, monitoring, access, and rollback.',
                    'Track quality, latency, cost, and safety in production, not only during initial evaluation.',
                ],
                'example': 'An agent may draft a test run but needs an explicit approval step before it launches tests against a shared staging environment.',
            },
        ],
        'key_terms': [
            ('Retrieval-augmented generation', 'Grounding generated responses with information retrieved from an external knowledge source.'),
            ('Agent', 'A model-enabled component that can select and perform actions through connected tools.'),
            ('Fine-tuning', 'Further training a pretrained model using examples to adapt its behavior.'),
            ('LLMOps', 'Operational practices for managing and monitoring LLM-based solutions.'),
        ],
        'exam_tips': [
            'RAG retrieves contextual information at use time; fine-tuning changes model behavior through additional training.',
            'For agents, assess permissions and action safety as well as answer quality.',
        ],
    },
    {
        'number': 5,
        'title': 'Deploying and Integrating Generative AI in Test Organizations',
        'minutes': 80,
        'intro': 'Adopt GenAI deliberately, with a strategy, team capability, and change process that fit testing needs.',
        'sections': [
            {
                'title': '5.1 Adoption roadmap and model selection',
                'summary': 'An adoption roadmap helps an organization explore value and manage risks in a controlled way. Model selection should consider the task, constraints, and complete cost of use.',
                'points': [
                    'Address shadow AI by providing approved options, guidance, and clear data-handling rules.',
                    'Set a strategy for goals, risks, governance, ownership, and success measures.',
                    'Compare LLMs and smaller language models (SLMs) for capability, privacy, latency, cost, and deployment needs.',
                    'Adopt incrementally: experiment, evaluate, pilot, and scale only when evidence supports it.',
                ],
                'example': 'A test organization pilots an approved model for generating draft test data, measures reviewer effort and defect rates, and expands only after a privacy review.',
            },
            {
                'title': '5.2 Managing organizational change',
                'summary': 'Integrating GenAI changes skills, responsibilities, and test workflows. Teams need training and clear process updates so the tool supports rather than weakens testing practice.',
                'points': [
                    'Build skills in prompting, output evaluation, model limitations, data protection, and test design.',
                    'Update workflows to identify when AI assistance is appropriate and how generated material is reviewed and traced.',
                    'Use feedback from testers to improve guidance, training, and adoption decisions.',
                ],
                'example': 'A testing team agrees that AI-drafted cases must include requirement links and receive peer review before joining the maintained regression suite.',
            },
        ],
        'key_terms': [
            ('Shadow AI', 'Use of AI services outside organizationally approved tools or controls.'),
            ('SLM', 'A smaller language model, often selected for constrained tasks or deployment needs.'),
            ('Adoption roadmap', 'A staged plan for evaluating and introducing a technology.'),
            ('Change management', 'Activities that help people and processes transition to a new way of working.'),
        ],
        'exam_tips': [
            'A responsible roadmap includes governance, risk, skills, and measurable value, not just tool selection.',
            'Compare models against practical constraints and the intended testing task, and plan human review of outputs.',
        ],
    },
]
