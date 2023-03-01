import numpy as np

def icd_chapter_section(condition_code):
    section = 0
    if condition_code[0] != 'E' and condition_code[0] != 'V':
        icd_section = int(condition_code[:3])
        # 1. Infectious And Parasitic Diseases
        if icd_section >= 1 and icd_section <= 9:
            section = 1
        elif icd_section >= 10 and icd_section <= 18:
            section = 2
        elif icd_section >= 20 and icd_section <= 27:
            section = 3
        elif icd_section >= 30 and icd_section <= 41:
            section = 4
        elif icd_section >= 42 and icd_section <= 44:
            section = 5
        elif icd_section >= 45 and icd_section <= 49:
            section = 6
        elif icd_section >= 50 and icd_section <= 59:
            section = 7
        elif icd_section >= 60 and icd_section <= 66:
            section = 8
        elif icd_section >= 70 and icd_section <= 79:
            section = 9
        elif icd_section >= 80 and icd_section <= 88:
            section = 10
        elif icd_section >= 90 and icd_section <= 99:
            section = 11
        elif icd_section >= 100 and icd_section <= 104:
            section = 12
        elif icd_section >= 110 and icd_section <= 118:
            section = 13
        elif icd_section >= 120 and icd_section <= 129:
            section = 14
        elif icd_section >= 130 and icd_section <= 136:
            section = 15
        elif icd_section >= 137 and icd_section <= 139:
            section = 16
        # 2. Neoplasms
        elif icd_section >= 140 and icd_section <= 149:
            section = 17
        elif icd_section >= 150 and icd_section <= 159:
            section = 18
        elif icd_section >= 160 and icd_section <= 165:
            section = 19
        elif icd_section >= 170 and icd_section <= 176:
            section = 20
        elif icd_section >= 179 and icd_section <= 189:
            section = 21
        elif icd_section >= 190 and icd_section <= 199:
            section = 22
        elif icd_section >= 200 and icd_section <= 209:
            section = 23
        elif icd_section >= 210 and icd_section <= 229:
            section = 24
        elif icd_section >= 230 and icd_section <= 234:
            section = 25
        elif icd_section >= 235 and icd_section <= 238:
            section = 26
        elif icd_section >= 239 and icd_section <= 239:
            section = 27
        # 3. endocrine, nutritional and metabolic diseases, and immunity disorders
        elif icd_section >= 240 and icd_section <= 246:
            section = 28
        elif icd_section >= 249 and icd_section <= 259:
            section = 29
        elif icd_section >= 260 and icd_section <= 269:
            section = 30
        elif icd_section >= 270 and icd_section <= 279:
            section = 31
        # 4. Diseases Of The Blood And Blood-Forming Organs
        elif icd_section >= 280 and icd_section <= 289:
            section = 32
        # 5. Mental disorder
        elif icd_section >= 290 and icd_section <= 294:
            section = 33
        elif icd_section >= 295 and icd_section <= 299:
            section = 34
        elif icd_section >= 300 and icd_section <= 316:
            section = 35
        elif icd_section >= 317 and icd_section <= 319:
            section = 36
        # 6. Diseases Of The Nervous System And Sense Organs
        elif icd_section >= 320 and icd_section <= 327:
            section = 37
        elif icd_section >= 330 and icd_section <= 337:
            section = 38
        elif icd_section >= 338 and icd_section <= 338:
            section = 39
        elif icd_section >= 339 and icd_section <= 339:
            section = 40
        elif icd_section >= 340 and icd_section <= 349:
            section = 41
        elif icd_section >= 350 and icd_section <= 359:
            section = 42
        elif icd_section >= 360 and icd_section <= 379:
            section = 43
        elif icd_section >= 380 and icd_section <= 389:
            section = 44
        # 7. Diseases Of The Circulatory System
        elif icd_section >= 390 and icd_section <= 392:
            section = 45
        elif icd_section >= 393 and icd_section <= 398:
            section = 46
        elif icd_section >= 401 and icd_section <= 405:
            section = 47
        elif icd_section >= 410 and icd_section <= 414:
            section = 48
        elif icd_section >= 415 and icd_section <= 417:
            section = 49
        elif icd_section >= 420 and icd_section <= 429:
            section = 50
        elif icd_section >= 430 and icd_section <= 438:
            section = 51
        elif icd_section >= 440 and icd_section <= 449:
            section = 52
        elif icd_section >= 451 and icd_section <= 459:
            section = 53
        # 8. Diseases Of The Respiratory System
        elif icd_section >= 460 and icd_section <= 466:
            section = 54
        elif icd_section >= 470 and icd_section <= 478:
            section = 55
        elif icd_section >= 480 and icd_section <= 488:
            section = 56
        elif icd_section >= 490 and icd_section <= 496:
            section = 57
        elif icd_section >= 500 and icd_section <= 508:
            section = 58
        elif icd_section >= 510 and icd_section <= 519:
            section = 59
        # 9. Diseases Of The Digestive System
        elif icd_section >= 520 and icd_section <= 529:
            section = 60
        elif icd_section >= 530 and icd_section <= 539:
            section = 61
        elif icd_section >= 540 and icd_section <= 543:
            section = 62
        elif icd_section >= 550 and icd_section <= 553:
            section = 63
        elif icd_section >= 555 and icd_section <= 558:
            section = 64
        elif icd_section >= 560 and icd_section <= 569:
            section = 65
        elif icd_section >= 570 and icd_section <= 579:
            section = 66
        # 10. Diseases Of The Genitourinary System
        elif icd_section >= 580 and icd_section <= 589:
            section = 67
        elif icd_section >= 590 and icd_section <= 599:
            section = 68
        elif icd_section >= 600 and icd_section <= 608:
            section = 69
        elif icd_section >= 610 and icd_section <= 612:
            section = 70
        elif icd_section >= 614 and icd_section <= 616:
            section = 71
        elif icd_section >= 617 and icd_section <= 629:
            section = 72
        # 11. Complications Of Pregnancy, Childbirth, And The Puerperium
        elif icd_section >= 630 and icd_section <= 639:
            section = 73
        elif icd_section >= 640 and icd_section <= 649:
            section = 74
        elif icd_section >= 650 and icd_section <= 659:
            section = 75
        elif icd_section >= 660 and icd_section <= 669:
            section = 76
        elif icd_section >= 670 and icd_section <= 677:
            section = 77
        elif icd_section >= 678 and icd_section <= 679:
            section = 78
        # 12. Diseases Of The Skin And Subcutaneous Tissue
        elif icd_section >= 680 and icd_section <= 686:
            section = 79
        elif icd_section >= 690 and icd_section <= 698:
            section = 80
        elif icd_section >= 700 and icd_section <= 709:
            section = 81
        # 13. Diseases Of The Musculoskeletal System And Connective Tissue
        elif icd_section >= 710 and icd_section <= 719:
            section = 82
        elif icd_section >= 720 and icd_section <= 724:
            section = 83
        elif icd_section >= 725 and icd_section <= 729:
            section = 84
        elif icd_section >= 730 and icd_section <= 739:
            section = 85
        # 14. Congenital Anomalies
        elif icd_section >= 740 and icd_section <= 759:
            section = 86
        # 15. Certain Conditions Originating In The Perinatal Period
        elif icd_section >= 760 and icd_section <= 763:
            section = 87
        elif icd_section >= 764 and icd_section <= 779:
            section = 88
        # 16. Symptoms, Signs, And Ill-Defined Conditions
        elif icd_section >= 780 and icd_section <= 789:
            section = 89
        elif icd_section >= 790 and icd_section <= 796:
            section = 90
        elif icd_section >= 797 and icd_section <= 809:
            section = 91
        # 17. Injury And Poisoning
        elif icd_section >= 800 and icd_section <= 804:
            section = 92
        elif icd_section >= 805 and icd_section <= 809:
            section = 93
        elif icd_section >= 810 and icd_section <= 819:
            section = 94
        elif icd_section >= 820 and icd_section <= 829:
            section = 95
        elif icd_section >= 830 and icd_section <= 839:
            section = 96
        elif icd_section >= 840 and icd_section <= 848:
            section = 97
        elif icd_section >= 850 and icd_section <= 854:
            section = 98
        elif icd_section >= 860 and icd_section <= 869:
            section = 99
        elif icd_section >= 870 and icd_section <= 879:
            section = 100
        elif icd_section >= 880 and icd_section <= 887:
            section = 101
        elif icd_section >= 890 and icd_section <= 897:
            section = 102
        elif icd_section >= 900 and icd_section <= 904:
            section = 103
        elif icd_section >= 905 and icd_section <= 909:
            section = 104
        elif icd_section >= 910 and icd_section <= 919:
            section = 105
        elif icd_section >= 920 and icd_section <= 924:
            section = 106
        elif icd_section >= 925 and icd_section <= 929:
            section = 107
        elif icd_section >= 930 and icd_section <= 939:
            section = 108
        elif icd_section >= 940 and icd_section <= 949:
            section = 109
        elif icd_section >= 950 and icd_section <= 957:
            section = 110
        elif icd_section >= 958 and icd_section <= 959:
            section = 111
        elif icd_section >= 960 and icd_section <= 979:
            section = 112
        elif icd_section >= 980 and icd_section <= 989:
            section = 113
        elif icd_section >= 990 and icd_section <= 995:
            section = 114
        elif icd_section >= 996 and icd_section <= 999:
            section = 115

    if condition_code[0] == 'V':
        if int(condition_code[1:]) == 9:
            section = 116 # Infection with drug-resistant microorganisms
        if int(condition_code[1:]) == 10:
            section = 117 # personal history of cancer
        if int(condition_code[1:]) == 16:
            section = 118 # family history of cancer
        if int(condition_code[1:]) == 46:
            section = 119 # dependence on machines and devices
        if int(condition_code[1:]) == 58:
            section = 120 # High-risk medications
        if int(condition_code[1:]) == 87:
            section = 121 # Personal exposures and history presenting hazards to health
        if float(condition_code[1:]) == 4983:
            section = 122 # On waiting list for organ transplant
        if section != 0: return section

        if int(condition_code[1:3]) >= 1 and int(condition_code[1:3]) <= 9:
            section = 123 # Persons With Potential Health Hazards Related To Communicable Diseases
        if int(condition_code[1:3]) >= 10 and int(condition_code[1:3]) <= 19:
            section =  124 # Persons With Potential Health Hazards Related To Personal And Family History
        if int(condition_code[1:3]) >= 20 and int(condition_code[1:3]) <= 29:
            section = 125 # Persons Encountering Health Services In Circumstances Related To Reproduction And Development
        if int(condition_code[1:3]) >= 30 and int(condition_code[1:3]) <= 39:
            section = 126 # Liveborn Infants According To Type Of Birth
        if int(condition_code[1:3]) >= 40 and int(condition_code[1:3]) <= 49:
            section = 127 # Persons With A Condition Influencing Their Health Status
        if int(condition_code[1:3]) >= 50 and int(condition_code[1:3]) <= 59:
            section = 128 # Persons Encountering Health Services For Specific Procedures And Aftercare
        if int(condition_code[1:3]) >= 60 and int(condition_code[1:3]) <= 69:
            section = 129 # Persons Encountering Health Services In Other Circumstances
        if int(condition_code[1:3]) >= 70 and int(condition_code[1:3]) <= 82:
            section = 130 # Persons Without Reported Diagnosis Encountered During Examination And Investigation Of Individuals And Populations
        if int(condition_code[1:3]) >= 83 and int(condition_code[1:3]) <= 84:
            section = 131 # Genetics
        if int(condition_code[1:3]) == 86 and float(condition_code[1:3]) == 86:
            section = 132 # Estrogen Receptor Status +
        if int(condition_code[1:3]) == 86 and float(condition_code[1:3]) == 86.1:
            section = 133 # Estrogen Receptor Status -
        if int(condition_code[1:3]) == 87:
            section = 134 # Other Specified Personal Exposures And History Presenting Hazards To Health
        if int(condition_code[1:3]) == 88:
            section = 135 # Acquired Absence Of Other Organs And Tissue
        if int(condition_code[1:3]) == 89:
            section = 136 # Other Suspected Conditions Not Found
        if int(condition_code[1:3]) == 90:
            section = 137 # Retained Foreign Body
        if int(condition_code[1:3]) == 91:
            section = 138 # Multiple Gestation Placenta Status

    if condition_code[0] == 'E':
        if int(condition_code[1:4]) >= 800 and int(condition_code[1:4]) < 850:
            section = 139 # Traffic Accidents
        if int(condition_code[1:4]) >= 850 and int(condition_code[1:4]) < 870:
            section = 140 # Accidental Poisoning
        if int(condition_code[1:4]) >= 870 and int(condition_code[1:4]) < 880:
            section = 141 # Misadventures To Patients During Surgical And Medical Care
        if int(condition_code[1:4]) >= 880 and int(condition_code[1:4]) < 889:
            section = 142 # Accidental falls
        if int(condition_code[1:4]) >= 890 and int(condition_code[1:4]) < 900:
            section = 143 # Accidents caused by fire and flames
        if int(condition_code[1:4]) >= 900 and int(condition_code[1:4]) < 910:
            section = 144 # Accidents due to natural and environmental factors
        if int(condition_code[1:4]) >= 910 and int(condition_code[1:4]) < 916:
            section = 145 # Accidents caused by submersion, suffocation, and foreign bodies
        if int(condition_code[1:4]) >= 916 and int(condition_code[1:4]) < 929:
            section = 146 # Other accidents
        if int(condition_code[1:4]) == 929:
            section = 147 # Late Effects Of Accidental Injury
        if int(condition_code[1:4]) >= 930 and int(condition_code[1:4]) < 950:
            section = 148 # Adverse Effects In Therapeutic Use
        if int(condition_code[1:4]) >= 950 and int(condition_code[1:4]) < 960:
            section = 149 # Suicide And Self-Inflicted Injury
        if int(condition_code[1:4]) >= 960 and int(condition_code[1:4]) < 970:
            section = 150 # Homicide
    return section - 1

