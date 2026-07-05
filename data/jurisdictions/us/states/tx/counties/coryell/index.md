---
type: Jurisdiction
title: "Coryell County, TX"
classification: county
fips: "48099"
state: "TX"
demographics:
  population: 84748
  population_under_18: 19058
  population_18_64: 56069
  population_65_plus: 9621
  median_household_income: 71301
  poverty_rate: 11.18
  homeownership_rate: 58.56
  unemployment_rate: 7.09
  median_home_value: 195300
  gini_index: 0.4131
  vacancy_rate: 8.56
  race_white: 49672
  race_black: 12161
  race_asian: 1665
  race_native: 764
  hispanic: 17559
  bachelors_plus: 14047
districts:
  - to: "us/states/tx/districts/31"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tx/districts/senate/24"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/59"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Coryell County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 84748 |
| Under 18 | 19058 |
| 18–64 | 56069 |
| 65+ | 9621 |
| Median household income | 71301 |
| Poverty rate | 11.18 |
| Homeownership rate | 58.56 |
| Unemployment rate | 7.09 |
| Median home value | 195300 |
| Gini index | 0.4131 |
| Vacancy rate | 8.56 |
| White | 49672 |
| Black | 12161 |
| Asian | 1665 |
| Native | 764 |
| Hispanic/Latino | 17559 |
| Bachelor's or higher | 14047 |

## Districts

- [TX-31](/us/states/tx/districts/31.md) — 100% (congressional)
- [TX Senate District 24](/us/states/tx/districts/senate/24.md) — 100% (state senate)
- [TX House District 59](/us/states/tx/districts/house/59.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
