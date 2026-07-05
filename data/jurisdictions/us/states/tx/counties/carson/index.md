---
type: Jurisdiction
title: "Carson County, TX"
classification: county
fips: "48065"
state: "TX"
demographics:
  population: 5801
  population_under_18: 1348
  population_18_64: 3257
  population_65_plus: 1196
  median_household_income: 85231
  poverty_rate: 7.44
  homeownership_rate: 79.2
  unemployment_rate: 1.18
  median_home_value: 143000
  gini_index: 0.4256
  vacancy_rate: 18.4
  race_white: 5237
  race_black: 40
  race_asian: 16
  race_native: 23
  hispanic: 635
  bachelors_plus: 1414
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/87"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Carson County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5801 |
| Under 18 | 1348 |
| 18–64 | 3257 |
| 65+ | 1196 |
| Median household income | 85231 |
| Poverty rate | 7.44 |
| Homeownership rate | 79.2 |
| Unemployment rate | 1.18 |
| Median home value | 143000 |
| Gini index | 0.4256 |
| Vacancy rate | 18.4 |
| White | 5237 |
| Black | 40 |
| Asian | 16 |
| Native | 23 |
| Hispanic/Latino | 635 |
| Bachelor's or higher | 1414 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 87](/us/states/tx/districts/house/87.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
