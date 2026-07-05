---
type: Jurisdiction
title: "Cheatham County, TN"
classification: county
fips: "47021"
state: "TN"
demographics:
  population: 41829
  population_under_18: 9771
  population_18_64: 13125
  population_65_plus: 18933
  median_household_income: 89852
  poverty_rate: 7.67
  homeownership_rate: 81.53
  unemployment_rate: 4.34
  median_home_value: 338700
  gini_index: 0.4133
  vacancy_rate: 6.71
  race_white: 37747
  race_black: 891
  race_asian: 300
  race_native: 108
  hispanic: 1993
  bachelors_plus: 10705
districts:
  - to: "us/states/tn/districts/07"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tn/districts/senate/23"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/house/78"
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

# Cheatham County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 41829 |
| Under 18 | 9771 |
| 18–64 | 13125 |
| 65+ | 18933 |
| Median household income | 89852 |
| Poverty rate | 7.67 |
| Homeownership rate | 81.53 |
| Unemployment rate | 4.34 |
| Median home value | 338700 |
| Gini index | 0.4133 |
| Vacancy rate | 6.71 |
| White | 37747 |
| Black | 891 |
| Asian | 300 |
| Native | 108 |
| Hispanic/Latino | 1993 |
| Bachelor's or higher | 10705 |

## Districts

- [TN-07](/us/states/tn/districts/07.md) — 100% (congressional)
- [TN Senate District 23](/us/states/tn/districts/senate/23.md) — 100% (state senate)
- [TN House District 78](/us/states/tn/districts/house/78.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
