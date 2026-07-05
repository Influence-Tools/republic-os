---
type: Jurisdiction
title: "Van Buren County, TN"
classification: county
fips: "47175"
state: "TN"
demographics:
  population: 6437
  population_under_18: 1303
  population_18_64: 3589
  population_65_plus: 1545
  median_household_income: 54931
  poverty_rate: 16.1
  homeownership_rate: 86.41
  unemployment_rate: 2.33
  median_home_value: 159200
  gini_index: 0.4205
  vacancy_rate: 12.08
  race_white: 6092
  race_black: 17
  race_asian: 8
  race_native: 9
  hispanic: 144
  bachelors_plus: 860
districts:
  - to: "us/states/tn/districts/06"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/tn/districts/senate/15"
    rel: in-district
    area_weight: 0.9997
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

# Van Buren County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6437 |
| Under 18 | 1303 |
| 18–64 | 3589 |
| 65+ | 1545 |
| Median household income | 54931 |
| Poverty rate | 16.1 |
| Homeownership rate | 86.41 |
| Unemployment rate | 2.33 |
| Median home value | 159200 |
| Gini index | 0.4205 |
| Vacancy rate | 12.08 |
| White | 6092 |
| Black | 17 |
| Asian | 8 |
| Native | 9 |
| Hispanic/Latino | 144 |
| Bachelor's or higher | 860 |

## Districts

- [TN-06](/us/states/tn/districts/06.md) — 100% (congressional)
- [TN Senate District 15](/us/states/tn/districts/senate/15.md) — 100% (state senate)
- [TN House District 31](/us/states/tn/districts/house/31.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
