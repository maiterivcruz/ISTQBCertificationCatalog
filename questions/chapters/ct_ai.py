"""Plain-language study chapters for ISTQB Certified Tester AI Testing."""

CHAPTERS = [
    {
        'number': 1,
        'title': 'Introduction to Artificial Intelligence',
        'minutes': 120,
        'intro': 'Build a practical vocabulary for AI and see how AI-based systems differ from conventional software.',
        'sections': [
            {
                'title': '1.1 AI foundations and system types',
                'summary': 'Artificial intelligence (AI) describes techniques that let software perform tasks associated with human intelligence. AI-based systems often infer behavior from data, while conventional software follows rules written directly by developers.',
                'points': [
                    'A conventional program applies explicit instructions; an AI system may learn a model from examples and use it to make predictions.',
                    'Narrow AI targets a bounded task. General and super AI describe broader hypothetical capabilities, not ordinary deployed products.',
                    'Machine learning (ML) is one way to build AI; deep learning uses multi-layer neural networks, and generative AI creates new content.',
                ],
                'example': 'A shop can calculate tax with a fixed formula, but use a learned model to predict which products a customer may want next.',
            },
            {
                'title': '1.2 AI applications and lifecycle',
                'summary': 'AI systems combine models with data, software, people, and operating processes. Their behavior can change when data or a model changes, so quality must be considered throughout the lifecycle.',
                'points': [
                    'Identify the intended use, users, and decisions before selecting an AI technique.',
                    'Distinguish the model from the surrounding system that collects inputs, applies outputs, and handles exceptions.',
                    'Monitor deployed behavior because real-world data can differ from training data.',
                ],
                'example': 'A clinic’s appointment system may use an ML model to flag likely missed visits, while staff decide how to contact patients and monitor whether the predictions remain useful.',
            },
        ],
        'key_terms': [
            ('Artificial intelligence', 'Methods that enable software to perform tasks commonly associated with human intelligence.'),
            ('Machine learning', 'An approach that derives a model from data rather than encoding every decision as a fixed rule.'),
            ('Deep learning', 'Machine learning based on neural networks with multiple processing layers.'),
            ('Narrow AI', 'AI designed for a specific task or limited range of tasks.'),
        ],
        'exam_tips': [
            'Separate AI, machine learning, deep learning, and generative AI by their relationship; they are not synonyms.',
            'When a question describes a system, distinguish its learned model from the complete product and its operating context.',
        ],
    },
    {
        'number': 2,
        'title': 'Quality Characteristics for AI-Based Systems',
        'minutes': 45,
        'intro': 'AI quality includes familiar software concerns plus characteristics that depend on data, learning, and model behavior.',
        'sections': [
            {
                'title': '2.1 Quality characteristics',
                'summary': 'An AI system must be fit for its intended use, not merely accurate on a test set. Quality evaluation considers the model, its data, the complete system, and effects on people.',
                'points': [
                    'Measure functional performance with suitable metrics, but also consider robustness, explainability, fairness, and security where relevant.',
                    'A model can perform well overall and still fail for an important subgroup or uncommon condition.',
                    'The appropriate quality priorities depend on potential harm, user expectations, and the operating environment.',
                ],
                'example': 'A loan-screening model may have high average accuracy but produce more false rejections for one demographic group, making fairness a necessary quality concern.',
            },
            {
                'title': '2.2 Acceptance criteria for AI systems',
                'summary': 'Acceptance criteria turn business needs into observable conditions for deciding whether an AI system is suitable. Criteria should account for uncertainty and the consequences of different errors.',
                'points': [
                    'Set measurable thresholds for relevant performance and quality characteristics before acceptance testing.',
                    'Define the data, population, and operating conditions against which each threshold applies.',
                    'Consider false positives and false negatives separately when their impacts differ.',
                    'Agree how to handle uncertain predictions, exceptions, and changes after deployment.',
                ],
                'example': 'A fraud detector could require a minimum recall on a representative holdout set while also capping false alerts per thousand legitimate transactions.',
            },
        ],
        'key_terms': [
            ('Robustness', 'The ability to maintain useful behavior despite expected variation or disruption.'),
            ('Explainability', 'The degree to which people can understand the basis or behavior of a system.'),
            ('False positive', 'A negative case incorrectly classified as positive.'),
            ('Acceptance criterion', 'A condition that must be met for a product or feature to be accepted.'),
        ],
        'exam_tips': [
            'Match quality characteristics to the system’s intended use and risks rather than assuming accuracy is enough.',
            'Check that acceptance thresholds identify the target population, test data, and error types being measured.',
        ],
    },
    {
        'number': 3,
        'title': 'Machine Learning',
        'minutes': 375,
        'intro': 'Follow the ML workflow from problem framing and data preparation through model evaluation.',
        'sections': [
            {
                'title': '3.1 Learning forms and workflow',
                'summary': 'Machine learning approaches differ in the feedback available during learning. A typical workflow frames a problem, prepares data, trains a model, evaluates it, and then monitors its use.',
                'points': [
                    'Supervised learning uses labeled examples; unsupervised learning looks for structure without target labels; reinforcement learning learns from rewards and actions.',
                    'Classification predicts a category, while regression predicts a numeric value.',
                    'Separate training, validation, and test data so final evaluation is not biased by information used to fit or tune the model.',
                    'Pretrained models can be adapted through fine-tuning; retrieval-augmented generation supplies relevant external information at response time.',
                ],
                'example': 'A delivery company trains a supervised classifier on labeled late and on-time deliveries, then uses separate validation and test records to compare candidate models.',
            },
            {
                'title': '3.2 Data for machine learning',
                'summary': 'Data quality and preparation shape what an ML model can learn. Preparation makes data usable while preserving the meaning needed for a fair evaluation.',
                'points': [
                    'Check accuracy, completeness, consistency, relevance, representativeness, and possible label errors.',
                    'Clean or transform data, encode features, and handle missing values using methods appropriate to the problem.',
                    'Avoid leakage: information unavailable at prediction time must not enter training features or evaluation.',
                    'Keep data provenance and preparation steps traceable so results can be reproduced.',
                ],
                'example': 'For a loan default model, a team removes a post-approval field that would reveal the outcome and checks that the training set includes applicants from all intended regions.',
            },
            {
                'title': '3.3 Classification performance metrics',
                'summary': 'A confusion matrix records correct and incorrect positive and negative predictions. Metrics summarize different aspects of classification and must be interpreted in context.',
                'points': [
                    'Accuracy = (TP + TN) / (TP + TN + FP + FN). It is the proportion of all predictions that are correct.',
                    'Precision = TP / (TP + FP); recall = TP / (TP + FN). Precision concerns positive predictions, while recall concerns actual positives.',
                    'F1 = 2 × precision × recall / (precision + recall), the harmonic mean of precision and recall.',
                    'For imbalanced data, accuracy alone can hide poor detection of a rare but important class.',
                ],
                'example': 'In medical screening, the team may prioritize recall to miss fewer cases, then assess the additional false alarms using precision.',
            },
            {
                'title': '3.4 Neural networks',
                'summary': 'A neural network transforms input values through connected layers with adjustable weights. Training adjusts those weights to reduce an error measure on examples.',
                'points': [
                    'Input, hidden, and output layers have different roles in transforming information and producing predictions.',
                    'Training iteratively updates weights; hyperparameters such as learning rate and network size control the training process.',
                    'Overfitting occurs when a model fits training examples too closely and performs poorly on unseen cases.',
                    'Use independent data and suitable controls to assess generalization rather than relying on training scores.',
                ],
                'example': 'A photo classifier that memorizes backgrounds from its training images may label a new animal incorrectly when the same animal is photographed outdoors.',
            },
        ],
        'key_terms': [
            ('Supervised learning', 'Learning from examples that include the expected target or label.'),
            ('Data leakage', 'Use of information in training or evaluation that would not legitimately be available for prediction.'),
            ('Confusion matrix', 'A table of actual versus predicted classes used to derive classification metrics.'),
            ('Overfitting', 'A model’s poor generalization after fitting training data too closely.'),
            ('Retrieval-augmented generation', 'A method that retrieves external information to ground a generated response.'),
        ],
        'exam_tips': [
            'For metric calculations, identify TP, TN, FP, and FN first, then apply the exact formula.',
            'Choose a metric based on the cost of missed positives and false alerts; do not treat accuracy as universally sufficient.',
            'Keep training, validation, and test purposes distinct, and look for leakage when results appear unrealistically strong.',
        ],
    },
    {
        'number': 4,
        'title': 'Testing AI-Based Systems',
        'minutes': 195,
        'intro': 'Combine conventional software testing with evaluation of learned behavior and AI-specific risks.',
        'sections': [
            {
                'title': '4.1 Testing approach for AI systems',
                'summary': 'AI testing covers the surrounding software as well as data, model behavior, and interactions between them. Oracle challenges and uncertain outputs call for carefully chosen evaluation methods.',
                'points': [
                    'Test conventional requirements, interfaces, error handling, and non-functional behavior as for other software.',
                    'Add tests for model quality, data quality, robustness, and appropriate behavior across relevant populations.',
                    'Use expected results, human judgment, statistical measures, or metamorphic relations when one exact output is unavailable.',
                    'Trace requirements and risks to tests and evaluation evidence.',
                ],
                'example': 'A route recommendation product can test its account and map interfaces conventionally, then assess whether route suggestions remain valid across traffic patterns and neighborhoods.',
            },
            {
                'title': '4.2 Generative AI and large language models',
                'summary': 'Generative AI produces outputs from prompts and context, so testing must assess both the response and the conditions that shaped it. Plausible wording is not proof of correctness.',
                'points': [
                    'Evaluate factuality, relevance, completeness, safety, and consistency against task-specific criteria.',
                    'Vary prompts, context, and input phrasing because small changes may alter the generated output.',
                    'Check for hallucinations, bias, privacy exposure, and unsafe content.',
                    'Record model version, prompt, settings, and retrieved context to make evaluations interpretable.',
                ],
                'example': 'A support chatbot is tested with paraphrased refund questions and misleading policy excerpts to check whether it gives grounded, consistent guidance.',
            },
            {
                'title': '4.3 Test levels and ML systems',
                'summary': 'Testing is useful at multiple levels, from data and model components to end-to-end decisions. The model’s integration and operational setting can introduce failures not visible in isolated evaluation.',
                'points': [
                    'Test data transformations, model components, interfaces, and the complete system at appropriate levels.',
                    'Check interactions between model outputs and downstream rules or human decisions.',
                    'Use realistic deployment conditions to examine performance, resource use, and fallback behavior.',
                ],
                'example': 'A claims triage model passes isolated accuracy tests, but integration testing reveals that its confidence score is interpreted backwards by the case-management service.',
            },
        ],
        'key_terms': [
            ('Test oracle', 'A means of deciding whether an observed result is acceptable.'),
            ('Metamorphic testing', 'Testing relationships between outputs when exact expected outputs are difficult to define.'),
            ('Hallucination', 'Generated content that is unsupported or incorrect but presented as plausible.'),
            ('End-to-end testing', 'Testing a complete workflow across integrated system components.'),
        ],
        'exam_tips': [
            'Separate model evaluation from testing the complete product and its integrations.',
            'For generative output, assess against explicit task criteria and include variation in prompts and context.',
        ],
    },
    {
        'number': 5,
        'title': 'Input Data Testing for Machine Learning Systems',
        'minutes': 180,
        'intro': 'Assess whether inputs used to train and operate an ML system are reliable, relevant, and representative.',
        'sections': [
            {
                'title': '5.1 Data quality and suitability',
                'summary': 'Input data should represent the problem and the people or conditions where the model will be used. Poor or skewed data can produce a model that fails despite sound implementation.',
                'points': [
                    'Check completeness, correctness, consistency, freshness, and relevance of records and labels.',
                    'Compare the data distribution with the intended operating population and investigate underrepresented groups.',
                    'Review collection and labeling processes for ambiguity, bias, and systematic gaps.',
                ],
                'example': 'A speech-recognition provider checks recordings across accents and noisy environments before claiming that its training data represents all intended callers.',
            },
            {
                'title': '5.2 Testing data preparation and features',
                'summary': 'Data pipelines can introduce defects while filtering, joining, labeling, or transforming records. Testing these steps helps protect the relationship between source information and model inputs.',
                'points': [
                    'Verify transformations, feature calculations, data types, boundaries, and missing-value handling.',
                    'Check that train and test partitions are independent and that duplicates or related records do not cross partitions inappropriately.',
                    'Detect leakage, invalid labels, unexpected class imbalance, and changes in input schema.',
                ],
                'example': 'A churn dataset is split by customer rather than by individual transaction so the same customer cannot appear in both training and test sets.',
            },
            {
                'title': '5.3 Operational input monitoring',
                'summary': 'After release, incoming data may drift from the data used for training. Monitoring can identify changed distributions and trigger investigation or retraining decisions.',
                'points': [
                    'Establish expected ranges and distributions for important inputs.',
                    'Detect missing, malformed, out-of-range, or shifted data before it silently degrades predictions.',
                    'Define responses to data drift, including investigation, fallback, or controlled model updates.',
                ],
                'example': 'After a bank changes its application form, a monitoring alert detects that a previously common employment field is now mostly empty.',
            },
        ],
        'key_terms': [
            ('Representativeness', 'How well a dataset reflects the population and conditions where a model is intended to operate.'),
            ('Data drift', 'A change over time in the distribution or characteristics of incoming data.'),
            ('Feature', 'An input variable used by a model to produce a prediction.'),
            ('Label', 'The expected outcome associated with a training example.'),
        ],
        'exam_tips': [
            'Assess data quality in relation to intended use; a large dataset is not automatically a representative one.',
            'Look for leakage and partition contamination when test results seem too optimistic.',
            'Distinguish data quality checks during preparation from monitoring of live inputs after release.',
        ],
    },
    {
        'number': 6,
        'title': 'Model Testing for Machine Learning Systems',
        'minutes': 225,
        'intro': 'Evaluate model behavior beyond a single score, including resilience, fairness, and generalization.',
        'sections': [
            {
                'title': '6.1 Model behavior and performance',
                'summary': 'Model tests evaluate whether predictions meet requirements on data that reflects expected use. Results must be interpreted with the model’s decision context and limitations in mind.',
                'points': [
                    'Use held-out data and suitable metrics to measure model performance on unseen examples.',
                    'Examine errors by class, subgroup, and operating condition instead of reporting only an aggregate score.',
                    'Compare model versions against a baseline and investigate meaningful regressions.',
                ],
                'example': 'A hiring-screening team reports precision and recall separately for job families and candidate groups rather than relying on one overall accuracy figure.',
            },
            {
                'title': '6.2 Robustness and model-specific tests',
                'summary': 'Robustness testing probes whether small, realistic input changes cause unacceptable prediction changes. The right techniques depend on the model and its purpose.',
                'points': [
                    'Test boundary values, noisy inputs, plausible perturbations, and unexpected but valid combinations.',
                    'Use adversarial examples where relevant to reveal inputs deliberately crafted to mislead a model.',
                    'Apply metamorphic relations when the precise expected prediction is unknown but a relationship should hold.',
                    'Check confidence or uncertainty handling and the system’s behavior when confidence is low.',
                ],
                'example': 'A road-sign classifier should not change its result when a photo is slightly brighter, but should signal uncertainty for a badly obscured sign.',
            },
            {
                'title': '6.3 Fairness, explainability, and change',
                'summary': 'Model assessment should consider the impacts of decisions on people and whether behavior remains dependable as models and data evolve.',
                'points': [
                    'Compare relevant outcomes across groups using measures suited to the use case and applicable requirements.',
                    'Check whether explanations are useful and consistent enough for the decisions they support.',
                    'Re-evaluate after retraining, feature changes, or shifts in the operating environment.',
                ],
                'example': 'A benefits eligibility model is reviewed for different false-denial rates across regions, and its decision rationale is checked before staff rely on it.',
            },
        ],
        'key_terms': [
            ('Generalization', 'A model’s ability to perform usefully on new data beyond its training examples.'),
            ('Adversarial example', 'An input deliberately altered to cause a model to make an incorrect prediction.'),
            ('Baseline', 'A reference result used to judge the performance of another model or version.'),
            ('Uncertainty', 'The model’s limited confidence or reliability about a prediction.'),
        ],
        'exam_tips': [
            'Use held-out representative data for evaluation and inspect subgroup results as well as overall metrics.',
            'Choose robustness techniques to match the model input and realistic threats; do not assume one technique fits every model.',
        ],
    },
    {
        'number': 7,
        'title': 'Machine Learning Development Testing',
        'minutes': 30,
        'intro': 'Treat the ML development pipeline as a system that needs repeatable checks, not as a one-time model experiment.',
        'sections': [
            {
                'title': '7.1 Testing the ML development pipeline',
                'summary': 'The pipeline covers data processing, training, evaluation, packaging, and delivery. Testing its steps helps ensure that an approved model can be rebuilt and released reliably.',
                'points': [
                    'Automate repeatable checks for data, code, configuration, and model artifacts.',
                    'Version datasets, code, parameters, and model outputs so a release can be traced and reproduced.',
                    'Gate deployment on agreed evaluation thresholds and retain evidence for review.',
                ],
                'example': 'A retailer’s build pipeline rejects a newly trained recommendation model if its validation score drops below the agreed baseline or the feature schema changes unexpectedly.',
            },
            {
                'title': '7.2 Reproducibility and ongoing checks',
                'summary': 'Reproducible development makes model results easier to investigate and compare. The pipeline also needs checks for dependency changes and behavior after deployment.',
                'points': [
                    'Record library versions, random seeds, training configuration, and data lineage where feasible.',
                    'Run regression checks when code, data, dependencies, or model parameters change.',
                    'Connect production monitoring to a defined review and retraining process.',
                ],
                'example': 'When a model’s score changes after a library upgrade, the team can compare the dependency versions and rerun the same training data and configuration.',
            },
        ],
        'key_terms': [
            ('ML pipeline', 'The connected activities and tools used to prepare data, train, evaluate, and deliver a model.'),
            ('Reproducibility', 'The ability to repeat an experiment and understand or recreate its results.'),
            ('Model artifact', 'A saved, deployable output of model training.'),
        ],
        'exam_tips': [
            'Remember that ML development testing includes the pipeline and data handling as well as the model itself.',
            'Traceable versions and repeatable checks help explain changes between model releases.',
        ],
    },
]
