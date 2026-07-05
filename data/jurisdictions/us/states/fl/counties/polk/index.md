---
type: Jurisdiction
title: "Polk County, FL"
classification: county
fips: "12105"
state: "FL"
demographics:
  population: 790694
  population_under_18: 173947
  population_18_64: 462554
  population_65_plus: 154193
  median_household_income: 65978
  poverty_rate: 14.47
  homeownership_rate: 70.47
  unemployment_rate: 4.83
  median_home_value: 266500
  gini_index: 0.4467
  vacancy_rate: 15.06
  race_white: 438493
  race_black: 115178
  race_asian: 14302
  race_native: 3459
  hispanic: 230841
  bachelors_plus: 170511
districts:
  - to: "us/states/fl/districts/18"
    rel: in-district
    area_weight: 0.774
  - to: "us/states/fl/districts/11"
    rel: in-district
    area_weight: 0.1348
  - to: "us/states/fl/districts/15"
    rel: in-district
    area_weight: 0.0587
  - to: "us/states/fl/districts/09"
    rel: in-district
    area_weight: 0.0324
  - to: "us/states/fl/districts/senate/27"
    rel: in-district
    area_weight: 0.5019
  - to: "us/states/fl/districts/senate/12"
    rel: in-district
    area_weight: 0.4977
  - to: "us/states/fl/districts/house/48"
    rel: in-district
    area_weight: 0.3664
  - to: "us/states/fl/districts/house/49"
    rel: in-district
    area_weight: 0.3172
  - to: "us/states/fl/districts/house/51"
    rel: in-district
    area_weight: 0.2443
  - to: "us/states/fl/districts/house/50"
    rel: in-district
    area_weight: 0.0717
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Polk County, FL

County jurisdiction — 108 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 790694 |
| Under 18 | 173947 |
| 18–64 | 462554 |
| 65+ | 154193 |
| Median household income | 65978 |
| Poverty rate | 14.47 |
| Homeownership rate | 70.47 |
| Unemployment rate | 4.83 |
| Median home value | 266500 |
| Gini index | 0.4467 |
| Vacancy rate | 15.06 |
| White | 438493 |
| Black | 115178 |
| Asian | 14302 |
| Native | 3459 |
| Hispanic/Latino | 230841 |
| Bachelor's or higher | 170511 |

## Districts

- [FL-18](/us/states/fl/districts/18.md) — 77% (congressional)
- [FL-11](/us/states/fl/districts/11.md) — 13% (congressional)
- [FL-15](/us/states/fl/districts/15.md) — 6% (congressional)
- [FL-09](/us/states/fl/districts/09.md) — 3% (congressional)
- [FL Senate District 27](/us/states/fl/districts/senate/27.md) — 50% (state senate)
- [FL Senate District 12](/us/states/fl/districts/senate/12.md) — 50% (state senate)
- [FL House District 48](/us/states/fl/districts/house/48.md) — 37% (state house)
- [FL House District 49](/us/states/fl/districts/house/49.md) — 32% (state house)
- [FL House District 51](/us/states/fl/districts/house/51.md) — 24% (state house)
- [FL House District 50](/us/states/fl/districts/house/50.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
