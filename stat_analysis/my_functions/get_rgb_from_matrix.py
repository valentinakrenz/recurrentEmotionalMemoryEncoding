

def get_rgb_from_matrix(threshold, T_value):
    
    if T_value > 0:
        matrix = [
        [0.8695,    0.8633,    0.8598],
        [0.8776,    0.8592,    0.8486],
        [0.8858,    0.8550,    0.8374],
        [0.8940,    0.8509,    0.8261],
        [0.9013,    0.8461,    0.8147],
        [0.9080,    0.8406,    0.8030],
        [0.9146,    0.8352,    0.7913],
        [0.9212,    0.8298,    0.7796],
        [0.9270,    0.8236,    0.7677],
        [0.9321,    0.8170,    0.7557],
        [0.9373,    0.8103,    0.7437],
        [0.9424,    0.8036,    0.7316],
        [0.9466,    0.7963,    0.7194],
        [0.9502,    0.7884,    0.7072],
        [0.9539,    0.7806,    0.6950],
        [0.9575,    0.7727,    0.6826],
        [0.9602,    0.7642,    0.6703],
        [0.9623,    0.7552,    0.6578],
        [0.9645,    0.7462,    0.6454],
        [0.9666,    0.7372,    0.6330],
        [0.9678,    0.7275,    0.6206],
        [0.9684,    0.7175,    0.6081],
        [0.9691,    0.7075,    0.5957],
        [0.9697,    0.6974,    0.5833],
        [0.9694,    0.6867,    0.5709],
        [0.9686,    0.6756,    0.5585],
        [0.9678,    0.6646,    0.5461],
        [0.9670,    0.6535,    0.5337],
        [0.9652,    0.6418,    0.5215],
        [0.9630,    0.6298,    0.5093],
        [0.9608,    0.6178,    0.4970],
        [0.9586,    0.6058,    0.4848],
        [0.9553,    0.5932,    0.4728],
        [0.9517,    0.5803,    0.4608],
        [0.9481,    0.5674,    0.4488],
        [0.9445,    0.5546,    0.4369],
        [0.9398,    0.5410,    0.4251],
        [0.9348,    0.5273,    0.4135],
        [0.9298,    0.5136,    0.4018],
        [0.9249,    0.4999,    0.3902],
        [0.9188,    0.4855,    0.3788],
        [0.9126,    0.4709,    0.3675],
        [0.9063,    0.4564,    0.3563],
        [0.9000,    0.4418,    0.3450],
        [0.8927,    0.4265,    0.3341],
        [0.8852,    0.4111,    0.3233],
        [0.8777,    0.3957,    0.3124],
        [0.8701,    0.3802,    0.3016],
        [0.8616,    0.3639,    0.2912],
        [0.8529,    0.3474,    0.2809],
        [0.8441,    0.3309,    0.2706],
        [0.8354,    0.3144,    0.2603],
        [0.8257,    0.2965,    0.2504],
        [0.8159,    0.2785,    0.2407],
        [0.8061,    0.2604,    0.2309],
        [0.7962,    0.2424,    0.2211],
        [0.7855,    0.2214,    0.2119],
        [0.7746,    0.2003,    0.2028],
        [0.7637,    0.1791,    0.1936],
        [0.7529,    0.1579,    0.1844],
        [0.7411,    0.1227,    0.1758],
        [0.7293,    0.0870,    0.1673],
        [0.7175,    0.0513,    0.1588],
        [0.7057,    0.0156,    0.1502]
        ]
        T_max = threshold
        T_min = 0
        
    elif T_value < 0:
        matrix = [
        [0.2298,    0.2987,    0.7537],
        [0.2390,    0.3124,    0.7657],
        [0.2482,    0.3261,    0.7778],
        [0.2573,    0.3398,    0.7898],
        [0.2665,    0.3535,    0.8018],
        [0.2760,    0.3670,    0.8128],
        [0.2855,    0.3804,    0.8237],
        [0.2950,    0.3939,    0.8347],
        [0.3045,    0.4074,    0.8456],
        [0.3143,    0.4205,    0.8553],
        [0.3241,    0.4337,    0.8651],
        [0.3339,    0.4468,    0.8749],
        [0.3438,    0.4600,    0.8845],
        [0.3539,    0.4727,    0.8930],
        [0.3640,    0.4855,    0.9015],
        [0.3741,    0.4982,    0.9100],
        [0.3843,    0.5110,    0.9183],
        [0.3947,    0.5232,    0.9254],
        [0.4052,    0.5355,    0.9325],
        [0.4156,    0.5478,    0.9396],
        [0.4260,    0.5600,    0.9465],
        [0.4367,    0.5717,    0.9522],
        [0.4474,    0.5834,    0.9579],
        [0.4580,    0.5951,    0.9635],
        [0.4687,    0.6066,    0.9689],
        [0.4795,    0.6176,    0.9731],
        [0.4904,    0.6287,    0.9773],
        [0.5012,    0.6397,    0.9815],
        [0.5120,    0.6505,    0.9854],
        [0.5229,    0.6608,    0.9880],
        [0.5339,    0.6710,    0.9907],
        [0.5448,    0.6812,    0.9934],
        [0.5557,    0.6913,    0.9957],
        [0.5666,    0.7007,    0.9968],
        [0.5775,    0.7100,    0.9979],
        [0.5884,    0.7194,    0.9990],
        [0.5993,    0.7285,    0.9997],
        [0.6101,    0.7369,    0.9993],
        [0.6209,    0.7454,    0.9989],
        [0.6317,    0.7538,    0.9984],
        [0.6425,    0.7619,    0.9975],
        [0.6531,    0.7693,    0.9956],
        [0.6637,    0.7767,    0.9936],
        [0.6743,    0.7841,    0.9917],
        [0.6848,    0.7911,    0.9892],
        [0.6951,    0.7974,    0.9857],
        [0.7054,    0.8037,    0.9822],
        [0.7158,    0.8100,    0.9787],
        [0.7259,    0.8159,    0.9747],
        [0.7358,    0.8210,    0.9698],
        [0.7457,    0.8261,    0.9648],
        [0.7556,    0.8313,    0.9599],
        [0.7653,    0.8359,    0.9544],
        [0.7747,    0.8398,    0.9480],
        [0.7840,    0.8437,    0.9416],
        [0.7934,    0.8476,    0.9353],
        [0.8025,    0.8509,    0.9283],
        [0.8113,    0.8536,    0.9206],
        [0.8200,    0.8562,    0.9129],
        [0.8288,    0.8588,    0.9052],
        [0.8372,    0.8608,    0.8969],
        [0.8453,    0.8621,    0.8879],
        [0.8533,    0.8634,    0.8789],
        [0.8614,    0.8648,    0.8699]
        ]

        T_max = 0
        T_min = threshold
        
    # Normalize T_value between 0 and 1 based on its position between T_min and T_max
    normalized_value = (T_value - T_min) / (T_max - T_min)
    
    # Get the corresponding index for the normalized value in the matrix
    index = int(normalized_value * (len(matrix) - 1))
    
    # Ensure the index doesn't go out of bounds
    index = max(0, min(index, len(matrix) - 1))
    
    return matrix[index]

