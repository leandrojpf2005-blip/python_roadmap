rooms = {
    'bedroom': {
        'description': 'A small room with a bed, a wooden table and an old wardrobe.',
        'containers': {
            'wardrobe': ['old_cloth', 'backpack'], 
            'wooden_table': ['unlabelled_pills'], 
            'bed': ['spawn', 'locker'],
            'painting': ['code_4832']
        },
        'locked': False,
        'connections': ['hallway']
    },

    'hallway': {
        'description': 'A tiny corridor that connects all the divisions.',
        'containers': {},
        'locked': False,
        'connections': ['bedroom', 'openplan', 'restroom']
    },

    'openplan': {
        'description': 'A tiny living room mixed with a kitchen.',
        'containers': {
            'sofa': [],
            'tvcabinet': ['aa_batteries', 'lighter', 'cd'],
            'kitchencabinet': ['knife', 'glass_bottle', 'electric_screwdriver'],
            'metal_plate': []   # requires screwdriver + batteries
        },
        'locked': True,
        'connections': ['hallway', 'end']
    },

    'restroom': {
        'description': 'A normal-sized bathroom with a few cabinets.',
        'containers': {
            'vanity_cabinet': ['alcohol', 'dressings'],
            'false_wall': ['final_key']   # requires knife to cut open
        },
        'locked': False,
        'connections': ['hallway']
    },

    'locker': {
        'locked': True,
        'code': '4832',
        'contains': ['openplan_key']
    },

    'end': {
        'description': 'A small exit room with a heavy locked door leading outside.',
        'containers': {},
        'locked': True,
        'connections': ['openplan']
    },
}
