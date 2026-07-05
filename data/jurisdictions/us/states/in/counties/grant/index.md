---
type: Jurisdiction
title: "Grant County, IN"
classification: county
fips: "18053"
state: "IN"
demographics:
  population: 66295
  population_under_18: 14136
  population_18_64: 39389
  population_65_plus: 12770
  median_household_income: 53522
  poverty_rate: 19.83
  homeownership_rate: 72.72
  unemployment_rate: 6.27
  median_home_value: 122300
  gini_index: 0.4483
  vacancy_rate: 10.48
  race_white: 56104
  race_black: 3222
  race_asian: 593
  race_native: 359
  hispanic: 3674
  bachelors_plus: 12399
districts:
  - to: "us/states/in/districts/05"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/in/districts/senate/17"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/in/districts/house/31"
    rel: in-district
    area_weight: 0.9417
  - to: "us/states/in/districts/house/30"
    rel: in-district
    area_weight: 0.0581
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Grant County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 66295 |
| Under 18 | 14136 |
| 18–64 | 39389 |
| 65+ | 12770 |
| Median household income | 53522 |
| Poverty rate | 19.83 |
| Homeownership rate | 72.72 |
| Unemployment rate | 6.27 |
| Median home value | 122300 |
| Gini index | 0.4483 |
| Vacancy rate | 10.48 |
| White | 56104 |
| Black | 3222 |
| Asian | 593 |
| Native | 359 |
| Hispanic/Latino | 3674 |
| Bachelor's or higher | 12399 |

## Districts

- [IN-05](/us/states/in/districts/05.md) — 100% (congressional)
- [IN Senate District 17](/us/states/in/districts/senate/17.md) — 100% (state senate)
- [IN House District 31](/us/states/in/districts/house/31.md) — 94% (state house)
- [IN House District 30](/us/states/in/districts/house/30.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
