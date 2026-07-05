---
type: Jurisdiction
title: "Monroe County, TN"
classification: county
fips: "47123"
state: "TN"
demographics:
  population: 47695
  population_under_18: 9792
  population_18_64: 27276
  population_65_plus: 10627
  median_household_income: 56895
  poverty_rate: 15.47
  homeownership_rate: 72.16
  unemployment_rate: 4.35
  median_home_value: 227500
  gini_index: 0.4376
  vacancy_rate: 9.42
  race_white: 41985
  race_black: 956
  race_asian: 104
  race_native: 140
  hispanic: 2220
  bachelors_plus: 7953
districts:
  - to: "us/states/tn/districts/03"
    rel: in-district
    area_weight: 0.996
  - to: "us/states/tn/districts/senate/2"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tn/districts/house/23"
    rel: in-district
    area_weight: 0.6778
  - to: "us/states/tn/districts/house/21"
    rel: in-district
    area_weight: 0.3216
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Monroe County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47695 |
| Under 18 | 9792 |
| 18–64 | 27276 |
| 65+ | 10627 |
| Median household income | 56895 |
| Poverty rate | 15.47 |
| Homeownership rate | 72.16 |
| Unemployment rate | 4.35 |
| Median home value | 227500 |
| Gini index | 0.4376 |
| Vacancy rate | 9.42 |
| White | 41985 |
| Black | 956 |
| Asian | 104 |
| Native | 140 |
| Hispanic/Latino | 2220 |
| Bachelor's or higher | 7953 |

## Districts

- [TN-03](/us/states/tn/districts/03.md) — 100% (congressional)
- [TN Senate District 2](/us/states/tn/districts/senate/2.md) — 100% (state senate)
- [TN House District 23](/us/states/tn/districts/house/23.md) — 68% (state house)
- [TN House District 21](/us/states/tn/districts/house/21.md) — 32% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
