feature_order = {
    'Eliciting': {
        'Description': [''],
        'Diagnosis': [''],
        'Discovery': [''],
        'Prediction': [''],
        'Prescription': ['']
    },
    'Defining': {
        'Form': ['Pre-defined goals', 'Template-based goals', 'Self-defined goals'],
        'Adjustability': [''],
        'Reason': [''],
        'Abstraction Level': ['Qualitative goals', 'Quantitative goals'],
        'Type': ['Achievement', 'Balance', 'Avoidance', 'Documenting'],
        'Constraints': ['Content', 'Temporal', 'Spatial'],
        'Goal Baseline': ['Absolute goals', 'Relative goals', 'Aggregation goals'],
        'Recurrence': ['One time goal', 'Recurring goal'],
        'Interdependencies': ['Collections', 'Alternatives', 'Sequences', 'Prioritisation', 'Hierarchies']},
    'Setting': {
        'Simultaneity': ['Single', 'Multiple'],
        'Timing': ['Permanent', 'Time-Frame', 'Start Date', 'End Date', ],
        'Feasibility': ['Plausibility', 'Difficulty']
    },
    'Operationalizing': {
        'Constraints': ['Content', 'Temporal', 'Spatial'],
        'Interdependencies': ['Alternatives', 'Sequences']
    },
    'Pursuing': {
        'Time-based reminder': ['Pre-defined time', 'Custom time', 'Custom days', 'Intervals'],
        'Event-based reminder': ['Pre-defined event', 'Custom event'],
        'Context of reminder': ['Goal specific reminder', 'Process specific reminder'],
        'Customization of reminder': ['Snooze reminder', 'Different alert types', 'Skip if completed'],
        'Additional Pursuing Features': ['']
    },
    'Tracking': {
        'Mode': ['Fully-automatic', 'Semi-automatic', 'Manually'],
        'Temporality': ['Immediate', 'Deferred'],
        'Granularity': ['Task', 'Goal'],
        'Adjustability': [''],
        'Verification': ['']
    },
    'Consequencing': {
        'Type': ['Positive', 'Negative'],
        'Persistence': ['Volatile', 'Permanent'],
        'Tangibility': ['Virtual ', 'Real']
    },
    'Reflecting': {
        'Description': [''],
        'Diagnosis': [''],
        'Discovery': [''],
        'Prediction': [''],
        'Prescription': ['']
    }
}

cross_cutting_order = {
    'System': {
        'Integration': [''],
        'Adaptation': [''],
        'Recommendation': ['']
    },
    'Knowledge': {
        'Profiles': [''],
        'Context': [''],
        'Interpretation of User Behaviour': [''],
        'Explanations of System Behaviour': ['']
    },
    'Social': {
        'Relations': [''],
        'Interactions': ['']
    }
}

cross_cutting_order_2 = {
    'System': {
        'Integration': [''],
        'Diversification': ['Adaption', 'Recommendation']
    },
    'Knowledge': {
        'Enrichment': ['Profiles', 'Context'],
        'Derivation': ['Interpretation of User Behaviour', 'Explanation of System Behaviour']
    },
    'Social': {
        'Relations': [''],
        'Interactions': ['']
    }
}

mapping = {
    'Adaptation': 'Diversification',
    'Recommendation': 'Diversification',
    'Profiles': 'Enrichment',
    'Context': 'Enrichment',
    'Interpretation of User Behaviour': 'Derivation',
    'Explanations of System Behaviour': 'Derivation',
    'Relations': 'Relations',
    'Interactions': 'Interactions',
    'Integration': 'Integration'
}

phase_order = ['Eliciting',
               'Defining',
               'Setting',
               'Operationalizing',
               'Pursuing',
               'Tracking',
               'Reflecting',
               'Consequencing'
               ]

apps_2024 = ['Calistree',
             'Cashew',
             'Dreamfora',
             'Duolingo',
             'Earth Hero',
             'Foodvisor',
             'Gikizero',
             'Goalgum',
             'Goalify',
             'Goals: Erreiche deine Ziele',
             'GoodBudget',
             'Habitica',
             'Habitify',
             'JouleBug',
             'Khan Academy',
             'Meditopia',
             'PackPoint',
             'Pin Traveler',
             'Reach it',
             'Sololearn',
             'Tain',
             'Timelog',
             'Timey',
             'Todoist',
             'Way of Life',
             'Workouts zuhause',
             'iBucket'
             ]

domain_order = ['Sustainability',
                'Learning',
                'Wellbeing',
                'Productivity',
                'Finance',
                'General',
                'All'
                ]

# define colors for phases
colors = [
    'rgb(182,179,200)',  # Planning
    'rgb(184,198,219)',  # Acting
    'rgb(235,241,170)',  # Analyzing
    'rgb(177,252,163)',  # Social
    'rgb(247,206,70)',  # System
    'rgb(255,255,126)',  # Knowledge
    f'rgb({(182 + 184 + 235 + 177 + 247 + 255) / 6}, {(179 + 198 + 241 + 252 + 206 + 255) / 6}, {(200 + 219 + 170 + 163 + 70 + 126) / 6}'
    # mean af all
]

# define colors for domains
darker_colors = [
    'rgb(155,143,180)',  # 'Sustainability'
    'rgb(147,158,190)',  # 'Learning'
    'rgb(188,192,136)',  # 'Wellbeing'
    'rgb(141,201,130)',  # 'Productivity'
    'rgb(197,164,56)',  # 'Finance'
    'rgb(200,200,120)',  # 'General'
    'rgb(180,000,127)'  # 'All'
]

# make a color map for phases
color_discrete_map = {
    domain: darker_colors[i] for i, domain in enumerate(domain_order)
}