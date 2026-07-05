---
type: Jurisdiction
title: "White County, IN"
classification: county
fips: "18181"
state: "IN"
demographics:
  population: 24717
  population_under_18: 5705
  population_18_64: 13780
  population_65_plus: 5232
  median_household_income: 67303
  poverty_rate: 10.18
  homeownership_rate: 81.0
  unemployment_rate: 3.49
  median_home_value: 175900
  gini_index: 0.4107
  vacancy_rate: 20.89
  race_white: 21486
  race_black: 113
  race_asian: 77
  race_native: 84
  hispanic: 2657
  bachelors_plus: 4172
districts:
  - to: "us/states/in/districts/04"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/in/districts/senate/5"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/in/districts/house/16"
    rel: in-district
    area_weight: 0.9301
  - to: "us/states/in/districts/house/13"
    rel: in-district
    area_weight: 0.0698
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# White County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24717 |
| Under 18 | 5705 |
| 18–64 | 13780 |
| 65+ | 5232 |
| Median household income | 67303 |
| Poverty rate | 10.18 |
| Homeownership rate | 81.0 |
| Unemployment rate | 3.49 |
| Median home value | 175900 |
| Gini index | 0.4107 |
| Vacancy rate | 20.89 |
| White | 21486 |
| Black | 113 |
| Asian | 77 |
| Native | 84 |
| Hispanic/Latino | 2657 |
| Bachelor's or higher | 4172 |

## Districts

- [IN-04](/us/states/in/districts/04.md) — 100% (congressional)
- [IN Senate District 5](/us/states/in/districts/senate/5.md) — 100% (state senate)
- [IN House District 16](/us/states/in/districts/house/16.md) — 93% (state house)
- [IN House District 13](/us/states/in/districts/house/13.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
