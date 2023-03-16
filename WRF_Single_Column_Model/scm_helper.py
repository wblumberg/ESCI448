def get_pbl_name(d):
    pbl_dict = {'0': ("No PBL Scheme", "None"),
                '1': ("YSU Scheme", "YSU"),
                '2': ("Mellor-Yamada-Janjic TKE scheme", "MYJ"),
                '3': ("Hybrid EDMF GFS scheme", "GFS"),
                '4': ("Eddy-diffusivity Mass Flux, Quasi-Normal Scale Elimination PBL", "QNSE"),
                '5': ("MYNN 2.5 level TKE scheme", "MYNN v2.5"),
                '6': ("MYNN 3rd level TKE scheme", "MYNN v3"),
                '7': ("ACM2 (Pleim) PBL", "ACM2"),
                '8': ("Bougeault and Lacarrere (BouLac) PBL", "BouLac"),
                '9': ("UW boundary layer scheme from CAM5 (CESM 1_0_1)", "UW"),
                '10': ("TEMF (Total Energy Mass Flux) scheme", "TEMF"),
                '11': ("Shin-Hong 'scale-aware' PBL scheme", "Shin-Hong"),
                '12': ("Grenier-Bretherton-McCaa scheme", "GBM"),
                '99': ("MRF scheme", "MRF")}
    
    return pbl_dict[str(d.BL_PBL_PHYSICS)]