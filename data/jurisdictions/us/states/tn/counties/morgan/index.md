---
type: Jurisdiction
title: "Morgan County, TN"
classification: county
fips: "47129"
state: "TN"
demographics:
  population: 21361
  population_under_18: 4031
  population_18_64: 13312
  population_65_plus: 4018
  median_household_income: 65954
  poverty_rate: 15.15
  homeownership_rate: 84.89
  unemployment_rate: 5.08
  median_home_value: 166300
  gini_index: 0.4675
  vacancy_rate: 16.09
  race_white: 19578
  race_black: 939
  race_asian: 25
  race_native: 33
  hispanic: 416
  bachelors_plus: 2926
districts:
  - to: "us/states/tn/districts/03"
    rel: in-district
    area_weight: 0.9963
  - to: "us/states/tn/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tn/districts/house/41"
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

# Morgan County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21361 |
| Under 18 | 4031 |
| 18–64 | 13312 |
| 65+ | 4018 |
| Median household income | 65954 |
| Poverty rate | 15.15 |
| Homeownership rate | 84.89 |
| Unemployment rate | 5.08 |
| Median home value | 166300 |
| Gini index | 0.4675 |
| Vacancy rate | 16.09 |
| White | 19578 |
| Black | 939 |
| Asian | 25 |
| Native | 33 |
| Hispanic/Latino | 416 |
| Bachelor's or higher | 2926 |

## Districts

- [TN-03](/us/states/tn/districts/03.md) — 100% (congressional)
- [TN Senate District 12](/us/states/tn/districts/senate/12.md) — 100% (state senate)
- [TN House District 41](/us/states/tn/districts/house/41.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
