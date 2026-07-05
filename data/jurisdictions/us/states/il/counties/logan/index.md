---
type: Jurisdiction
title: "Logan County, IL"
classification: county
fips: "17107"
state: "IL"
demographics:
  population: 27713
  population_under_18: 5338
  population_18_64: 16966
  population_65_plus: 5409
  median_household_income: 66358
  poverty_rate: 13.13
  homeownership_rate: 68.49
  unemployment_rate: 3.98
  median_home_value: 134400
  gini_index: 0.4222
  vacancy_rate: 5.86
  race_white: 24136
  race_black: 1492
  race_asian: 130
  race_native: 18
  hispanic: 966
  bachelors_plus: 5535
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/il/districts/senate/44"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/house/87"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Logan County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27713 |
| Under 18 | 5338 |
| 18–64 | 16966 |
| 65+ | 5409 |
| Median household income | 66358 |
| Poverty rate | 13.13 |
| Homeownership rate | 68.49 |
| Unemployment rate | 3.98 |
| Median home value | 134400 |
| Gini index | 0.4222 |
| Vacancy rate | 5.86 |
| White | 24136 |
| Black | 1492 |
| Asian | 130 |
| Native | 18 |
| Hispanic/Latino | 966 |
| Bachelor's or higher | 5535 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 100% (congressional)
- [IL Senate District 44](/us/states/il/districts/senate/44.md) — 100% (state senate)
- [IL House District 87](/us/states/il/districts/house/87.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
