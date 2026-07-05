---
type: Jurisdiction
title: "Morgan County, IN"
classification: county
fips: "18109"
state: "IN"
demographics:
  population: 72659
  population_under_18: 16023
  population_18_64: 43459
  population_65_plus: 13177
  median_household_income: 79429
  poverty_rate: 9.28
  homeownership_rate: 82.13
  unemployment_rate: 4.18
  median_home_value: 237600
  gini_index: 0.4267
  vacancy_rate: 5.88
  race_white: 68339
  race_black: 576
  race_asian: 363
  race_native: 14
  hispanic: 1560
  bachelors_plus: 14133
districts:
  - to: "us/states/in/districts/04"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/in/districts/senate/37"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/house/60"
    rel: in-district
    area_weight: 0.9107
  - to: "us/states/in/districts/house/57"
    rel: in-district
    area_weight: 0.0891
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Morgan County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 72659 |
| Under 18 | 16023 |
| 18–64 | 43459 |
| 65+ | 13177 |
| Median household income | 79429 |
| Poverty rate | 9.28 |
| Homeownership rate | 82.13 |
| Unemployment rate | 4.18 |
| Median home value | 237600 |
| Gini index | 0.4267 |
| Vacancy rate | 5.88 |
| White | 68339 |
| Black | 576 |
| Asian | 363 |
| Native | 14 |
| Hispanic/Latino | 1560 |
| Bachelor's or higher | 14133 |

## Districts

- [IN-04](/us/states/in/districts/04.md) — 100% (congressional)
- [IN Senate District 37](/us/states/in/districts/senate/37.md) — 100% (state senate)
- [IN House District 60](/us/states/in/districts/house/60.md) — 91% (state house)
- [IN House District 57](/us/states/in/districts/house/57.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
