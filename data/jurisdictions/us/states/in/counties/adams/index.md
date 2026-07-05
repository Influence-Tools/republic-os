---
type: Jurisdiction
title: "Adams County, IN"
classification: county
fips: "18001"
state: "IN"
demographics:
  population: 36227
  population_under_18: 11335
  population_18_64: 18971
  population_65_plus: 5921
  median_household_income: 65289
  poverty_rate: 11.16
  homeownership_rate: 83.45
  unemployment_rate: 2.8
  median_home_value: 178400
  gini_index: 0.4036
  vacancy_rate: 6.82
  race_white: 34120
  race_black: 115
  race_asian: 136
  race_native: 165
  hispanic: 1729
  bachelors_plus: 4604
districts:
  - to: "us/states/in/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/senate/19"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/in/districts/house/79"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Adams County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36227 |
| Under 18 | 11335 |
| 18–64 | 18971 |
| 65+ | 5921 |
| Median household income | 65289 |
| Poverty rate | 11.16 |
| Homeownership rate | 83.45 |
| Unemployment rate | 2.8 |
| Median home value | 178400 |
| Gini index | 0.4036 |
| Vacancy rate | 6.82 |
| White | 34120 |
| Black | 115 |
| Asian | 136 |
| Native | 165 |
| Hispanic/Latino | 1729 |
| Bachelor's or higher | 4604 |

## Districts

- [IN-03](/us/states/in/districts/03.md) — 100% (congressional)
- [IN Senate District 19](/us/states/in/districts/senate/19.md) — 100% (state senate)
- [IN House District 79](/us/states/in/districts/house/79.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
