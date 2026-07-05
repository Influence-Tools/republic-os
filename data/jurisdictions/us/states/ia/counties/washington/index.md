---
type: Jurisdiction
title: "Washington County, IA"
classification: county
fips: "19183"
state: "IA"
demographics:
  population: 22561
  population_under_18: 5533
  population_18_64: 12490
  population_65_plus: 4538
  median_household_income: 75647
  poverty_rate: 8.2
  homeownership_rate: 74.02
  unemployment_rate: 2.21
  median_home_value: 203900
  gini_index: 0.4287
  vacancy_rate: 7.09
  race_white: 20337
  race_black: 236
  race_asian: 87
  race_native: 2
  hispanic: 1749
  bachelors_plus: 5415
districts:
  - to: "us/states/ia/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/46"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/house/92"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Washington County, IA

County jurisdiction — 4 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22561 |
| Under 18 | 5533 |
| 18–64 | 12490 |
| 65+ | 4538 |
| Median household income | 75647 |
| Poverty rate | 8.2 |
| Homeownership rate | 74.02 |
| Unemployment rate | 2.21 |
| Median home value | 203900 |
| Gini index | 0.4287 |
| Vacancy rate | 7.09 |
| White | 20337 |
| Black | 236 |
| Asian | 87 |
| Native | 2 |
| Hispanic/Latino | 1749 |
| Bachelor's or higher | 5415 |

## Districts

- [IA-01](/us/states/ia/districts/01.md) — 100% (congressional)
- [IA Senate District 46](/us/states/ia/districts/senate/46.md) — 100% (state senate)
- [IA House District 92](/us/states/ia/districts/house/92.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
