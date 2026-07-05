---
type: Jurisdiction
title: "Woodson County, KS"
classification: county
fips: "20207"
state: "KS"
demographics:
  population: 3109
  population_under_18: 638
  population_18_64: 1667
  population_65_plus: 804
  median_household_income: 50326
  poverty_rate: 12.36
  homeownership_rate: 84.61
  unemployment_rate: 1.6
  median_home_value: 81200
  gini_index: 0.4369
  vacancy_rate: 32.03
  race_white: 2891
  race_black: 6
  race_asian: 0
  race_native: 7
  hispanic: 90
  bachelors_plus: 656
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/senate/12"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/house/13"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Woodson County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3109 |
| Under 18 | 638 |
| 18–64 | 1667 |
| 65+ | 804 |
| Median household income | 50326 |
| Poverty rate | 12.36 |
| Homeownership rate | 84.61 |
| Unemployment rate | 1.6 |
| Median home value | 81200 |
| Gini index | 0.4369 |
| Vacancy rate | 32.03 |
| White | 2891 |
| Black | 6 |
| Asian | 0 |
| Native | 7 |
| Hispanic/Latino | 90 |
| Bachelor's or higher | 656 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 12](/us/states/ks/districts/senate/12.md) — 100% (state senate)
- [KS House District 13](/us/states/ks/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
