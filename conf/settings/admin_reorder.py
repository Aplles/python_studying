ADMIN_REORDER = (
    'sites',
    {
        'app': 'models_app',
        "label": "Блоки",
        'models': (
            'models_app.Page',
            'models_app.Block',
            'models_app.CalloutBlock',
            'models_app.DividerBlock',
            'models_app.ImageBlock',
            'models_app.LinkBlock',
            'models_app.TextBlock',
        )
    },
    {
        'app': 'models_app',
        "label": "Пользователи и доступы",
        'models': (
            'models_app.User',
            'models_app.Access',
        )
    },
    {
        'app': 'auth',
        "label": "Группы",
        'models': (
            'auth.Group',
        )
    },
)
