def summary(score: list[float]) -> dict:
    if not score:
        raise ValueError
    chuoi_da_sap_xep = sorted(score)
    do_dai = len(score)
    TB = sum(score) / do_dai
    mid = do_dai // 2
    if do_dai % 2 == 1:
        trung_vi = chuoi_da_sap_xep[mid]
    else:
        trung_vi = (chuoi_da_sap_xep[mid - 1] + chuoi_da_sap_xep[mid]) / 2
    return {
        "min": chuoi_da_sap_xep[0],
        "max": chuoi_da_sap_xep[do_dai - 1],
        "mean": round(TB, 2),
        "median": round(trung_vi, 2),
    }
