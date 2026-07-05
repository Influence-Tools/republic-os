---
type: Jurisdiction
title: "DeKalb County, IN"
classification: county
fips: "18033"
state: "IN"
demographics:
  population: 43807
  population_under_18: 10553
  population_18_64: 25624
  population_65_plus: 7630
  median_household_income: 74331
  poverty_rate: 9.52
  homeownership_rate: 82.06
  unemployment_rate: 4.52
  median_home_value: 194100
  gini_index: 0.4065
  vacancy_rate: 7.01
  race_white: 41507
  race_black: 46
  race_asian: 241
  race_native: 24
  hispanic: 1347
  bachelors_plus: 7828
districts:
  - to: "us/states/in/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/senate/14"
    rel: in-district
    area_weight: 0.7051
  - to: "us/states/in/districts/senate/13"
    rel: in-district
    area_weight: 0.2949
  - to: "us/states/in/districts/house/52"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# DeKalb County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43807 |
| Under 18 | 10553 |
| 18–64 | 25624 |
| 65+ | 7630 |
| Median household income | 74331 |
| Poverty rate | 9.52 |
| Homeownership rate | 82.06 |
| Unemployment rate | 4.52 |
| Median home value | 194100 |
| Gini index | 0.4065 |
| Vacancy rate | 7.01 |
| White | 41507 |
| Black | 46 |
| Asian | 241 |
| Native | 24 |
| Hispanic/Latino | 1347 |
| Bachelor's or higher | 7828 |

## Districts

- [IN-03](/us/states/in/districts/03.md) — 100% (congressional)
- [IN Senate District 14](/us/states/in/districts/senate/14.md) — 71% (state senate)
- [IN Senate District 13](/us/states/in/districts/senate/13.md) — 29% (state senate)
- [IN House District 52](/us/states/in/districts/house/52.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
