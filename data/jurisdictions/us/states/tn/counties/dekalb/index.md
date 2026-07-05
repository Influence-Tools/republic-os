---
type: Jurisdiction
title: "DeKalb County, TN"
classification: county
fips: "47041"
state: "TN"
demographics:
  population: 20959
  population_under_18: 4965
  population_18_64: 6328
  population_65_plus: 9666
  median_household_income: 53153
  poverty_rate: 18.57
  homeownership_rate: 72.61
  unemployment_rate: 5.64
  median_home_value: 235500
  gini_index: 0.4454
  vacancy_rate: 14.8
  race_white: 18453
  race_black: 325
  race_asian: 231
  race_native: 58
  hispanic: 1624
  bachelors_plus: 4237
districts:
  - to: "us/states/tn/districts/06"
    rel: in-district
    area_weight: 0.9971
  - to: "us/states/tn/districts/senate/16"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/house/40"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# DeKalb County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20959 |
| Under 18 | 4965 |
| 18–64 | 6328 |
| 65+ | 9666 |
| Median household income | 53153 |
| Poverty rate | 18.57 |
| Homeownership rate | 72.61 |
| Unemployment rate | 5.64 |
| Median home value | 235500 |
| Gini index | 0.4454 |
| Vacancy rate | 14.8 |
| White | 18453 |
| Black | 325 |
| Asian | 231 |
| Native | 58 |
| Hispanic/Latino | 1624 |
| Bachelor's or higher | 4237 |

## Districts

- [TN-06](/us/states/tn/districts/06.md) — 100% (congressional)
- [TN Senate District 16](/us/states/tn/districts/senate/16.md) — 100% (state senate)
- [TN House District 40](/us/states/tn/districts/house/40.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
