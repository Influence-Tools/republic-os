---
type: Jurisdiction
title: "Lake County, OH"
classification: county
fips: "39085"
state: "OH"
demographics:
  population: 232216
  population_under_18: 44800
  population_18_64: 137108
  population_65_plus: 50308
  median_household_income: 80925
  poverty_rate: 8.34
  homeownership_rate: 75.76
  unemployment_rate: 3.88
  median_home_value: 214100
  gini_index: 0.4293
  vacancy_rate: 4.88
  race_white: 198440
  race_black: 11492
  race_asian: 3443
  race_native: 302
  hispanic: 12314
  bachelors_plus: 72271
districts:
  - to: "us/states/oh/districts/14"
    rel: in-district
    area_weight: 0.2364
  - to: "us/states/oh/districts/senate/18"
    rel: in-district
    area_weight: 0.2346
  - to: "us/states/oh/districts/house/57"
    rel: in-district
    area_weight: 0.185
  - to: "us/states/oh/districts/house/23"
    rel: in-district
    area_weight: 0.0496
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Lake County, OH

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 232216 |
| Under 18 | 44800 |
| 18–64 | 137108 |
| 65+ | 50308 |
| Median household income | 80925 |
| Poverty rate | 8.34 |
| Homeownership rate | 75.76 |
| Unemployment rate | 3.88 |
| Median home value | 214100 |
| Gini index | 0.4293 |
| Vacancy rate | 4.88 |
| White | 198440 |
| Black | 11492 |
| Asian | 3443 |
| Native | 302 |
| Hispanic/Latino | 12314 |
| Bachelor's or higher | 72271 |

## Districts

- [OH-14](/us/states/oh/districts/14.md) — 24% (congressional)
- [OH Senate District 18](/us/states/oh/districts/senate/18.md) — 23% (state senate)
- [OH House District 57](/us/states/oh/districts/house/57.md) — 18% (state house)
- [OH House District 23](/us/states/oh/districts/house/23.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
