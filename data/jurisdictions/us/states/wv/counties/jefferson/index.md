---
type: Jurisdiction
title: "Jefferson County, WV"
classification: county
fips: "54037"
state: "WV"
demographics:
  population: 59260
  population_under_18: 12512
  population_18_64: 36486
  population_65_plus: 10262
  median_household_income: 98806
  poverty_rate: 8.69
  homeownership_rate: 80.27
  unemployment_rate: 3.86
  median_home_value: 350800
  gini_index: 0.423
  vacancy_rate: 7.95
  race_white: 47826
  race_black: 3375
  race_asian: 827
  race_native: 154
  hispanic: 4630
  bachelors_plus: 19315
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.9977
  - to: "us/states/wv/districts/senate/16"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/wv/districts/house/98"
    rel: in-district
    area_weight: 0.4332
  - to: "us/states/wv/districts/house/100"
    rel: in-district
    area_weight: 0.3025
  - to: "us/states/wv/districts/house/97"
    rel: in-district
    area_weight: 0.1368
  - to: "us/states/wv/districts/house/99"
    rel: in-district
    area_weight: 0.1258
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Jefferson County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 59260 |
| Under 18 | 12512 |
| 18–64 | 36486 |
| 65+ | 10262 |
| Median household income | 98806 |
| Poverty rate | 8.69 |
| Homeownership rate | 80.27 |
| Unemployment rate | 3.86 |
| Median home value | 350800 |
| Gini index | 0.423 |
| Vacancy rate | 7.95 |
| White | 47826 |
| Black | 3375 |
| Asian | 827 |
| Native | 154 |
| Hispanic/Latino | 4630 |
| Bachelor's or higher | 19315 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 16](/us/states/wv/districts/senate/16.md) — 100% (state senate)
- [WV House District 98](/us/states/wv/districts/house/98.md) — 43% (state house)
- [WV House District 100](/us/states/wv/districts/house/100.md) — 30% (state house)
- [WV House District 97](/us/states/wv/districts/house/97.md) — 14% (state house)
- [WV House District 99](/us/states/wv/districts/house/99.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
