---
type: Jurisdiction
title: "Clark County, IN"
classification: county
fips: "18019"
state: "IN"
demographics:
  population: 124354
  population_under_18: 27419
  population_18_64: 76138
  population_65_plus: 20797
  median_household_income: 74214
  poverty_rate: 10.2
  homeownership_rate: 74.74
  unemployment_rate: 4.01
  median_home_value: 222900
  gini_index: 0.4143
  vacancy_rate: 6.92
  race_white: 101612
  race_black: 9069
  race_asian: 1514
  race_native: 429
  hispanic: 8547
  bachelors_plus: 32186
districts:
  - to: "us/states/in/districts/09"
    rel: in-district
    area_weight: 0.9983
  - to: "us/states/in/districts/senate/45"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/in/districts/house/66"
    rel: in-district
    area_weight: 0.7254
  - to: "us/states/in/districts/house/70"
    rel: in-district
    area_weight: 0.1748
  - to: "us/states/in/districts/house/71"
    rel: in-district
    area_weight: 0.0988
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Clark County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 124354 |
| Under 18 | 27419 |
| 18–64 | 76138 |
| 65+ | 20797 |
| Median household income | 74214 |
| Poverty rate | 10.2 |
| Homeownership rate | 74.74 |
| Unemployment rate | 4.01 |
| Median home value | 222900 |
| Gini index | 0.4143 |
| Vacancy rate | 6.92 |
| White | 101612 |
| Black | 9069 |
| Asian | 1514 |
| Native | 429 |
| Hispanic/Latino | 8547 |
| Bachelor's or higher | 32186 |

## Districts

- [IN-09](/us/states/in/districts/09.md) — 100% (congressional)
- [IN Senate District 45](/us/states/in/districts/senate/45.md) — 100% (state senate)
- [IN House District 66](/us/states/in/districts/house/66.md) — 73% (state house)
- [IN House District 70](/us/states/in/districts/house/70.md) — 17% (state house)
- [IN House District 71](/us/states/in/districts/house/71.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