def race_encoder_mimiciii():
    # white:0, black:1, asian:2, hispanic:3, other:4
    dic_race_encode = {
        'WHITE': 0,
        'BLACK/AFRICAN AMERICAN': 1,
        'UNKNOWN/NOT SPECIFIED': 4,
        'HISPANIC OR LATINO': 3,
        'OTHER': 4,
        'ASIAN': 2,
        'UNABLE TO OBTAIN': 4,
        'PATIENT DECLINED TO ANSWER': 4,
        'ASIAN - CHINESE': 2,
        'HISPANIC/LATINO - PUERTO RICAN': 3,
        'BLACK/CAPE VERDEAN': 1,
        'WHITE - RUSSIAN': 0,
        'MULTI RACE ETHNICITY': 4,
        'BLACK/HAITIAN': 1,
        'ASIAN - ASIAN INDIAN': 2,
        'WHITE - OTHER EUROPEAN': 0,
        'HISPANIC/LATINO - DOMINICAN': 3,
        'PORTUGUESE': 0,
        'WHITE - BRAZILIAN': 0,
        'ASIAN - VIETNAMESE': 2,
        'AMERICAN INDIAN/ALASKA NATIVE': 4,
        'BLACK/AFRICAN': 1,
        'MIDDLE EASTERN': 2,
        'HISPANIC/LATINO - GUATEMALAN': 3,
        'WHITE - EASTERN EUROPEAN': 0,
        'ASIAN - FILIPINO': 2,
        'HISPANIC/LATINO - CUBAN': 3,
        'HISPANIC/LATINO - SALVADORAN': 3,
        'NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER': 4,
        'ASIAN - OTHER': 2,
        'ASIAN - CAMBODIAN': 2,
        'ASIAN - KOREAN': 2,
        'HISPANIC/LATINO - CENTRAL AMERICAN (OTHER)': 3,
        'HISPANIC/LATINO - MEXICAN': 3,
        'CARIBBEAN ISLAND': 3,
        'HISPANIC/LATINO - COLOMBIAN': 3,
        'SOUTH AMERICAN': 3,
        'ASIAN - JAPANESE': 2,
        'ASIAN - THAI': 2,
        'HISPANIC/LATINO - HONDURAN': 3,
        'AMERICAN INDIAN/ALASKA NATIVE FEDERALLY RECOGNIZED TRIBE': 4
    }
    return dic_race_encode

