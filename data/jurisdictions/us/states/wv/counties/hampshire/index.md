---
type: Jurisdiction
title: "Hampshire County, WV"
classification: county
fips: "54027"
state: "WV"
demographics:
  population: 23465
  population_under_18: 4228
  population_18_64: 13526
  population_65_plus: 5711
  median_household_income: 63116
  poverty_rate: 13.07
  homeownership_rate: 82.69
  unemployment_rate: 9.02
  median_home_value: 219200
  gini_index: 0.4559
  vacancy_rate: 31.62
  race_white: 21939
  race_black: 227
  race_asian: 7
  race_native: 17
  hispanic: 409
  bachelors_plus: 4483
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/wv/districts/senate/15"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/wv/districts/house/89"
    rel: in-district
    area_weight: 0.5864
  - to: "us/states/wv/districts/house/88"
    rel: in-district
    area_weight: 0.4132
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Hampshire County, WV

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23465 |
| Under 18 | 4228 |
| 18–64 | 13526 |
| 65+ | 5711 |
| Median household income | 63116 |
| Poverty rate | 13.07 |
| Homeownership rate | 82.69 |
| Unemployment rate | 9.02 |
| Median home value | 219200 |
| Gini index | 0.4559 |
| Vacancy rate | 31.62 |
| White | 21939 |
| Black | 227 |
| Asian | 7 |
| Native | 17 |
| Hispanic/Latino | 409 |
| Bachelor's or higher | 4483 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 15](/us/states/wv/districts/senate/15.md) — 100% (state senate)
- [WV House District 89](/us/states/wv/districts/house/89.md) — 59% (state house)
- [WV House District 88](/us/states/wv/districts/house/88.md) — 41% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
