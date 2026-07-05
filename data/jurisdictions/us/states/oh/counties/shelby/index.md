---
type: Jurisdiction
title: "Shelby County, OH"
classification: county
fips: "39149"
state: "OH"
demographics:
  population: 47929
  population_under_18: 11724
  population_18_64: 27516
  population_65_plus: 8689
  median_household_income: 73978
  poverty_rate: 11.6
  homeownership_rate: 73.68
  unemployment_rate: 4.07
  median_home_value: 208100
  gini_index: 0.4189
  vacancy_rate: 6.17
  race_white: 44104
  race_black: 1073
  race_asian: 271
  race_native: 41
  hispanic: 835
  bachelors_plus: 9123
districts:
  - to: "us/states/oh/districts/04"
    rel: in-district
    area_weight: 0.5104
  - to: "us/states/oh/districts/15"
    rel: in-district
    area_weight: 0.4895
  - to: "us/states/oh/districts/senate/12"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/house/85"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Shelby County, OH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47929 |
| Under 18 | 11724 |
| 18–64 | 27516 |
| 65+ | 8689 |
| Median household income | 73978 |
| Poverty rate | 11.6 |
| Homeownership rate | 73.68 |
| Unemployment rate | 4.07 |
| Median home value | 208100 |
| Gini index | 0.4189 |
| Vacancy rate | 6.17 |
| White | 44104 |
| Black | 1073 |
| Asian | 271 |
| Native | 41 |
| Hispanic/Latino | 835 |
| Bachelor's or higher | 9123 |

## Districts

- [OH-04](/us/states/oh/districts/04.md) — 51% (congressional)
- [OH-15](/us/states/oh/districts/15.md) — 49% (congressional)
- [OH Senate District 12](/us/states/oh/districts/senate/12.md) — 100% (state senate)
- [OH House District 85](/us/states/oh/districts/house/85.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
