---
type: Jurisdiction
title: "Meigs County, TN"
classification: county
fips: "47121"
state: "TN"
demographics:
  population: 13343
  population_under_18: 2704
  population_18_64: 7831
  population_65_plus: 2808
  median_household_income: 61375
  poverty_rate: 14.27
  homeownership_rate: 80.96
  unemployment_rate: 5.47
  median_home_value: 180000
  gini_index: 0.4626
  vacancy_rate: 16.57
  race_white: 11901
  race_black: 296
  race_asian: 52
  race_native: 17
  hispanic: 249
  bachelors_plus: 1759
districts:
  - to: "us/states/tn/districts/04"
    rel: in-district
    area_weight: 0.9846
  - to: "us/states/tn/districts/03"
    rel: in-district
    area_weight: 0.0154
  - to: "us/states/tn/districts/senate/1"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tn/districts/house/22"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Meigs County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13343 |
| Under 18 | 2704 |
| 18–64 | 7831 |
| 65+ | 2808 |
| Median household income | 61375 |
| Poverty rate | 14.27 |
| Homeownership rate | 80.96 |
| Unemployment rate | 5.47 |
| Median home value | 180000 |
| Gini index | 0.4626 |
| Vacancy rate | 16.57 |
| White | 11901 |
| Black | 296 |
| Asian | 52 |
| Native | 17 |
| Hispanic/Latino | 249 |
| Bachelor's or higher | 1759 |

## Districts

- [TN-04](/us/states/tn/districts/04.md) — 98% (congressional)
- [TN-03](/us/states/tn/districts/03.md) — 2% (congressional)
- [TN Senate District 1](/us/states/tn/districts/senate/1.md) — 100% (state senate)
- [TN House District 22](/us/states/tn/districts/house/22.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
