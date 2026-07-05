---
type: Jurisdiction
title: "Montgomery County, TN"
classification: county
fips: "47125"
state: "TN"
demographics:
  population: 234153
  population_under_18: 62685
  population_18_64: 148040
  population_65_plus: 23428
  median_household_income: 75613
  poverty_rate: 11.27
  homeownership_rate: 61.88
  unemployment_rate: 5.08
  median_home_value: 280200
  gini_index: 0.4014
  vacancy_rate: 6.08
  race_white: 146834
  race_black: 45681
  race_asian: 6107
  race_native: 743
  hispanic: 26629
  bachelors_plus: 63230
districts:
  - to: "us/states/tn/districts/07"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tn/districts/senate/22"
    rel: in-district
    area_weight: 0.9666
  - to: "us/states/tn/districts/senate/23"
    rel: in-district
    area_weight: 0.0329
  - to: "us/states/tn/districts/house/68"
    rel: in-district
    area_weight: 0.4919
  - to: "us/states/tn/districts/house/75"
    rel: in-district
    area_weight: 0.4315
  - to: "us/states/tn/districts/house/67"
    rel: in-district
    area_weight: 0.0761
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Montgomery County, TN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 234153 |
| Under 18 | 62685 |
| 18–64 | 148040 |
| 65+ | 23428 |
| Median household income | 75613 |
| Poverty rate | 11.27 |
| Homeownership rate | 61.88 |
| Unemployment rate | 5.08 |
| Median home value | 280200 |
| Gini index | 0.4014 |
| Vacancy rate | 6.08 |
| White | 146834 |
| Black | 45681 |
| Asian | 6107 |
| Native | 743 |
| Hispanic/Latino | 26629 |
| Bachelor's or higher | 63230 |

## Districts

- [TN-07](/us/states/tn/districts/07.md) — 100% (congressional)
- [TN Senate District 22](/us/states/tn/districts/senate/22.md) — 97% (state senate)
- [TN Senate District 23](/us/states/tn/districts/senate/23.md) — 3% (state senate)
- [TN House District 68](/us/states/tn/districts/house/68.md) — 49% (state house)
- [TN House District 75](/us/states/tn/districts/house/75.md) — 43% (state house)
- [TN House District 67](/us/states/tn/districts/house/67.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
