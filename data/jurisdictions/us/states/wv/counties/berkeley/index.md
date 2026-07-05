---
type: Jurisdiction
title: "Berkeley County, WV"
classification: county
fips: "54003"
state: "WV"
demographics:
  population: 129514
  population_under_18: 29910
  population_18_64: 79833
  population_65_plus: 19771
  median_household_income: 80815
  poverty_rate: 11.1
  homeownership_rate: 76.01
  unemployment_rate: 4.74
  median_home_value: 266300
  gini_index: 0.4084
  vacancy_rate: 5.2
  race_white: 104505
  race_black: 9606
  race_asian: 1251
  race_native: 151
  hispanic: 8294
  bachelors_plus: 30467
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/wv/districts/senate/15"
    rel: in-district
    area_weight: 0.6556
  - to: "us/states/wv/districts/senate/16"
    rel: in-district
    area_weight: 0.3438
  - to: "us/states/wv/districts/house/91"
    rel: in-district
    area_weight: 0.2434
  - to: "us/states/wv/districts/house/90"
    rel: in-district
    area_weight: 0.1607
  - to: "us/states/wv/districts/house/92"
    rel: in-district
    area_weight: 0.1573
  - to: "us/states/wv/districts/house/97"
    rel: in-district
    area_weight: 0.1083
  - to: "us/states/wv/districts/house/93"
    rel: in-district
    area_weight: 0.1054
  - to: "us/states/wv/districts/house/96"
    rel: in-district
    area_weight: 0.0876
  - to: "us/states/wv/districts/house/94"
    rel: in-district
    area_weight: 0.0686
  - to: "us/states/wv/districts/house/95"
    rel: in-district
    area_weight: 0.0681
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Berkeley County, WV

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 129514 |
| Under 18 | 29910 |
| 18–64 | 79833 |
| 65+ | 19771 |
| Median household income | 80815 |
| Poverty rate | 11.1 |
| Homeownership rate | 76.01 |
| Unemployment rate | 4.74 |
| Median home value | 266300 |
| Gini index | 0.4084 |
| Vacancy rate | 5.2 |
| White | 104505 |
| Black | 9606 |
| Asian | 1251 |
| Native | 151 |
| Hispanic/Latino | 8294 |
| Bachelor's or higher | 30467 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 15](/us/states/wv/districts/senate/15.md) — 66% (state senate)
- [WV Senate District 16](/us/states/wv/districts/senate/16.md) — 34% (state senate)
- [WV House District 91](/us/states/wv/districts/house/91.md) — 24% (state house)
- [WV House District 90](/us/states/wv/districts/house/90.md) — 16% (state house)
- [WV House District 92](/us/states/wv/districts/house/92.md) — 16% (state house)
- [WV House District 97](/us/states/wv/districts/house/97.md) — 11% (state house)
- [WV House District 93](/us/states/wv/districts/house/93.md) — 11% (state house)
- [WV House District 96](/us/states/wv/districts/house/96.md) — 9% (state house)
- [WV House District 94](/us/states/wv/districts/house/94.md) — 7% (state house)
- [WV House District 95](/us/states/wv/districts/house/95.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
