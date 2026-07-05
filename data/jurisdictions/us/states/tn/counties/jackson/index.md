---
type: Jurisdiction
title: "Jackson County, TN"
classification: county
fips: "47087"
state: "TN"
demographics:
  population: 12029
  population_under_18: 2200
  population_18_64: 7027
  population_65_plus: 2802
  median_household_income: 47951
  poverty_rate: 20.25
  homeownership_rate: 81.08
  unemployment_rate: 7.64
  median_home_value: 155500
  gini_index: 0.4817
  vacancy_rate: 18.09
  race_white: 11171
  race_black: 49
  race_asian: 0
  race_native: 19
  hispanic: 342
  bachelors_plus: 1729
districts:
  - to: "us/states/tn/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tn/districts/senate/15"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/house/40"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Jackson County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12029 |
| Under 18 | 2200 |
| 18–64 | 7027 |
| 65+ | 2802 |
| Median household income | 47951 |
| Poverty rate | 20.25 |
| Homeownership rate | 81.08 |
| Unemployment rate | 7.64 |
| Median home value | 155500 |
| Gini index | 0.4817 |
| Vacancy rate | 18.09 |
| White | 11171 |
| Black | 49 |
| Asian | 0 |
| Native | 19 |
| Hispanic/Latino | 342 |
| Bachelor's or higher | 1729 |

## Districts

- [TN-06](/us/states/tn/districts/06.md) — 100% (congressional)
- [TN Senate District 15](/us/states/tn/districts/senate/15.md) — 100% (state senate)
- [TN House District 40](/us/states/tn/districts/house/40.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
