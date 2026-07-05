---
type: Jurisdiction
title: "Boone County, IN"
classification: county
fips: "18011"
state: "IN"
demographics:
  population: 74718
  population_under_18: 19066
  population_18_64: 44458
  population_65_plus: 11194
  median_household_income: 111250
  poverty_rate: 4.51
  homeownership_rate: 78.78
  unemployment_rate: 2.78
  median_home_value: 376200
  gini_index: 0.4719
  vacancy_rate: 3.36
  race_white: 65197
  race_black: 2284
  race_asian: 2678
  race_native: 18
  hispanic: 3234
  bachelors_plus: 36353
districts:
  - to: "us/states/in/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/senate/7"
    rel: in-district
    area_weight: 0.9477
  - to: "us/states/in/districts/senate/29"
    rel: in-district
    area_weight: 0.0522
  - to: "us/states/in/districts/house/41"
    rel: in-district
    area_weight: 0.4307
  - to: "us/states/in/districts/house/25"
    rel: in-district
    area_weight: 0.231
  - to: "us/states/in/districts/house/28"
    rel: in-district
    area_weight: 0.1702
  - to: "us/states/in/districts/house/24"
    rel: in-district
    area_weight: 0.1681
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Boone County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 74718 |
| Under 18 | 19066 |
| 18–64 | 44458 |
| 65+ | 11194 |
| Median household income | 111250 |
| Poverty rate | 4.51 |
| Homeownership rate | 78.78 |
| Unemployment rate | 2.78 |
| Median home value | 376200 |
| Gini index | 0.4719 |
| Vacancy rate | 3.36 |
| White | 65197 |
| Black | 2284 |
| Asian | 2678 |
| Native | 18 |
| Hispanic/Latino | 3234 |
| Bachelor's or higher | 36353 |

## Districts

- [IN-04](/us/states/in/districts/04.md) — 100% (congressional)
- [IN Senate District 7](/us/states/in/districts/senate/7.md) — 95% (state senate)
- [IN Senate District 29](/us/states/in/districts/senate/29.md) — 5% (state senate)
- [IN House District 41](/us/states/in/districts/house/41.md) — 43% (state house)
- [IN House District 25](/us/states/in/districts/house/25.md) — 23% (state house)
- [IN House District 28](/us/states/in/districts/house/28.md) — 17% (state house)
- [IN House District 24](/us/states/in/districts/house/24.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
