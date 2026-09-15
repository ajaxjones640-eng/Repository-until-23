import json

user_data = [{"id": 1, "user_username": "Travis Scott", "Score": 90210}]

question = [
    [
        {
            "id": 1,
            "category": "Plastic",
            "item_name": "Garrafa PET",
            "image_path": "assets/images/plastic/png1.png",
            "feedback": {
                "correct": "Muito bem! Garrafas PET podem ser recicladas infinitamente se descartadas corretamente.",
                "wrong": "Ops! Embora pareça rígida, a garrafa PET deve ir para a lixeira vermelha de Plástico.",
            },
        },
        {
            "id": 4,
            "category": "Paper",
            "item_name": "Volume of Boruto",
            "image_path": "assets/images/organic/png3.png",
            "feedback": {
                "correct": "Exato! Papelão engordurado não pode ser reciclado como papel comum, indo para o lixo orgânico/compostagem.",
                "wrong": "Cuidado! Muita gente confunde, mas o papelão com óleo de pizza não pode",
            },
        },
        {
            "id": 3,
            "category": "Organic",
            "item_name": "Caixa de Pizza Suja",
            "image_path": "assets/images/organic/png3.png",
            "feedback": {
                "correct": "Exato! Papelão engordurado não pode ser reciclado como papel comum, indo para o lixo orgânico/compostagem.",
                "wrong": "Cuidado! Muita gente confunde, mas o papelão com óleo de pizza não pode ser reciclado na lixeira de Papel.",
            },
        },
    ]
]
