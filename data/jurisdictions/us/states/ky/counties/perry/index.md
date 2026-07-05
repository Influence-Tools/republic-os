---
type: Jurisdiction
title: "Perry County, KY"
classification: county
fips: "21193"
state: "KY"
demographics:
  population: 27499
  population_under_18: 6435
  population_18_64: 16116
  population_65_plus: 4948
  median_household_income: 42181
  poverty_rate: 26.84
  homeownership_rate: 70.41
  unemployment_rate: 5.78
  median_home_value: 91800
  gini_index: 0.5575
  vacancy_rate: 16.68
  race_white: 25765
  race_black: 470
  race_asian: 165
  race_native: 34
  hispanic: 67
  bachelors_plus: 4497
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/30"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ky/districts/house/84"
    rel: in-district
    area_weight: 0.9991
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Perry County, KY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27499 |
| Under 18 | 6435 |
| 18–64 | 16116 |
| 65+ | 4948 |
| Median household income | 42181 |
| Poverty rate | 26.84 |
| Homeownership rate | 70.41 |
| Unemployment rate | 5.78 |
| Median home value | 91800 |
| Gini index | 0.5575 |
| Vacancy rate | 16.68 |
| White | 25765 |
| Black | 470 |
| Asian | 165 |
| Native | 34 |
| Hispanic/Latino | 67 |
| Bachelor's or higher | 4497 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 30](/us/states/ky/districts/senate/30.md) — 100% (state senate)
- [KY House District 84](/us/states/ky/districts/house/84.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
