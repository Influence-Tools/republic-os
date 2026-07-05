---
type: Jurisdiction
title: "Jefferson County, IN"
classification: county
fips: "18077"
state: "IN"
demographics:
  population: 32998
  population_under_18: 6579
  population_18_64: 20079
  population_65_plus: 6340
  median_household_income: 64577
  poverty_rate: 12.34
  homeownership_rate: 71.84
  unemployment_rate: 4.39
  median_home_value: 194600
  gini_index: 0.4223
  vacancy_rate: 11.9
  race_white: 30457
  race_black: 343
  race_asian: 270
  race_native: 60
  hispanic: 1148
  bachelors_plus: 6623
districts:
  - to: "us/states/in/districts/09"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/in/districts/senate/43"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/in/districts/house/67"
    rel: in-district
    area_weight: 0.7472
  - to: "us/states/in/districts/house/66"
    rel: in-district
    area_weight: 0.1557
  - to: "us/states/in/districts/house/68"
    rel: in-district
    area_weight: 0.0966
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Jefferson County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32998 |
| Under 18 | 6579 |
| 18–64 | 20079 |
| 65+ | 6340 |
| Median household income | 64577 |
| Poverty rate | 12.34 |
| Homeownership rate | 71.84 |
| Unemployment rate | 4.39 |
| Median home value | 194600 |
| Gini index | 0.4223 |
| Vacancy rate | 11.9 |
| White | 30457 |
| Black | 343 |
| Asian | 270 |
| Native | 60 |
| Hispanic/Latino | 1148 |
| Bachelor's or higher | 6623 |

## Districts

- [IN-09](/us/states/in/districts/09.md) — 100% (congressional)
- [IN Senate District 43](/us/states/in/districts/senate/43.md) — 100% (state senate)
- [IN House District 67](/us/states/in/districts/house/67.md) — 75% (state house)
- [IN House District 66](/us/states/in/districts/house/66.md) — 16% (state house)
- [IN House District 68](/us/states/in/districts/house/68.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
