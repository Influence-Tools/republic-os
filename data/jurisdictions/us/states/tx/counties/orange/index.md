---
type: Jurisdiction
title: "Orange County, TX"
classification: county
fips: "48361"
state: "TX"
demographics:
  population: 85307
  population_under_18: 21636
  population_18_64: 49902
  population_65_plus: 13769
  median_household_income: 72104
  poverty_rate: 12.54
  homeownership_rate: 75.17
  unemployment_rate: 6.03
  median_home_value: 173400
  gini_index: 0.4567
  vacancy_rate: 14.5
  race_white: 67656
  race_black: 6635
  race_asian: 953
  race_native: 148
  hispanic: 8216
  bachelors_plus: 12966
districts:
  - to: "us/states/tx/districts/14"
    rel: in-district
    area_weight: 0.9949
  - to: "us/states/tx/districts/senate/3"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/tx/districts/house/21"
    rel: in-district
    area_weight: 0.9987
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Orange County, TX

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 85307 |
| Under 18 | 21636 |
| 18–64 | 49902 |
| 65+ | 13769 |
| Median household income | 72104 |
| Poverty rate | 12.54 |
| Homeownership rate | 75.17 |
| Unemployment rate | 6.03 |
| Median home value | 173400 |
| Gini index | 0.4567 |
| Vacancy rate | 14.5 |
| White | 67656 |
| Black | 6635 |
| Asian | 953 |
| Native | 148 |
| Hispanic/Latino | 8216 |
| Bachelor's or higher | 12966 |

## Districts

- [TX-14](/us/states/tx/districts/14.md) — 99% (congressional)
- [TX Senate District 3](/us/states/tx/districts/senate/3.md) — 100% (state senate)
- [TX House District 21](/us/states/tx/districts/house/21.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
