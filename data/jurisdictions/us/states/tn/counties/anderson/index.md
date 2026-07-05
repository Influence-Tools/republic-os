---
type: Jurisdiction
title: "Anderson County, TN"
classification: county
fips: "47001"
state: "TN"
demographics:
  population: 79153
  population_under_18: 18430
  population_18_64: 24130
  population_65_plus: 36593
  median_household_income: 66183
  poverty_rate: 13.36
  homeownership_rate: 71.7
  unemployment_rate: 3.74
  median_home_value: 239400
  gini_index: 0.4526
  vacancy_rate: 8.71
  race_white: 68854
  race_black: 2662
  race_asian: 1112
  race_native: 248
  hispanic: 3226
  bachelors_plus: 21992
districts:
  - to: "us/states/tn/districts/03"
    rel: in-district
    area_weight: 0.993
  - to: "us/states/tn/districts/02"
    rel: in-district
    area_weight: 0.007
  - to: "us/states/tn/districts/senate/5"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tn/districts/house/33"
    rel: in-district
    area_weight: 0.5847
  - to: "us/states/tn/districts/house/41"
    rel: in-district
    area_weight: 0.4148
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Anderson County, TN

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 79153 |
| Under 18 | 18430 |
| 18–64 | 24130 |
| 65+ | 36593 |
| Median household income | 66183 |
| Poverty rate | 13.36 |
| Homeownership rate | 71.7 |
| Unemployment rate | 3.74 |
| Median home value | 239400 |
| Gini index | 0.4526 |
| Vacancy rate | 8.71 |
| White | 68854 |
| Black | 2662 |
| Asian | 1112 |
| Native | 248 |
| Hispanic/Latino | 3226 |
| Bachelor's or higher | 21992 |

## Districts

- [TN-03](/us/states/tn/districts/03.md) — 99% (congressional)
- [TN-02](/us/states/tn/districts/02.md) — 1% (congressional)
- [TN Senate District 5](/us/states/tn/districts/senate/5.md) — 100% (state senate)
- [TN House District 33](/us/states/tn/districts/house/33.md) — 58% (state house)
- [TN House District 41](/us/states/tn/districts/house/41.md) — 41% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
