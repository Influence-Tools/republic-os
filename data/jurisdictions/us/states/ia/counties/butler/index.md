---
type: Jurisdiction
title: "Butler County, IA"
classification: county
fips: "19023"
state: "IA"
demographics:
  population: 14268
  population_under_18: 3193
  population_18_64: 7769
  population_65_plus: 3306
  median_household_income: 73715
  poverty_rate: 9.22
  homeownership_rate: 84.1
  unemployment_rate: 3.13
  median_home_value: 165400
  gini_index: 0.3893
  vacancy_rate: 10.76
  race_white: 13549
  race_black: 24
  race_asian: 179
  race_native: 7
  hispanic: 249
  bachelors_plus: 2687
districts:
  - to: "us/states/ia/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/29"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/57"
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

# Butler County, IA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14268 |
| Under 18 | 3193 |
| 18–64 | 7769 |
| 65+ | 3306 |
| Median household income | 73715 |
| Poverty rate | 9.22 |
| Homeownership rate | 84.1 |
| Unemployment rate | 3.13 |
| Median home value | 165400 |
| Gini index | 0.3893 |
| Vacancy rate | 10.76 |
| White | 13549 |
| Black | 24 |
| Asian | 179 |
| Native | 7 |
| Hispanic/Latino | 249 |
| Bachelor's or higher | 2687 |

## Districts

- [IA-02](/us/states/ia/districts/02.md) — 100% (congressional)
- [IA Senate District 29](/us/states/ia/districts/senate/29.md) — 100% (state senate)
- [IA House District 57](/us/states/ia/districts/house/57.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
