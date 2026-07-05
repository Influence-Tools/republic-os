---
type: Jurisdiction
title: "Rhea County, TN"
classification: county
fips: "47143"
state: "TN"
demographics:
  population: 33992
  population_under_18: 7196
  population_18_64: 20065
  population_65_plus: 6731
  median_household_income: 55033
  poverty_rate: 15.89
  homeownership_rate: 71.48
  unemployment_rate: 5.83
  median_home_value: 206000
  gini_index: 0.4704
  vacancy_rate: 12.79
  race_white: 29863
  race_black: 506
  race_asian: 241
  race_native: 26
  hispanic: 2142
  bachelors_plus: 5806
districts:
  - to: "us/states/tn/districts/04"
    rel: in-district
    area_weight: 0.9979
  - to: "us/states/tn/districts/senate/1"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/house/31"
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

# Rhea County, TN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33992 |
| Under 18 | 7196 |
| 18–64 | 20065 |
| 65+ | 6731 |
| Median household income | 55033 |
| Poverty rate | 15.89 |
| Homeownership rate | 71.48 |
| Unemployment rate | 5.83 |
| Median home value | 206000 |
| Gini index | 0.4704 |
| Vacancy rate | 12.79 |
| White | 29863 |
| Black | 506 |
| Asian | 241 |
| Native | 26 |
| Hispanic/Latino | 2142 |
| Bachelor's or higher | 5806 |

## Districts

- [TN-04](/us/states/tn/districts/04.md) — 100% (congressional)
- [TN Senate District 1](/us/states/tn/districts/senate/1.md) — 100% (state senate)
- [TN House District 31](/us/states/tn/districts/house/31.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
