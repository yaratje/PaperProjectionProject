# navigation_config.py

NAV_CONFIG = {
    "main": {
        "image_path": "nav/main_1.png",
        "regions": [
            {
                # goes to "machine1"
                "polygon_rel": [
                    [0.3922,  0.2865],
                    [0.4733,  0.2828],
                    [0.4754,  0.6916],
                    [0.3922,  0.6916],
                ],
                "label": "Go to Machine 1",
                "target": "machine1"
            },
            {
                #goes to "machine2"
                "polygon_rel": [
                    [0.5893,  0.2828],
                    [0.848,  0.2865],
                    [0.8491,  0.3978],
                    [0.5893,  0.3978],
                ],
                "label": "Go to Machine 2",
                "target": "machine2"
            }
            #more regions here
        ]
    },
    "machine1": {
        "image_path": "nav/machine1_1.png",
        "regions": [
            {
                # “back” button in the bottom‐left that returns to "main"
                "polygon_rel": [
[0.019,  0.9217],
[0.0409,  0.9269],
[0.0439,  0.9608],
[0.0175,  0.9608],
                ],
                "label": "Back to Main",
                "target": "main"
            },
            #
        ]
    },
    "machine2": {
        "image_path": "nav/machine2_1.png",
        "regions": [
            {
                "polygon_rel": [
                    [0.019,  0.9217],
[0.0409,  0.9269],
[0.0439,  0.9608],
[0.0175,  0.9608],
                ],
                "label": "Back to Main",
                "target": "main"
            },
            #
        ]
    },
    #
}
