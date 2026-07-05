---
type: Jurisdiction
title: "Franklin County, IN"
classification: county
fips: "18047"
state: "IN"
demographics:
  population: 23020
  population_under_18: 5064
  population_18_64: 13282
  population_65_plus: 4674
  median_household_income: 78074
  poverty_rate: 6.9
  homeownership_rate: 81.52
  unemployment_rate: 3.93
  median_home_value: 249500
  gini_index: 0.4168
  vacancy_rate: 5.97
  race_white: 22081
  race_black: 18
  race_asian: 207
  race_native: 8
  hispanic: 270
  bachelors_plus: 4058
districts:
  - to: "us/states/in/districts/09"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/in/districts/senate/27"
    rel: in-district
    area_weight: 0.5183
  - to: "us/states/in/districts/senate/42"
    rel: in-district
    area_weight: 0.4817
  - to: "us/states/in/districts/house/55"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Franklin County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23020 |
| Under 18 | 5064 |
| 18–64 | 13282 |
| 65+ | 4674 |
| Median household income | 78074 |
| Poverty rate | 6.9 |
| Homeownership rate | 81.52 |
| Unemployment rate | 3.93 |
| Median home value | 249500 |
| Gini index | 0.4168 |
| Vacancy rate | 5.97 |
| White | 22081 |
| Black | 18 |
| Asian | 207 |
| Native | 8 |
| Hispanic/Latino | 270 |
| Bachelor's or higher | 4058 |

## Districts

- [IN-09](/us/states/in/districts/09.md) — 100% (congressional)
- [IN Senate District 27](/us/states/in/districts/senate/27.md) — 52% (state senate)
- [IN Senate District 42](/us/states/in/districts/senate/42.md) — 48% (state senate)
- [IN House District 55](/us/states/in/districts/house/55.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