def relocate_icd9_section(sec):
    if sec == 1: res = (10,1)
    if sec == 2: res = (9,10)
    if sec == 3: res = (8,20)
    if sec == 4: res = (12,30)
    if sec == 5: res = (13,42)
    if sec == 6: res = (15,45)
    if sec == 7: res = (10,50)
    if sec == 8: res = (7,60)
    if sec == 9: res = (10,70)
    if sec == 10: res = (9,80)
    if sec == 11: res = (10,90)
    if sec == 12: res = (5,100)
    if sec == 13: res = (9,110)
    if sec == 14: res = (10,120)
    if sec == 15: res = (7,130)
    if sec == 16: res = (3,137)
    if sec == 17: res = (10,140)
    if sec == 18: res = (10,150)
    if sec == 19: res = (6,160)
    if sec == 20: res = (7,170)
    if sec == 21: res = (11,179)
    if sec == 22: res = (10,190)
    if sec == 23: res = (10,200)
    if sec == 24: res = (20,210)
    if sec == 25: res = (5,230)
    if sec == 26: res = (4,235)
    if sec == 27: res = (1,239)
    if sec == 28: res = (7,240)
    if sec == 29: res = (11,249)
    if sec == 30: res = (10,260)
    if sec == 31: res = (10,270)
    if sec == 32: res = (10,280)
    if sec == 33: res = (5,290)
    if sec == 34: res = (5,295)
    if sec == 35: res = (17,300)
    if sec == 36: res = (3,317)
    if sec == 37: res = (8,320)
    if sec == 38: res = (8,330)
    if sec == 39: res = (1,338)
    if sec == 40: res = (1,339)
    if sec == 41: res = (10,340)
    if sec == 42: res = (10,350)
    if sec == 43: res = (20,360)
    if sec == 44: res = (10,380)
    if sec == 45: res = (3,390)
    if sec == 46: res = (6,393)
    if sec == 47: res = (5,401)
    if sec == 48: res = (5,410)
    if sec == 49: res = (3,415)
    if sec == 50: res = (10,420)
    if sec == 51: res = (9,430)
    if sec == 52: res = (10,440)
    if sec == 53: res = (9,451)
    if sec == 54: res = (7,460)
    if sec == 55: res = (9,470)
    if sec == 56: res = (9,480)
    if sec == 57: res = (7,490)
    if sec == 58: res = (9,500)
    if sec == 59: res = (10,510)
    if sec == 60: res = (10,520)
    if sec == 61: res = (10,530)
    if sec == 62: res = (4,540)
    if sec == 63: res = (4,550)
    if sec == 64: res = (4,555)
    if sec == 65: res = (10,560)
    if sec == 66: res = (10,570)
    if sec == 67: res = (10,580)
    if sec == 68: res = (10,590)
    if sec == 69: res = (9,600)
    if sec == 70: res = (3,610)
    if sec == 71: res = (3,614)
    if sec == 72: res = (13,617)
    if sec == 73: res = (10,630)
    if sec == 74: res = (10,640)
    if sec == 75: res = (10,650)
    if sec == 76: res = (10,660)
    if sec == 77: res = (8,670)
    if sec == 78: res = (2,678)
    if sec == 79: res = (7,680)
    if sec == 80: res = (9,690)
    if sec == 81: res = (10,700)
    if sec == 82: res = (10,710)
    if sec == 83: res = (5,720)
    if sec == 84: res = (5,725)
    if sec == 85: res = (10,730)
    if sec == 86: res = (20,740)
    if sec == 87: res = (4,760)
    if sec == 88: res = (16,764)
    if sec == 89: res = (10,780)
    if sec == 90: res = (7,790)
    if sec == 91: res = (13,797)
    if sec == 92: res = (5,800)
    if sec == 93: res = (5,805)
    if sec == 94: res = (10,810)
    if sec == 95: res = (10,820)
    if sec == 96: res = (10,830)
    if sec == 97: res = (9,840)
    if sec == 98: res = (5,850)
    if sec == 99: res = (10,860)
    if sec == 100: res = (10,870)
    if sec == 101: res = (8,880)
    if sec == 102: res = (8,890)
    if sec == 103: res = (5,900)
    if sec == 104: res = (5,905)
    if sec == 105: res = (10,910)
    if sec == 106: res = (5,920)
    if sec == 107: res = (5,925)
    if sec == 108: res = (10,930)
    if sec == 109: res = (10,940)
    if sec == 110: res = (8,950)
    if sec == 111: res = (2,958)
    if sec == 112: res = (20,960)
    if sec == 113: res = (10,980)
    if sec == 114: res = (6,990)
    if sec == 115: res = (4,996)
    if sec == 116: res = (1,'V9')
    if sec == 117: res = (1,'V10')
    if sec == 118: res = (1,'V16')
    if sec == 119: res = (1,'V46')
    if sec == 120: res = (1,'V58')
    if sec == 121: res = (1,'V87')
    if sec == 122: res = (1,'V4983')
    return res

def fairness_measurement(y_test_sub, y_pred_sub, y_pred_sub_binary):
    """
    Given the true label and prob/bianry predictions
    Return Equal Opportunity and Demographic Parity
    """
    # -1: binary pred, -2: probrobalistic pred, -3: y true
    Xy_total = np.concatenate([y_test_sub.reshape(-1,1),
                               y_pred_sub.reshape(-1,1), y_pred_sub_binary.reshape(-1,1)], axis=1)
    # Equal Opportunity and Demographic Parity
    n_yhat_a = Xy_total[(Xy_total[:,-1]==1),:].shape[0]
    n_a = Xy_total.shape[0]
    n_yhat_y_a = Xy_total[(Xy_total[:,-1]==1)&(Xy_total[:,-3]==1),:].shape[0]
    n_y_a = Xy_total[(Xy_total[:,-3]==1),:].shape[0]
    return round(n_yhat_y_a/n_y_a,3), round(n_yhat_a/n_a,3)
