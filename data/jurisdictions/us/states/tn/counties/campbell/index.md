---
type: Jurisdiction
title: "Campbell County, TN"
classification: county
fips: "47013"
state: "TN"
demographics:
  population: 39761
  population_under_18: 8805
  population_18_64: 11403
  population_65_plus: 19553
  median_household_income: 51557
  poverty_rate: 18.53
  homeownership_rate: 69.2
  unemployment_rate: 4.96
  median_home_value: 186500
  gini_index: 0.4485
  vacancy_rate: 16.41
  race_white: 38085
  race_black: 201
  race_asian: 79
  race_native: 60
  hispanic: 636
  bachelors_plus: 5334
districts:
  - to: "us/states/tn/districts/02"
    rel: in-district
    area_weight: 0.6887
  - to: "us/states/tn/districts/03"
    rel: in-district
    area_weight: 0.3095
  - to: "us/states/tn/districts/senate/12"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/house/36"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Campbell County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39761 |
| Under 18 | 8805 |
| 18–64 | 11403 |
| 65+ | 19553 |
| Median household income | 51557 |
| Poverty rate | 18.53 |
| Homeownership rate | 69.2 |
| Unemployment rate | 4.96 |
| Median home value | 186500 |
| Gini index | 0.4485 |
| Vacancy rate | 16.41 |
| White | 38085 |
| Black | 201 |
| Asian | 79 |
| Native | 60 |
| Hispanic/Latino | 636 |
| Bachelor's or higher | 5334 |

## Districts

- [TN-02](/us/states/tn/districts/02.md) — 69% (congressional)
- [TN-03](/us/states/tn/districts/03.md) — 31% (congressional)
- [TN Senate District 12](/us/states/tn/districts/senate/12.md) — 100% (state senate)
- [TN House District 36](/us/states/tn/districts/house/36.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
