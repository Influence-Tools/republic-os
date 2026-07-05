---
type: Jurisdiction
title: "Knox County, OH"
classification: county
fips: "39083"
state: "OH"
demographics:
  population: 63142
  population_under_18: 14386
  population_18_64: 36630
  population_65_plus: 12126
  median_household_income: 73878
  poverty_rate: 11.64
  homeownership_rate: 75.51
  unemployment_rate: 2.48
  median_home_value: 239400
  gini_index: 0.4176
  vacancy_rate: 9.92
  race_white: 59106
  race_black: 606
  race_asian: 506
  race_native: 9
  hispanic: 1288
  bachelors_plus: 14209
districts:
  - to: "us/states/oh/districts/12"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/oh/districts/senate/19"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/house/98"
    rel: in-district
    area_weight: 0.6209
  - to: "us/states/oh/districts/house/61"
    rel: in-district
    area_weight: 0.3789
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Knox County, OH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 63142 |
| Under 18 | 14386 |
| 18–64 | 36630 |
| 65+ | 12126 |
| Median household income | 73878 |
| Poverty rate | 11.64 |
| Homeownership rate | 75.51 |
| Unemployment rate | 2.48 |
| Median home value | 239400 |
| Gini index | 0.4176 |
| Vacancy rate | 9.92 |
| White | 59106 |
| Black | 606 |
| Asian | 506 |
| Native | 9 |
| Hispanic/Latino | 1288 |
| Bachelor's or higher | 14209 |

## Districts

- [OH-12](/us/states/oh/districts/12.md) — 100% (congressional)
- [OH Senate District 19](/us/states/oh/districts/senate/19.md) — 100% (state senate)
- [OH House District 98](/us/states/oh/districts/house/98.md) — 62% (state house)
- [OH House District 61](/us/states/oh/districts/house/61.md) — 38% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
