---
type: Jurisdiction
title: "Wayne County, IA"
classification: county
fips: "19185"
state: "IA"
demographics:
  population: 6532
  population_under_18: 1695
  population_18_64: 3362
  population_65_plus: 1475
  median_household_income: 61964
  poverty_rate: 10.14
  homeownership_rate: 80.9
  unemployment_rate: 2.92
  median_home_value: 111300
  gini_index: 0.4778
  vacancy_rate: 15.04
  race_white: 6145
  race_black: 12
  race_asian: 6
  race_native: 8
  hispanic: 77
  bachelors_plus: 974
districts:
  - to: "us/states/ia/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/24"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Wayne County, IA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6532 |
| Under 18 | 1695 |
| 18–64 | 3362 |
| 65+ | 1475 |
| Median household income | 61964 |
| Poverty rate | 10.14 |
| Homeownership rate | 80.9 |
| Unemployment rate | 2.92 |
| Median home value | 111300 |
| Gini index | 0.4778 |
| Vacancy rate | 15.04 |
| White | 6145 |
| Black | 12 |
| Asian | 6 |
| Native | 8 |
| Hispanic/Latino | 77 |
| Bachelor's or higher | 974 |

## Districts

- [IA-03](/us/states/ia/districts/03.md) — 100% (congressional)
- [IA Senate District 12](/us/states/ia/districts/senate/12.md) — 100% (state senate)
- [IA House District 24](/us/states/ia/districts/house/24.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
