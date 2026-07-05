---
type: Jurisdiction
title: "Switzerland County, IN"
classification: county
fips: "18155"
state: "IN"
demographics:
  population: 9909
  population_under_18: 2348
  population_18_64: 5702
  population_65_plus: 1859
  median_household_income: 65343
  poverty_rate: 12.62
  homeownership_rate: 78.53
  unemployment_rate: 4.18
  median_home_value: 175800
  gini_index: 0.389
  vacancy_rate: 13.04
  race_white: 9410
  race_black: 27
  race_asian: 30
  race_native: 26
  hispanic: 61
  bachelors_plus: 781
districts:
  - to: "us/states/in/districts/09"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/in/districts/senate/43"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/in/districts/house/68"
    rel: in-district
    area_weight: 0.9988
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Switzerland County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9909 |
| Under 18 | 2348 |
| 18–64 | 5702 |
| 65+ | 1859 |
| Median household income | 65343 |
| Poverty rate | 12.62 |
| Homeownership rate | 78.53 |
| Unemployment rate | 4.18 |
| Median home value | 175800 |
| Gini index | 0.389 |
| Vacancy rate | 13.04 |
| White | 9410 |
| Black | 27 |
| Asian | 30 |
| Native | 26 |
| Hispanic/Latino | 61 |
| Bachelor's or higher | 781 |

## Districts

- [IN-09](/us/states/in/districts/09.md) — 100% (congressional)
- [IN Senate District 43](/us/states/in/districts/senate/43.md) — 100% (state senate)
- [IN House District 68](/us/states/in/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
