---
type: Jurisdiction
title: "Polk County, TN"
classification: county
fips: "47139"
state: "TN"
demographics:
  population: 17898
  population_under_18: 3356
  population_18_64: 10778
  population_65_plus: 3764
  median_household_income: 62522
  poverty_rate: 13.95
  homeownership_rate: 83.59
  unemployment_rate: 5.28
  median_home_value: 169900
  gini_index: 0.49
  vacancy_rate: 18.09
  race_white: 16032
  race_black: 142
  race_asian: 53
  race_native: 6
  hispanic: 388
  bachelors_plus: 3141
districts:
  - to: "us/states/tn/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/senate/2"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/house/22"
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

# Polk County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17898 |
| Under 18 | 3356 |
| 18–64 | 10778 |
| 65+ | 3764 |
| Median household income | 62522 |
| Poverty rate | 13.95 |
| Homeownership rate | 83.59 |
| Unemployment rate | 5.28 |
| Median home value | 169900 |
| Gini index | 0.49 |
| Vacancy rate | 18.09 |
| White | 16032 |
| Black | 142 |
| Asian | 53 |
| Native | 6 |
| Hispanic/Latino | 388 |
| Bachelor's or higher | 3141 |

## Districts

- [TN-03](/us/states/tn/districts/03.md) — 100% (congressional)
- [TN Senate District 2](/us/states/tn/districts/senate/2.md) — 100% (state senate)
- [TN House District 22](/us/states/tn/districts/house/22.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
