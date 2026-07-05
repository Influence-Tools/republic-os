---
type: Jurisdiction
title: "Columbia County, PA"
classification: county
fips: "42037"
state: "PA"
demographics:
  population: 65362
  population_under_18: 11483
  population_18_64: 40585
  population_65_plus: 13294
  median_household_income: 64644
  poverty_rate: 13.74
  homeownership_rate: 69.5
  unemployment_rate: 5.98
  median_home_value: 206200
  gini_index: 0.4362
  vacancy_rate: 11.65
  race_white: 59749
  race_black: 1184
  race_asian: 485
  race_native: 134
  hispanic: 2663
  bachelors_plus: 16465
districts:
  - to: "us/states/pa/districts/09"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/pa/districts/senate/27"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/pa/districts/house/109"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Columbia County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 65362 |
| Under 18 | 11483 |
| 18–64 | 40585 |
| 65+ | 13294 |
| Median household income | 64644 |
| Poverty rate | 13.74 |
| Homeownership rate | 69.5 |
| Unemployment rate | 5.98 |
| Median home value | 206200 |
| Gini index | 0.4362 |
| Vacancy rate | 11.65 |
| White | 59749 |
| Black | 1184 |
| Asian | 485 |
| Native | 134 |
| Hispanic/Latino | 2663 |
| Bachelor's or higher | 16465 |

## Districts

- [PA-09](/us/states/pa/districts/09.md) — 100% (congressional)
- [PA Senate District 27](/us/states/pa/districts/senate/27.md) — 100% (state senate)
- [PA House District 109](/us/states/pa/districts/house/109.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
