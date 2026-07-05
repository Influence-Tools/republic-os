---
type: Jurisdiction
title: "Sequatchie County, TN"
classification: county
fips: "47153"
state: "TN"
demographics:
  population: 16809
  population_under_18: 3346
  population_18_64: 9801
  population_65_plus: 3662
  median_household_income: 58750
  poverty_rate: 21.94
  homeownership_rate: 78.01
  unemployment_rate: 6.63
  median_home_value: 232600
  gini_index: 0.4659
  vacancy_rate: 11.41
  race_white: 15468
  race_black: 84
  race_asian: 139
  race_native: 5
  hispanic: 831
  bachelors_plus: 3501
districts:
  - to: "us/states/tn/districts/04"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/tn/districts/senate/10"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tn/districts/house/31"
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

# Sequatchie County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16809 |
| Under 18 | 3346 |
| 18–64 | 9801 |
| 65+ | 3662 |
| Median household income | 58750 |
| Poverty rate | 21.94 |
| Homeownership rate | 78.01 |
| Unemployment rate | 6.63 |
| Median home value | 232600 |
| Gini index | 0.4659 |
| Vacancy rate | 11.41 |
| White | 15468 |
| Black | 84 |
| Asian | 139 |
| Native | 5 |
| Hispanic/Latino | 831 |
| Bachelor's or higher | 3501 |

## Districts

- [TN-04](/us/states/tn/districts/04.md) — 100% (congressional)
- [TN Senate District 10](/us/states/tn/districts/senate/10.md) — 100% (state senate)
- [TN House District 31](/us/states/tn/districts/house/31.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
