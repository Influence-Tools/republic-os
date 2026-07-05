---
type: Jurisdiction
title: "Chickasaw County, IA"
classification: county
fips: "19037"
state: "IA"
demographics:
  population: 11807
  population_under_18: 2743
  population_18_64: 6393
  population_65_plus: 2671
  median_household_income: 75675
  poverty_rate: 8.82
  homeownership_rate: 80.93
  unemployment_rate: 1.58
  median_home_value: 182600
  gini_index: 0.4126
  vacancy_rate: 9.83
  race_white: 11154
  race_black: 64
  race_asian: 2
  race_native: 46
  hispanic: 545
  bachelors_plus: 2179
districts:
  - to: "us/states/ia/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/29"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/58"
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

# Chickasaw County, IA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11807 |
| Under 18 | 2743 |
| 18–64 | 6393 |
| 65+ | 2671 |
| Median household income | 75675 |
| Poverty rate | 8.82 |
| Homeownership rate | 80.93 |
| Unemployment rate | 1.58 |
| Median home value | 182600 |
| Gini index | 0.4126 |
| Vacancy rate | 9.83 |
| White | 11154 |
| Black | 64 |
| Asian | 2 |
| Native | 46 |
| Hispanic/Latino | 545 |
| Bachelor's or higher | 2179 |

## Districts

- [IA-02](/us/states/ia/districts/02.md) — 100% (congressional)
- [IA Senate District 29](/us/states/ia/districts/senate/29.md) — 100% (state senate)
- [IA House District 58](/us/states/ia/districts/house/58.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
