# navigation_config.py

NAV_CONFIG = {
    "main_1_1": {
        "image_path": "nav/main_1_1.png",
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
                "target": "machine1_1"
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
                "target": "machine2_1"
            }
            #more regions
        ]
    },
    "machine1_1": {
        "image_path": "nav/machine1_1_1.png",
        "regions": [
            {
                # “back” 
                "polygon_rel": [
                    [0.019,  0.9217],
                    [0.0409,  0.9269],
                    [0.0439,  0.9608],
                    [0.0175,  0.9608],
                ],
                "label": "Back to Main",
                "target": "main_1_1"
            },
            #
            {
                #open 1
                "polygon_rel": [
                    [0.0368,  0.1569],
                    [0.2224,  0.156],
                    [0.2234,  0.2241],
                    [0.0363,  0.225],
                ],
                "label": "open1",
                "target": "machine1_2"
            },
            {       
                  #open 2
                "polygon_rel": [
                    [0.0373,  0.2526],
                    [0.2219,  0.2526],
                    [0.2234,  0.3216],
                    [0.0359,  0.3224],
                ],
                "label": "open2",
                "target": "machine1_3"
            },
            {       
                  #open 3
                "polygon_rel": [
                    [0.0373,  0.3474],
                    [0.2238,  0.3491],
                    [0.2234,  0.4164],
                    [0.0359,  0.4172],
                ],
                "label": "open3",
                "target": "machine1_4"
            },
            {       
                  #open 3
                "polygon_rel": [
                    [0.7902,  0.7526],
                    [0.9725,  0.7526],
                    [0.9725,  0.9538],
                    [0.7902,  0.9538],
                ],
                "label": "notify",
                "target": "notify"
            }
        ]
    },

          
        "machine1_2": {
        "image_path": "nav/machine1_1_2.png",
        "regions": [
            {
                # “back” 
                "polygon_rel": [
                    [0.019,  0.9217],
                    [0.0409,  0.9269],
                    [0.0439,  0.9608],
                    [0.0175,  0.9608],
                ],
                "label": "Back to Main",
                "target": "main_1_1"
            },
            #
            {
                #open 1
                "polygon_rel": [
                    [0.0368,  0.1569],
                    [0.2224,  0.156],
                    [0.2234,  0.2241],
                    [0.0363,  0.225],
                ],
                "label": "open1",
                "target": "machine1_1"
            },
            {       
                  #open 2
                "polygon_rel": [
                    [0.0373,  0.2526],
                    [0.2219,  0.2526],
                    [0.2234,  0.3216],
                    [0.0359,  0.3224],
                ],
                "label": "open2",
                "target": "machine1_3"
            },
            {       
                  #open 3
                "polygon_rel": [
                    [0.0373,  0.3474],
                    [0.2238,  0.3491],
                    [0.2234,  0.4164],
                    [0.0359,  0.4172],
                ],
                "label": "open3",
                "target": "machine1_4"
            }

        ]
    },
    "machine1_3": {
        "image_path": "nav/machine1_1_3.png",
        "regions": [
            {
                # “back” 
                "polygon_rel": [
                    [0.019,  0.9217],
                    [0.0409,  0.9269],
                    [0.0439,  0.9608],
                    [0.0175,  0.9608],
                ],
                "label": "Back to Main",
                "target": "main_1_1"
            },
            #
            {
                #open 1
                "polygon_rel": [
                    [0.0368,  0.1569],
                    [0.2224,  0.156],
                    [0.2234,  0.2241],
                    [0.0363,  0.225],
                ],
                "label": "open1",
                "target": "machine1_2"
            },
            {       
                  #open 2
                "polygon_rel": [
                    [0.0373,  0.2526],
                    [0.2219,  0.2526],
                    [0.2234,  0.3216],
                    [0.0359,  0.3224],
                ],
                "label": "open2",
                "target": "machine1_1"
            },
            {       
                  #open 3
                "polygon_rel": [
                    [0.0373,  0.3474],
                    [0.2238,  0.3491],
                    [0.2234,  0.4164],
                    [0.0359,  0.4172],
                ],
                "label": "open3",
                "target": "machine1_4"
            }

        ]
    },
    "machine1_4": {
        "image_path": "nav/machine1_1_4.png",
        "regions": [
            {
                # “back” 
                "polygon_rel": [
                    [0.019,  0.9217],
                    [0.0409,  0.9269],
                    [0.0439,  0.9608],
                    [0.0175,  0.9608],
                ],
                "label": "Back to Main",
                "target": "main_1_1"
            },
            #
            {
                #open 1
                "polygon_rel": [
                    [0.0368,  0.1569],
                    [0.2224,  0.156],
                    [0.2234,  0.2241],
                    [0.0363,  0.225],
                ],
                "label": "open1",
                "target": "machine1_2"
            },
            {       
                  #open 2
                "polygon_rel": [
                    [0.0373,  0.2526],
                    [0.2219,  0.2526],
                    [0.2234,  0.3216],
                    [0.0359,  0.3224],
                ],
                "label": "open2",
                "target": "machine1_3"
            },
            {       
                  #open 3
                "polygon_rel": [
                    [0.0373,  0.3474],
                    [0.2238,  0.3491],
                    [0.2234,  0.4164],
                    [0.0359,  0.4172],
                ],
                "label": "open3",
                "target": "machine1_1"
            }

        ]
    },






    "machine2_1": {
        "image_path": "nav/machine2_1_1.png",
        "regions": [
            {
                # “back” 
                "polygon_rel": [
                    [0.019,  0.9217],
                    [0.0409,  0.9269],
                    [0.0439,  0.9608],
                    [0.0175,  0.9608],
                ],
                "label": "Back to Main",
                "target": "main_1_1"
            },
            #
            {
                #open 1
                "polygon_rel": [
                    [0.0368,  0.1569],
                    [0.2224,  0.156],
                    [0.2234,  0.2241],
                    [0.0363,  0.225],
                ],
                "label": "open1",
                "target": "machine2_2"
            },
            {       
                  #open 2
                "polygon_rel": [
                    [0.0373,  0.2526],
                    [0.2219,  0.2526],
                    [0.2234,  0.3216],
                    [0.0359,  0.3224],
                ],
                "label": "open2",
                "target": "machine2_3"
            },
            {       
                  #open 3
                "polygon_rel": [
                    [0.0373,  0.3474],
                    [0.2238,  0.3491],
                    [0.2234,  0.4164],
                    [0.0359,  0.4172],
                ],
                "label": "open3",
                "target": "machine2_4"
            }

        ]
    },
        "machine2_2": {
        "image_path": "nav/machine2_1_2.png",
        "regions": [
            {
                # “back” 
                "polygon_rel": [
                    [0.019,  0.9217],
                    [0.0409,  0.9269],
                    [0.0439,  0.9608],
                    [0.0175,  0.9608],
                ],
                "label": "Back to Main",
                "target": "main_1_1"
            },
            #
            {
                #open 1
                "polygon_rel": [
                    [0.0368,  0.1569],
                    [0.2224,  0.156],
                    [0.2234,  0.2241],
                    [0.0363,  0.225],
                ],
                "label": "open1",
                "target": "machine2_1"
            },
            {       
                  #open 2
                "polygon_rel": [
                    [0.0373,  0.2526],
                    [0.2219,  0.2526],
                    [0.2234,  0.3216],
                    [0.0359,  0.3224],
                ],
                "label": "open2",
                "target": "machine2_3"
            },
            {       
                  #open 3
                "polygon_rel": [
                    [0.0373,  0.3474],
                    [0.2238,  0.3491],
                    [0.2234,  0.4164],
                    [0.0359,  0.4172],
                ],
                "label": "open3",
                "target": "machine2_4"
            }

        ]
    },
    "machine2_3": {
        "image_path": "nav/machine2_1_3.png",
        "regions": [
            {
                # “back” 
                "polygon_rel": [
                    [0.019,  0.9217],
                    [0.0409,  0.9269],
                    [0.0439,  0.9608],
                    [0.0175,  0.9608],
                ],
                "label": "Back to Main",
                "target": "main_1_1"
            },
            #
            {
                #open 1
                "polygon_rel": [
                    [0.0368,  0.1569],
                    [0.2224,  0.156],
                    [0.2234,  0.2241],
                    [0.0363,  0.225],
                ],
                "label": "open1",
                "target": "machine2_2"
            },
            {       
                  #open 2
                "polygon_rel": [
                    [0.0373,  0.2526],
                    [0.2219,  0.2526],
                    [0.2234,  0.3216],
                    [0.0359,  0.3224],
                ],
                "label": "open2",
                "target": "machine2_1"
            },
            {       
                  #open 3
                "polygon_rel": [
                    [0.0373,  0.3474],
                    [0.2238,  0.3491],
                    [0.2234,  0.4164],
                    [0.0359,  0.4172],
                ],
                "label": "open3",
                "target": "machine2_4"
            }

        ]
    },
    "machine2_4": {
        "image_path": "nav/machine2_1_4.png",
        "regions": [
            {
                # “back” 
                "polygon_rel": [
                    [0.019,  0.9217],
                    [0.0409,  0.9269],
                    [0.0439,  0.9608],
                    [0.0175,  0.9608],
                ],
                "label": "Back to Main",
                "target": "main_1_1"
            },
            #
            {
                #open 1
                "polygon_rel": [
                    [0.0368,  0.1569],
                    [0.2224,  0.156],
                    [0.2234,  0.2241],
                    [0.0363,  0.225],
                ],
                "label": "open1",
                "target": "machine2_2"
            },
            {       
                  #open 2
                "polygon_rel": [
                    [0.0373,  0.2526],
                    [0.2219,  0.2526],
                    [0.2234,  0.3216],
                    [0.0359,  0.3224],
                ],
                "label": "open2",
                "target": "machine2_3"
            },
            {       
                  #open 3
                "polygon_rel": [
                    [0.0373,  0.3474],
                    [0.2238,  0.3491],
                    [0.2234,  0.4164],
                    [0.0359,  0.4172],
                ],
                "label": "open3",
                "target": "machine2_1"
            }

        ]
    },
    #
    "main_2_1": {
        "image_path": "nav/main_2_1.png",
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
                "target": "machine1_2_1"
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
                "target": "machine2_2_1"
            }
            #more regions
        ]
    },
    "machine1_2_1": {
        "image_path": "nav/machine1_2_1.png",
        "regions": [
            {
                # “back” 
                "polygon_rel": [
                    [0.019,  0.9217],
                    [0.0409,  0.9269],
                    [0.0439,  0.9608],
                    [0.0175,  0.9608],
                ],
                "label": "Back to Main",
                "target": "main_2_1"
            },
            #
            {
                #open 1
                "polygon_rel": [
                    [0.0368,  0.1569],
                    [0.2224,  0.156],
                    [0.2234,  0.2241],
                    [0.0363,  0.225],
                ],
                "label": "open1",
                "target": "machine1_2_2"
            },
            {       
                  #open 2
                "polygon_rel": [
                    [0.0373,  0.2526],
                    [0.2219,  0.2526],
                    [0.2234,  0.3216],
                    [0.0359,  0.3224],
                ],
                "label": "open2",
                "target": "machine1_2_3"
            },
            {       
                  #open 3
                "polygon_rel": [
                    [0.0373,  0.3474],
                    [0.2238,  0.3491],
                    [0.2234,  0.4164],
                    [0.0359,  0.4172],
                ],
                "label": "open3",
                "target": "machine1_2_4"
            }

        ]
    },
        "machine1_2_2": {
        "image_path": "nav/machine1_2_2.png",
        "regions": [
            {
                # “back” 
                "polygon_rel": [
                    [0.019,  0.9217],
                    [0.0409,  0.9269],
                    [0.0439,  0.9608],
                    [0.0175,  0.9608],
                ],
                "label": "Back to Main",
                "target": "main_2_1"
            },
            #
            {
                #open 1
                "polygon_rel": [
                    [0.0368,  0.1569],
                    [0.2224,  0.156],
                    [0.2234,  0.2241],
                    [0.0363,  0.225],
                ],
                "label": "open1",
                "target": "machine1_2_1"
            },
            {       
                  #open 2
                "polygon_rel": [
                    [0.0373,  0.2526],
                    [0.2219,  0.2526],
                    [0.2234,  0.3216],
                    [0.0359,  0.3224],
                ],
                "label": "open2",
                "target": "machine1_2_3"
            },
            {       
                  #open 3
                "polygon_rel": [
                    [0.0373,  0.3474],
                    [0.2238,  0.3491],
                    [0.2234,  0.4164],
                    [0.0359,  0.4172],
                ],
                "label": "open3",
                "target": "machine1_2_4"
            }

        ]
    },
    "machine1_2_3": {
        "image_path": "nav/machine1_2_3.png",
        "regions": [
            {
                # “back” 
                "polygon_rel": [
                    [0.019,  0.9217],
                    [0.0409,  0.9269],
                    [0.0439,  0.9608],
                    [0.0175,  0.9608],
                ],
                "label": "Back to Main",
                "target": "main_2_1"
            },
            #
            {
                #open 1
                "polygon_rel": [
                    [0.0368,  0.1569],
                    [0.2224,  0.156],
                    [0.2234,  0.2241],
                    [0.0363,  0.225],
                ],
                "label": "open1",
                "target": "machine1_2_2"
            },
            {       
                  #open 2
                "polygon_rel": [
                    [0.0373,  0.2526],
                    [0.2219,  0.2526],
                    [0.2234,  0.3216],
                    [0.0359,  0.3224],
                ],
                "label": "open2",
                "target": "machine1_2_1"
            },
            {       
                  #open 3
                "polygon_rel": [
                    [0.0373,  0.3474],
                    [0.2238,  0.3491],
                    [0.2234,  0.4164],
                    [0.0359,  0.4172],
                ],
                "label": "open3",
                "target": "machine1_2_4"
            }

        ]
    },
    "machine1_2_4": {
        "image_path": "nav/machine1_2_4.png",
        "regions": [
            {
                # “back” 
                "polygon_rel": [
                    [0.019,  0.9217],
                    [0.0409,  0.9269],
                    [0.0439,  0.9608],
                    [0.0175,  0.9608],
                ],
                "label": "Back to Main",
                "target": "main_2_1"
            },
            #
            {
                #open 1
                "polygon_rel": [
                    [0.0368,  0.1569],
                    [0.2224,  0.156],
                    [0.2234,  0.2241],
                    [0.0363,  0.225],
                ],
                "label": "open1",
                "target": "machine1_2_2"
            },
            {       
                  #open 2
                "polygon_rel": [
                    [0.0373,  0.2526],
                    [0.2219,  0.2526],
                    [0.2234,  0.3216],
                    [0.0359,  0.3224],
                ],
                "label": "open2",
                "target": "machine1_2_3"
            },
            {       
                  #open 3
                "polygon_rel": [
                    [0.0373,  0.3474],
                    [0.2238,  0.3491],
                    [0.2234,  0.4164],
                    [0.0359,  0.4172],
                ],
                "label": "open3",
                "target": "machine1_2_1"
            }

        ]
    },






    "machine2_2_1": {
        "image_path": "nav/machine2_2_1.png",
        "regions": [
            {
                # “back” 
                "polygon_rel": [
                    [0.019,  0.9217],
                    [0.0409,  0.9269],
                    [0.0439,  0.9608],
                    [0.0175,  0.9608],
                ],
                "label": "Back to Main",
                "target": "main_2_1"
            },
            #
            {
                #open 1
                "polygon_rel": [
                    [0.0368,  0.1569],
                    [0.2224,  0.156],
                    [0.2234,  0.2241],
                    [0.0363,  0.225],
                ],
                "label": "open1",
                "target": "machine2_2_2"
            },
            {       
                  #open 2
                "polygon_rel": [
                    [0.0373,  0.2526],
                    [0.2219,  0.2526],
                    [0.2234,  0.3216],
                    [0.0359,  0.3224],
                ],
                "label": "open2",
                "target": "machine2_2_3"
            },
            {       
                  #open 3
                "polygon_rel": [
                    [0.0373,  0.3474],
                    [0.2238,  0.3491],
                    [0.2234,  0.4164],
                    [0.0359,  0.4172],
                ],
                "label": "open3",
                "target": "machine2_2_4"
            }

        ]
    },
        "machine2_2_2": {
        "image_path": "nav/machine2_2_2.png",
        "regions": [
            {
                # “back” 
                "polygon_rel": [
                    [0.019,  0.9217],
                    [0.0409,  0.9269],
                    [0.0439,  0.9608],
                    [0.0175,  0.9608],
                ],
                "label": "Back to Main",
                "target": "main_2_1"
            },
            #
            {
                #open 1
                "polygon_rel": [
                    [0.0368,  0.1569],
                    [0.2224,  0.156],
                    [0.2234,  0.2241],
                    [0.0363,  0.225],
                ],
                "label": "open1",
                "target": "machine2_2_1"
            },
            {       
                  #open 2
                "polygon_rel": [
                    [0.0373,  0.2526],
                    [0.2219,  0.2526],
                    [0.2234,  0.3216],
                    [0.0359,  0.3224],
                ],
                "label": "open2",
                "target": "machine2_2_3"
            },
            {       
                  #open 3
                "polygon_rel": [
                    [0.0373,  0.3474],
                    [0.2238,  0.3491],
                    [0.2234,  0.4164],
                    [0.0359,  0.4172],
                ],
                "label": "open3",
                "target": "machine2_2_4"
            }

        ]
    },
    "machine2_2_3": {
        "image_path": "nav/machine2_2_3.png",
        "regions": [
            {
                # “back” 
                "polygon_rel": [
                    [0.019,  0.9217],
                    [0.0409,  0.9269],
                    [0.0439,  0.9608],
                    [0.0175,  0.9608],
                ],
                "label": "Back to Main",
                "target": "main_2_1"
            },
            #
            {
                #open 1
                "polygon_rel": [
                    [0.0368,  0.1569],
                    [0.2224,  0.156],
                    [0.2234,  0.2241],
                    [0.0363,  0.225],
                ],
                "label": "open1",
                "target": "machine2_2_2"
            },
            {       
                  #open 2
                "polygon_rel": [
                    [0.0373,  0.2526],
                    [0.2219,  0.2526],
                    [0.2234,  0.3216],
                    [0.0359,  0.3224],
                ],
                "label": "open2",
                "target": "machine2_2_1"
            },
            {       
                  #open 3
                "polygon_rel": [
                    [0.0373,  0.3474],
                    [0.2238,  0.3491],
                    [0.2234,  0.4164],
                    [0.0359,  0.4172],
                ],
                "label": "open3",
                "target": "machine2_2_4"
            }

        ]
    },
    "machine2_2_4": {
        "image_path": "nav/machine2_2_4.png",
        "regions": [
            {
                # “back” 
                "polygon_rel": [
                    [0.019,  0.9217],
                    [0.0409,  0.9269],
                    [0.0439,  0.9608],
                    [0.0175,  0.9608],
                ],
                "label": "Back to Main",
                "target": "main_2_1"
            },
            #
            {
                #open 1
                "polygon_rel": [
                    [0.0368,  0.1569],
                    [0.2224,  0.156],
                    [0.2234,  0.2241],
                    [0.0363,  0.225],
                ],
                "label": "open1",
                "target": "machine2_2_2"
            },
            {       
                  #open 2
                "polygon_rel": [
                    [0.0373,  0.2526],
                    [0.2219,  0.2526],
                    [0.2234,  0.3216],
                    [0.0359,  0.3224],
                ],
                "label": "open2",
                "target": "machine2_2_3"
            },
            {       
                  #open 3
                "polygon_rel": [
                    [0.0373,  0.3474],
                    [0.2238,  0.3491],
                    [0.2234,  0.4164],
                    [0.0359,  0.4172],
                ],
                "label": "open3",
                "target": "machine2_2_1"
            }

        ]
    },
    #
}
