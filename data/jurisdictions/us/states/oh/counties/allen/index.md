---
type: Jurisdiction
title: "Allen County, OH"
classification: county
fips: "39003"
state: "OH"
demographics:
  population: 101348
  population_under_18: 23836
  population_18_64: 58137
  population_65_plus: 19375
  median_household_income: 64038
  poverty_rate: 13.29
  homeownership_rate: 67.69
  unemployment_rate: 5.74
  median_home_value: 165300
  gini_index: 0.4396
  vacancy_rate: 7.81
  race_white: 81056
  race_black: 9744
  race_asian: 942
  race_native: 286
  hispanic: 3682
  bachelors_plus: 19093
districts:
  - to: "us/states/oh/districts/04"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/house/78"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Allen County, OH

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 101348 |
| Under 18 | 23836 |
| 18–64 | 58137 |
| 65+ | 19375 |
| Median household income | 64038 |
| Poverty rate | 13.29 |
| Homeownership rate | 67.69 |
| Unemployment rate | 5.74 |
| Median home value | 165300 |
| Gini index | 0.4396 |
| Vacancy rate | 7.81 |
| White | 81056 |
| Black | 9744 |
| Asian | 942 |
| Native | 286 |
| Hispanic/Latino | 3682 |
| Bachelor's or higher | 19093 |

## Districts

- [OH-04](/us/states/oh/districts/04.md) — 100% (congressional)
- [OH Senate District 12](/us/states/oh/districts/senate/12.md) — 100% (state senate)
- [OH House District 78](/us/states/oh/districts/house/78.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
