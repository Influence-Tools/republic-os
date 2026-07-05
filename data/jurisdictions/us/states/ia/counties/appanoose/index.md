---
type: Jurisdiction
title: "Appanoose County, IA"
classification: county
fips: "19007"
state: "IA"
demographics:
  population: 12184
  population_under_18: 2626
  population_18_64: 6676
  population_65_plus: 2882
  median_household_income: 54934
  poverty_rate: 17.5
  homeownership_rate: 68.78
  unemployment_rate: 3.85
  median_home_value: 124200
  gini_index: 0.4505
  vacancy_rate: 17.63
  race_white: 11604
  race_black: 100
  race_asian: 111
  race_native: 3
  hispanic: 249
  bachelors_plus: 2113
districts:
  - to: "us/states/ia/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/senate/13"
    rel: in-district
    area_weight: 0.814
  - to: "us/states/ia/districts/senate/12"
    rel: in-district
    area_weight: 0.1859
  - to: "us/states/ia/districts/house/26"
    rel: in-district
    area_weight: 0.814
  - to: "us/states/ia/districts/house/24"
    rel: in-district
    area_weight: 0.1859
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Appanoose County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12184 |
| Under 18 | 2626 |
| 18–64 | 6676 |
| 65+ | 2882 |
| Median household income | 54934 |
| Poverty rate | 17.5 |
| Homeownership rate | 68.78 |
| Unemployment rate | 3.85 |
| Median home value | 124200 |
| Gini index | 0.4505 |
| Vacancy rate | 17.63 |
| White | 11604 |
| Black | 100 |
| Asian | 111 |
| Native | 3 |
| Hispanic/Latino | 249 |
| Bachelor's or higher | 2113 |

## Districts

- [IA-03](/us/states/ia/districts/03.md) — 100% (congressional)
- [IA Senate District 13](/us/states/ia/districts/senate/13.md) — 81% (state senate)
- [IA Senate District 12](/us/states/ia/districts/senate/12.md) — 19% (state senate)
- [IA House District 26](/us/states/ia/districts/house/26.md) — 81% (state house)
- [IA House District 24](/us/states/ia/districts/house/24.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
