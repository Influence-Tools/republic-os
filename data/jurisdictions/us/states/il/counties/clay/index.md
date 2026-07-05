---
type: Jurisdiction
title: "Clay County, IL"
classification: county
fips: "17025"
state: "IL"
demographics:
  population: 13052
  population_under_18: 3111
  population_18_64: 7214
  population_65_plus: 2727
  median_household_income: 60417
  poverty_rate: 17.51
  homeownership_rate: 79.29
  unemployment_rate: 4.84
  median_home_value: 97400
  gini_index: 0.4569
  vacancy_rate: 13.85
  race_white: 12431
  race_black: 38
  race_asian: 28
  race_native: 15
  hispanic: 264
  bachelors_plus: 1566
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/senate/55"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/house/110"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Clay County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13052 |
| Under 18 | 3111 |
| 18–64 | 7214 |
| 65+ | 2727 |
| Median household income | 60417 |
| Poverty rate | 17.51 |
| Homeownership rate | 79.29 |
| Unemployment rate | 4.84 |
| Median home value | 97400 |
| Gini index | 0.4569 |
| Vacancy rate | 13.85 |
| White | 12431 |
| Black | 38 |
| Asian | 28 |
| Native | 15 |
| Hispanic/Latino | 264 |
| Bachelor's or higher | 1566 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL Senate District 55](/us/states/il/districts/senate/55.md) — 100% (state senate)
- [IL House District 110](/us/states/il/districts/house/110.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
