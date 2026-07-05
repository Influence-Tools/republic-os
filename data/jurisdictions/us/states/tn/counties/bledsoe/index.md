---
type: Jurisdiction
title: "Bledsoe County, TN"
classification: county
fips: "47007"
state: "TN"
demographics:
  population: 15032
  population_under_18: 2677
  population_18_64: 4720
  population_65_plus: 7635
  median_household_income: 54720
  poverty_rate: 20.73
  homeownership_rate: 82.5
  unemployment_rate: 1.82
  median_home_value: 189400
  gini_index: 0.4358
  vacancy_rate: 17.83
  race_white: 13213
  race_black: 910
  race_asian: 26
  race_native: 45
  hispanic: 525
  bachelors_plus: 2086
districts:
  - to: "us/states/tn/districts/04"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/tn/districts/senate/10"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/house/31"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Bledsoe County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15032 |
| Under 18 | 2677 |
| 18–64 | 4720 |
| 65+ | 7635 |
| Median household income | 54720 |
| Poverty rate | 20.73 |
| Homeownership rate | 82.5 |
| Unemployment rate | 1.82 |
| Median home value | 189400 |
| Gini index | 0.4358 |
| Vacancy rate | 17.83 |
| White | 13213 |
| Black | 910 |
| Asian | 26 |
| Native | 45 |
| Hispanic/Latino | 525 |
| Bachelor's or higher | 2086 |

## Districts

- [TN-04](/us/states/tn/districts/04.md) — 100% (congressional)
- [TN Senate District 10](/us/states/tn/districts/senate/10.md) — 100% (state senate)
- [TN House District 31](/us/states/tn/districts/house/31.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
