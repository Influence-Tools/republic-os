---
type: Jurisdiction
title: "Greene County, IA"
classification: county
fips: "19073"
state: "IA"
demographics:
  population: 8688
  population_under_18: 1889
  population_18_64: 4680
  population_65_plus: 2119
  median_household_income: 63409
  poverty_rate: 9.76
  homeownership_rate: 76.42
  unemployment_rate: 2.3
  median_home_value: 155400
  gini_index: 0.4154
  vacancy_rate: 9.19
  race_white: 8136
  race_black: 10
  race_asian: 55
  race_native: 23
  hispanic: 307
  bachelors_plus: 1636
districts:
  - to: "us/states/ia/districts/03"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ia/districts/senate/24"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/house/47"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Greene County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8688 |
| Under 18 | 1889 |
| 18–64 | 4680 |
| 65+ | 2119 |
| Median household income | 63409 |
| Poverty rate | 9.76 |
| Homeownership rate | 76.42 |
| Unemployment rate | 2.3 |
| Median home value | 155400 |
| Gini index | 0.4154 |
| Vacancy rate | 9.19 |
| White | 8136 |
| Black | 10 |
| Asian | 55 |
| Native | 23 |
| Hispanic/Latino | 307 |
| Bachelor's or higher | 1636 |

## Districts

- [IA-03](/us/states/ia/districts/03.md) — 100% (congressional)
- [IA Senate District 24](/us/states/ia/districts/senate/24.md) — 100% (state senate)
- [IA House District 47](/us/states/ia/districts/house/47.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
